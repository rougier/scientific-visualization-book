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


def ortho(left, right, bottom, top, znear, zfar):
    M = np.zeros((4, 4), dtype=float)
    M[0, 0] = +2.0 / (right - left)
    M[1, 1] = +2.0 / (top - bottom)
    M[2, 2] = -2.0 / (zfar - znear)
    M[3, 3] = 1.0
    M[0, 2] = -(right + left) / float(right - left)
    M[1, 3] = -(top + bottom) / float(top - bottom)
    M[2, 3] = -(zfar + znear) / float(zfar - znear)
    return M


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


def mesh(MVP, V, F, cmap=None, clip=True):
    V = np.c_[V, np.ones(len(V))] @ MVP.T
    V /= V[:, 3].reshape(-1, 1)
    V = V[F]
    T = V[:, :, :2]
    Z = -V[:, :, 2].mean(axis=1)
    zmin, zmax = Z.min(), Z.max()
    Z = (Z - zmin) / (zmax - zmin)
    I = np.argsort(Z)
    T = T[I, :]
    if cmap is not None:
        C = plt.get_cmap(cmap)(Z)
        C = C[I, :]
    else:
        C = 1.0, 1.0, 1.0, 0.5
    return PolyCollection(
        T, closed=True, linewidth=0.1, clip_on=clip, facecolor=C, edgecolor="black"
    )


fig = plt.figure(figsize=(6, 6))

ax = plt.subplot(
    2, 2, 1, xlim=[-1, +1], ylim=[-1, +1], xticks=[], yticks=[], aspect=1, frameon=False
)
model = xrotate(20) @ yrotate(45)
view = translate(0, 0, -2.5)
proj = perspective(25, 1, 1, 100)
ax.add_collection(mesh(proj @ view @ model, V, F, "magma", False))

ax = plt.subplot(
    2, 2, 2, xlim=[-1, +1], ylim=[-1, +1], xticks=[], yticks=[], aspect=1, frameon=False
)
model = xrotate(90)
view = np.eye(4)
proj = ortho(-1, 1, -1, 1, 0, 100)
ax.add_collection(mesh(proj @ view @ model, 2 * V, F))

ax = plt.subplot(
    2, 2, 3, xlim=[-1, +1], ylim=[-1, +1], xticks=[], yticks=[], aspect=1, frameon=False
)
model = yrotate(90)
view = np.eye(4)
proj = ortho(-1, 1, -1, 1, 0, 100)
ax.add_collection(mesh(proj @ view @ model, 2 * V, F))

ax = plt.subplot(
    2, 2, 4, xlim=[-1, +1], ylim=[-1, +1], xticks=[], yticks=[], aspect=1, frameon=False
)
model = view = np.eye(4)
proj = ortho(-1, 1, -1, 1, 0, 100)
ax.add_collection(mesh(proj @ view @ model, 2 * V, F))

plt.tight_layout()
plt.savefig("../../figures/threed/bunnies.pdf")
plt.show()
