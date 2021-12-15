import glm
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.textpath import TextPath
from matplotlib.patches import PathPatch
from matplotlib.collections import PolyCollection


# -----------------------------------------------------------------------------
def axis(ax, camera, ticks=True):
    """
    Draw three dimension axis with ticks and tick labels.

    Parameters:
    -----------

    ax : matplotlib.axes instance
      The regulmat axes where to draw 

    camera : 4x4 numpy array
      A transformation matrix in homogenous coordinates (4x4)

    ticks : bool
      Whether to draw tick and tick labels

    Note:
    -----

    The axis is drawn inside the unit cube centered on the origin:

     - XZ lies on the plane Y = -0.5
     - XY lies on the plane Z = -0.5
     - YZ lies on the plane X = +0.5
     - xticks goes from (-0.5, -0.5, +0.5) to (+0.5, -0.5, +0.5)
     - zticks goes from (-0.5, -0.5, -0.5) to (-0.5, -0.5, +0.5)
     - yticks goes from (-0.5, -0.5, -0.5) to (-0.5, +0.5, -0.5)    
    """

    # Mandatory settings for matplotlib axes
    # --------------------------------------
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect(1)
    ax.axis("off")

    # Parameters
    # ---------------------------------
    axis_linewidth = 1.00
    grid_linewidth = 0.50
    ticks_linewidth = 0.75

    grid_color = "0.5"
    axis_color = "0.0"
    ticks_color = "0.0"
    ticks_length = 0.025
    ticks_pad = 0.05

    # ticks and ticklabels
    nx = 11
    xticks = np.linspace(-0.5, +0.5, nx, endpoint=True)
    xticklabels = ["%.1f" % x for x in xticks]

    ny = 11
    yticks = np.linspace(-0.5, +0.5, ny, endpoint=True)
    yticklabels = ["%.1f" % y for y in yticks]

    nz = 11
    zticks = np.linspace(-0.5, +0.5, nz, endpoint=True)
    zticklabels = ["%.1f" % z for z in zticks]

    colors = []
    segments = []
    linewidths = []

    # XZ axis
    # ---------------------------------
    X0 = np.linspace([0, 0, 0], [1, 0, 0], nx) - 0.5
    X1 = X0 + [0, 0, 1]
    X2 = X1 + [0, 0, ticks_length]
    X3 = X2 + [0, 0, ticks_pad]
    X0 = glm.transform(X0, camera)[..., :2]
    X1 = glm.transform(X1, camera)[..., :2]
    X2 = glm.transform(X2, camera)[..., :2]
    X3 = glm.transform(X3, camera)[..., :2]

    Z0 = np.linspace([0, 0, 0], [0, 0, 1], nz) - 0.5
    Z1 = Z0 + [1, 0, 0]
    Z2 = Z0 - [ticks_length, 0, 0]
    Z3 = Z2 - [ticks_pad, 0, 0]
    Z0 = glm.transform(Z0, camera)[..., :2]
    Z1 = glm.transform(Z1, camera)[..., :2]
    Z2 = glm.transform(Z2, camera)[..., :2]
    Z3 = glm.transform(Z3, camera)[..., :2]

    for p0, p1, p2, p3, label in zip(X0, X1, X2, X3, xticklabels):
        # grid line
        segments.append([p0, p1])
        linewidths.append(grid_linewidth)
        colors.append(grid_color)

        if not ticks:
            continue

        # tick
        segments.append([p1, p2])
        linewidths.append(ticks_linewidth)
        colors.append(ticks_color)

        # label
        ax.text(p3[0], p3[1], label, ha="center", va="center", size="x-small")

    for p0, p1, p2, p3, label in zip(Z0, Z1, Z2, Z3, zticklabels):
        # grid lines
        segments.append([p0, p1])
        linewidths.append(grid_linewidth)
        colors.append(grid_color)

        if not ticks:
            continue

        # ticks
        segments.append([p0, p2])
        linewidths.append(ticks_linewidth)
        colors.append(ticks_color)

        # label
        ax.text(p3[0], p3[1], label, ha="center", va="center", size="x-small")

    # axis border
    segments.append([X0[0], X0[-1], X1[-1], X1[0], X0[0]])
    linewidths.append(axis_linewidth)
    colors.append(axis_color)

    # XY axis
    # ---------------------------------
    X0 = np.linspace([0, 0, 0], [1, 0, 0], nx) - 0.5
    X1 = X0 + [0, 1, 0]
    X0 = glm.transform(X0, camera)[..., :2]
    X1 = glm.transform(X1, camera)[..., :2]
    Y0 = np.linspace([0, 0, 0], [0, 1, 0], ny) - 0.5
    Y1 = Y0 + [1, 0, 0]
    Y2 = Y0 - [ticks_length, 0, 0]
    Y3 = Y2 - [ticks_pad, 0, 0]
    Y0 = glm.transform(Y0, camera)[..., :2]
    Y1 = glm.transform(Y1, camera)[..., :2]
    Y2 = glm.transform(Y2, camera)[..., :2]
    Y3 = glm.transform(Y3, camera)[..., :2]

    for p0, p1 in zip(X0, X1):
        # grid lines
        segments.append([p0, p1])
        linewidths.append(grid_linewidth)
        colors.append(grid_color)

    for p0, p1, p2, p3, label in zip(Y0, Y1, Y2, Y3, yticklabels):
        # grid lines
        segments.append([p0, p1])
        linewidths.append(grid_linewidth)
        colors.append(grid_color)

        if not ticks:
            continue
        # ticks
        segments.append([p0, p2])
        linewidths.append(ticks_linewidth)
        colors.append(ticks_color)

        # label
        ax.text(p3[0], p3[1], label, ha="center", va="center", size="x-small")

    # axis border
    segments.append([X0[0], X0[-1], X1[-1], X1[0], X0[0]])
    linewidths.append(axis_linewidth)
    colors.append(axis_color)

    # ZY axis
    # ---------------------------------
    Z0 = np.linspace([1, 0, 0], [1, 0, 1], nx) - 0.5
    Z1 = Z0 + [0, 1, 0]
    Z0 = glm.transform(Z0, camera)[..., :2]
    Z1 = glm.transform(Z1, camera)[..., :2]

    Y0 = np.linspace([1, 0, 0], [1, 1, 0], ny) - 0.5
    Y1 = Y0 + [0, 0, 1]
    Y0 = glm.transform(Y0, camera)[..., :2]
    Y1 = glm.transform(Y1, camera)[..., :2]

    for p0, p1 in zip(Z0, Z1):
        # grid lines
        segments.append([p0, p1])
        linewidths.append(grid_linewidth)
        colors.append(grid_color)

    for p0, p1 in zip(Y0, Y1):
        # grid lines
        segments.append([p0, p1])
        linewidths.append(grid_linewidth)
        colors.append(grid_color)

    # axis border
    segments.append([Y0[0], Y0[-1], Y1[-1], Y1[0], Y0[0]])
    linewidths.append(axis_linewidth)
    colors.append(axis_color)

    # Actual rendering
    collection = PolyCollection(
        segments,
        closed=False,
        clip_on=False,
        linewidths=linewidths,
        facecolors="None",
        edgecolor=colors,
    )
    ax.add_collection(collection)


