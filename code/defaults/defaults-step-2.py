# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
# Defaults settings / explicit defaults
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 257, endpoint=True)
C, S = np.cos(X), np.sin(X)
p = plt.rcParams

fig = plt.figure(
    figsize=p["figure.figsize"],
    dpi=p["figure.dpi"],
    facecolor=p["figure.facecolor"],
    edgecolor=p["figure.edgecolor"],
    frameon=p["figure.frameon"],
)

ax = plt.subplot(1, 1, 1)

ax.plot(
    X, C, color="C0", linewidth=p["lines.linewidth"], linestyle=p["lines.linestyle"]
)

ax.plot(
    X, S, color="C1", linewidth=p["lines.linewidth"], linestyle=p["lines.linestyle"]
)

xmin, xmax = X.min(), X.max()
xmargin = p["axes.xmargin"] * (xmax - xmin)
ax.set_xlim(xmin - xmargin, xmax + xmargin)

ymin, ymax = min(C.min(), S.min()), max(C.max(), S.max())
ymargin = p["axes.ymargin"] * (ymax - ymin)
ax.set_ylim(ymin - ymargin, ymax + ymargin)

ax.tick_params(
    axis="x",
    which="major",
    direction=p["xtick.direction"],
    length=p["xtick.major.size"],
    width=p["xtick.major.width"],
)

ax.tick_params(
    axis="y",
    which="major",
    direction=p["ytick.direction"],
    length=p["ytick.major.size"],
    width=p["ytick.major.width"],
)

plt.tight_layout()
plt.savefig("../../figures/defaults/defaults-step-2.pdf")
plt.show()
