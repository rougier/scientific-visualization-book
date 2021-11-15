# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import imageio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.backends.backend_agg import FigureCanvasAgg

figsize = 4.25, 5 * 0.55
xlim = 0.0, 11.0
ylim = 0.5, 5.0
dx = figsize[0] / (xlim[1] - xlim[0])
dy = figsize[1] / (ylim[1] - ylim[0])
widths = 1, 2, 3, 4, 5, 6
w, h = 0.75 * 10 / len(widths), 0.5
figsize = w * dx, h * dy
dpi = 600

for width in widths:
    plt.rcParams["hatch.linewidth"] = width
    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1], xlim=[0, 1], ylim=[0, 1])
    ax.axis("off")
    canvas = FigureCanvasAgg(fig)
    rect = Rectangle(
        (0, 0), 1, 1, hatch="/", facecolor="0.85", edgecolor="0.00", linewidth=0.0
    )
    ax.add_patch(rect)
    canvas.draw()
    image = np.frombuffer(canvas.tostring_rgb(), dtype="uint8")
    image = image.reshape(int(figsize[1] * dpi), int(figsize[0] * dpi), 3)
    imageio.imwrite("hatch-%d.png" % width, image)
