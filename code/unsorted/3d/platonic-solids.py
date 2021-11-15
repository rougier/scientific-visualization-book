import glm
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection


def tetrahedron():
    """ Tetrahedron with 4 faces, 6 edges and 4 vertices """
    a = 2 * np.pi / 3
    vertices = [
        (0, 0.5, 0),
        (0.5 * np.cos(0 * a), -0.25, 0.5 * np.sin(0 * a)),
        (0.5 * np.cos(1 * a), -0.25, 0.5 * np.sin(1 * a)),
        (0.5 * np.cos(2 * a), -0.25, 0.5 * np.sin(2 * a)),
    ]
    faces = [(1, 2, 3), (1, 2, 0), (2, 3, 0), (3, 1, 0)]
    return np.array(vertices), np.array(faces)


def octahedron():
    """ Octahedron with 8 faces, 12 edges and 6 vertices """

    r = 0.5 * 1 / np.sqrt(2)
    vertices = [
        (0, 0.5, 0),
        (0, -0.5, 0),
        (-r, 0, -r),
        (r, 0, -r),
        (r, 0, r),
        (-r, 0, r),
    ]
    faces = [
        (2, 3, 0),
        (3, 4, 0),
        (4, 5, 0),
        (5, 2, 0),
        (3, 2, 1),
        (4, 3, 1),
        (5, 4, 1),
        (2, 5, 1),
    ]
    return np.array(vertices), np.array(faces)


def dodecahedron():
    """ Regular dodecahedron with 12 faces, 30 edges and 20 vertices """

    r = (1 + np.sqrt(5)) / 2
    vertices = [
        (-1, -1, +1),
        (r, 1 / r, 0),
        (r, -1 / r, 0),
        (-r, 1 / r, 0),
        (-r, -1 / r, 0),
        (0, r, 1 / r),
        (0, r, -1 / r),
        (1 / r, 0, -r),
        (-1 / r, 0, -r),
        (0, -r, -1 / r),
        (0, -r, 1 / r),
        (1 / r, 0, r),
        (-1 / r, 0, r),
        (+1, +1, -1),
        (+1, +1, +1),
        (-1, +1, -1),
        (-1, +1, +1),
        (+1, -1, -1),
        (+1, -1, +1),
        (-1, -1, -1),
    ]
    # faces = [ (19, 3, 2), (12, 19, 2), (15, 12, 2),
    #           (8, 14, 2), (18, 8, 2), (3, 18, 2),
    #           (20, 5, 4), (9, 20, 4), (16, 9, 4),
    #           (13, 17, 4), (1, 13, 4), (5, 1, 4),
    #           (7, 16, 4), (6, 7, 4), (17, 6, 4),
    #           (6, 15, 2), (7, 6, 2), (14, 7, 2),
    #           (10, 18, 3), (11, 10, 3), (19, 11, 3),
    #           (11, 1, 5), (10, 11, 5), (20, 10, 5),
    #           (20, 9, 8), (10, 20, 8), (18, 10, 8),
    #           (9, 16, 7), (8, 9, 7), (14, 8, 7),
    #           (12, 15, 6), (13, 12, 6), (17, 13, 6),
    #           (13, 1, 11), (12, 13, 11), (19, 12, 11) ]
    faces = [
        (19, 3, 2, 15, 12),
        (8, 14, 2, 3, 18),
        (20, 5, 4, 16, 9),
        (13, 17, 4, 5, 1),
        (7, 16, 4, 17, 6),
        (6, 15, 2, 14, 7),
        (10, 18, 3, 19, 11),
        (11, 1, 5, 20, 10),
        (20, 9, 8, 18, 10),
        (9, 16, 7, 14, 8),
        (12, 15, 6, 17, 13),
        (13, 1, 11, 19, 12),
    ]
    vertices = np.array(vertices) / np.sqrt(3) / 2
    faces = np.array(faces) - 1
    return vertices, faces


def icosahedron():
    """ Regular icosahedron with 20 faces, 30 edges and 12 vertices """

    a = (1 + np.sqrt(5)) / 2
    vertices = [
        (-1, a, 0),
        (1, a, 0),
        (-1, -a, 0),
        (1, -a, 0),
        (0, -1, a),
        (0, 1, a),
        (0, -1, -a),
        (0, 1, -a),
        (a, 0, -1),
        (a, 0, 1),
        (-a, 0, -1),
        (-a, 0, 1),
    ]
    faces = [
        [0, 11, 5],
        [0, 5, 1],
        [0, 1, 7],
        [0, 7, 10],
        [0, 10, 11],
        [1, 5, 9],
        [5, 11, 4],
        [11, 10, 2],
        [10, 7, 6],
        [7, 1, 8],
        [3, 9, 4],
        [3, 4, 2],
        [3, 2, 6],
        [3, 6, 8],
        [3, 8, 9],
        [4, 9, 5],
        [2, 4, 11],
        [6, 2, 10],
        [8, 6, 7],
        [9, 8, 1],
    ]
    vertices = np.array(vertices) / np.sqrt(a + 2) / 2
    faces = np.array(faces)
    return vertices, faces


