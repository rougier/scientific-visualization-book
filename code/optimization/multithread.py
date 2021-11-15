# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvas

X = np.random.normal(4.5, 2, 5_000_000)
Y = np.random.normal(4.5, 2, 5_000_000)


def plot(extent):
    """ Offline rendering """

    xmin, xmax, ymin, ymax = extent
    fig = Figure(figsize=(2, 2))
    canvas = FigureCanvas(fig)
    ax = fig.add_axes(
        [0, 0, 1, 1],
        frameon=False,
        xlim=[xmin, xmax],
        xticks=[],
        ylim=[ymin, ymax],
        yticks=[],
    )
    epsilon = 0.1
    I = np.argwhere(
        (X >= (xmin - epsilon))
        & (X <= (xmax + epsilon))
        & (Y >= (ymin - epsilon))
        & (Y <= (ymax + epsilon))
    )
    ax.scatter(
        X[I], Y[I], 3, clip_on=False, color="black", edgecolor="None", alpha=0.0025
    )
    canvas.draw()
    return np.array(canvas.renderer.buffer_rgba())


if __name__ == "__main__":
    from multiprocessing import Pool

    extents = [[x, x + 3, y, y + 3] for x in range(0, 9, 3) for y in range(0, 9, 3)]
    pool = Pool()
    images = pool.map(plot, extents)
    pool.close()

    fig = plt.figure(figsize=(6, 6))
    ax = plt.subplot(xlim=[0, 9], ylim=[0, 9])
    for img, extent in zip(images, extents):
        ax.imshow(img, extent=extent, interpolation="None")

    plt.savefig("../../figures/optimization/multithread.png", dpi=600)
    plt.show()
