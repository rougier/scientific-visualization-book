# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection


def frustum(left, right, bottom, top, znear, zfar):
    M = np.zeros((4, 4))
    M[0, 0] = +2.0 * znear / (right - left)
    M[2, 0] = (right + left) / (right - left)
    M[1, 1] = +2.0 * znear / (top - bottom)
    M[2, 1] = (top + bottom) / (top - bottom)
    M[2, 2] = -(zfar + znear) / (zfar - znear)
    M[3, 2] = -2.0 * znear * zfar / (zfar - znear)
    M[2, 3] = -1.0
    return M.T


def perspective(fovy, aspect, znear, zfar):
    h = np.tan(fovy / 360.0 * np.pi) * znear
    w = h * aspect
    return frustum(-w, w, -h, h, znear, zfar)


def scale(x, y, z):
    return np.array(
        [[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]], dtype=float
    )


def zoom(z):
    return scale(z, z, z)


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


def obj_load(filename):
    V, Vi = [], []
    with open(filename) as f:
        for line in f.readlines():
            if line.startswith("#"):
                continue
            values = line.split()
            if not values:
                continue
            if values[0] == "v":
                V.append([float(x) for x in values[1:4]])
            elif values[0] == "f":
                Vi.append([int(x) for x in values[1:4]])
    return np.array(V), np.array(Vi) - 1


# -----------------------------------------------------------------------------

# Loading and centering
V, Vi = obj_load("bunny.obj")
V = (V - (V.max(axis=0) + V.min(axis=0)) / 2) / max(V.max(axis=0) - V.min(axis=0))

# Computing model-view-projection matrix
model = zoom(1.5) @ xrotate(20) @ yrotate(45)
view = translate(0, 0, -4.5)
proj = perspective(25, 1, 1, 100)
MVP = proj @ view @ model

# Applying MVP
VH = np.c_[V, np.ones(len(V))]  # Homogenous coordinates
VT = VH @ MVP.T  # Transformed coordinates
VN = VT / VT[:, 3].reshape(-1, 1)  # Normalization
VS = VN[:, :3]  # Normalized device coordinates

# Actual faces
V = VS[Vi]

# Backface culling
CW = (
    (V[:, 1, 0] - V[:, 0, 0]) * (V[:, 1, 1] + V[:, 0, 1])
    + (V[:, 2, 0] - V[:, 1, 0]) * (V[:, 2, 1] + V[:, 1, 1])
    + (V[:, 0, 0] - V[:, 2, 0]) * (V[:, 0, 1] + V[:, 2, 1])
)
V = V[CW < 0]

# Rendering as a collection of polygons (triangles)
segments = V[:, :, :2]
zbuffer = -V[:, :, 2].mean(axis=1)

# Color according to depth
zmin, zmax = zbuffer.min(), zbuffer.max()
zbuffer = (zbuffer - zmin) / (zmax - zmin)
colors = plt.get_cmap("magma")(zbuffer)

# Sort triangles according to z buffer
I = np.argsort(zbuffer)
segments, colors = segments[I, :], colors[I, :]

# Actual rendering
fig = plt.figure(figsize=(6, 6))
ax = fig.add_axes([0, 0, 1, 1], xlim=[-1, +1], ylim=[-1, +1], aspect=1)
ax.axis("off")

for fc, ec, lw in [
    ("None", "black", 6.0),
    ("None", "white", 3.0),
    (colors, "black", 0.25),
]:
    collection = PolyCollection(
        segments, closed=True, linewidth=lw, facecolor=fc, edgecolor=ec
    )
    ax.add_collection(collection)

plt.savefig("../../figures/threed/bunny.pdf", transparent=True)
plt.show()
