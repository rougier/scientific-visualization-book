# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath
from matplotlib.collections import LineCollection
from matplotlib.collections import PathCollection
from matplotlib.collections import CircleCollection
from matplotlib.collections import PolyCollection
from matplotlib.collections import EllipseCollection
from matplotlib.collections import RegularPolyCollection
from matplotlib.collections import StarPolygonCollection
from matplotlib.collections import AsteriskPolygonCollection


fig = plt.figure(figsize=(4.25, 8 * 0.4))
ax = fig.add_axes(
    [0, 0, 1, 1],
    xlim=[0, 11],
    ylim=[0.5, 8.5],
    frameon=False,
    xticks=[],
    yticks=[],
    aspect=1,
)
y = 8


# Line collection
# ----------------------------------------------------------------------------
n = 50
segments = np.zeros((n, 2, 2))
segments[:, 0, 0] = np.linspace(1, 10.25, n) - 0.2
segments[:, 0, 1] = y - 0.2
segments[:, 1, 0] = segments[:, 0, 0] + 0.2
segments[:, 1, 1] = y + 0.15
linewidths = np.linspace(0.5, 2.5, n)

collection = LineCollection(segments, linewidths=linewidths, edgecolor="black")
ax.add_collection(collection)

ax.text(1 - 0.25, y + 0.25, "Line collection", size="small", ha="left", va="baseline")
ax.text(
    10 + 0.25,
    y + 0.25,
    "LineCollection",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1

# Circle collection
# ----------------------------------------------------------------------------
n = 10
offsets = np.ones((n, 2))
offsets[:, 0], offsets[:, 1] = np.linspace(1, 10, n), y
X, Y = offsets[:, 0], offsets[:, 1]
sizes = np.linspace(25, 100, n)
linewidths = np.linspace(1, 2, n)
facecolors = ["%.1f" % c for c in np.linspace(0.25, 0.75, n)]

collection = CircleCollection(
    sizes,
    # linewidths = linewidths,
    facecolors=facecolors,
    edgecolor="black",
    offsets=offsets,
    transOffset=ax.transData,
)
ax.add_collection(collection)

ax.text(
    X[0] - 0.25, y + 0.35, "Circle collection", size="small", ha="left", va="baseline"
)
ax.text(
    X[-1] + 0.25,
    y + 0.35,
    "CircleCollection",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1


# Ellipse collection
# ----------------------------------------------------------------------------
n = 10
offsets = np.ones((n, 2))
offsets[:, 0], offsets[:, 1] = np.linspace(1, 10, n), y
X, Y = offsets[:, 0], offsets[:, 1]
widths, heights = 15 * np.ones(n), 10 * np.ones(n)
angles = np.linspace(0, 45, n)
linewidths = np.linspace(1, 2, n)
facecolors = ["%.1f" % c for c in np.linspace(0.25, 0.75, n)]
collection = EllipseCollection(
    widths,
    heights,
    angles,
    # linewidths = linewidths,
    facecolors=facecolors,
    edgecolor="black",
    offsets=offsets,
    transOffset=ax.transData,
)
ax.add_collection(collection)
ax.text(
    X[0] - 0.25, y + 0.35, "Ellipse collection", size="small", ha="left", va="baseline"
)
ax.text(
    X[-1] + 0.25,
    y + 0.35,
    "EllipseCollection",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1


# Polygon collection
# ----------------------------------------------------------------------------
n = 10
offsets = np.ones((n, 2))
offsets[:, 0], offsets[:, 1] = np.linspace(1, 10, n) - 0.2, y + 0.1
X, Y = offsets[:, 0], offsets[:, 1]
verts = np.zeros((n, 4, 2))
verts[:] = [0, 0], [1, 0], [1, 1], [0, 1]
sizes = np.linspace(0.25, 0.50, n)
verts *= sizes.reshape(n, 1, 1)
widths, heights = 15 * np.ones(n), 10 * np.ones(n)
numsides = 5
rotation = np.pi / 4

offsets[:, 1] -= sizes / 2 - 0.25
linewidths = np.linspace(1, 2, n)
facecolors = ["%.1f" % c for c in np.linspace(0.25, 0.75, n)]
collection = PolyCollection(
    verts,
    # linewidths = linewidths,
    sizes=None,
    facecolors=facecolors,
    edgecolor="black",
    offsets=offsets,
    transOffset=ax.transData,
)
ax.add_collection(collection)
ax.text(
    1 - 0.25, y + 0.35, "Polygon collection", size="small", ha="left", va="baseline"
)
ax.text(
    10 + 0.25,
    y + 0.35,
    "PolyCollection",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1


# Path collection
# ----------------------------------------------------------------------------
n = 10
paths = []
for i in range(n):
    angle1 = np.random.randint(0, 180)
    angle2 = angle1 + np.random.randint(180, 270)
    path = mpath.Path.wedge(angle1, angle2)
    verts, codes = path.vertices * 0.25, path.codes
    path = mpath.Path(verts, codes)
    paths.append(path)

offsets = np.ones((n, 2))
offsets[:, 0], offsets[:, 1] = np.linspace(1, 10, n) + 0.2, y
X, Y = offsets[:, 0], offsets[:, 1]
sizes = np.ones(n) / 100
offsets[:, 1] -= sizes / 2 - 0.125
facecolors = ["%.1f" % c for c in np.linspace(0.25, 0.75, n)]
collection = PathCollection(
    paths,
    sizes=None,
    linewidths=1.0,
    facecolors=facecolors,
    edgecolor="black",
    offsets=offsets - (0.2, -0.25),
    transOffset=ax.transData,
)
ax.add_collection(collection)
ax.text(1 - 0.25, y + 0.35, "Path collection", size="small", ha="left", va="baseline")
ax.text(
    10 + 0.25,
    y + 0.35,
    "PathCollection",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1


# Regular collection
# ----------------------------------------------------------------------------
n = 10
offsets = np.ones((n, 2))
offsets[:, 0], offsets[:, 1] = np.linspace(1, 10, n), y
X, Y = offsets[:, 0], offsets[:, 1]
widths, heights = 15 * np.ones(n), 10 * np.ones(n)
numsides = 5
rotation = np.pi / 4
sizes = np.linspace(100, 200, n)
linewidths = np.linspace(1, 2, n)
facecolors = ["%.1f" % c for c in np.linspace(0.25, 0.75, n)]
collection = RegularPolyCollection(
    numsides,
    rotation,
    # linewidths = linewidths,
    sizes=sizes,
    facecolors=facecolors,
    edgecolor="black",
    offsets=offsets,
    transOffset=ax.transData,
)
ax.add_collection(collection)
ax.text(
    X[0] - 0.25,
    y + 0.35,
    "Regular polygon collection",
    size="small",
    ha="left",
    va="baseline",
)
ax.text(
    X[-1] + 0.25,
    y + 0.35,
    "RegularPolyCollection",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1


# Star collection
# ----------------------------------------------------------------------------
n = 10
offsets = np.ones((n, 2))
offsets[:, 0], offsets[:, 1] = np.linspace(1, 10, n), y
X, Y = offsets[:, 0], offsets[:, 1]
widths, heights = 15 * np.ones(n), 10 * np.ones(n)
numsides = 5
rotation = np.pi / 4
sizes = np.linspace(100, 200, n)
linewidths = np.linspace(1, 2, n)
facecolors = ["%.1f" % c for c in np.linspace(0.25, 0.75, n)]
collection = StarPolygonCollection(
    numsides,
    rotation,
    # linewidths = linewidths,
    sizes=sizes,
    facecolors=facecolors,
    edgecolor="black",
    offsets=offsets,
    transOffset=ax.transData,
)
ax.add_collection(collection)
ax.text(
    X[0] - 0.25, y + 0.35, "Star collection", size="small", ha="left", va="baseline"
)
ax.text(
    X[-1] + 0.25,
    y + 0.35,
    "StarPolygonCollection",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1

# Asterisk collection
# ----------------------------------------------------------------------------
n = 10
offsets = np.ones((n, 2))
offsets[:, 0], offsets[:, 1] = np.linspace(1, 10, n), y
X, Y = offsets[:, 0], offsets[:, 1]
widths, heights = 15 * np.ones(n), 10 * np.ones(n)
numsides = 8
rotation = np.pi / 4
sizes = np.linspace(50, 150, n)
linewidths = np.linspace(0.5, 2.5, n)
facecolors = ["%.1f" % c for c in np.linspace(0.35, 0.65, n)]
collection = AsteriskPolygonCollection(
    numsides,
    rotation,
    linewidths=linewidths,
    sizes=sizes,
    edgecolor=facecolors,
    offsets=offsets,
    transOffset=ax.transData,
)
ax.add_collection(collection)
ax.text(
    X[0] - 0.25, y + 0.35, "Asterisk collection", size="small", ha="left", va="baseline"
)
ax.text(
    X[-1] + 0.25,
    y + 0.35,
    "AsteriskPolygonCollection",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1


plt.savefig("reference-collection.pdf", dpi=600)
plt.show()
