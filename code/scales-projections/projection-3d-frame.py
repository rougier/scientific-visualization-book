# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D, proj3d, art3d
import matplotlib.patheffects as path_effects


# Style
# -----------------------------------------------------------------------------
# plt.rc('font', family="Roboto Condensed")
plt.rc("font", family="Roboto")
plt.rc("xtick", labelsize="small")
plt.rc("ytick", labelsize="small")
plt.rc("axes", labelsize="medium", titlesize="medium")

fig = plt.figure(figsize=(6, 6))
ax = plt.subplot(1, 1, 1, projection="3d")
ax.set_axis_off()
ax.set_xlim(0, 10)
ax.set_ylim(10, 0)
ax.set_zlim(0, 10)

for d in np.arange(0, 11):
    color, linewidth, zorder = "0.75", 0.5, -100
    if d in [0, 5, 10]:
        color, linewidth, zorder = "0.5", 0.75, -50
    ax.plot([0, 0], [d, d], [0, 10], linewidth=linewidth, color=color, zorder=zorder)
    ax.plot([0, 0], [0, 10], [d, d], linewidth=linewidth, color=color, zorder=zorder)
    ax.plot([0, 10], [0, 0], [d, d], linewidth=linewidth, color=color, zorder=zorder)
    ax.plot([d, d], [0, 10], [0, 0], linewidth=linewidth, color=color, zorder=zorder)
    ax.plot([0, 10], [d, d], [0, 0], linewidth=linewidth, color=color, zorder=zorder)
    ax.plot([d, d], [0, 0], [0, 10], linewidth=linewidth, color=color, zorder=zorder)

size, color = "small", "0.75"
for d in np.arange(1, 11):
    ax.text(d, 10.75, 0, "%d" % d, color=color, size=size, ha="center", va="center")
    ax.text(10.5, d, 0, "%d" % d, color=color, size=size, ha="center", va="center")
    ax.text(0, 10.75, d, "%d" % d, color=color, size=size, ha="center", va="center")
    ax.text(10.5, 0, d, "%d" % d, color=color, size=size, ha="center", va="center")
    ax.text(d, 0, 10.5, "%d" % d, color=color, size=size, ha="center", va="center")

    ax.text(0, d, 10.5, "%d" % d, color=color, size=size, ha="center", va="center")


plt.plot([0, 10], [0, 0], [0, 0], linewidth=1.5, color="red")
ax.text(10.5, 0, 0, "X", color="black", ha="center", va="center")

plt.plot([0, 0], [0, 10], [0, 0], linewidth=1.5, color="green")
ax.text(0, 10.5, 0, "Y", color="black", ha="center", va="center")

plt.plot([0, 0], [0, 0], [0, 10], linewidth=1.5, color="blue")
ax.text(0, 0, 10.5, "Z", color="black", ha="center", va="center")


text = ax.text(0, 0, 0, "O", color="black", size="large", ha="center", va="center")
text.set_path_effects(
    [path_effects.Stroke(linewidth=3, foreground="white"), path_effects.Normal()]
)


rect = mpatches.Rectangle((0, 0), 7, 5, facecolor="k", alpha=0.03, zorder=50)
ax.add_patch(rect)
art3d.pathpatch_2d_to_3d(rect, z=6, zdir="z")

rect = mpatches.Rectangle((0, 0), 7, 6, facecolor="k", alpha=0.06, zorder=50)
ax.add_patch(rect)
art3d.pathpatch_2d_to_3d(rect, z=5, zdir="y")

rect = mpatches.Rectangle((0, 0), 5, 6, facecolor="k", alpha=0.09, zorder=50)
ax.add_patch(rect)
art3d.pathpatch_2d_to_3d(rect, z=7, zdir="x")


class Arrow3D(mpatches.FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        mpatches.FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        return np.min(zs)

ax.add_artist(
    Arrow3D(
        [7, 0],
        [5, 5],
        [6, 6],
        mutation_scale=10,
        lw=1.5,
        arrowstyle="-|>",
        color="black",
    )
)
ax.add_artist(
    Arrow3D(
        [7, 7],
        [5, 0],
        [6, 6],
        mutation_scale=10,
        lw=1.5,
        arrowstyle="-|>",
        color="black",
    )
)
ax.add_artist(
    Arrow3D(
        [7, 7],
        [5, 5],
        [6, 0],
        mutation_scale=10,
        lw=1.5,
        arrowstyle="-|>",
        color="black",
    )
)

ax.scatter([7], [5], [6], s=50, facecolor="black", edgecolor="black", linewidth=1.5)

ax.text(
    7.5, 5, 6, "(7.0, 5.0, 6.0)", color="black", size="small", ha="left", va="center"
)

ax.plot([7, 0], [5, 0], [6, 6], color="blue", linewidth=1.5, linestyle="--", marker="o")
ax.text(0.5, 0.5, 6.5, "6", color="black", size="small", ha="left", va="bottom")

ax.plot([7, 7], [5, 0], [6, 0], color="red", linewidth=1.5, linestyle="--", marker="o")
ax.text(0, 5.5, 0, "7", color="black", size="small", ha="right", va="bottom")

ax.plot(
    [7, 0], [5, 5], [6, 0], color="green", linewidth=1.5, linestyle="--", marker="o"
)
ax.text(7.5, 0, 0, "5", color="black", size="small", ha="left", va="bottom")


plt.tight_layout()
plt.savefig("../../figures/scales-projections/projection-3d-frame.pdf")
plt.show()
