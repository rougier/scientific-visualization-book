# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
# Requirements:
# - noise library at https://pypi.org/project/noise/
# - shapely library at https://pypi.org/project/Shapely/
# - "Celtic Garamond" font at https://www.dafont.com/celtic-garamond-2nd.font
# - "Morris Roman" font at https://www.dafont.com/morris-roman.font
# - Nessy image from Irina Miroshnichenko (Sudowoodo)
#    (not included in the book because of rights)
#
# Note: After having installed font, you might need to erase your font cache
#       such that newly installed font can be found. Have a look at
#       https://matplotlib.org/faq/troubleshooting_faq.html
# ----------------------------------------------------------------------------

import noise
import numpy as np
import scipy.spatial
import shapely.geometry
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.collections import PolyCollection
from math import cos, sin, floor, sqrt, pi, ceil


# This is important because "cities" have been manually positioned
np.random.seed(1)


# Blue noise sampling
# -------------------
def blue_noise(shape, radius, k=32, seed=None):
    """
    Generate blue noise over a two-dimensional rectangle of size (width,height)

    Parameters
    ----------

    shape : tuple
        Two-dimensional domain (width x height) 
    radius : float
        Minimum distance between samples
    k : int, optional
        Limit of samples to choose before rejection (typically k = 30)
    seed : int, optional
        If provided, this will set the random seed before generating noise,
        for valid pseudo-random comparisons.

    References
    ----------

    .. [1] Fast Poisson Disk Sampling in Arbitrary Dimensions, Robert Bridson,
           Siggraph, 2007. :DOI:`10.1145/1278780.1278807`
    """

    def sqdist(a, b):
        """ Squared Euclidean distance """
        dx, dy = a[0] - b[0], a[1] - b[1]
        return dx * dx + dy * dy

    def grid_coords(p):
        """ Return index of cell grid corresponding to p """
        return int(floor(p[0] / cellsize)), int(floor(p[1] / cellsize))

    def fits(p, radius):
        """ Check whether p can be added to the queue """

        radius2 = radius * radius
        gx, gy = grid_coords(p)
        for x in range(max(gx - 2, 0), min(gx + 3, grid_width)):
            for y in range(max(gy - 2, 0), min(gy + 3, grid_height)):
                g = grid[x + y * grid_width]
                if g is None:
                    continue
                if sqdist(p, g) <= radius2:
                    return False
        return True

    # When given a seed, we use a private random generator in order to not
    # disturb the default global random generator
    if seed is not None:
        from numpy.random.mtrand import RandomState

        rng = RandomState(seed=seed)
    else:
        rng = np.random

    width, height = shape
    cellsize = radius / sqrt(2)
    grid_width = int(ceil(width / cellsize))
    grid_height = int(ceil(height / cellsize))
    grid = [None] * (grid_width * grid_height)

    p = rng.uniform(0, shape, 2)
    queue = [p]
    grid_x, grid_y = grid_coords(p)
    grid[grid_x + grid_y * grid_width] = p

    while queue:
        qi = rng.randint(len(queue))
        qx, qy = queue[qi]
        queue[qi] = queue[-1]
        queue.pop()
        for _ in range(k):
            theta = rng.uniform(0, 2 * pi)
            r = radius * np.sqrt(rng.uniform(1, 4))
            p = qx + r * cos(theta), qy + r * sin(theta)
            if not (0 <= p[0] < width and 0 <= p[1] < height) or not fits(p, radius):
                continue
            queue.append(p)
            gx, gy = grid_coords(p)
            grid[gx + gy * grid_width] = p

    return np.array([p for p in grid if p is not None])


# Hatch pattern with given orientation (or random if None given)
def hatch(n=4, theta=None):
    theta = theta or np.random.uniform(0, np.pi)
    P = np.zeros((n, 2, 2))
    X = np.linspace(-0.5, +0.5, n, endpoint=True)
    P[:, 0, 1] = -0.5 + np.random.normal(0, 0.05, n)
    P[:, 1, 1] = +0.5 + np.random.normal(0, 0.05, n)
    P[:, 1, 0] = X + np.random.normal(0, 0.025, n)
    P[:, 0, 0] = X + np.random.normal(0, 0.025, n)
    c, s = np.cos(theta), np.sin(theta)
    Z = np.array([[c, s], [-s, c]])
    return P @ Z.T


# Actual drawing
fig = plt.figure(figsize=(6, 6))
fig.patch.set_facecolor("#ffffff")
ax = plt.subplot(1, 1, 1, aspect=1, frameon=False)


