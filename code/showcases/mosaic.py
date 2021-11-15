# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi
from math import sqrt, ceil, floor, pi, cos, sin
from matplotlib.collections import PolyCollection


def blue_noise(shape, radius, k=30, seed=None):
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


I = plt.imread("../data/poppy.png")
P = blue_noise((1, 1), radius=0.005)
P = np.append(P, [[+999, +999], [-999, +999], [+999, -999], [-999, -999]], axis=0)
voronoi = Voronoi(P)


polys, colors = [], []
for i, region in enumerate(voronoi.regions):
    if -1 in region:
        continue
    poly = [list(voronoi.vertices[i]) for i in region]
    if len(poly) <= 0:
        continue
    polys.append(poly)
    index = np.where(voronoi.point_region == i)[0][0]
    row, col = int((1 - P[index, 1]) * I.shape[1]), int(P[index, 0] * I.shape[0])
    colors.append(I[row, col])
colors = np.array(colors)
collection = PolyCollection(
    polys, linewidth=0.5, facecolor=colors, edgecolors=colors * 0.5
)

fig = plt.figure(figsize=(6, 6))
ax = fig.add_axes([0, 0, 1, 1], xlim=[0, 1], ylim=[0, 1], aspect=1)
ax.axis("off")

ax.add_collection(collection)

plt.savefig("../../figures/showcases/mosaic.pdf")
plt.show()
