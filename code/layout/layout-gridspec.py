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
nrows, ncols = 3, 3
gspec = gridspec.GridSpec(ncols=ncols, nrows=nrows, figure=fig)


def plot(ax, text):
    ax.set_xlim(0, 1)
    ax.set_xticks(np.linspace(0, 1, 5))
    ax.set_xlabel("X Label")
    ax.set_ylim(0, 1)
    ax.set_yticks(np.linspace(0, 1, 5))
    ax.set_ylabel("Y Label")
    ax.text(
        0.5, 0.5, text, alpha=0.75, ha="center", va="center", weight="bold", size=12
    )
    ax.set_title("Title", family="Roboto", weight=500)


for i in range(ncols):
    plot(plt.subplot(gspec[0, i]), "subplot(gspec[0,%d])" % i)
for i in range(1, nrows):
    plot(plt.subplot(gspec[i, 0]), "subplot(gspec[%d,0])" % i)
plot(plt.subplot(gspec[1:, 1:]), "subplot(gspec[1:,1:])")

plt.savefig("../../figures/layout/layout-gridspec.pdf")
plt.show()
