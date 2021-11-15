# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
# Defaults settings / Custom defaults
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("./mystyle.txt")

X = np.linspace(-np.pi, np.pi, 257, endpoint=True)
C, S = np.cos(X), np.sin(X)

fig = plt.figure(linewidth=1)
ax = plt.subplot(1, 1, 1, aspect=1)
ax.plot(X, C, markevery=(0, 32))
ax.plot(X, S, markevery=(0, 32))
ax.set_yticks([-1, 0, 1])

plt.tight_layout()
plt.savefig("../../figures/defaults/defaults-step-4.pdf")
plt.show()
