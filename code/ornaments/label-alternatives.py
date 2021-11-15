# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6, 6))

n = 5
for i in range(n):
    index = i + 1
    ax = plt.subplot(
        n,
        1,
        index,
        facecolor="None",
        xlim=[0, 10.5],
        xticks=[],
        ylim=[0, 10],
        yticks=[],
    )

    for j in range(5):
        ax.plot(
            [0, 10],
            [1 + j * 1.5, 1 + j * 1.5],
            clip_on=False,
            linewidth=5,
            color=".9",
            solid_capstyle="round",
        )

        x = np.random.uniform(1, 9)
        ax.plot(
            [0, x],
            [1 + j * 1.5, 1 + j * 1.5],
            clip_on=False,
            linewidth=5,
            color="C1",
            solid_capstyle="round",
        )

    ax.text(
        10.5,
        0,
        " %d " % (2000 + index),
        font="Roboto Condensed",
        weight="medium",
        color="black",
        ha="center",
        va="center",
        size="small",
        bbox=dict(
            facecolor="white",
            edgecolor="black",
            linewidth=0.75,
            boxstyle="round,pad=0.25",
        ),
    )

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_visible(False)
    # ax.spines['bottom'].set_position(('data', -1.25))

plt.tight_layout()
plt.savefig("../../figures/ornaments/legend-regular.pdf")
plt.show()
