# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: Creative Commons BY-NC-SA International 4.0
# ----------------------------------------------------------------------------
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import findfont, FontProperties


def font_text(x, y, text, family, dy=0):

    ax.text(x, y + dy, text, family=family, size=size, va="bottom")
    font = findfont(FontProperties(family=family))
    filename = os.path.basename(font)
    ax.text(
        x,
        y,
        filename,
        va="top",
        family="Roboto Condensed",
        weight=400,
        size=10,
        color="0.5",
    )


plt.figure(figsize=(8, 2), dpi=100)
size = 20
dx = 15
xmin, xmax = -1, 4 * dx - 5

ax = plt.subplot(
    3, 1, 1, frameon=False, xlim=(xmin, xmax), ylim=(-1, 1), xticks=[], yticks=[]
)
font_text(0 * dx, 0, "Serif", "Serif")
font_text(1 * dx, 0, "Sans", "Sans")
font_text(2 * dx, 0, "Monospace", "Monospace")
font_text(3 * dx, 0, "Cursive", "Cursive", -0.25)


ax = plt.subplot(
    3, 1, 2, frameon=False, xlim=(xmin, xmax), ylim=(-1, 1), xticks=[], yticks=[]
)
font_text(0 * dx, 0, "Serif", "Roboto Slab")
font_text(1 * dx, 0, "Sans", "Roboto Condensed")
font_text(2 * dx, 0, "Monospace", "Roboto Mono")
font_text(3 * dx, 0, "Cursive", "Merienda", -0.25)


ax = plt.subplot(
    3, 1, 3, frameon=False, xlim=(xmin, xmax), ylim=(-1, 1), xticks=[], yticks=[]
)
font_text(0 * dx, 0, "Serif", "Source Serif Pro")
font_text(1 * dx, 0, "Sans", "Source Sans Pro")
font_text(2 * dx, 0, "Monospace", "Source Code Pro")
font_text(3 * dx, 0, "Cursive", "ITC Zapf Chancery")

# ax.text(0*dx, 0, "Serif",      family="Roboto Slab",      size=size)
# ax.text(0*dx, -0.5, find("Roboto Slab"),
#         family="Roboto Slab", weight=300, size=8, color="0.25")

# ax.text(1*dx, 0, "Sans-serif", family="Roboto Condensed", size=size)
# ax.text(2*dx, 0, "Monospace",  family="Roboto Mono",      size=size)
# ax.text(3*dx, 0, "Cursive",    family="Pacifico",         size=size)

plt.tight_layout()
plt.savefig("../../figures/typography/typography-font-stacks.pdf", dpi=100)
plt.show()
