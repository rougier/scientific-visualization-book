# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Rectangle
from matplotlib.patches import ConnectionPatch


fig = plt.figure(figsize=(5, 4))

n = 5
gs = GridSpec(n, n + 1)

ax = plt.subplot(
    gs[:n, :n], xlim=[-1, +1], xticks=[], ylim=[-1, +1], yticks=[], aspect=1
)

np.random.seed(123)
X = np.random.normal(0, 0.35, 1000)
Y = np.random.normal(0, 0.35, 1000)
ax.scatter(X, Y, edgecolor="None", facecolor="C1", alpha=0.5)

I = np.random.choice(len(X), size=n, replace=False)
Px, Py = X[I], Y[I]
I = np.argsort(Y[I])[::-1]
Px, Py = Px[I], Py[I]

ax.scatter(Px, Py, edgecolor="black", facecolor="None", linewidth=0.75)

dx, dy = 0.075, 0.075
for i, (x, y) in enumerate(zip(Px, Py)):
    sax = plt.subplot(
        gs[i, n],
        xlim=[x - dx, x + dx],
        xticks=[],
        ylim=[y - dy, y + dy],
        yticks=[],
        aspect=1,
    )
    sax.scatter(X, Y, edgecolor="None", facecolor="C1", alpha=0.5)
    sax.scatter(Px, Py, edgecolor="black", facecolor="None", linewidth=0.75)

    sax.text(
        1.1,
        0.5,
        "Point " + chr(ord("A") + i),
        rotation=90,
        size=8,
        ha="left",
        va="center",
        transform=sax.transAxes,
    )

    rect = Rectangle(
        (x - dx, y - dy),
        2 * dx,
        2 * dy,
        edgecolor="black",
        facecolor="None",
        linestyle="--",
        linewidth=0.75,
    )
    ax.add_patch(rect)

    con = ConnectionPatch(
        xyA=(x, y),
        coordsA=ax.transData,
        xyB=(0, 0.5),
        coordsB=sax.transAxes,
        linestyle="--",
        linewidth=0.75,
        patchA=rect,
        arrowstyle="->",
    )
    fig.add_artist(con)


plt.tight_layout()
plt.savefig("../../figures/ornaments/annotation-zoom.pdf")
plt.show()
