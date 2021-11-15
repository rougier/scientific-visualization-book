# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import scipy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.textpath import TextPath
from matplotlib.patches import PathPatch
from matplotlib.font_manager import FontProperties


def interpolate(X, Y, T):
    dR = (np.diff(X) ** 2 + np.diff(Y) ** 2) ** 0.5
    R = np.zeros_like(X)
    R[1:] = np.cumsum(dR)
    return np.interp(T, R, X), np.interp(T, R, Y), R[-1]


def contour(X, Y, text, offset=0):

    # Interpolate text along curve
    # X0,Y0 for position  + X1,Y1 for normal vectors
    path = TextPath(
        (0, -0.75), text, prop=FontProperties(size=2, family="Roboto", weight="bold")
    )
    V = path.vertices
    X0, Y0, D = interpolate(X, Y, offset + V[:, 0])
    X1, Y1, _ = interpolate(X, Y, offset + V[:, 0] + 0.1)

    # Here we interpolate the original path to get the "remainder"
    #  (path minus text)
    X, Y, _ = interpolate(X, Y, np.linspace(V[:, 0].max() + 1, D - 1, 200))
    plt.plot(
        X, Y, color="black", linewidth=0.5, markersize=1, marker="o", markevery=[0, -1]
    )

    # Transform text vertices
    dX, dY = X1 - X0, Y1 - Y0
    norm = np.sqrt(dX ** 2 + dY ** 2)
    dX, dY = dX / norm, dY / norm
    X0 += -V[:, 1] * dY
    Y0 += +V[:, 1] * dX
    V[:, 0], V[:, 1] = X0, Y0

    # Faint outline
    patch = PathPatch(
        path,
        facecolor="white",
        zorder=10,
        alpha=0.25,
        edgecolor="white",
        linewidth=1.25,
    )
    ax.add_artist(patch)

    # Actual text
    patch = PathPatch(
        path, facecolor="black", zorder=30, edgecolor="black", linewidth=0.0
    )
    ax.add_artist(patch)


# Some data
n = 64
X, Z = np.meshgrid(
    np.linspace(-0.5 + 0.5 / n, +0.5 - 0.5 / n, n),
    np.linspace(-0.5 + 0.5 / n, +0.5 - 0.5 / n, n),
)
Y = 0.75 * np.exp(-10 * (X ** 2 + Z ** 2))


def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-(x ** 2) - y ** 2)


n = 100
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)
Z = 0.5 * f(X, Y)


fig = plt.figure(figsize=(10, 5), dpi=100)
levels = 10

# Regular contour with straight labels
ax = fig.add_subplot(1, 2, 1, aspect=1, xticks=[], yticks=[])
CF = plt.contourf(Z, origin="lower", levels=levels)
CS = plt.contour(Z, origin="lower", levels=levels, colors="black", linewidths=0.5)
ax.clabel(CS, CS.levels)

# Regular contour with curved labels
# ! aspect=1 is critical here, else text path would be deformed
ax = fig.add_subplot(1, 2, 2, aspect=1, xticks=[], yticks=[])
CF = plt.contourf(Z, origin="lower", levels=levels)
CS = plt.contour(
    Z, origin="lower", levels=levels, alpha=0, colors="black", linewidths=0.5
)

for level, collection in zip(CS.levels[:], CS.collections[:]):
    for path in collection.get_paths():
        V = np.array(path.vertices)
        text = "%.3f" % level
        if level == 0.0:
            text = "  DO NOT CROSS  •••" * 8
        contour(V[:, 0], V[:, 1], text)

plt.tight_layout()
plt.savefig("../../figures/typography/typography-text-path.png", dpi=600)
plt.savefig("../../figures/typography/typography-text-path.pdf", dpi=600)
plt.show()
