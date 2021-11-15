# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6, 2.5))
ax = plt.subplot(
    xlim=[-np.pi, np.pi],
    xticks=[-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
    xticklabels=["-π", "-π/2", "0", "+π/2", "+π"],
    ylim=[-1, 1],
    yticks=[-1, 0, 1],
    yticklabels=["-1", "0", "+1"],
)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

ax.plot(X, C, label="cosine", clip_on=False)
ax.plot(X, S, label="sine", clip_on=False)

ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["left"].set_position(("data", -3.25))
ax.spines["bottom"].set_position(("data", -1.25))
ax.legend(edgecolor="None")

plt.tight_layout()
plt.savefig("../../figures/ornaments/legend-regular.pdf")
plt.show()
