import numpy as np


def normalize(X):
    return X / (1e-16 + np.sqrt((np.array(X) ** 2).sum(axis=-1)))[..., np.newaxis]


def rescale(V, vmin=0, vmax=1):
    Vmin, Vmax = V.min(), V.max()
    return vmin + (vmax - vmin) * (V - Vmin) / (Vmax - Vmin)


def center(V):
    return V - (V.min(axis=-1) + V.max(axis=-1)) / 2


def clip(V, vmin=0, vmax=1):
    return np.minimum(np.maximum(V, vmin), vmax)


def degrees(angle):
    return 180 * angle / np.pi


def radians(angle):
    return np.pi * angle / 180


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
    h = np.tan(0.5 * radians(fovy)) * znear
    w = h * aspect
    return frustum(-w, w, -h, h, znear, zfar)


def ortho(left, right, bottom, top, znear, zfar):
    M = np.zeros((4, 4), dtype=np.float32)
    M[0, 0] = +2.0 / (right - left)
    M[1, 1] = +2.0 / (top - bottom)
    M[2, 2] = -2.0 / (zfar - znear)
    M[3, 3] = 1.0
    M[0, 2] = -(right + left) / float(right - left)
    M[1, 3] = -(top + bottom) / float(top - bottom)
    M[2, 3] = -(zfar + znear) / float(zfar - znear)
    return M


def scale(x=1, y=1, z=1):
    return np.array(
        [[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]], dtype=np.float32
    )


def translate(x=0, y=0, z=0):
    return np.array(
        [[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]], dtype=np.float32
    )


def xrotate(theta=0):
    t = radians(theta)
    c, s = np.cos(t), np.sin(t)
    return np.array(
        [[1, 0, 0, 0], [0, c, -s, 0], [0, s, c, 0], [0, 0, 0, 1]], dtype=np.float32
    )


def yrotate(theta=0):
    t = radians(theta)
    c, s = np.cos(t), np.sin(t)
    return np.array(
        [[c, 0, s, 0], [0, 1, 0, 0], [-s, 0, c, 0], [0, 0, 0, 1]], dtype=np.float32
    )


def zrotate(theta=0):
    t = radians(theta)
    c, s = np.cos(t), np.sin(t)
    return np.array(
        [[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], dtype=np.float32
    )


def fit_unit_cube(V):
    xmin, xmax = V[:, 0].min(), V[:, 0].max()
    ymin, ymax = V[:, 1].min(), V[:, 1].max()
    zmin, zmax = V[:, 2].min(), V[:, 2].max()
    scale = max([xmax - xmin, ymax - ymin, zmax - zmin])
    V /= scale
    V[:, 0] -= (xmax + xmin) / 2 / scale
    V[:, 1] -= (ymax + ymin) / 2 / scale
    V[:, 2] -= (zmax + zmin) / 2 / scale
    return V


def transform(V, mvp):
    V = np.asarray(V)
    shape = V.shape
    V = V.reshape(-1, 3)
    ones = np.ones(len(V), dtype=np.float32)
    V = np.c_[V.astype(np.float32), ones]  # Homogenous coordinates
    V = V @ mvp.T  # Transformed coordinates
    V = V / V[:, 3].reshape(-1, 1)  # Normalization
    V = V[:, :3]  # Normalized device coordinates
    return V.reshape(shape)


def frontback(T):
    Z = (
        (T[:, 1, 0] - T[:, 0, 0]) * (T[:, 1, 1] + T[:, 0, 1])
        + (T[:, 2, 0] - T[:, 1, 0]) * (T[:, 2, 1] + T[:, 1, 1])
        + (T[:, 0, 0] - T[:, 2, 0]) * (T[:, 0, 1] + T[:, 2, 1])
    )
    return Z < 0, Z >= 0


def camera(xrotation=25, yrotation=45, zoom=1, mode="perspective"):
    xrotation = min(max(xrotation, 0), 90)
    yrotation = min(max(yrotation, 0), 90)
    zoom = max(0.1, zoom)
    model = scale(zoom, zoom, zoom) @ xrotate(xrotation) @ yrotate(yrotation)
    view = translate(0, 0, -4.5)
    if mode == "ortho":
        proj = ortho(-1, +1, -1, +1, 1, 100)
    else:
        proj = perspective(25, 1, 1, 100)
    return proj @ view @ model
