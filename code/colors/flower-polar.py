# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
# Flower polar / flower power (poly collection and polar projection)
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.collections import PolyCollection


def flower(ax, n_branches=24, n_sections=4, lw=1):
    R = np.linspace(0.1, 1.0, 25)
    paths = []
    facecolors = []
    n_sections += 1

    for i in range(n_branches):
        for j in range(n_sections - 1):
            R_, T_ = [], []
            T = np.linspace(
                i * 2 * np.pi / n_branches,
                (i + n_sections / 2) * 2 * np.pi / n_branches,
                len(R),
            )
            t = np.interp(
                np.linspace(j + 1, j + 2, 20), np.linspace(0, n_sections, len(T)), T
            )
            r = np.interp(
                np.linspace(j + 1, j + 2, 20), np.linspace(0, n_sections, len(R)), R
            )
            R_.extend(r[::1].tolist())
            T_.extend(t[::1].tolist())

            T = np.linspace(
                (i + 1 + j + 1) * 2 * np.pi / n_branches,
                (i + 1 + j + 1 - n_sections / 2) * 2 * np.pi / n_branches,
                len(R),
            )
            t = np.interp(
                np.linspace(j + 1, j + 2, 20), np.linspace(0, n_sections, len(T)), T
            )
            r = np.interp(
                np.linspace(j + 1, j + 2, 20), np.linspace(0, n_sections, len(R)), R
            )
            R_.extend(r[::-1].tolist())
            T_.extend(t[::-1].tolist())

            T = np.linspace(
                (i + 1) * 2 * np.pi / n_branches,
                (i + 1 + n_sections / 2) * 2 * np.pi / n_branches,
                len(R),
            )
            t = np.interp(
                np.linspace(j, j + 1, 20), np.linspace(0, n_sections, len(T)), T
            )
            r = np.interp(
                np.linspace(j, j + 1, 20), np.linspace(0, n_sections, len(R)), R
            )
            R_.extend(r[::-1].tolist())
            T_.extend(t[::-1].tolist())

            T = np.linspace(
                (i + 1 + j) * 2 * np.pi / n_branches,
                (i + 1 + j - n_sections / 2) * 2 * np.pi / n_branches,
                len(R),
            )
            t = np.interp(
                np.linspace(j, j + 1, 20), np.linspace(0, n_sections, len(T)), T
            )
            r = np.interp(
                np.linspace(j, j + 1, 20), np.linspace(0, n_sections, len(R)), R
            )
            R_.extend(r[::1].tolist())
            T_.extend(t[::1].tolist())

            P = np.dstack([T_, R_]).squeeze()
            paths.append(P)
            h = i / n_branches
            s = 0.5 + 0.5 * j / (n_sections - 1)
            v = 1.00
            facecolors.append(colors.hsv_to_rgb([h, s, v]))

    collection = PolyCollection(
        paths, linewidths=5.5 * lw, facecolors="None", edgecolors="black"
    )
    ax.add_collection(collection)

    collection = PolyCollection(
        paths, linewidths=4 * lw, facecolors="None", edgecolors="white"
    )
    ax.add_collection(collection)

    ax.fill_between(np.linspace(0, 2 * np.pi, 100), 0.0, 0.5, facecolor="white")

    collection = PolyCollection(
        paths, linewidths=lw, facecolors=facecolors, edgecolors="white"
    )
    ax.add_collection(collection)


fig = plt.figure(figsize=(12, 4))

ax = fig.add_subplot(1, 3, 1, polar=True, frameon=False)
flower(ax, 6, 3, lw=2.0)
ax.set_xticks([]), ax.set_yticks([])
ax.set_rlim(0, 1.1)

ax = fig.add_subplot(1, 3, 2, polar=True, frameon=False)
flower(ax, 12, 4, lw=1.5)
ax.set_xticks([]), ax.set_yticks([])
ax.set_rlim(0, 1.1)

ax = fig.add_subplot(1, 3, 3, polar=True, frameon=False)
flower(ax, 24, 5, lw=1.0)
ax.set_xticks([]), ax.set_yticks([])
ax.set_rlim(0, 1.1)

plt.tight_layout()
plt.savefig("../../figures/colors/flower-polar.pdf", dpi=600)
# plt.savefig("../../figures/colors/flower-polar.png", dpi=300)
plt.show()
