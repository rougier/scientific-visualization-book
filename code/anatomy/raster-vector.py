# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.patches import Rectangle


def pixelated_text(dpi=100):
    fig = Figure(figsize=(1, 1), dpi=dpi)
    canvas, ax = FigureCanvasAgg(fig), fig.gca()
    ax.text(0.5, 0.5, "a", fontsize=75, ha="center", va="center")
    ax.axis("off")
    canvas.draw()
    image = np.frombuffer(canvas.tostring_argb(), dtype="uint8")
    image = image.reshape(dpi, dpi, 4)
    image = np.roll(image, 3, axis=2)
    return image


def square(position, size, edgecolor, facecolor, zorder):
    rect = Rectangle(
        position,
        size,
        size,
        transform=ax.transAxes,
        clip_on=False,
        zorder=zorder,
        linewidth=0.5,
        edgecolor=edgecolor,
        facecolor=facecolor,
    )
    ax.add_artist(rect)


image = pixelated_text(75)
fig = plt.figure(figsize=(4.25, 2), dpi=100)

# Left (raster)
ax = plt.subplot(
    1, 2, 1, frameon=False, aspect=1, xticks=[], yticks=[], xlim=[0, 1], ylim=[0, 1]
)

ax.imshow(image, extent=[0.1, 1.0, 0.1, 1.0], zorder=10, interpolation="nearest")
square((0.1, 0.1), 0.9, "black", "None", 20)

square((0.0, 0.0), 0.2, "black", "white", 20)
ax.imshow(image, extent=[0.0, 0.2, 0.0, 0.2], zorder=30, interpolation="nearest")
square((0.0, 0.0), 0.2, "black", "None", 40)

ax.text(0.55, 1.025, "Raster rendering", fontsize="small", ha="center", va="bottom")
ax.text(
    0.6, 0.1 - 0.025, ".PNG / .JPG / .TIFF", fontsize="x-small", ha="center", va="top"
)

# Right (vector)
ax = plt.subplot(
    1, 2, 2, frameon=False, aspect=1, xticks=[], yticks=[], xlim=[0, 1], ylim=[0, 1]
)
ax.text(0.55, 0.55, "a", fontsize=100, ha="center", va="center", color="#000099")
square((0.1, 0.1), 0.9, "#000099", "None", 20)
square((0.0, 0.0), 0.2, "#000099", "white", 20)
ax.text(
    0.1,
    0.1,
    "a",
    fontsize=22,
    ha="center",
    va="center",
    clip_on=False,
    zorder=30,
    color="#000099",
)
square((0.0, 0.0), 0.2, "#000099", "None", 40)

ax.text(
    0.55,
    1.025,
    "Vector rendering",
    fontsize="small",
    ha="center",
    va="bottom",
    color="#000099",
)
ax.text(
    0.6,
    0.1 - 0.025,
    ".PDF / .SVG / .PS",
    fontsize="x-small",
    ha="center",
    va="top",
    color="#000099",
)


plt.savefig("../../figures/anatomy/raster-vector.pdf", dpi=600)
plt.show()
