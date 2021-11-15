# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

fig = plt.figure(figsize=(8, 1.5))

n = 3
X = np.append(np.linspace(0, n * 2 * np.pi, 500), [0])
Y = np.sin(X)

ax = plt.subplot(
    1,
    2,
    1,
    frameon=False,
    xlim=(0, n * 2 * np.pi + 1),
    xticks=[],
    ylim=(-1, 1.1),
    yticks=[],
)
ax.plot(X, Y, "C0", linewidth=8, alpha=0.5, solid_capstyle="round", clip_on=False)
ax.set_title("No self covering")

ax = plt.subplot(
    1,
    2,
    2,
    frameon=False,
    xlim=(0, n * 2 * np.pi),
    xticks=[],
    ylim=(-1, 1.1),
    yticks=[],
)
ax.plot(
    X[:-1], Y[:-1], "C0", linewidth=8, alpha=0.5, solid_capstyle="round", clip_on=False
)
ax.plot(
    [X[-2], X[-1]],
    [Y[-2], Y[-1]],
    "C0",
    linewidth=8,
    alpha=0.5,
    solid_capstyle="round",
    clip_on=False,
)
ax.set_title("Simulated self covering")

plt.tight_layout()
plt.savefig("../../figures/optimization/self-cover.pdf")
plt.show()
