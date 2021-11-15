# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(5.5, 1.5))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)  # , aspect=1)
# ymin, ymax=  0, 7
# xmin, xmax = 0, figsize[0]/figsize[1]
# ax.set_xlim(xmin, xmax), ax.set_xticks([])
# ax.set_ylim(ymin, ymax), ax.set_yticks([])
# ax = plt.subplot()

palettes = {
    "raw": ["b", "g", "r", "c", "m", "y", "k", "w"],
    "rgba": [(1, 0, 0), (1, 0, 0, 0.75), (1, 0, 0, 0.50), (1, 0, 0, 0.25)],
    "HexRGBA": ["#FF0000", "#FF0000BB", "#FF000088", "#FF000044"],
    "cycle": ["C%d" % i for i in range(10)],
    "grey": ["%1.1f" % (i / 10) for i in range(11)],
    "name": ["DarkRed", "Firebrick", "Crimson", "IndianRed", "Salmon"],
}


ymin, ymax = 0, len(palettes)
xmin, xmax = 0, 22
ax.set_xlim(xmin, xmax), ax.set_xticks([])
ax.set_ylim(ymin, ymax), ax.set_yticks([])


for y, (name, colors) in enumerate(palettes.items()):
    C = mpl.colors.to_rgba_array(colors).reshape((1, len(colors), 4))
    ax.imshow(C, extent=[xmin, xmax, y + 0.025, y + 0.95])
    dx = (xmax - xmin) / len(colors)
    for i in range(len(colors)):
        color = "white"
        if colors[i] in ["1.0", "w"]:
            color = "black"
        text = str(colors[i]).replace(" ", "")
        ax.text(
            (i + 0.5) * dx,
            y + 0.5,
            text,
            color=color,
            zorder=10,
            family="Source Code Pro",
            size=9,
            ha="center",
            va="center",
        )

plt.savefig("../../figures/reference/colorspec.pdf")
plt.show()
