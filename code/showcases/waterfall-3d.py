# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from shapely.geometry import box, Polygon
from scipy.ndimage import gaussian_filter1d
from matplotlib.collections import PolyCollection
from matplotlib.transforms import Affine2D
from matplotlib.text import TextPath
from matplotlib.patches import PathPatch
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


# Some nice but random curves
def random_curve(n=100):
    Y = np.random.uniform(0, 1, n)
    Y = gaussian_filter1d(Y, 1)
    X = np.linspace(-1, 1, len(Y))
    Y *= np.exp(-2 * (X * X))
    return Y


def cmap_plot(Y, ymin=0, ymax=1, n=50, cmap="magma", y0=0):
    X = np.linspace(0.3, 0.7, len(Y))
    Y = gaussian_filter1d(Y, 2)

    verts = []
    colors = []
    P = Polygon([(X[0], 0), *zip(X, Y), (X[-1], 0)])

    dy = (ymax - ymin) / n
    cmap = plt.cm.get_cmap(cmap)
    cnorm = matplotlib.colors.Normalize(vmin=ymin, vmax=ymax)

    for y in np.arange(Y.min(), Y.max(), dy):
        B = box(0, y, 10, y + dy)
        I = P.intersection(B)
        if hasattr(I, "geoms"):
            for p in I.geoms:
                V = np.array(p.exterior.coords)
                V[:, 1] += y0
                verts.append(V)
                colors.append(cmap(cnorm(y)))
        else:
            if I.exterior.coords:
                V = np.array(I.exterior.coords)
                V[:, 1] += y0
                verts.append(V)
                colors.append(cmap(cnorm(y)))

    return verts, colors


fig = plt.figure(figsize=(10, 10))
fig.patch.set_facecolor("black")
ax = fig.gca(projection="3d", proj_type="ortho")
ax.patch.set_facecolor("black")

# Make panes transparent
ax.xaxis.pane.fill = False  # Left pane
ax.yaxis.pane.fill = False  # Right pane
ax.zaxis.pane.fill = False  # Right pane

# Remove grid lines
ax.grid(False)

# Remove tick labels
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])

# Transparent spines
ax.w_xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.w_yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.w_zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))

# Transparent panes
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

# No ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])


np.random.seed(1)

# text3d(ax, (1.05, 0.5, 0), "Series A", zdir="x",
#        size=0.05, facecolor="white", edgecolor="None", alpha=.25)

# text3d(ax, (1.05, 0.5, 0.6), "Series B", zdir="x",
#        size=0.05, facecolor="white", edgecolor="None", alpha=.25)

# text3d(ax, (1.05, 0.5, 1.2), "Series C", zdir="x",
#        size=0.05, facecolor="white", edgecolor="None", alpha=.25)


for zs in np.linspace(0, 1, 50):
    Y = 0.1 * random_curve()
    verts, colors = cmap_plot(Y, ymin=0, ymax=0.075, n=50, cmap="magma", y0=-0.2)
    collection = PolyCollection(
        verts, antialiased=False, edgecolors="None", facecolor=colors
    )
    ax.add_collection3d(collection, zdir="x", zs=zs)

    Y = 0.1 * random_curve()
    verts, colors = cmap_plot(Y, ymin=0, ymax=0.075, n=50, cmap="magma", y0=0.4)
    collection = PolyCollection(
        verts, antialiased=False, edgecolors="None", facecolor=colors
    )
    ax.add_collection3d(collection, zdir="x", zs=zs)

    Y = 0.1 * random_curve()
    verts, colors = cmap_plot(Y, ymin=0, ymax=0.075, n=50, cmap="magma", y0=1.0)
    collection = PolyCollection(
        verts, antialiased=False, edgecolors="None", facecolor=colors
    )
    ax.add_collection3d(collection, zdir="x", zs=zs)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

ax.view_init(elev=40, azim=-40)

plt.tight_layout()
plt.savefig("../../figures/showcases/waterfall-3d.pdf")
# plt.savefig("./waterfall-3d.png", dpi=300)
plt.show()
