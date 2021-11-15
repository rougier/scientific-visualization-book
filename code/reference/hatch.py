# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import imageio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig = plt.figure(figsize=(4.25, 4.5 * 0.55))
ax = fig.add_axes(
    [0, 0, 1, 1], xlim=[0, 11], ylim=[0.5, 4.5], frameon=False, xticks=[], yticks=[]
)  # , aspect=1)
y = 3.75


# Hatch pattern
# ----------------------------------------------------------------------------
patterns = "/", "\\", "|", "-", "+", "x", "o", "O", ".", "*"
w, h = 0.75 * 10 / len(patterns), 0.5
X = np.linspace(1, 10 - w, len(patterns))

for x, pattern in zip(X, patterns):
    rect = Rectangle(
        (x, y),
        w,
        h,
        hatch=pattern * 2,
        facecolor="0.85",
        edgecolor="0.00",
        linewidth=1.0,
    )
    ax.add_patch(rect)
    plt.text(
        x + w / 2,
        y - 0.125,
        '"%s"' % pattern,
        size="x-small",
        ha="center",
        va="top",
        family="monospace",
    )

plt.text(X[0] - 0.25, y + 0.65, "Hatch pattern", size="small", ha="left", va="baseline")
plt.text(
    X[-1] + w + 0.25,
    y + 0.65,
    "hatch",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1.5


# Hatch density
# ----------------------------------------------------------------------------
patterns = "/", "//", "///", "////"
w, h = 0.75 * 10 / len(patterns), 0.5
X = np.linspace(1, 10 - w, len(patterns))

for x, pattern in zip(X, patterns):
    rect = Rectangle(
        (x, y), w, h, hatch=pattern, facecolor="0.85", edgecolor="0.00", linewidth=1.0
    )
    ax.add_patch(rect)
    plt.text(
        x + w / 2,
        y - 0.125,
        '"%s"' % pattern,
        size="x-small",
        ha="center",
        va="top",
        family="monospace",
    )

plt.text(X[0] - 0.25, y + 0.65, "Hatch density", size="small", ha="left", va="baseline")
plt.text(
    X[-1] + w + 0.25,
    y + 0.65,
    "hatch",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1.5


# Hatch linewidth (hack)
# ----------------------------------------------------------------------------
# We cannot have different hatch linewidth in a single figure and the solution
# was to generate images and to show them here. Images were generated from the
# make-hatch-linewidth.py script.
widths = 1, 2, 3, 4, 5, 6
w, h = 0.75 * 10 / len(widths), 0.5
X = np.linspace(1, 10 - w, len(widths))
for (x, width) in zip(X, widths):
    image = imageio.imread("hatch-%d.png" % width)
    ax.imshow(image, extent=[x, x + w, y, y + h])
    rect = Rectangle((x, y), w, h, facecolor="none", edgecolor="black", linewidth=1.0)
    ax.add_patch(rect)
    plt.text(
        x + w / 2,
        y - 0.125,
        "%d" % width,
        size="x-small",
        ha="center",
        va="top",
        family="monospace",
    )
plt.text(
    X[0] - 0.25, y + 0.65, "Hatch linewidth", size="small", ha="left", va="baseline"
)
plt.text(
    X[-1] + w + 0.25,
    y + 0.65,
    "rcParams['hatch.linewidth']",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1.5

plt.savefig("reference-hatch.pdf", dpi=600)
plt.show()
