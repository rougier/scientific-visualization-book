# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvas
from scipy.ndimage import gaussian_filter

# Initialize random generator
np.random.seed(123)

# Create a figure that pyplot does not know about.
fig = Figure(figsize=(10, 10))
# attach a non-interactive Agg canvas to the figure
# (as a side-effect of the ``__init__``)
canvas = FigureCanvas(fig)
ax = fig.add_axes([0, 0, 1, 1], frameon=False)

n = 50_000
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
ax.scatter(X, Y, s=75, facecolors="C0", alpha=0.10, linewidth=0)
ax.set_xlim(-2, 2), ax.set_ylim(-2, 2)

# ax.plot([1, 2, 3])
canvas.draw()
I = np.array(canvas.renderer.buffer_rgba())[..., 0]
I = 1.0 - I / I.max()

# now display the array X as an Axes in a new figure
fig = plt.figure(figsize=(12, 4.5))

ax = plt.subplot(1, 3, 1, aspect=1)
ax.scatter(X, Y, s=10, facecolors="black", alpha=0.10, linewidth=0, rasterized=True)
ax.set_xlim(-2, 2), ax.set_ylim(-2, 2)
ax.set_xticks([]), ax.set_yticks([])
ax.set_title("Scatter plot (n=50,000)")

ax = plt.subplot(1, 3, 2)
ax.imshow(I, cmap="gray_r", extent=[-2, 2, -2, 2])
ax.set_xlim(-2, 2), ax.set_ylim(-2, 2)
ax.set_xticks([]), ax.set_yticks([])
ax.set_title("Scatter/Image plot (n=50,000)")

ax = plt.subplot(1, 3, 3)
image = ax.imshow(gaussian_filter(I, 25), cmap="gray_r", extent=[-2, 2, -2, 2])
ax.contour(
    gaussian_filter(I, 25),
    extent=[-2, 2, -2, 2],
    linestyles="--",
    linewidths=1.0,
    colors="white",
    alpha=0.5,
)
ax.set_xlim(-2, 2), ax.set_ylim(-2, 2)
ax.set_xticks([]), ax.set_yticks([])
ax.set_title("Density plot")

plt.tight_layout()
plt.savefig("../../figures/colors/alpha-scatter.pdf", dpi=600)
plt.show()
