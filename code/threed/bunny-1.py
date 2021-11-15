# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection

# Data processing
V, F = [], []
with open("bunny.obj") as f:
    for line in f.readlines():
        if line.startswith("#"):
            continue
        values = line.split()
        if not values:
            continue
        if values[0] == "v":
            V.append([float(x) for x in values[1:4]])
        elif values[0] == "f":
            F.append([int(x) for x in values[1:4]])
V, F = np.array(V), np.array(F) - 1
V = (V - (V.max(0) + V.min(0)) / 2) / max(V.max(0) - V.min(0))
T = V[F][..., :2]

# Rendering
fig = plt.figure(figsize=(6, 6))
ax = fig.add_axes([0, 0, 1, 1], xlim=[-1, +1], ylim=[-1, +1], aspect=1, frameon=False)
collection = PolyCollection(
    T, closed=True, linewidth=0.1, facecolor="None", edgecolor="black"
)
ax.add_collection(collection)
plt.savefig("../../figures/threed/bunny-1.pdf")
plt.show()