# Figure border using the hatch pattern. They are first spread according to
# a blue noise distribution, scaled according to the distance to the nearest
# neighbour and then lines composing the hatch are clipped against the
# corresponding Voronoi cell.
h = 4  # Number of line segments composing a hatch
radius = 0.2  # Minimum radius between points
# (the smaller, the longer to compute)

P = blue_noise((11, 11), radius=radius) - (0.5, 0.5)
D = scipy.spatial.distance.cdist(P, P)
D.sort(axis=1)
S = []
vor = scipy.spatial.Voronoi(P)
for i in range(len(vor.point_region)):
    region = vor.regions[vor.point_region[i]]
    if not -1 in region:
        verts = np.array([vor.vertices[i] for i in region])
        poly = shapely.geometry.Polygon(verts)
        H = 1.25 * D[i, 1] * hatch(h) + P[i]
        for i in range(len(H)):
            line = shapely.geometry.LineString(H[i])
            intersect = poly.intersection(line)
            if intersect:
                S.append(intersect.coords)

# Grey background using thick lines
hatches = LineCollection(S, color="#eeeeee", linewidth=7, capstyle="round", zorder=-20)
ax.add_collection(hatches)

# Actual hatches
hatches = LineCollection(S, color="black", linewidth=1.5, capstyle="round", zorder=-10)
ax.add_collection(hatches)

# Plain rectangle
rectangle = plt.Rectangle((0, 0), 10, 10, fc="none", ec="white", lw=3.5)
ax.add_patch(rectangle)
rectangle = plt.Rectangle((0, 0), 10, 10, fc="white", ec="black", lw=2.5)
ax.add_patch(rectangle)


# A cheap map using Perlin noise and contour/contourf
shape = 256, 256
scale = 150
octaves = 5
persistence = 0.5
lacunarity = 2.5
Z = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        Z[i][j] = noise.pnoise2(
            i / scale,
            j / scale,
            octaves=octaves,
            persistence=persistence,
            lacunarity=lacunarity,
            repeatx=1024,
            repeaty=1024,
            base=0,
        )
X = np.linspace(0, 10, 256)
Y = np.linspace(0, 10, 256)
plt.contourf(X, Y, Z, 2, colors=["#eeeeee", "#ffffff"], zorder=10)
plt.contour(X, Y, Z, 2, colors="black", linestyles="-", zorder=10)


# Text (could be factorized)
plt.text(1.0, 5.25, "MATPLOTLIB", family="Celtic Garamond the 2nd", size=16, zorder=20)

plt.scatter([6.5], [6.15], s=25, color="black", zorder=20)
plt.text(6.65, 6.20, "Beautiful", family="Morris Roman", size=12, zorder=20)

plt.scatter([1], [7.5], s=25, color="black", zorder=20)
plt.text(1, 7.75, "Versatile", ha="center", family="Morris Roman", size=12, zorder=20)

plt.scatter([1.7], [1.7], s=25, color="black", zorder=20)
plt.text(1.7, 1.35, "Powerful", ha="center", family="Morris Roman", size=12, zorder=20)

plt.scatter([6.2], [3.2], s=25, color="black", zorder=20)
plt.text(6.2, 2.8, "Scalable", ha="center", family="Morris Roman", size=12, zorder=20)


# Wind rose at the bottom right
V = np.zeros((8, 2, 3, 2))
for i in range(4):
    theta = np.pi / 4 + i * np.pi / 2
    c, s = np.cos(theta), np.sin(theta)
    Z = np.array([[c, s], [-s, c]])
    V[i, 0] = [(0, 0), (-1, 1), (0, 5)] @ Z.T
    V[i, 1] = [(0, 0), (+1, 1), (0, 5)] @ Z.T
    theta -= np.pi / 4
    c, s = np.cos(theta), np.sin(theta)
    Z = np.array([[c, s], [-s, c]])
    V[4 + i, 0] = [(0, 0), (-1, 1), (0, 5)] @ Z.T
    V[4 + i, 1] = [(0, 0), (+1, 1), (0, 5)] @ Z.T
V = V.reshape(16, 3, 2)
V = 0.9 * V / 5 + (9, 1)
FC = np.zeros((16, 4))
FC[0::2] = 0, 0, 0, 1
FC[1::2] = 1, 1, 1, 1
collection = PolyCollection(V, edgecolors="black", facecolors=FC, lw=0.75, zorder=20)
ax.add_collection(collection)


# Done
ax.set_xlim(-1, 11), ax.set_xticks([])
ax.set_ylim(-1, 11), ax.set_yticks([])
plt.tight_layout()
# plt.savefig("dyson-hatching.pdf")
plt.show()
