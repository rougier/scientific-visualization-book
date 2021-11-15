# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

n_points = 100_000
np.random.seed(1)
X = np.random.normal(0, 1, n_points)
Y = np.random.normal(0, 1, n_points)

fig = plt.figure(figsize=(9, 3.5))

# -----------------------------
ax = fig.add_subplot(
    1, 3, 2, aspect=1, xlim=[-5, 5], xticks=[], ylim=[-5, 5], yticks=[]
)
start = timer()
ax.scatter(X, Y, s=4, color="black", alpha=0.008, linewidth=0)
end = timer()
ax.set_title("Scatter: %.4fs" % (end - start))

# -----------------------------
ax = fig.add_subplot(
    1, 3, 3, aspect=1, xlim=[-5, 5], xticks=[], ylim=[-5, 5], yticks=[]
)
start = timer()
ax.plot(X, Y, "o", markersize=2, color="black", alpha=0.008, markeredgewidth=0)
end = timer()
ax.set_title("Plot: %.4fs" % (end - start))

# -----------------------------
ax = fig.add_subplot(
    1, 3, 1, aspect=1, xlim=[-5, 5], xticks=[], ylim=[-5, 5], yticks=[]
)
start = timer()
ax.hist2d(X, Y, 128, cmap="gray_r")
end = timer()
ax.set_title("Hist2d: %.4fs" % (end - start))

plt.tight_layout()
plt.savefig("../../figures/optimization/scatter-benchmark.png", dpi=600)
plt.show()
