# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

p = plt.rcParams
p["figure.figsize"] = 7, 7
p["figure.dpi"] = 100
p["figure.facecolor"] = "#ffffff"
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
gspec = gridspec.GridSpec(
    ncols=ncols, nrows=nrows, figure=fig, width_ratios=[1, 2], height_ratios=[1, 2]
)


def plot(ax, xmax=1, ymax=1):
    ax.set_xlim(0, xmax)
    ax.set_xticks(np.linspace(0, xmax, 4 * xmax + 1))
    ax.set_xlabel("X Label")
    ax.set_ylim(0, ymax)
    ax.set_yticks(np.linspace(0, ymax, 4 * ymax + 1))
    ax.set_ylabel("Y Label")
    ax.set_title("Title", family="Roboto", weight=500)


if 0:  # No constraints
    plot(plt.subplot(gspec[0, 0]))
    plot(plt.subplot(gspec[1, 0]))
    plot(plt.subplot(gspec[0, 1]))
    plot(plt.subplot(gspec[1, 1]))

if 0:  # Aspect is constrained
    plot(plt.subplot(gspec[0, 0]))
    plot(plt.subplot(gspec[1, 0], aspect=1))
    plot(plt.subplot(gspec[0, 1], aspect=1))
    plot(plt.subplot(gspec[1, 1], aspect=1))

if 1:  # Aspect is constrained but limits fit
    plot(plt.subplot(gspec[0, 0]))
    plot(plt.subplot(gspec[1, 0], aspect=1), ymax=2)
    plot(plt.subplot(gspec[0, 1], aspect=1), xmax=2)
    plot(plt.subplot(gspec[1, 1], aspect=1), xmax=2, ymax=2)

plt.savefig("../../figures/layout/layout-aspect-3.pdf")
plt.show()