# -----------------------------------------------------------------------------
def mesh(
    ax,
    camera,
    vertices,
    faces,
    cmap=None,
    facecolor="white",
    edgecolor="none",
    linewidth=1.0,
    mode="all",
):

    # Mandatory settings for matplotlib axes
    # --------------------------------------
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect(1)
    ax.axis("off")

    facecolor = mpl.colors.to_rgba_array(facecolor)
    edgecolor = mpl.colors.to_rgba_array(edgecolor)

    T = glm.transform(vertices, camera)[faces]
    Z = -T[:, :, 2].mean(axis=1)

    # Facecolor using depth buffer
    if cmap is not None:
        cmap = plt.get_cmap("magma")
        norm = mpl.colors.Normalize(vmin=Z.min(), vmax=Z.max())
        facecolor = cmap(norm(Z))

    # Back face culling
    if mode == "front":
        front, back = glm.frontback(T)
        T, Z = T[front], Z[front]
        if len(facecolor) == len(faces):
            facecolor = facecolor[front]
        if len(edgecolor) == len(faces):
            facecolor = edgecolor[front]
    # Front face culling
    elif mode == "back":
        front, back = glm.frontback(T)
        T, Z = T[back], Z[back]
        if len(facecolor) == len(faces):
            facecolor = facecolor[back]
        if len(edgecolor) == len(faces):
            facecolor = edgecolor[back]

    # Separate 2d triangles from zbuffer
    triangles = T[:, :, :2]
    antialiased = True
    if linewidth == 0.0:
        antialiased = False

    # Sort triangles according to z buffer
    I = np.argsort(Z)
    triangles = triangles[I, :]
    if len(facecolor) == len(I):
        facecolor = facecolor[I, :]
    if len(edgecolor) == len(I):
        edgecolor = edgecolor[I, :]

    collection = PolyCollection(
        triangles,
        linewidth=linewidth,
        antialiased=antialiased,
        facecolor=facecolor,
        edgecolor=edgecolor,
    )
    ax.add_collection(collection)


