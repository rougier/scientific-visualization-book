# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import imageio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

I = imageio.imread("../data/mona-lisa.png")
height, width = np.array(I.shape)

cmap = plt.get_cmap("cividis")
fig = plt.figure(figsize=(width / 150, height / 150))
ax = fig.add_axes(
    [0, 0, 1, 1],
    aspect=1,
    frameon=False,
    xlim=[0, width],
    xticks=[],
    ylim=[0, height],
    yticks=[],
)

box = FancyBboxPatch(
    (0, 0),
    width,
    height,
    zorder=40,
    boxstyle="roundtooth,tooth_size=24",
    lw=8,
    ec="white",
    fc="None",
)
ax.add_patch(box)
box = FancyBboxPatch(
    (0, 0),
    width,
    height,
    zorder=50,
    boxstyle="roundtooth,tooth_size=24",
    lw=3,
    ec="black",
    fc="None",
)
ax.add_patch(box)

im = ax.imshow(I, extent=[0, width, 0, height], zorder=30, cmap=cmap)
im.set_clip_path(box)

plt.savefig("../../figures/beyond/stamp.png", dpi=300)
plt.show()
