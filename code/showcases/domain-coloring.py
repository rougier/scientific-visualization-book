# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patheffects import Stroke, Normal


def normalize(Z):
    zmin, zmax = Z.min(), Z.max()
    return (Z - zmin) / (zmax - zmin)


T = np.linspace(-2.5, 2.5, 2048)
X, Y = np.meshgrid(T, T)
Z = X + 1j * Y
Z = Z + 1 / Z
A = normalize(np.angle(Z))
N = normalize(np.abs(Z)) * 2 * np.pi * 200


fig = plt.figure(figsize=(8, 8))
e = 0.001
ax = fig.add_axes([e, e, 1 - 2 * e, 1 - 2 * e], frameon=True, facecolor="black")

ax.imshow(
    A,
    interpolation="bicubic",
    cmap="Spectral",
    rasterized=True,
    alpha=1 - (N < 1.5 * np.pi) * 0.25 * abs(np.cos(N % (np.pi / 2))) ** 2,
)
ax.contour(np.abs(Z.real - np.round(Z.real)), 1, colors="black", linewidths=0.25)
ax.contour(np.abs(Z.imag - np.round(Z.imag)), 1, colors="black", linewidths=0.25)


ax.set_xticks([])
ax.set_yticks([])
plt.savefig("../../figures/showcases/domain-coloring.png", dpi=600)
plt.savefig("../../figures/showcases/domain-coloring.pdf")
plt.show()
