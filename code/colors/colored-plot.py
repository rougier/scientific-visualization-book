# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
# Illustrate colored plots
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


def plot(ax, X, Y, cmap, alpha):
    P = np.array([X, Y]).T.reshape(-1, 1, 2)
    S = np.concatenate([P[:-1], P[1:]], axis=1)
    C = cmap(np.linspace(0, 1, len(S)))
    L = LineCollection(S, color=C, alpha=alpha, linewidth=1.25)
    ax.add_collection(L)


fig = plt.figure(figsize=(12, 3))
fig.patch.set_facecolor("black")
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
X = np.linspace(-5 * np.pi, +5 * np.pi, 2500)
for d in np.linspace(0, 1, 15):
    dy = d / 2 + (1 - np.abs(X) / X.max()) ** 2
    dx = 1 + d / 3
    Y = dy * np.sin(dx * X) + 0.1 * np.cos(3 + 5 * X)
    plot(ax, X, Y, plt.get_cmap("rainbow"), d)
ax.set_xlim(X.min(), X.max())
ax.set_ylim(-2.0, 2.0)
plt.savefig("../../figures/colors/colored-plot.pdf")
plt.show()
