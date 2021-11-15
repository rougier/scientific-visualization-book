# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: Creative Commons BY-NC-SA International 4.0
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def lighten_color(color, amount=0.66):
    import matplotlib.colors as mc
    import colorsys

    try:
        c = mc.cnames[color]
    except:
        c = color
    c = np.array(colorsys.rgb_to_hls(*mc.to_rgb(c)))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])


cmap = plt.get_cmap("tab10")
color = cmap(0)
plt.rcParams["hatch.color"] = lighten_color(color)
plt.rcParams["hatch.linewidth"] = 8


fig = plt.figure(figsize=(4.25, 2))
ax = plt.subplot(1, 1, 1)
np.random.seed(123)

x1, y1 = 3 * np.arange(4), np.random.randint(25, 50, 4)
x2, y2 = x1 + 1, np.random.randint(25, 75, 4)

ax.bar(x1, y1, color=color)
for i in range(len(x1)):
    plt.annotate(
        "%d%%" % y1[i],
        (x1[i], y1[i]),
        xytext=(0, 1),
        fontsize="x-small",
        color=color,
        textcoords="offset points",
        va="bottom",
        ha="center",
    )

ax.bar(x2, y2, color=color, hatch="/")
for i in range(len(x2)):
    plt.annotate(
        "%d%%" % y2[i],
        (x2[i], y2[i]),
        xytext=(0, 1),
        fontsize="x-small",
        color=color,
        textcoords="offset points",
        va="bottom",
        ha="center",
    )

ax.set_yticks([])
ax.set_xticks(0.5 + np.arange(0, 12, 3))
ax.set_xticklabels(["2016", "2017", "2018", "2019"])
ax.tick_params("x", length=0, labelsize="small", which="major")

ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)

plt.tight_layout()
# plt.savefig("hatched-bars.pdf")
plt.show()
