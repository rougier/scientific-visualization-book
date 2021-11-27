# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import bluenoise
import numpy as np
import scipy.spatial
import shapely.geometry
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


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


# Points (blue noise distribution)
P = bluenoise.generate((10, 10), radius=0.5)

# Voronoi cells
V = scipy.spatial.Voronoi(P)

# Sorted distances between points
D = scipy.spatial.distance.cdist(P, P)
D.sort(axis=1)


# Actual drawing
fig = plt.figure(figsize=(9, 3.25))


# Point + Voronoi cells
ax = plt.subplot(1, 3, 1, aspect=1, xlim=[0, 10], xticks=[], ylim=[0, 10], yticks=[])
for i in range(len(V.point_region)):
    region = V.regions[V.point_region[i]]
    if not -1 in region:
        verts = np.array([V.vertices[i] for i in region])
        cell = plt.Polygon(verts, edgecolor=".25", facecolor="None")
        ax.add_artist(cell)
ax.scatter(P[:, 0], P[:, 1], s=5, color="black", zorder=10)
ax.set_title("Random points (blue noise)")


# Hatches (unclipped)
ax = plt.subplot(1, 3, 2, aspect=1, xlim=[0, 10], xticks=[], ylim=[0, 10], yticks=[])
S = []
for i in range(len(V.point_region)):
    region = V.regions[V.point_region[i]]
    if not -1 in region:
        verts = np.array([V.vertices[i] for i in region])
        S.extend((1.25 * D[i, 1] * hatch(5) + P[i]))
ax.add_collection(LineCollection(S, color="black"))
ax.set_title("Unclipped hatches")


# Hatches (clipped)
ax = plt.subplot(1, 3, 3, aspect=1, xlim=[0, 10], xticks=[], ylim=[0, 10], yticks=[])
S = []
for i in range(len(V.point_region)):
    region = V.regions[V.point_region[i]]
    if not -1 in region:
        verts = np.array([V.vertices[i] for i in region])
        poly = shapely.geometry.Polygon(verts)
        for l in 1.25 * D[i, 1] * hatch(5) + P[i]:
            line = shapely.geometry.LineString(l)
            intersect = poly.intersection(line)
            if intersect:
                S.append(intersect.coords)
ax.add_collection(LineCollection(S, color="black"))
ax.set_title("Clipped hatches")

plt.tight_layout()
plt.savefig("../../figures/beyond/dyson-hatching.pdf")
plt.show()