def cube():
    vertices = [
        (0, 0, 0),
        (1, 0, 0),
        (1, 0, 1),
        (0, 0, 1),
        (0, 1, 0),
        (1, 1, 0),
        (1, 1, 1),
        (0, 1, 1),
    ]
    faces = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [0, 1, 5, 4],
        [1, 2, 6, 5],
        [2, 3, 7, 6],
        [3, 0, 4, 7],
    ]
    return (np.array(vertices) - 0.5) / np.sqrt(2), np.array(faces)


def plot(ax, camera, V, F):
    ax.axis("off")

    T = glm.transform(V[F], camera)
    V, Z = T[..., :2], T[..., 2].mean(axis=-1)
    V = V[np.argsort(-Z)]
    collection = PolyCollection(
        V,
        antialiased=True,
        linewidth=1.0,
        facecolor=(0.9, 0.9, 1, 0.75),
        edgecolor=(0, 0, 0.75, 0.25),
    )
    ax.add_collection(collection)


fig = plt.figure(figsize=(8, 5.5))
camera = glm.camera(25, 35, 1.5, "perspective")

ax = plt.subplot(2, 3, 1, xlim=[-1, +1], ylim=[-1, +1], aspect=1)
ax.axis("off")
ax.text(
    0.5,
    0.6,
    "PLATONIC",
    transform=ax.transAxes,
    weight="black",
    size=24,
    va="bottom",
    ha="center",
    family="Source Sans Pro",
)
ax.text(
    0.5,
    0.6,
    "S  O  L  I  D  S",
    transform=ax.transAxes,
    weight="light",
    size=22,
    va="top",
    ha="center",
    family="Source Sans Pro",
)
ax.text(
    0.5,
    0.475,
    "matplotlib.org",
    transform=ax.transAxes,
    weight="light",
    size=13,
    va="top",
    ha="center",
    family="Source Code Pro",
)


# -----------------------------------------------------------------------------
ax = plt.subplot(2, 3, 2, xlim=[-1, +1], ylim=[-1, +1], aspect=1)
plot(ax, camera, *tetrahedron())
ax.text(
    0.5,
    1.0,
    "Tetrahedron",
    transform=ax.transAxes,
    weight="bold",
    va="bottom",
    ha="center",
)
ax.text(
    0.5,
    1.0,
    "4 faces, 4 vertices, 6 edges",
    transform=ax.transAxes,
    va="top",
    ha="center",
    size="x-small",
)

# -----------------------------------------------------------------------------
ax = plt.subplot(2, 3, 3, xlim=[-1, +1], ylim=[-1, +1], aspect=1)
plot(ax, camera, *cube())
ax.text(
    0.5, 1.0, "Cube", transform=ax.transAxes, weight="bold", va="bottom", ha="center"
)
ax.text(
    0.5,
    1.0,
    "6 faces, 8 vertices, 12 edges",
    transform=ax.transAxes,
    va="top",
    ha="center",
    size="x-small",
)

# -----------------------------------------------------------------------------
ax = plt.subplot(2, 3, 4, xlim=[-1, +1], ylim=[-1, +1], aspect=1)
plot(ax, camera, *octahedron())
ax.text(
    0.5,
    1.0,
    "Octahedron",
    transform=ax.transAxes,
    weight="bold",
    va="bottom",
    ha="center",
)
ax.text(
    0.5,
    1.0,
    "8 faces, 6 vertices, 12 edges",
    transform=ax.transAxes,
    va="top",
    ha="center",
    size="x-small",
)

# -----------------------------------------------------------------------------
ax = plt.subplot(2, 3, 5, xlim=[-1, +1], ylim=[-1, +1], aspect=1)
plot(ax, camera, *dodecahedron())
ax.text(
    0.5,
    1.0,
    "Dodecahedron",
    transform=ax.transAxes,
    weight="bold",
    va="bottom",
    ha="center",
)
ax.text(
    0.5,
    1.0,
    "12 faces, 20 vertices, 30 edges",
    transform=ax.transAxes,
    va="top",
    ha="center",
    size="x-small",
)

# -----------------------------------------------------------------------------
ax = plt.subplot(2, 3, 6, xlim=[-1, +1], ylim=[-1, +1], aspect=1)
plot(ax, camera, *icosahedron())
ax.text(
    0.5,
    1.0,
    "Icosahedron",
    transform=ax.transAxes,
    weight="bold",
    va="bottom",
    ha="center",
)
ax.text(
    0.5,
    1.0,
    "20 faces, 12 vertices, 30 edges",
    transform=ax.transAxes,
    va="top",
    ha="center",
    size="x-small",
)


plt.tight_layout()
plt.savefig("platonic-solids.png", dpi=300)
plt.savefig("platonic-solids.pdf")
plt.show()
