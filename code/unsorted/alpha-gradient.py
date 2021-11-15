# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# Setup
fig = plt.figure(figsize=(6, 3))

X = np.linspace(0, 4 * np.pi, 256)
Y1 = np.zeros((50, len(X)))
Y2 = np.zeros((len(Y1), len(X)))
for i in range(len(Y1)):
    Y1[i] = np.cos(X) + np.random.uniform(-1, 1)
    Y2[i] = np.sin(X) + np.random.uniform(-1, 1)


# Usage of transparency
ax = plt.subplot(1, 1, 1)

Y, SD, VAR = Y1.mean(axis=0), Y1.std(axis=0), Y1.var(axis=0)

ax.fill_between(X, Y + VAR, Y - VAR, facecolor="C0", alpha=0.25, zorder=-40)
ax.fill_between(X, Y + SD, Y - SD, facecolor="C0", alpha=0.25, zorder=-30)
ax.plot(X, Y + VAR, color="C0", linestyle="--", linewidth=1)
ax.plot(X, Y - VAR, color="C0", linestyle="--", linewidth=1)
ax.plot(X, Y, color="C0", zorder=-20)

ax.set_xticks([]), ax.set_yticks([])

plt.tight_layout()
# plt.savefig("../figures/alpha-gradient.pdf")
plt.show()
