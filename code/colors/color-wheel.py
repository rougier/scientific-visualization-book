# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
# Color wheel in HSV
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.textpath import TextPath
from matplotlib.patches import PathPatch
from matplotlib.collections import QuadMesh
from matplotlib.font_manager import FontProperties

# Curved label (polar coordinates)
def polar_text(text, angle, radius=1, scale=0.005, family="sans"):
    prop = FontProperties(family=family, weight="regular")
    path = TextPath((0, 0), text, size=1, prop=prop)
    V = path.vertices
    xmin, xmax = V[:, 0].min(), V[:, 0].max()
    V[:, 0] = angle - (V[:, 0] - (xmin + xmax) / 2) * scale
    V[:, 1] = radius + V[:, 1] * scale
    patch = PathPatch(path, facecolor="black", linewidth=0, clip_on=False)
    ax.add_artist(patch)


# Polar imshow using quadmesh
def polar_imshow(
    ax, Z, extents=[0, 1, 0, 2 * np.pi], vmin=None, vmax=None, cmap="viridis"
):

    Z = np.atleast_3d(Z)
    nr, nt, d = Z.shape
    rmin, rmax, tmin, tmax = extents

    if d == 1:
        cmap = plt.get_cmap(cmap)
        vmin = vmin or Z.min()
        vmax = vmax or Z.max()
        norm = colors.Normalize(vmin=vmin, vmax=vmax)
        facecolors = cmap(norm(Z))
    else:
        facecolors = Z.reshape(nr, nt, 3).reshape(-1, 3)

    R = np.linspace(rmin, rmax, nr + 1)
    T = np.linspace(tmin, tmax, nt + 1)
    T, R = np.meshgrid(T, R)
    nr, nt = R.shape
    R, T = R.ravel(), T.ravel()
    coords = np.column_stack((T, R))
    collection = QuadMesh(
        nt - 1,
        nr - 1,
        coords,
        rasterized=True,
        facecolors=facecolors,
        edgecolors="None",
        linewidth=0,
        antialiased=False,
    )
    ax.add_collection(collection)
    return collection


radius = 1.05
scale = 0.085
family = "Yanone Kaffeesatz"

fig = plt.figure(figsize=(8, 4))

n = 50
R = np.linspace(0, 1, 2 * n)
T = np.linspace(0, 1, 10 * n)
T, R = np.meshgrid(T, R)
H, S, V = T, R, np.ones_like(T)

# -----------------------------------------------------------------------------
ax = fig.add_subplot(2, 4, 1, polar=True, frameon=True)
Z = colors.hsv_to_rgb(np.dstack([H, S, V]))
ax.set_xticks([]), ax.set_yticks([])
polar_text(
    "<––– hue –––", family=family, angle=np.pi / 4, radius=radius, scale=2 * scale
)
ax.text(
    3 * np.pi / 4,
    1.5,
    "value = 1.00",
    family=family,
    size=10,
    bbox={
        "pad": 1.5,
        "linewidth": 0.5,
        "boxstyle": "round,pad=.2",
        "edgecolor": "black",
        "facecolor": "white",
    },
)

ax.text(np.pi, 0.0, "––– saturation –––> ", size=8, family=family)
polar_imshow(ax, Z)

# -----------------------------------------------------------------------------
ax = fig.add_subplot(2, 4, 2, polar=True, frameon=True)
Z = colors.hsv_to_rgb(np.dstack([H, S, 0.75 * V]))
ax.set_xticks([]), ax.set_yticks([])
polar_text(
    "<––– hue –––", family=family, angle=np.pi / 4, radius=radius, scale=2 * scale
)
ax.text(
    3 * np.pi / 4,
    1.5,
    "value = 0.75",
    family=family,
    size=10,
    bbox={
        "pad": 1.5,
        "linewidth": 0.5,
        "boxstyle": "round,pad=.2",
        "edgecolor": "None",
        "facecolor": "0.75",
    },
)
ax.text(np.pi, 0.0, "––– saturation –––> ", size=8, family=family)
polar_imshow(ax, Z)

# -----------------------------------------------------------------------------
ax = fig.add_subplot(2, 4, 5, polar=True, frameon=True)
Z = colors.hsv_to_rgb(np.dstack([H, S, 0.5 * V]))
ax.set_xticks([]), ax.set_yticks([])
polar_text(
    "<––– hue –––", family=family, angle=np.pi / 4, radius=radius, scale=2 * scale
)
ax.text(
    3 * np.pi / 4,
    1.5,
    "value = 0.50",
    family=family,
    size=10,
    color="white",
    bbox={
        "pad": 1.5,
        "linewidth": 0.5,
        "boxstyle": "round,pad=.2",
        "edgecolor": "None",
        "facecolor": "0.5",
    },
)
ax.text(np.pi, 0.0, "––– saturation –––> ", size=8, family=family, color="1.0")
polar_imshow(ax, Z)

# -----------------------------------------------------------------------------
ax = fig.add_subplot(2, 4, 6, polar=True, frameon=True)
Z = colors.hsv_to_rgb(np.dstack([H, S, 0.25 * V]))
ax.set_xticks([]), ax.set_yticks([])
polar_text(
    "<––– hue –––", family=family, angle=np.pi / 4, radius=radius, scale=2 * scale
)
ax.text(
    3 * np.pi / 4,
    1.5,
    "value = 0.25",
    family=family,
    size=10,
    color="white",
    bbox={
        "pad": 1.5,
        "linewidth": 0.5,
        "boxstyle": "round,pad=.2",
        "edgecolor": "None",
        "facecolor": "0.25",
    },
)
ax.text(np.pi, 0.0, "-–– saturation –––> ", size=8, family=family, color="1.0")
polar_imshow(ax, Z)

# -----------------------------------------------------------------------------
ax = fig.add_subplot(1, 2, 2, polar=True, frameon=False)
n = 100
R = np.linspace(0, 1, n)
R -= R % (1 / 5.99)
T = np.linspace(0, 1, 10 * n)
T -= T % (1 / 11.99)
T, R = np.meshgrid(T, R)
H, S, V = T, R, np.ones_like(T)
Z = colors.hsv_to_rgb(np.dstack([H, S, V]))
polar_imshow(ax, Z)
ax.set_xticks(np.linspace(0, 2 * np.pi, 13))
ax.set_yticks(np.linspace(0, 1, 7))
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.grid(linewidth=1, color="white")
labels = [
    "red",
    "orange",
    "yellow",
    "lime",
    "green",
    "turquoise",
    "cyan",
    "skyblue",
    "blue",
    "violet",
    "purple",
    "magenta",
]
for label, x in zip(labels, np.linspace(0.5, 12.5, 12)):
    label = label.upper()
    angle = x / 13 * 2 * np.pi
    polar_text(
        label.upper(), family=family, angle=angle, radius=radius, scale=1.25 * scale
    )
ax.set_theta_offset(-np.pi / 12)

R = np.ones(100)
T = np.linspace(0, 2 * np.pi, 100)
ax.plot(T, R, color="white")

plt.tight_layout()
plt.savefig("../../figures/colors/color-wheel.png", dpi=600)
plt.savefig("../../figures/colors/color-wheel.pdf", dpi=600)
plt.show()
