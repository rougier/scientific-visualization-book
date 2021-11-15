# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.ticker import NullFormatter

X = np.random.uniform(0, 1, 1000)
Y = np.random.uniform(0, 1, 1000)
S = np.sqrt((X - 0.5) ** 2 + (Y - 0.5) ** 2)
C = np.ones((1000, 4)) * colors.to_rgba("C0")
C[S > 0.5] = colors.to_rgba("C1")

figure = plt.figure(figsize=(8, 4))

# Linear scale
ax = plt.subplot(1, 2, 1, xlim=(0, 1), ylim=(0, 1))
ax.scatter(X, Y, s=25, facecolor=C, edgecolor="none", alpha=0.5)
T = np.linspace(0, 2 * np.pi, 100)
X2 = 0.5 + 0.5 * np.cos(T)
Y2 = 0.5 + 0.5 * np.sin(T)
ax.plot(X2, Y2, color="black", linestyle="--", linewidth=0.75)

#
ax = plt.subplot(1, 2, 2, xlim=(0.01, 0.99), ylim=(0.01, 0.99))
ax.set_xscale("logit")
ax.set_yscale("logit")
ax.scatter(X, Y, s=25, facecolor=C, edgecolor="none", alpha=0.5)
ax.yaxis.set_minor_formatter(NullFormatter())
ax.xaxis.set_minor_formatter(NullFormatter())
T = np.linspace(0, 2 * np.pi, 256)
X2 = 0.5 + 0.5 * np.cos(T)
Y2 = 0.5 + 0.5 * np.sin(T)
ax.plot(X2, Y2, color="black", linestyle="--", linewidth=0.75)


# Show
plt.tight_layout()
# plt.savefig("scale-logit.pdf")
plt.show()
