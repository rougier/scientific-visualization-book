# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


def annotate(ax, x, y, text, fc="#ff7777", y0=0):
    y = y - 0.5
    ax.annotate(
        " " + text + " ",
        xy=(x, y),
        xycoords="data",
        xytext=(0, 12),
        textcoords="offset points",
        color="white",
        size="x-small",
        va="center",
        ha="center",
        weight="bold",
        bbox=dict(boxstyle="round", fc=fc, ec="none"),
        arrowprops=dict(
            arrowstyle="wedge,tail_width=1.", fc=fc, ec="none", patchA=None
        ),
    )
    plt.plot([x, x], [y, y0], color="black", linestyle=":", linewidth=0.75)


fig = plt.figure(figsize=(5, 2))
ax = fig.add_subplot(111, xlim=(2002.5, 2021.5), ylim=(0, 6.5), yticks=([]))
ax.tick_params("x", labelsize="x-small", which="major")
plt.plot([2002.5, 2021.5], [0, 0], color="black", linewidth=1.0, clip_on=False)
X = np.arange(2003, 2022)
Y = np.zeros(len(X))
plt.scatter(
    X,
    Y,
    s=50,
    linewidth=1.0,
    zorder=10,
    clip_on=False,
    edgecolor="black",
    facecolor="white",
)

annotate(ax, 2021, 4, "3.4")
annotate(ax, 2020, 3, "3.3")
annotate(ax, 2019, 4, "3.2", y0=2.5)
annotate(ax, 2019, 2, "3.1")
annotate(ax, 2018, 3, "3.0", y0=1.5)
annotate(ax, 2018, 1, "2.2", fc="#777777")
annotate(ax, 2017, 4, "2.1", y0=2.5)
annotate(ax, 2017, 2, "2.0")
annotate(ax, 2015, 2, "1.5")
annotate(ax, 2014, 1, "1.4")
annotate(ax, 2013, 2, "1.3")
annotate(ax, 2012, 1, "1.2")
annotate(ax, 2011, 3, "1.1", y0=2.5)
annotate(ax, 2011, 2, "1.0")
annotate(ax, 2009, 1, "0.99")
annotate(ax, 2003, 1, "0.10")

x0, x1 = 2002.5, 2011.9
ax.plot(
    [x0, x1], [5, 5], color="black", linewidth=1, marker="|", clip_on=False
)
ax.text(
    (x0 + x1) / 2, 5.1, "J.D. Hunter", ha="center", va="bottom", size="x-small"
)

x0, x1 = 2012.1, 2017.9
ax.plot(
    [x0, x1], [5, 5], color="black", linewidth=1, marker="|", clip_on=False
)
ax.text(
    (x0 + x1) / 2,
    5.1,
    "M. Droettboom",
    ha="center",
    va="bottom",
    size="x-small",
)

x0, x1 = 2014.1, 2021.5
ax.plot([x0, x1 + 1], [6, 6], color="black", linewidth=1, marker="|")
ax.text(
    (x0 + x1) / 2, 6.1, "T. Caswell", ha="center", va="bottom", size="x-small"
)

ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.set_xticks(np.arange(2003, 2022, 2))

plt.tight_layout()
plt.savefig("../../figures/introduction/matplotlib-timeline.pdf")
plt.savefig("../../figures/introduction/matplotlib-timeline.png", dpi=300)
plt.show()
