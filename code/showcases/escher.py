# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def line(A, B, thickness=0.005, n=100):
    T = (B - A) / np.linalg.norm(B - A)
    O = np.array([-T[1], T[0]])
    P0 = A + thickness * O
    P1 = B + thickness * O
    P2 = B - thickness * O
    P3 = A - thickness * O
    P = np.concatenate(
        [
            np.linspace(P0, P1, n),
            np.linspace(P1, P2, n // 10),
            np.linspace(P2, P3, n),
            np.linspace(P3, P0, n // 10),
        ]
    )
    X, Y = P[:, 0], P[:, 1]
    return np.dstack([np.exp(X) * np.cos(Y), np.exp(X) * np.sin(Y)]).squeeze()


a, b = 11, 9
y = 2 * np.pi / (a + b * b / a)
x = b * y / a
v1, v2 = np.array([x, y]), np.array([-y, x])


fig = plt.figure(figsize=(8, 8))
ax = fig.add_axes([0, 0, 1, 1], aspect=1, frameon=False)

for i, z in enumerate(np.linspace(0, 1, b * 10, endpoint=False)):
    zorder = 0
    color = "0.5"
    thickness = 0.001
    if i % 10 == 0:
        thickness = 0.0025
        color = "0.0"
        zorder = 10
    P0, P1 = (2 + z) * b * v2, (2 + z) * b * v2 + 4 * a * v1
    L = line(P0, P1, thickness=thickness, n=500)
    ax.add_patch(Polygon(L, facecolor=color, zorder=zorder))

for i, z in enumerate(np.linspace(0, 1, a * 10, endpoint=False)):
    zorder = 0
    color = "0.5"
    thickness = 0.001
    if i % 10 == 0:
        thickness = 0.0025
        color = "0.0"
        zorder = 10

    P0, P1 = (1 + z) * a * v1, (1 + z) * a * v1 + 4 * b * v2
    L = line(P0, P1, thickness=thickness, n=500)
    ax.add_patch(Polygon(L, facecolor=color, zorder=zorder))


ax.set_xlim(-np.pi, np.pi), ax.set_xticks([])
ax.set_ylim(-np.pi, np.pi), ax.set_yticks([])
plt.savefig("../../figures/showcases/escher.pdf")
plt.show()
