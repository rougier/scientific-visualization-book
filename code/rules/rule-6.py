import numpy as np
import matplotlib

import matplotlib.pylab as plt
import matplotlib.patheffects as PathEffects
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import matplotlib.gridspec as gridspec


def make(ax1, ax2, cmap, title, y, color="k"):
    # -----------------
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.set_xticks([])
    ax1.set_yticks([0, 0.5, 1])
    ax1.get_yaxis().tick_left()

    ax1.axhline(y, lw=1, c=color, xmin=0, xmax=1)
    ax1.text(0.025, y + 0.015, "Slice y=%.2f" % y, fontsize=10, color=color)
    ax1.imshow(Z, cmap=cmap, origin="upper", extent=[0, 1, 0, 1])
    ax1.set_xticks([]), ax1.set_yticks([])
    ax1.set_title(title)

    ax2.set_xlim(0, 1)
    ax2.set_ylim(-0.1, +1.1)
    ax2.set_xticks([0, 0.5, 1])
    ax2.get_xaxis().tick_bottom()
    ax2.set_yticks([0, 1])
    ax2.get_yaxis().tick_left()
    ax2.plot(T / np.pi, Z[int(1024 * (1 - y))], c="k", lw=0.5)
    ax2.axis("off")
    ax2.text(0.025, 1.25, "Slice detail")


if __name__ == "__main__":
    fg = 0.0, 0.0, 0.0
    bg = 1.0, 1.0, 1.0
    matplotlib.rcParams["xtick.direction"] = "out"
    matplotlib.rcParams["ytick.direction"] = "out"
    matplotlib.rcParams["font.size"] = 12.0
    matplotlib.rc("axes", facecolor=bg)
    matplotlib.rc("axes", edgecolor=fg)
    matplotlib.rc("xtick", color=fg)
    matplotlib.rc("ytick", color=fg)
    matplotlib.rc("figure", facecolor=bg)
    matplotlib.rc("savefig", facecolor=bg)

    plt.figure(figsize=(18, 6))

    G = gridspec.GridSpec(2, 3, width_ratios=[1, 1, 1], height_ratios=[15, 1])

    T = np.linspace(0, np.pi, 2 * 512)
    X, Y = np.meshgrid(T, T)
    Z = np.power(Y / 2, 5) * np.sin(np.exp(np.pi / 2 * X))
    Z = (Z - Z.min()) / (Z.max() - Z.min())

    ax1 = plt.subplot(G[0, 0], aspect=1)
    ax2 = plt.subplot(G[1, 0])
    make(ax1, ax2, plt.cm.rainbow, "Rainbow colormap (qualitative)", y=0.3)

    ax1 = plt.subplot(G[0, 1], aspect=1)
    ax2 = plt.subplot(G[1, 1])
    make(ax1, ax2, plt.cm.seismic, "Seismic colormap (diverging)", y=0.2)

    ax1 = plt.subplot(G[0, 2], aspect=1)
    ax2 = plt.subplot(G[1, 2])
    make(ax1, ax2, plt.cm.Purples, "Purples colormap (sequential)", 0.1, "white")

    plt.savefig("../../figures/rules/rule-6.pdf")
    plt.show()
