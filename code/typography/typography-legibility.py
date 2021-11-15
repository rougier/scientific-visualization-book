# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: Creative Commons BY-NC-SA International 4.0
# ----------------------------------------------------------------------------
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patheffects import Stroke, Normal

dpi = 200
figsize = (4.25, 3.0)

shape = 20, 80
I = np.random.uniform(0, 1, shape)
cmap = plt.cm.get_cmap("gray")
x, y = 0.5, 2

fig = plt.figure(figsize=figsize, dpi=dpi)

# Regular
ax = fig.add_subplot(4, 2, 1, xticks=[], yticks=[])
ax.imshow(I, cmap=cmap, origin="lower")
ax.text(x, y, "Read me", color="black", transform=ax.transData)

ax = fig.add_subplot(4, 2, 2, xticks=[], yticks=[])
ax.imshow(I, cmap=cmap, origin="lower")
ax.text(x, y, "Read me", color="white", transform=ax.transData)

# Bold
ax = fig.add_subplot(4, 2, 3, xticks=[], yticks=[])
ax.imshow(I, cmap=cmap, origin="lower")
ax.text(x, y, "Read me", color="black", weight="bold", transform=ax.transData)

ax = fig.add_subplot(4, 2, 4, xticks=[], yticks=[])
ax.imshow(I, cmap=cmap, origin="lower")
ax.text(x, y, "Read me", color="white", weight="bold", transform=ax.transData)

# Boxes
ax = fig.add_subplot(4, 2, 5, xticks=[], yticks=[])
ax.imshow(I, cmap=cmap, origin="lower")
ax.text(
    x,
    y,
    "Read me",
    color="black",
    transform=ax.transData,
    bbox={"facecolor": "white", "edgecolor": "None", "pad": 1, "alpha": 0.75},
)

ax = fig.add_subplot(4, 2, 6, xticks=[], yticks=[])
ax.imshow(I, cmap=cmap, origin="lower")
ax.text(
    x,
    y,
    "Read me",
    color="white",
    transform=ax.transData,
    bbox={"facecolor": "black", "edgecolor": "None", "pad": 1, "alpha": 0.75},
)

ax = fig.add_subplot(4, 2, 7, xticks=[], yticks=[])
ax.imshow(I, cmap=cmap, origin="lower")
text = ax.text(x, y, "Read me", color="black", transform=ax.transData)
text.set_path_effects([Stroke(linewidth=1.5, foreground="white"), Normal()])

ax = fig.add_subplot(4, 2, 8, xticks=[], yticks=[])
ax.imshow(I, cmap=cmap, origin="lower")
text = ax.text(x, y, "Read me", color="white", transform=ax.transData)
text.set_path_effects([Stroke(linewidth=1.5, foreground="black"), Normal()])

plt.tight_layout()
plt.savefig("../../figures/typography/typography-legibility.pdf", dpi=600)
plt.show()
