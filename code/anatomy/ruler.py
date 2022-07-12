# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


class Ruler:
    """ Ruler add a whole figure axis whose ticks indicate figure
        dimensions and adapt itself to figure resize event.
    """

    def __init__(self, fig=None):
        self.fig = fig or plt.gcf()
        self.ax = None
        self.show()

    def show(self):

        if self.ax is None:
            ax = self.fig.add_axes([0, 0, 1, 1], zorder=-10, facecolor="None")
            ax.spines["right"].set_visible(False)
            ax.spines["bottom"].set_visible(False)

            ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
            ax.tick_params(
                axis="x", which="both", labelsize="x-small", direction="in", pad=-15
            )
            ax.xaxis.tick_top()

            ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
            ax.yaxis.tick_left()
            ax.tick_params(
                axis="y", which="both", labelsize="x-small", direction="in", pad=-8
            )
            ax.yaxis.tick_left()
            for label in ax.yaxis.get_ticklabels():
                label.set_horizontalalignment("left")

            self.text = ax.text(
                0.5, 0.4, "cm", ha="center", va="center", size="x-small"
            )
            ax.grid(linestyle="--", linewidth=0.5)

            self.ax = ax

        self.update()
        plt.connect("resize_event", self.update)

    def update(self, *args):

        inch = 2.54
        width_cm = self.fig.get_figwidth() * inch
        height_cm = self.fig.get_figheight() * inch

        n = int(width_cm) + 1
        self.ax.set_xlim(0, width_cm)
        self.ax.set_xticks(np.arange(n))
        self.ax.set_xticklabels([""] + ["%d" % x for x in np.arange(1, n)])

        markersize = self.ax.xaxis.get_ticklines(True)[0].get_markersize()
        for line in self.ax.xaxis.get_ticklines(True)[2::9]:
            line.set_markersize(1.5 * markersize)

        n = int(height_cm) + 1
        self.ax.set_ylim(height_cm, 0)
        self.ax.set_yticks(np.arange(n))
        self.ax.set_yticklabels([""] + ["%d" % y for y in np.arange(1, n)])

        markersize = self.ax.yaxis.get_ticklines(True)[0].get_markersize()
        for line in self.ax.yaxis.get_ticklines(True)[1::9]:
            line.set_markersize(1.5 * markersize)


# width = page width - left margin - right margin
width = (14.8 - 1.5 - 2.0) / 2.54
height = width / 2

fig = plt.figure(figsize=(width, height), dpi=100)
ax = plt.subplot()
ruler = Ruler()

plt.savefig("../../figures/anatomy/ruler.pdf")
plt.show()
