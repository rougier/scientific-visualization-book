# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.text import TextPath
from matplotlib.patches import PathPatch
from matplotlib.colors import LightSource
from matplotlib.transforms import Affine2D
from mpl_toolkits.mplot3d import Axes3D, art3d
from matplotlib.font_manager import FontProperties


def text3d(ax, xyz, s, zdir="z", size=0.1, angle=0, **kwargs):
    x, y, z = xyz
    if zdir == "y":
        xy, z = (x, z), y
    elif zdir == "x":
        xy, z = (y, z), x
    else:
        xy, z = (x, y), z
    path = TextPath((0, 0), s, size=size, prop=FontProperties(family="Roboto"))
    V = path.vertices
    V[:, 0] -= (V[:, 0].max() - V[:, 0].min()) / 2
    trans = Affine2D().rotate(angle).translate(xy[0], xy[1])
    path = PathPatch(trans.transform_path(path), **kwargs)
    ax.add_patch(path)
    art3d.pathpatch_2d_to_3d(path, z=z, zdir=zdir)


fig = plt.figure(figsize=(6, 6))
ax = plt.subplot(1, 1, 1, projection="3d")
ax.view_init(elev=30, azim=-55)
ax.set_axis_off()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

xrange = 0, 5
yrange = 0, 5
zrange = 0, 2
xticks = (1.0, 0.2)
yticks = (1.0, 0.2)
zticks = (1.0, 0.2)

maxrange = max(xrange[1] - xrange[0], yrange[1] - yrange[0], zrange[1] - zrange[0])
xtransform = lambda x: (x - xrange[0]) / maxrange
ytransform = lambda y: (y - yrange[0]) / maxrange
ztransform = lambda z: (z - zrange[0]) / maxrange
xmin, xmax = xtransform(xrange[0]), xtransform(xrange[1])
ymin, ymax = ytransform(yrange[0]), ytransform(yrange[1])
zmin, zmax = ztransform(zrange[0]), ztransform(zrange[1])


# Minor gridlines
linewidth, color = 0.25, "0.75"
for x in np.arange(xrange[0], xrange[1] + xticks[1], xticks[1]):
    x = xtransform(x)
    ax.plot(
        [x, x, x],
        [ymin, ymax, ymax],
        [zmin, zmin, zmax],
        linewidth=linewidth,
        color=color,
        zorder=-50,
    )
for y in np.arange(yrange[0], yrange[1] + yticks[1], yticks[1]):
    y = ytransform(y)
    ax.plot(
        [xmax, xmin, xmin],
        [y, y, y],
        [zmin, zmin, zmax],
        linewidth=linewidth,
        color=color,
        zorder=-50,
    )
for z in np.arange(zrange[0], zrange[1] + zticks[1], zticks[1]):
    z = ztransform(z)
    ax.plot(
        [xmax, xmin, xmin],
        [ymax, ymax, ymin],
        [z, z, z],
        linewidth=linewidth,
        color=color,
        zorder=-50,
    )

# Major gridlines
linewidth, color = 0.50, "0.50"
for x in np.arange(xrange[0], xrange[1] + xticks[0], xticks[0]):
    x = xtransform(x)
    ax.plot(
        [x, x, x],
        [ymin, ymax, ymax],
        [zmin, zmin, zmax],
        linewidth=linewidth,
        color=color,
        zorder=-25,
    )
for y in np.arange(yrange[0], yrange[1] + yticks[0], yticks[0]):
    y = ytransform(y)
    ax.plot(
        [xmax, xmin, xmin],
        [y, y, y],
        [zmin, zmin, zmax],
        linewidth=linewidth,
        color=color,
        zorder=-25,
    )
for z in np.arange(zrange[0], zrange[1] + zticks[0], zticks[0]):
    z = ztransform(z)
    ax.plot(
        [xmax, xmin, xmin],
        [ymax, ymax, ymin],
        [z, z, z],
        linewidth=linewidth,
        color=color,
        zorder=-25,
    )

# Frame
linewidth, color = 1.00, "0.00"
ax.plot(
    [xmin, xmin, xmax, xmax, xmin],
    [ymin, ymax, ymax, ymin, ymin],
    [zmin, zmin, zmin, zmin, zmin],
    linewidth=linewidth,
    color=color,
    zorder=-10,
)
ax.plot(
    [xmin, xmin, xmax, xmax, xmin],
    [ymax, ymax, ymax, ymax, ymax],
    [zmin, zmax, zmax, zmin, zmin],
    linewidth=linewidth,
    color=color,
    zorder=-10,
)
ax.plot(
    [xmin, xmin, xmin, xmin, xmin],
    [ymin, ymin, ymax, ymax, ymin],
    [zmin, zmax, zmax, zmin, zmin],
    linewidth=linewidth,
    color=color,
    zorder=-10,
)

