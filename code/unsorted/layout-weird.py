# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
# Weird axes layout (just for fun)
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

p = plt.rcParams
p["figure.figsize"] = 7, 7
p["font.sans-serif"] = ["Roboto Condensed"]
p["font.weight"] = "light"
p["ytick.minor.visible"] = True
p["xtick.minor.visible"] = True
p["axes.grid"] = True
p["grid.color"] = "0.5"
p["grid.linewidth"] = 0.5


X = np.linspace(-np.pi, np.pi, 257, endpoint=True)
C, S = np.cos(X), np.sin(X)

fig = plt.figure(constrained_layout=True)
nrows, ncols = 2, 2
gspec = gridspec.GridSpec(ncols=ncols, nrows=nrows, figure=fig)


ax = plt.subplot(1, 1, 1)
ax.set_xlim(0, 1)
ax.set_xticks(np.linspace(0, 1, 5))
ax.set_xlabel("X Label")
ax.set_ylim(0, 1)
ax.set_yticks(np.linspace(0, 1, 5))
ax.set_ylabel("Y Label")
ax.set_title("Close-up", x=0.25, family="Roboto", weight=500)

# Manual edit for the axes limits
ax2 = fig.add_axes([0.53, 0.515, 0.4485, 0.4505])
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.grid(False)
ax2.set_xticks([])
ax2.set_yticks([])

n = 10000
X = np.random.normal(0.25, 1, n)
Y = np.random.normal(0.25, 1, n)

# Manual edit for the axes limits
ax3 = fig.add_axes([0.575, 0.56, 0.4, 0.4])
ax3.set_title("Distribution", family="Roboto", weight=500)
ax3.set_xlim(-3, 3)
ax3.set_ylim(-3, 3)
S = ax3.scatter(X, Y, s=0.5, linewidths=0, color=".5")
S = ax3.scatter(X, Y, s=0.5, linewidths=0, color="black")
from matplotlib.patches import Polygon

p = Polygon(
    [(0, 0), (0, 1), (0.5, 1), (0.5, 0.5), (1, 0.5), (1, 0), (0, 0)],
    transform=ax3.transData,
    closed=True,
    facecolor="None",
    edgecolor="black",
    linewidth=0.75,
    zorder=50,
)
S.set_clip_path(p)
ax3.add_artist(p)


S = ax.scatter(X, Y, s=100, linewidths=1, color="black")
S = ax.scatter(X, Y, s=100, linewidths=0, color="white")
for s in np.linspace(5, 100, 10):
    S = ax.scatter(X, Y, s=s, linewidths=0, alpha=0.05, color="red")
S = ax.scatter(X, Y, s=3, linewidths=0, alpha=0.75, color="black")

# plt.savefig("../figures/layout-weird.pdf")
plt.show()