# -----------------------------------------------------------------------------
def surf(
    ax,
    camera,
    Y,
    facecolor="white",
    edgecolor="black",
    facecolors=None,
    edgecolors=None,
    linewidth=0.5,
    shading=(1.00, 1.00, 1.00, 0.75, 0.50, 1.00),
):

    # Mandatory settings for matplotlib axes
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect(1)
    ax.axis("off")

    # Facecolor
    if facecolors is None:
        facecolors = np.zeros((Y.shape[0], Y.shape[1], 3))
        facecolors[...] = mpl.colors.to_rgb(facecolor)
    facecolors[...] = facecolors[..., :3]

    # Facecolor
    if edgecolors is None:
        edgecolors = np.zeros((Y.shape[0], Y.shape[1], 3))
        edgecolors[...] = mpl.colors.to_rgb(edgecolor)
    edgecolors[...] = edgecolors[..., :3]

    # Surface
    n = Y.shape[0]
    T = np.linspace(-0.5, +0.5, n)
    X, Z = np.meshgrid(T, T)
    V = np.c_[X.ravel(), Y.ravel() - 0.5, Z.ravel()]
    F = (np.arange((n - 1) * (n)).reshape(n - 1, n))[:, :-1].T
    F = np.repeat(F.ravel(), 6).reshape(n - 1, n - 1, 6)
    F[:, :] += np.array([0, n + 1, 1, 0, n, n + 1])
    F = F.reshape(-1, 3)
    V = glm.transform(V, camera)
    T = V[F]

    # Create list from array such that we can add lines
    polys = T[..., :2].tolist()
    zbuffer = (-T[..., 2].mean(axis=1)).tolist()
    edgecolors = ["none",] * len(polys)
    antialiased = [False,] * len(polys)
    linewidths = [1.0,] * len(polys)
    facecolors = ((facecolors.reshape(-1, 3))[F].mean(axis=1)).tolist()

    # Helper function for creating a line segment between two points
    def segment(p0, p1, linewidth=1.5, epsilon=0.01):
        polys.append([p0[:2], p1[:2]])
        facecolors.append("none")
        edgecolors.append("black")
        antialiased.append(True)
        linewidths.append(linewidth)
        zbuffer.append(-(p0[2] + p1[2]) / 2 + epsilon)

    # Border + grid over the surface
    V = V.reshape(n, n, -1)

    # Border
    for i in range(0, n - 1):
        segment(V[i, 0], V[i + 1, 0])
        segment(V[i, -1], V[i + 1, -1])
        segment(V[0, i], V[0, i + 1])
        segment(V[-1, i], V[-1, i + 1])

    for i in range(0, n - 1):
        for j in range(0, n - 1):
            segment(V[i, j], V[i + 1, j], 0.5)
            segment(V[j, i], V[j, i + 1], 0.5)

    # Sort everything
    I = np.argsort(zbuffer)
    polys = [polys[i] for i in I]
    facecolors = [facecolors[i] for i in I]
    edgecolors = [edgecolors[i] for i in I]
    linewidths = [linewidths[i] for i in I]
    antialiased = [antialiased[i] for i in I]

    # Display
    collection = PolyCollection(
        polys,
        linewidth=linewidths,
        antialiased=antialiased,
        facecolors=facecolors,
        edgecolors=edgecolors,
    )
    ax.add_collection(collection)


