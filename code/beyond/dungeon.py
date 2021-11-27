# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import scipy.spatial
import shapely.geometry
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.patches import Polygon, Ellipse
import bluenoise

# This is important because "cities" have been manually positioned
np.random.seed(1)


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


def seg_dists(p, a, b):
    """Cartesian distance from point to line segment

    Args:
        - p: np.array of single point, shape (2,) or 2D array, shape (x, 2)
        - a: np.array of shape (x, 2)
        - b: np.array of shape (x, 2)
    """
    # normalized tangent vectors
    d_ba = b - a
    d = np.divide(d_ba, (np.hypot(d_ba[:, 0], d_ba[:, 1]).reshape(-1, 1)))

    # signed parallel distance components
    # rowwise dot products of 2D vectors
    s = np.multiply(a - p, d).sum(axis=1)
    t = np.multiply(p - b, d).sum(axis=1)

    # clamped parallel distance
    h = np.maximum.reduce([s, t, np.zeros(len(s))])

    # perpendicular distance component
    # rowwise cross products of 2D vectors
    d_pa = p - a
    c = d_pa[:, 0] * d[:, 1] - d_pa[:, 1] * d[:, 0]

    return np.hypot(h, c)


# Actual drawing
fig = plt.figure(figsize=(7, 7))
fig.patch.set_facecolor("#ffffff")
ax = plt.subplot(1, 1, 1, aspect=1, frameon=False)


# Figure border using the hatch pattern. They are first spread according to
# a blue noise distribution, scaled according to the distance to the nearest
# neighbour and then lines composing the hatch are clipped against the
# corresponding Voronoi cell.
h = 4  # Number of line segments composing a hatch
radius = 0.2  # Minimum radius between points
# (the smaller, the longer to compute)

P = bluenoise.generate((15, 15), radius=radius) - (0.5, 0.5)
Walls = np.array(
    [
        [1, 1],
        [5, 1],
        [5, 3],
        [8, 3],
        [8, 2],
        [11, 2],
        [11, 5],
        [10, 5],
        [10, 6],
        [12, 6],
        [12, 8],
        [13, 8],
        [13, 10],
        [11, 10],
        [11, 12],
        [2, 12],
        [2, 10],
        [1, 10],
        [1, 7],
        [4, 7],
        [4, 10],
        [3, 10],
        [3, 11],
        [10, 11],
        [10, 10],
        [9, 10],
        [9, 8],
        [11, 8],
        [11, 7],
        [9, 7],
        [9, 5],
        [8, 5],
        [8, 4],
        [5, 4],
        [5, 6],
        [1, 6],
        [1, 1],
    ]
)
walls = Polygon(
    Walls,
    closed=True,
    zorder=10,
    facecolor="white",
    edgecolor="None",
    lw=3,
    joinstyle="round",
)
ax.add_patch(walls)

for i in range(-5, 15):
    ax.axhline(
        i,
        color=".5",
        clip_path=walls,
        zorder=20,
        linestyle=(0, (1, 4)),
        linewidth=1,
        dash_capstyle="round",
    )
    ax.axvline(
        i,
        color=".5",
        clip_path=walls,
        zorder=20,
        linestyle=(0, (1, 4)),
        linewidth=1,
        dash_capstyle="round",
    )

walls = Polygon(
    Walls,
    closed=True,
    zorder=30,
    facecolor="None",
    edgecolor="black",
    lw=3,
    joinstyle="round",
)
ax.add_patch(walls)

# ax.scatter([3.5], [7.5], s=250, marker="x", zorder=100, color="black", linewidth=5)
# ax.text(3.5, 7.5, "X",
#         family="Morris Roman", size=24, zorder=20, ha="center", va="center")

for i in range(30):
    ellipse = Ellipse(
        xy=np.random.uniform(1, 12, 2),
        width=np.random.uniform(0.05, 0.15),
        height=np.random.uniform(0.05, 0.15),
        zorder=100,
        facecolor="white",
        edgecolor="black",
        linewidth=1.25,
        clip_on=True,
        angle=np.random.uniform(0, 360),
    )
    ax.add_artist(ellipse)
    ellipse.set_clip_path(walls)

for i in range(20):
    ellipse = Ellipse(
        xy=np.random.normal(2, 0.2, 2),
        width=np.random.uniform(0.05, 0.15),
        height=np.random.uniform(0.05, 0.15),
        zorder=100,
        facecolor="white",
        edgecolor="black",
        linewidth=1.25,
        clip_on=True,
        angle=np.random.uniform(0, 360),
    )
    ax.add_artist(ellipse)
    ellipse.set_clip_path(walls)


D = scipy.spatial.distance.cdist(P, P)
D.sort(axis=1)
S = []
vor = scipy.spatial.Voronoi(P)
for i in range(len(vor.point_region)):
    region = vor.regions[vor.point_region[i]]
    if not -1 in region and min(seg_dists(vor.points[i], Walls[:-1], Walls[1:])) < 0.35:
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

ax.text(
    6,
    0.75,
    "Matplotlib Dungeon",
    clip_on=False,
    family="Morris Roman",
    size=32,
    zorder=20,
    ha="left",
    va="center",
)
ax.text(
    6,
    0.1,
    "A brand new adventure in Scientific Python",
    clip_on=False,
    family="Morris Roman",
    size=16,
    zorder=20,
    ha="left",
    va="center",
)


ax.set_xlim(0, 14), ax.set_xticks([])
ax.set_ylim(-0, 12.5), ax.set_yticks([])

plt.tight_layout()
plt.savefig("../../figures/beyond/dungeon.pdf")
plt.show()
