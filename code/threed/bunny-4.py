# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection


def frustum(left, right, bottom, top, znear, zfar):
    M = np.zeros((4, 4), dtype=np.float32)
    M[0, 0] = +2.0 * znear / (right - left)
    M[1, 1] = +2.0 * znear / (top - bottom)
    M[2, 2] = -(zfar + znear) / (zfar - znear)
    M[0, 2] = (right + left) / (right - left)
    M[2, 1] = (top + bottom) / (top - bottom)
    M[2, 3] = -2.0 * znear * zfar / (zfar - znear)
    M[3, 2] = -1.0
    return M


def perspective(fovy, aspect, znear, zfar):
    h = np.tan(0.5 * np.radians(fovy)) * znear
    w = h * aspect
    return frustum(-w, w, -h, h, znear, zfar)


def translate(x, y, z):
    return np.array(
        [[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]], dtype=float
    )


def xrotate(theta):
    t = np.pi * theta / 180
    c, s = np.cos(t), np.sin(t)
    return np.array(
        [[1, 0, 0, 0], [0, c, -s, 0], [0, s, c, 0], [0, 0, 0, 1]], dtype=float
    )


def yrotate(theta):
    t = np.pi * theta / 180
    c, s = np.cos(t), np.sin(t)
    return np.array(
        [[c, 0, s, 0], [0, 1, 0, 0], [-s, 0, c, 0], [0, 0, 0, 1]], dtype=float
    )


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

model = xrotate(20) @ yrotate(45)
view = translate(0, 0, -3.5)
proj = perspective(25, 1, 1, 100)
MVP = proj @ view @ model

V = np.c_[V, np.ones(len(V))] @ MVP.T
V /= V[:, 3].reshape(-1, 1)
T = V[F][..., :2]

# Rendering
fig = plt.figure(figsize=(6, 6))
ax = fig.add_axes([0, 0, 1, 1], xlim=[-1, +1], ylim=[-1, +1], aspect=1, frameon=False)
collection = PolyCollection(
    T, closed=True, linewidth=0.1, facecolor="None", edgecolor="black"
)
ax.add_collection(collection)
plt.savefig("../../figures/threed/bunny-4.pdf")
plt.show()