# -----------------------------------------------------------------------------
def bar(
    ax,
    camera,
    Y,
    facecolor="white",
    edgecolor="black",
    facecolors=None,
    edgecolors=None,
    linewidth=0.5,
    shading=(1.00, 1.00, 1.00, 0.75, 0.50, 1.00),
):

    # Mandatory settings for matplotlib axes
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect(1)
    ax.axis("off")

    # Facecolor
    if facecolors is None:
        facecolors = np.zeros((Y.shape[0], Y.shape[1], 3))
        facecolors[...] = mpl.colors.to_rgb(facecolor)
    facecolors[...] = facecolors[..., :3]

    # Facecolor
    if edgecolors is None:
        edgecolors = np.zeros((Y.shape[0], Y.shape[1], 3))
        edgecolors[...] = mpl.colors.to_rgb(edgecolor)
    edgecolors[...] = edgecolors[..., :3]

    # Here we compute the eight 3D vertices necessary to render a bar
    shape = Y.shape
    dx, dz = 0.5 / shape[0], 0.5 / shape[1]
    X, Z = np.meshgrid(
        np.linspace(-0.5 + dx, 0.5 - dx, shape[0]),
        np.linspace(-0.5 + dz, 0.5 - dz, shape[1]),
    )
    P = np.c_[X.ravel(), np.zeros(X.size), Z.ravel()]
    P = P.reshape(shape[0], shape[1], 3)
    dx = np.array([dx, 0, 0])
    dz = np.array([0, 0, dz])
    dy = np.zeros((shape[0], shape[1], 3))
    V = np.zeros((8, shape[0], shape[1], 3))

    dy[..., 1] = -0.5
    V[0] = P + dx - dz + dy
    V[1] = P - dx - dz + dy
    V[2] = P + dx + dz + dy
    V[3] = P - dx + dz + dy

    dy[..., 1] = -0.5 + Y
    V[4] = P + dx - dz + dy
    V[5] = P - dx - dz + dy
    V[6] = P + dx + dz + dy
    V[7] = P - dx + dz + dy

    # Transformation of the vertices in 2D + z
    T = glm.transform(V, camera)
    V = T[:, :2].reshape(8, shape[0], shape[1], 2)
    Z = -T[:, 2].reshape(8 * shape[0] * shape[1])

    # Normalization of the z value such that we can manipulate zbar / zface
    # Drawback is that it cannot be sorted anymore with other 3d objects
    Z = glm.rescale(Z, 0, 1)

    # Building of individual bars (without bottom face)
    #  and a new z buffer that is a combination of the bar and face mean z
    faces, colors, zbuffer = [], [], []
    indices = (
        [4, 5, 7, 6],  # +Y
        [0, 1, 3, 2],  # -Y
        [0, 1, 5, 4],  # +X
        [1, 3, 7, 5],  # -X
        [2, 3, 7, 6],  # -Z
        [0, 2, 6, 4],
    )  # +Z
    FC = np.zeros((shape[0], shape[1], len(indices), 3))
    EC = np.zeros((shape[0], shape[1], len(indices), 3))
    F = np.zeros((shape[0], shape[1], len(indices), 4, 2))
    Z_ = np.zeros((shape[0], shape[1], len(indices)))

    # This could probably be vectorized but it might be tricky
    for i in range(shape[0]):
        for j in range(shape[1]):
            index = np.arange(8) * shape[0] * shape[1] + i * shape[1] + j
            zbar = 1 * Z[index].mean()
            for k, ((v0, v1, v2, v3), shade) in enumerate(zip(indices, shading)):
                zface = (Z[index[v0]] + Z[index[v1]] + Z[index[v2]] + Z[index[v3]]) / 4
                F[i, j, k] = V[v0, i, j], V[v1, i, j], V[v2, i, j], V[v3, i, j]
                Z_[i, j, k] = 10 * zbar + zface
                FC[i, j, k] = facecolors[i, j] * shade
                EC[i, j, k] = edgecolors[i, j]

    # Final reshape for sorting quads
    Z = Z_.reshape(shape[0] * shape[1] * len(indices))
    F = F.reshape(shape[0] * shape[1] * len(indices), 4, 2)
    FC = FC.reshape(shape[0] * shape[1] * len(indices), 3)
    EC = EC.reshape(shape[0] * shape[1] * len(indices), 3)
    I = np.argsort(Z)

    collection = PolyCollection(
        F[I], linewidth=0.25, facecolors=FC[I], edgecolors=EC[I]
    )
    ax.add_collection(collection)


