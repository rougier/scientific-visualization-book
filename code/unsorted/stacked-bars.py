# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: Creative Commons BY-NC-SA International 4.0
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def lighten_color(color, amount=0.66):
    import colorsys

    try:
        c = mcolors.cnames[color]
    except:
        c = color
    c = np.array(colorsys.rgb_to_hls(*mcolors.to_rgb(c)))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])


# cmap = plt.get_cmap("Blues")
cmap = plt.get_cmap("tab10")


V = np.array(
    [
        [50, 23, 20, 7],
        [45, 33, 12, 10],
        [35, 43, 10, 12],
        [54, 23, 15, 8],
        [65, 23, 7, 5],
    ]
)


fig = plt.figure(figsize=(6, 2), dpi=100)
ax = plt.subplot(111, xticks=[], ylim=[-0.5, len(V) - 0.5])

ratings = ["Excellent", "Good", "Average", "Awful"]
Y = np.arange(len(V))
L = np.zeros(len(V))

for i in range(4):
    color = lighten_color(cmap(3), 1.00 - i / 4)
    ax.barh(Y, V[:, i], left=L, color=color, label=ratings[i])
    for j in range(len(V)):
        ax.text(
            L[j] + V[j, i] / 2,
            Y[j],
            "%d%%" % V[j, i],
            zorder=10,
            ha="center",
            va="center",
            color="white",
            size="x-small",
        )
    L += V[:, i]


ax.legend(frameon=False, bbox_to_anchor=(1.0, 1), loc=2, borderaxespad=0)
ax.set_yticks(Y)
ax.set_yticklabels(["Rating %d" % (i + 1) for i in Y])

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)

plt.tight_layout()
plt.savefig("stacked-bars.pdf")
plt.show()
