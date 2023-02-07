# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.textpath import TextPath
from matplotlib.collections import PolyCollection
from matplotlib.font_manager import FontProperties

n = 100
A = np.linspace(np.pi, n * 2 * np.pi, 10_000)
R = 5 + np.linspace(np.pi, n * 2 * np.pi, 10_000)
T = np.stack([R * np.cos(A), R * np.sin(A)], axis=1)
dx = np.cos(A) - R * np.sin(A)
dy = np.sin(A) + R * np.cos(A)
O = np.stack([-dy, dx], axis=1)
O = O / (np.linalg.norm(O, axis=1)).reshape(len(O), 1)

L = np.zeros(len(T))
np.cumsum(np.sqrt(((T[1:] - T[:-1]) ** 2).sum(axis=1)), out=L[1:])

import mpmath

mpmath.mp.dps = 15000
text = str(mpmath.pi)

path = TextPath((0, 0), text, size=6, prop=FontProperties(family="Source Serif Pro"))
path.vertices.setflags(write=1)
Vx, Vy = path.vertices[:, 0], path.vertices[:, 1]
X = np.interp(Vx, L, T[:, 0]) + Vy * np.interp(Vx, L, O[:, 0])
Y = np.interp(Vx, L, T[:, 1]) + Vy * np.interp(Vx, L, O[:, 1])
Vx[...], Vy[...] = X, Y

fig = plt.figure(figsize=(8, 8))
ax = fig.add_axes([0, 0, 1, 1], aspect=1)
patch = PathPatch(path, facecolor="k", linewidth=0)
ax.add_artist(patch)

# from matplotlib.patheffects import Stroke, Normal
# text = fig.text(.05, .060, "Scientific Visualization — Python & Matplotlib",
#                 va="bottom", size="16", color="white",
#                 transform=ax.transAxes,
#                 weight="bold", family="Roboto Condensed")
# text.set_path_effects([Stroke(linewidth=2, foreground="black"), Normal()])
# text = fig.text(.05, .055, "github.com/rougier/scientific-visualization-book",
#                 size = 10.2,  transform=ax.transAxes,
#                 va="top", color="blue", family="Roboto Mono", weight="bold")
# text.set_path_effects([Stroke(linewidth=5, foreground="white"), Normal()])

plt.rcParams["text.usetex"] = True
ax.text(-3, 0, "$\pi$", ha="center", va="center", size=500, color="white", alpha=0.6)

ax.set_xlim(-200, 200), ax.set_xticks([])
ax.set_ylim(-200, 200), ax.set_yticks([])

# plt.savefig("/Users/rougier/Desktop/spiral-pi.png", dpi=150)
plt.savefig("../../figures/showcases/text-spiral.pdf")
plt.show()
