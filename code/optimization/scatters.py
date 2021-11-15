# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

n = [10_000, 100_000, 1_000_000]
alpha = [0.2, 0.02, 0.002]
fig = plt.figure(figsize=(9, 9))

index = 1
for i in range(3):

    X = np.random.normal(0, 2, n[i])
    Y = np.random.normal(0, 2, n[i])

    ax = plt.subplot(3, 3, index, aspect=1)
    ax.scatter(
        X, Y, 5, facecolor="black", edgecolor="None", alpha=alpha[i], antialiased=True
    )
    ax.set_xlim(-5, 5), ax.set_xticks([])
    ax.set_ylim(-5, 5), ax.set_yticks([])
    ax.text(
        -5,
        4.75,
        " scatter, n={:,}, alpha={:.3f}".format(n[i], alpha[i]),
        ha="left",
        va="top",
        size="small",
    )
    index += 1

    ax = plt.subplot(3, 3, index, aspect=1)
    ax.hist2d(X, Y, 128, cmap="gray_r")
    ax.set_xlim(-5, 5), ax.set_xticks([])
    ax.set_ylim(-5, 5), ax.set_yticks([])
    ax.text(
        -5,
        4.75,
        " hist2d (128x128 bins), n={:,}".format(n[i]),
        ha="left",
        va="top",
        size="small",
    )
    index += 1

    ax = plt.subplot(3, 3, index, aspect=1)
    ax.hexbin(X, Y, gridsize=64, cmap="gray_r", linewidth=0, antialiased=0)
    ax.set_xlim(-5, 5), ax.set_xticks([])
    ax.set_ylim(-5, 5), ax.set_yticks([])
    ax.text(
        -5,
        4.75,
        " hexbin (64x64 bins), n={:,}".format(n[i]),
        ha="left",
        va="top",
        size="small",
    )
    index += 1

plt.tight_layout()
plt.savefig("../../figures/optimization/scatters.png", dpi=600)
plt.show()
