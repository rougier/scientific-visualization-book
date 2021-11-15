# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


fig = plt.figure(figsize=(6.5, 6))
gspec = gridspec.GridSpec(
    ncols=7, nrows=7, figure=fig, height_ratios=[1, 0.25, 1, 1, 1, 1, 1]
)
cmap = plt.get_cmap("Blues")


for row in range(2, 7):
    ax = plt.subplot(
        gspec[row, :2], frameon=False, xlim=[0, 1], xticks=[], ylim=[0, 1], yticks=[]
    )
    ax.text(
        1,
        1,
        "Very long text using\n newlines and small font",
        family="Roboto Condensed",
        horizontalalignment="right",
        verticalalignment="top",
    )

    for col in range(2, 7):
        ax = plt.subplot(
            gspec[row, col],
            aspect=1,
            frameon=False,
            xlim=[0, 1],
            xticks=[],
            ylim=[0, 1],
            yticks=[],
        )
        ax.axhline(0.5, color="white", lw=1)
        ax.axvline(0.5, color="white", lw=1)

        Z = np.random.uniform(0.25, 0.75, (2, 2))
        ax.imshow(Z, extent=[0, 1, 0, 1], cmap=cmap, vmin=0, vmax=1)
        if row == 2:
            ax.text(
                0.5,
                1.1,
                "Subject %d" % (col - 1),
                ha="center",
                va="bottom",
                size="small",
                weight="bold",
            )


ax = plt.subplot(
    gspec[0, 4], frameon=True, aspect=1, xlim=[0, 1], xticks=[], ylim=[0, 1], yticks=[]
)
ax.axhline(0.5, color="black", lw=0.75)
ax.axvline(0.5, color="black", lw=0.75)


# First quadrant
ax.text(
    -0.5, 0.75, "First quadrant", ha="right", va="center", size="small", weight="bold"
)
ax.text(
    -0.5,
    0.55,
    "Explanation of first quadrant",
    ha="right",
    va="center",
    size="x-small",
    family="Roboto Condensed",
)
ax.plot(
    [-0.25, 0.25],
    [0.75, 0.75],
    color="black",
    marker="o",
    markevery=[-1],
    clip_on=False,
    linewidth=0.75,
    markersize=2,
)

# Second quadrant
ax.text(
    -0.5, 0.25, "Second quadrant", ha="right", va="center", size="small", weight="bold"
)
ax.text(
    -0.5,
    0.05,
    "Explanation of second quadrant",
    ha="right",
    va="center",
    size="x-small",
    family="Roboto Condensed",
)
ax.plot(
    [-0.25, 0.25],
    [0.25, 0.25],
    color="black",
    marker="o",
    markevery=[-1],
    clip_on=False,
    linewidth=0.75,
    markersize=2,
)

# Third quadrant
ax.text(
    1.5, 0.75, "Third quadrant", ha="left", va="center", size="small", weight="bold"
)
ax.text(
    1.5,
    0.55,
    "Explanation of third quadrant",
    ha="left",
    va="center",
    size="x-small",
    family="Roboto Condensed",
)
ax.plot(
    [1.25, 0.75],
    [0.75, 0.75],
    color="black",
    marker="o",
    markevery=[-1],
    clip_on=False,
    linewidth=0.75,
    markersize=2,
)

# Fourth quadrant
ax.text(
    1.5, 0.25, "Fourth quadrant", ha="left", va="center", size="small", weight="bold"
)
ax.text(
    1.5,
    0.05,
    "Explanation of fourth quadrant",
    ha="left",
    va="center",
    size="x-small",
    family="Roboto Condensed",
)
ax.plot(
    [1.25, 0.75],
    [0.25, 0.25],
    color="black",
    marker="o",
    markevery=[-1],
    clip_on=False,
    linewidth=0.75,
    markersize=2,
)


# Legend
ax = plt.subplot(
    gspec[0, :2], frameon=False, xlim=[0, 10], xticks=[], ylim=[0, 4], yticks=[]
)
ax.scatter([1, 1, 1], [3, 2, 1], color=[cmap(0.25), cmap(0.50), cmap(0.75)])
ax.text(
    2, 1, "Large", ha="left", va="center", size="small", weight="bold", family="Roboto"
)
ax.text(
    2, 2, "Medium", ha="left", va="center", size="small", weight="bold", family="Roboto"
)
ax.text(
    2,
    3,
    "Limited",
    ha="left",
    va="center",
    size="small",
    weight="bold",
    family="Roboto",
)

plt.savefig("../../figures/layout/complex-layout.pdf")
plt.show()
