# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

n_lines, n_points = 1_000, 2
X = [np.random.uniform(0, 1, n_points) for i in range(n_lines)]
Y = [np.random.uniform(0, 1, n_points) for i in range(n_lines)]

fig = plt.figure(figsize=(9, 3.5))

# -----------------------------
ax = fig.add_subplot(1, 3, 1, aspect=1, xlim=[0, 1], xticks=[], ylim=[0, 1], yticks=[])
start = timer()
for x, y in zip(X, Y):
    ax.plot(x, y, color="blue", alpha=0.1, linewidth=0.5)
end = timer()
ax.set_title("Individual plots: %.4fs" % (end - start))


# -----------------------------
ax = fig.add_subplot(1, 3, 2, aspect=1, xlim=[0, 1], xticks=[], ylim=[0, 1], yticks=[])
start = timer()
X_, Y_ = [], []
for x, y in zip(X, Y):
    X_.extend(x), X_.extend([None])
    Y_.extend(y), Y_.extend([None])
ax.plot(X_, Y_, color="blue", alpha=0.1, linewidth=0.5)
end = timer()
ax.set_title("Unified plot: %.4fs" % (end - start))

# -----------------------------
from matplotlib.collections import LineCollection

ax = fig.add_subplot(1, 3, 3, aspect=1, xlim=[0, 1], xticks=[], ylim=[0, 1], yticks=[])
start = timer()
V = [np.stack([x, y], axis=1) for x, y in zip(X, Y)]
lines = LineCollection(V, color="blue", alpha=0.1, linewidth=0.5)
ax.add_collection(lines)
end = timer()
ax.set_title("Line collection: %.4fs" % (end - start))

plt.tight_layout()
plt.savefig("../../figures/optimization/line-benchmark.png", dpi=600)
plt.show()