# Minor ticks
linewidth, length, color = 0.25, 0.02, "0.5"
for x in np.arange(xrange[0], xrange[1] + xticks[1], xticks[1]):
    x = xtransform(x)
    ax.plot(
        [x, x],
        [ymin, ymin - length],
        [zmin, zmin],
        linewidth=linewidth,
        color=color,
        zorder=-50,
    )
for y in np.arange(yrange[0], yrange[1] + yticks[1], yticks[1]):
    y = ytransform(y)
    ax.plot(
        [xmax, xmax + length],
        [y, y],
        [zmin, zmin],
        linewidth=linewidth,
        color=color,
        zorder=-50,
    )
for z in np.arange(zrange[0], zrange[1] + zticks[1], zticks[1]):
    z = ztransform(z)
    ax.plot(
        [xmin, xmin - length],
        [ymin, ymin],
        [z, z],
        linewidth=linewidth,
        color=color,
        zorder=-50,
    )

# Major ticks & labels
linewidth, length, color = 0.75, 0.04, "0.0"
for x in np.arange(xrange[0], xrange[1] + xticks[0], xticks[0]):
    x_ = xtransform(x)
    ax.plot(
        [x_, x_],
        [ymin, ymin - length],
        [zmin, zmin],
        linewidth=linewidth,
        color=color,
        zorder=-50,
    )
    text3d(
        ax,
        (x_, ymin - 2 * length, zmin),
        "%.1f" % x,
        size=0.04,
        facecolor="black",
        edgecolor="None",
    )
for y in np.arange(yrange[0], yrange[1] + yticks[0], yticks[0]):
    y_ = ytransform(y)
    ax.plot(
        [xmax, xmax + length],
        [y_, y_],
        [zmin, zmin],
        linewidth=linewidth,
        color=color,
        zorder=-50,
    )
    text3d(
        ax,
        (xmax + 2 * length, y_, zmin),
        "%.1f" % y,
        angle=np.pi / 2,
        size=0.04,
        facecolor="black",
        edgecolor="None",
    )
for z in np.arange(zrange[0], zrange[1] + zticks[1], zticks[0]):
    z_ = ztransform(z)
    ax.plot(
        [xmin, xmin - length],
        [ymin, ymin],
        [z_, z_],
        linewidth=linewidth,
        color=color,
        zorder=-50,
    )
    text3d(
        ax,
        (xmin - 2 * length, ymin, z_),
        "%.1f" % z,
        zdir="y",
        size=0.04,
        facecolor="black",
        edgecolor="None",
    )


# Data
n = 101
X = Y = np.linspace(-1, 1, n)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(5 * (X ** 2 + Y ** 2))
Z = 0.5 * np.exp(-0.5 * R * R)
X, Y = (1 + X) / 2, (1 + Y) / 2

# Plot
C = np.ones((n, n, 3))
I1 = LightSource(azdeg=0, altdeg=25).hillshade(Z).reshape(n, n, 1)
I2 = LightSource(azdeg=120, altdeg=25).hillshade(Z).reshape(n, n, 1)
I3 = LightSource(azdeg=240, altdeg=25).hillshade(Z).reshape(n, n, 1)
C = 0.5 * C + (I1 * (1, 0, 0) + I2 * (0, 1, 0) + I3 * (0, 0, 1))
C = np.minimum(C, (1, 1, 1))
C[::2, ::2] = C[1::2, 1::2] = 0.0, 0.0, 0.0


# ax.plot_wireframe(X, Y, Z, rstride=n-1, cstride=n-1, color="black",
#                  linewidth=3, antialiased=True, zorder=25)
ax.plot_wireframe(
    X,
    Y,
    Z,
    rstride=1,
    cstride=1,
    color="black",
    linewidth=5,
    antialiased=True,
    zorder=10,
)
ax.plot_wireframe(
    X,
    Y,
    Z,
    rstride=1,
    cstride=1,
    color="white",
    linewidth=2,
    antialiased=True,
    zorder=20,
)
ax.plot_surface(
    X,
    Y,
    Z,
    rstride=5,
    cstride=5,
    facecolors=C,
    shade=False,
    edgecolor="None",
    linewidth=0,
    antialiased=True,
    zorder=30,
)

text3d(
    ax,
    ((xmin + xmax) / 2, ymax, 1.05 * zmax),
    "X axis",
    zdir="y",
    size=0.05,
    facecolor="black",
    edgecolor="None",
)
text3d(
    ax,
    (xmin, (ymin + ymax) / 2, 1.05 * zmax),
    "Y axis",
    zdir="x",
    size=0.05,
    facecolor="black",
    edgecolor="None",
)
text3d(
    ax,
    (1.05 * xmax, ymax, (zmin + zmax) / 2),
    "Z axis",
    angle=np.pi / 2,
    zdir="y",
    size=0.05,
    facecolor="black",
    edgecolor="None",
)


plt.tight_layout()
plt.savefig("../../figures/typography/projection-3d-gaussian.pdf")
plt.show()
