# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection


fig = plt.figure(figsize=(4.25, 4.25 * 95 / 115))
ax = fig.add_axes(
    [0, 0, 1, 1],
    frameon=False,
    aspect=1,
    xlim=(0 - 5, 100 + 10),
    ylim=(-10, 80 + 5),
    xticks=[],
    yticks=[],
)


box = mpatches.FancyBboxPatch(
    (0, 0),
    100,
    83,
    mpatches.BoxStyle("Round", pad=0, rounding_size=2),
    linewidth=1.0,
    facecolor="0.9",
    edgecolor="black",
)
ax.add_artist(box)

box = mpatches.FancyBboxPatch(
    (0, 0),
    100,
    75,
    mpatches.BoxStyle("Round", pad=0, rounding_size=0),
    linewidth=1.0,
    facecolor="white",
    edgecolor="black",
)
ax.add_artist(box)


box = mpatches.Rectangle(
    (5, 5), 45, 30, zorder=10, linewidth=1.0, facecolor="white", edgecolor="black"
)
ax.add_artist(box)

box = mpatches.Rectangle(
    (5, 40), 45, 30, zorder=10, linewidth=1.0, facecolor="white", edgecolor="black"
)
ax.add_artist(box)

box = mpatches.Rectangle(
    (55, 5), 40, 65, zorder=10, linewidth=1.0, facecolor="white", edgecolor="black"
)
ax.add_artist(box)

# Window button
X, Y = [5, 10, 15], [79, 79, 79]
plt.scatter(X, Y, s=75, zorder=10, edgecolor="black", facecolor="white", linewidth=1)


# Window size extension
X, Y = [0, 0], [0, -8]
plt.plot(X, Y, color="black", linestyle=":", linewidth=1, clip_on=False)

X, Y = [100, 100], [0, -8]
plt.plot(X, Y, color="black", linestyle=":", linewidth=1, clip_on=False)

X, Y = [100, 108], [0, 0]
plt.plot(X, Y, color="black", linestyle=":", linewidth=1, clip_on=False)

X, Y = [100, 108], [75, 75]
plt.plot(X, Y, color="black", linestyle=":", linewidth=1, clip_on=False)


def ext_arrow(p0, p1, p2, p3):
    p0, p1 = np.asarray(p0), np.asarray(p1)
    p2, p3 = np.asarray(p2), np.asarray(p3)
    ax.arrow(
        *p0,
        *(p1 - p0),
        zorder=20,
        linewidth=0,
        length_includes_head=True,
        width=0.4,
        head_width=2,
        head_length=2,
        color="black"
    )
    ax.arrow(
        *p3,
        *(p2 - p3),
        zorder=20,
        linewidth=0,
        length_includes_head=True,
        width=0.4,
        head_width=2,
        head_length=2,
        color="black"
    )
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], linewidth=0.9, color="black")


def int_arrow(p0, p1):
    p0, p1 = np.asarray(p0), np.asarray(p1)
    ax.arrow(
        *((p0 + p1) / 2),
        *((p1 - p0) / 2),
        zorder=20,
        linewidth=0,
        length_includes_head=True,
        width=0.4,
        head_width=2,
        head_length=2,
        color="black"
    )
    ax.arrow(
        *((p0 + p1) / 2),
        *(-(p1 - p0) / 2),
        zorder=20,
        linewidth=0,
        length_includes_head=True,
        width=0.4,
        head_width=2,
        head_length=2,
        color="black"
    )


x = 0
y = 10
ext_arrow((x - 4, y), (x, y), (x + 5, y), (x + 9, y))
ax.text(x + 9.5, y, "left", ha="left", va="center", size="x-small", zorder=20)

x += 50
ext_arrow((x - 4, y), (x, y), (x + 5, y), (x + 9, y))
ax.text(x - 4.5, y, "wspace", ha="right", va="center", size="x-small", zorder=20)

x += 45
ext_arrow((x - 4, y), (x, y), (x + 5, y), (x + 9, y))
ax.text(x - 4.5, y, "right", ha="right", va="center", size="x-small", zorder=20)

y = 0
x = 25
ext_arrow((x, y - 4), (x, y), (x, y + 5), (x, y + 9))
ax.text(x, y + 9.5, "bottom", ha="center", va="bottom", size="x-small", zorder=20)

y += 35
ext_arrow((x, y - 4), (x, y), (x, y + 5), (x, y + 9))
ax.text(x, y - 4.5, "hspace", ha="center", va="top", size="x-small", zorder=20)

y += 35
ext_arrow((x, y - 4), (x, y), (x, y + 5), (x, y + 9))
ax.text(x, y - 4.5, "top", ha="center", va="top", size="x-small", zorder=20)

int_arrow((0, -5), (100, -5))
ax.text(
    50,
    -5,
    "figure width",
    backgroundcolor="white",
    zorder=30,
    ha="center",
    va="center",
    size="x-small",
)

int_arrow((105, 0), (105, 75))
ax.text(
    105,
    75 / 2,
    "figure height",
    backgroundcolor="white",
    zorder=30,
    rotation="vertical",
    ha="center",
    va="center",
    size="x-small",
)

int_arrow((55, 62.5), (95, 62.5))
ax.text(
    75,
    62.5,
    "axes width",
    backgroundcolor="white",
    zorder=30,
    ha="center",
    va="center",
    size="x-small",
)

int_arrow((62.5, 5), (62.5, 70))
ax.text(
    62.5,
    35,
    "axes height",
    backgroundcolor="white",
    zorder=30,
    rotation="vertical",
    ha="center",
    va="center",
    size="x-small",
)


plt.savefig("reference-axes-adjustment.pdf", dpi=600)
plt.show()
