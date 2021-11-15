# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.patches import Circle
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvas


plt.rc("font", family="Roboto")
plt.rc("xtick", labelsize="small")
plt.rc("ytick", labelsize="small")
plt.rc("axes", labelsize="medium", titlesize="medium")


P = np.random.uniform(0, 5, (500, 2))
C = np.random.uniform(5, 25, 500)


def plot(ax):
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1.0))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))
    ax.yaxis.set_minor_formatter(ticker.FormatStrFormatter("%.2f"))
    for i, label in enumerate(ax.get_yticklabels(which="minor")):
        label.set_size(7)
    ax.xaxis.set_minor_formatter(ticker.FormatStrFormatter("%.2f"))
    for i, label in enumerate(ax.get_xticklabels(which="minor")):
        label.set_size(7)
    ax.grid(True, "minor", color="0.85", linewidth=0.50, zorder=-20)
    ax.grid(True, "major", color="0.65", linewidth=0.75, zorder=-10)

    ax.scatter(P[:, 0], P[:, 1], C, color="black", zorder=10)


fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(xlim=(0.0, 5), ylim=(0.0, 5), aspect=1)
plot(ax)

ifig = Figure(figsize=(6, 6), dpi=100, frameon=False)
canvas = FigureCanvas(ifig)
iax = ifig.add_subplot(xlim=(0.0, 5), ylim=(0.0, 5), aspect=1)
plot(iax)
plt.tight_layout()
canvas.draw()
Z = np.array(canvas.renderer.buffer_rgba())
del ifig


background = fig.canvas.copy_from_bbox(ax.bbox)


def on_motion(event):
    x, y = event.xdata, event.ydata
    if x is None or y is None:
        return
    fig.canvas.restore_region(background)

    circle_bg.set_center((x, y))
    ax.draw_artist(circle_bg)

    circle_fg.set_center((x, y))
    ax.draw_artist(circle_fg)

    image.set_extent([0 - x, 10 - x, 0 - y, 10 - y])
    image.set_clip_path(circle_bg)
    ax.draw_artist(image)

    fig.canvas.blit(ax.bbox)


cid = fig.canvas.mpl_connect("motion_notify_event", on_motion)

circle_bg = Circle(
    (1, 1),
    1,
    transform=ax.transData,
    zorder=20,
    clip_on=False,
    edgecolor="none",
    facecolor="white",
)
ax.add_artist(circle_bg)

circle_fg = Circle(
    (1, 1),
    1,
    transform=ax.transData,
    zorder=30,
    clip_on=False,
    linewidth=2,
    edgecolor="black",
    facecolor="None",
)
ax.add_artist(circle_fg)

image = ax.imshow(Z, extent=[0, 5, 0, 5], zorder=25, clip_on=True)
image.set_extent([0, 10, 0, 10])
image.set_clip_path(circle_bg)

plt.tight_layout()
plt.show()
