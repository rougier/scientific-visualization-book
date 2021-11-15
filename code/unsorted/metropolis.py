# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import tqdm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from scipy.ndimage import gaussian_filter
from matplotlib.collections import LineCollection
from matplotlib.backends.backend_agg import FigureCanvas


# Nothing complicated here.
# Directly translated from https://github.com/marcusvolz/metropolis
# See also https://github.com/marcusvolz
#
# Don't use n > 11000 or you'll be stuck forever...
def metropolis(width=10000, height=10000, n=11000, step=75, branching=0.1, noise=2.0):
    delta = noise * np.pi / 180
    points = np.zeros(
        n, dtype=[("x", float), ("y", float), ("dir", float), ("level", int)]
    )
    edges = np.zeros(
        n,
        dtype=[
            ("x0", float),
            ("y0", float),
            ("x1", float),
            ("y1", float),
            ("level", int),
        ],
    )
    points[0] = width / 2, height / 2, np.random.uniform(-2 * np.pi, 2 * np.pi), 1

    for i in tqdm.trange(1, n):
        while True:
            point = np.random.choice(points[:i])
            branch = 1 if np.random.uniform(0, 1) <= branching else 0
            alpha = point["dir"] + delta * np.random.uniform(-1, +1)
            alpha += branch * np.random.choice([-np.pi / 2, +np.pi / 2])
            v = np.array((np.cos(alpha), np.sin(alpha)))
            v = v * step * (1 + 1 / (point["level"] + branch))
            x = point["x"] + v[0]
            y = point["y"] + v[1]
            level = point["level"] + branch
            if x < 0 or x > width or y < 0 or y > height:
                continue
            dist = np.sqrt((points["x"] - x) ** 2 + (points["y"] - y) ** 2)
            if dist.min() >= step:
                points[i] = x, y, alpha, level
                edges[i] = x, y, point["x"], point["y"], level
                break
    return edges[edges["level"] > 0]


np.random.seed(12345)
width, height, border = 10000, 10000, 500
if 1:  # Set to 0 after computation
    edges = metropolis(width, height)
    np.save("egdes.npy", edges)
else:
    edges = np.load("egdes.npy")


segments = []
for edge in edges:
    x0, y0, x1, y1, level = edge
    segments.append([(x0, y0), (x1, y1)])

# Drop shadow pre-processing
# We render into an array and we apply Gaussian blur
fig = Figure(figsize=(6, 6))
canvas = FigureCanvas(fig)
ax = fig.add_axes(
    [0, 0, 1, 1],
    aspect=1,
    frameon=False,
    xticks=[],
    yticks=[],
    xlim=[0, width],
    ylim=[0, height],
)
sigma = 2.0
collection = LineCollection(segments, linewidths=1.5, colors="black", capstyle="round")
ax.add_collection(collection)
canvas.draw()
I = np.array(canvas.renderer.buffer_rgba())[..., :3]
I[:, :, 0] = gaussian_filter(I[:, :, 0], sigma=sigma)
I[:, :, 1] = gaussian_filter(I[:, :, 1], sigma=sigma)
I[:, :, 2] = gaussian_filter(I[:, :, 2], sigma=sigma)


# Actual rendering
fig = plt.figure(figsize=(6, 6))
ax = fig.add_axes(
    [0, 0, 1, 1],
    aspect=1,
    frameon=False,
    xticks=[],
    xlim=[border, width - border],
    yticks=[],
    ylim=[border, height - border],
)
ax.imshow(I, extent=[0, width, 0, height], alpha=0.5)
collection = LineCollection(segments, linewidths=1.0, colors="black", capstyle="round")
ax.add_collection(collection)
plt.savefig("metropolis.pdf", dpi=600)
plt.show()
