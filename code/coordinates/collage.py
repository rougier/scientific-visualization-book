# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms


def imshow(ax, I, position=(0, 0), scale=1, angle=0, zorder=10):
    height, width = I.shape[0], I.shape[1]
    extent = scale * np.array([-width / 2, width / 2, -height / 2, height / 2])
    im = ax.imshow(I, extent=extent, zorder=zorder, cmap="cividis")
    transform = transforms.Affine2D().rotate_deg(angle).translate(*position)
    trans_data = transform + ax.transData
    im.set_transform(trans_data)
    x1, x2, y1, y2 = im.get_extent()
    ax.plot(
        [x1, x2, x2, x1, x1],
        [y1, y1, y2, y2, y1],
        "white",
        linewidth=25 * scale,
        transform=trans_data,
        zorder=zorder - 0.1,
    )
    ax.plot(
        [x1, x2, x2, x1, x1],
        [y1, y1, y2, y2, y1],
        "black",
        alpha=0.25,
        linewidth=40 * scale,
        transform=trans_data,
        zorder=zorder - 0.2,
    )


fig = plt.figure(figsize=(5, 5))
ax = fig.add_axes([0, 0, 1, 1], aspect=1, frameon=False, xlim=[0, 1000], ylim=[0, 1000])


np.random.seed(123)
I = imageio.imread("../data/mona-lisa.png")
for i in range(200):
    position = np.random.uniform(-100, 1100, 2)
    scale = np.random.uniform(0.20, 0.25)
    angle = np.random.uniform(-75, +75)
    imshow(ax, I, position, scale, angle, zorder=10 + i)

plt.savefig("../../figures/coordinates/collage.png", dpi=300)
plt.show()
