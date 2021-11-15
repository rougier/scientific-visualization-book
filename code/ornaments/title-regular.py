# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6, 3))
ax = plt.subplot(
    xlim=[-np.pi, np.pi],
    xticks=[-np.pi, -np.pi / 2, np.pi / 2, np.pi],
    xticklabels=["-π", "-π/2", "+π/2", "+π"],
    ylim=[-1, 1],
    yticks=[-1, 1],
    yticklabels=["-1", "+1"],
)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

ax.plot(X, C, label="cosine", clip_on=False)
ax.plot(X, S, label="sine", clip_on=False)

ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["left"].set_position(("data", -3.25))
ax.spines["bottom"].set_position(("data", -1.25))
ax.legend(
    edgecolor="None",
    ncol=2,
    loc="upper right",
    bbox_to_anchor=(1.01, 1.225),
    borderaxespad=0,
)
ax.set_title("Trigonometric functions", x=1, y=1.2, ha="right")

ax.set_xlabel("Angle", va="center", weight="bold")
ax.xaxis.set_label_coords(0.5, -0.25)

ax.set_ylabel("Value", ha="center", weight="bold")
ax.yaxis.set_label_coords(-0.025, 0.5)


plt.tight_layout()
plt.savefig("../../figures/ornaments/title-regular.pdf")
plt.show()