# -----------------------------------------------------------------------------
def contour(ax, camera, Y, n_levels=32):

    n = Y.shape[0]
    T = np.linspace(-0.5, +0.5, n)
    X, Z = np.meshgrid(T, T)
    C = ax.contour(X, Z, Y, n_levels)

    cmap = plt.get_cmap("magma")
    ymin, ymax = Y.min(), Y.max()
    norm = mpl.colors.Normalize(vmin=2 * ymin, vmax=ymax)

    dy = 0.99 * (ymax - ymin) / n_levels

    segments = []
    facecolors = []
    edgecolors = []
    closed = []
    antialiased = []
    epsilon = 0.0025

    for level, collection in zip(C.levels, C.collections):

        local_segments = []
        local_zbuffer = []
        local_antialiased = []
        local_edgecolors = []
        local_facecolors = []
        local_closed = []

        # Collect and transform all paths
        paths = []
        for path in collection.get_paths():
            V = np.array(path.vertices)
            V = np.c_[V[:, 0], level * np.ones(len(path)), V[:, 1]]
            V0 = V
            V1 = V0 - [0, dy, 0]
            T0 = glm.transform(V0, camera)
            T1 = glm.transform(V1, camera)
            V0, Z0 = T0[:, :2], T0[:, 2]
            V1, Z1 = T1[:, :2], T1[:, 2]
            paths.append([V, V0, Z0, V1, Z1])

        for (V, V0, Z0, V1, Z1) in paths:

            for i in range(len(V0) - 1):
                local_segments.append([V0[i], V0[i + 1], V1[i + 1], V1[i]])
                local_zbuffer.append(-(Z0[i] + Z0[i + 1] + Z1[i + 1] + Z1[i]) / 4)
                local_antialiased.append(False)
                local_edgecolors.append("none")
                facecolor = np.array(cmap(norm(level))[:3])
                local_facecolors.append(0.75 * facecolor)
                local_closed.append(True)

                local_segments.append([V1[i + 1], V1[i]])
                local_zbuffer.append(-(Z1[i + 1] + Z1[i]) / 2 + epsilon)
                local_antialiased.append(True)
                facecolor = np.array(cmap(norm(level))[:3])
                local_edgecolors.append(facecolor * 0.25)
                local_facecolors.append("none")
                local_closed.append(False)

                if ((V[0] - V[-1]) ** 2).sum() > 0.00001:
                    local_segments.append([V0[i + 1], V0[i]])
                    local_zbuffer.append(-(Z0[i + 1] + Z0[i]) / 2 + epsilon)
                    local_antialiased.append(True)
                    facecolor = np.array(cmap(norm(level))[:3])
                    local_edgecolors.append(facecolor * 0.25)
                    local_facecolors.append("none")
                    local_closed.append(False)

        I = np.argsort(local_zbuffer)
        local_segments = [local_segments[i] for i in I]
        local_facecolors = [local_facecolors[i] for i in I]
        local_edgecolors = [local_edgecolors[i] for i in I]
        local_closed = [local_closed[i] for i in I]
        local_antialiased = [local_antialiased[i] for i in I]

        segments.extend(local_segments)
        facecolors.extend(local_facecolors)
        edgecolors.extend(local_edgecolors)
        closed.extend(local_closed)
        antialiased.extend(local_antialiased)

        for (V, V0, Z0, V1, Z1) in paths:
            if ((V[0] - V[-1]) ** 2).sum() < 0.00001:
                segments.append(V0)
                antialiased.append(True)
                facecolor = cmap(norm(level))[:3]
                facecolors.append(facecolor)
                edgecolors.append("black")
                closed.append(True)

        collection.remove()

    collection = PolyCollection(
        segments,
        linewidth=0.5,
        antialiased=antialiased,
        closed=closed,
        facecolors=facecolors,
        edgecolors=edgecolors,
    )
    ax.add_collection(collection)
