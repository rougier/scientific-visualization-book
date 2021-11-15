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
p["figure.figsize"] = 6, 6
p["font.sans-serif"] = ["Roboto Condensed"]
p["font.weight"] = "light"
p["ytick.minor.visible"] = True
p["xtick.minor.visible"] = True

X = np.random.normal(0.5, 0.15, 5000)
Y = np.random.normal(0.5, 0.15, 5000)

fig = plt.figure(constrained_layout=True)
nrows, ncols, ratio = 2, 2, 5
gspec = gridspec.GridSpec(
    ncols=ncols,
    nrows=nrows,
    figure=fig,
    height_ratios=[1, ratio],
    width_ratios=[ratio, 1],
)

ax = plt.subplot(gspec[1, 0])
ax.scatter(X, Y, s=15, facecolor="black", linewidth=0, alpha=0.25)
ax.set_xlim(0, 1), ax.set_xticks(np.linspace(0, 1, 5))
ax.set_ylim(0, 1), ax.set_yticks(np.linspace(0, 1, 5))

ax = plt.subplot(gspec[0, 0])
ax.set_xlim(0, 1), ax.set_xticks(np.linspace(0, 1, 5))
ax.set_xticklabels([]), ax.set_yticks([])
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.hist(
    X, bins=np.linspace(0, 1, 21), facecolor="0.75", edgecolor="white", linewidth=0.5
)

ax = plt.subplot(gspec[1, 1])
ax.set_ylim(0, 1), ax.set_yticks(np.linspace(0, 1, 5))
ax.set_yticklabels([]), ax.set_xticks([])
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["top"].set_visible(False)
H = ax.hist(
    Y,
    bins=np.linspace(0, 1, 21),
    facecolor="0.75",
    edgecolor="white",
    orientation="horizontal",
    linewidth=0.5,
)

plt.savefig("../../figures/layout/standard-layout-2.pdf")
plt.show()
