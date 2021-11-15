# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
# Defaults settings / Custom defaults
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 257, endpoint=True)
C, S = np.cos(X), np.sin(X)
p = plt.rcParams

p["figure.figsize"] = 6, 2.5
p["figure.facecolor"] = "#fff"

p["axes.axisbelow"] = True
p["axes.linewidth"] = 1
p["axes.facecolor"] = "#f9f9f9"
p["axes.ymargin"] = 0.0

p["axes.grid"] = True
p["axes.grid.axis"] = "x"
p["grid.color"] = "#999999"
p["grid.linestyle"] = "--"

p["axes.spines.bottom"] = True
p["axes.spines.left"] = True
p["axes.spines.right"] = False
p["axes.spines.top"] = False
p["font.sans-serif"] = ["Fira Sans Condensed"]

p["xtick.bottom"] = True
p["xtick.top"] = False
p["xtick.direction"] = "out"
p["xtick.major.size"] = 0
p["xtick.major.width"] = 1
p["xtick.major.pad"] = 65

p["ytick.left"] = True
p["ytick.right"] = False
p["ytick.direction"] = "out"
p["ytick.major.size"] = 5
p["ytick.major.width"] = 1

p["lines.linewidth"] = 2
p["lines.marker"] = "o"
p["lines.markeredgewidth"] = 1.5
p["lines.markeredgecolor"] = "auto"
p["lines.markerfacecolor"] = "white"
p["lines.markersize"] = 6


fig = plt.figure()
ax = plt.subplot(1, 1, 1, aspect=1)
ax.plot(X, C, markevery=(0, 64), clip_on=False, zorder=10)
ax.plot(X, S, markevery=(0, 64), clip_on=False, zorder=10)
ax.set_yticks([-1, 0, 1])
ax.set_xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
ax.set_xticklabels(["-π", "-π/2", "0", "+π/2", "+π"])
ax.spines["bottom"].set_position(("data", 0))

plt.tight_layout()
plt.savefig("../../figures/defaults/defaults-exercice-1.pdf")
plt.show()
