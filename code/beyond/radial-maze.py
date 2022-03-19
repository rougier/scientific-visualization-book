# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import os
import numpy as np
import matplotlib.path as path
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection

# Maze parameters
n_arms = 8
n_squares = 5
square_width = 1.5
square_height = 1.5
inner_radius = 3
outer_radius = inner_radius + n_squares * square_height
delta = 0.1  # cosmetic to widen a bit maze arms

W, C = [], []
for i in range(n_arms):
    theta = i / n_arms * 2 * np.pi

    # Build external walls
    N = (square_width / 2 + delta) * np.array([np.sin(theta), -np.cos(theta)])
    V_in = inner_radius * np.array([np.cos(theta), np.sin(theta)])
    V_out = (outer_radius + delta) * np.array([np.cos(theta), np.sin(theta)])
    W.extend([V_in + N, V_out + N, V_out - N, V_in - N])

    # Build arm start (pie)
    t0 = theta - 0.5 / n_arms * 2 * np.pi
    t1 = theta + 0.5 / n_arms * 2 * np.pi
    V = []
    for t in np.linspace(t0, t1, 25):
        V.append(1.00 * inner_radius * np.array([np.cos(t), np.sin(t)]))
    for t in np.linspace(t1, t0, 25):
        V.append(0.25 * inner_radius * np.array([np.cos(t), np.sin(t)]))
    V.append(V[-1])
    C.append(V)

    # Build arms squares
    N = square_width / 2 * np.array([np.sin(theta), -np.cos(theta)])
    T = square_height / 2 * np.array([np.cos(theta), np.sin(theta)])
    for j in range(n_squares):
        r = inner_radius + (j + 0.5) / n_squares * (outer_radius - inner_radius)
        V = r * np.array([np.cos(theta), np.sin(theta)])
        C.append([V - T + N, V + T + N, V + T - N, V - T - N])

W.append(W[0])
W = np.array(W)


class PathTracer:
    """ Path tracer on a figure

    You can trace a path using your mouse:
      1. Click to start
      2. Move th mouse
      3. Click to stop and save (if save=True)
    """

    def __init__(self, line=None, load=True, save=True, filename="path.npy"):
        self.line = line
        self.save = save
        self.filename = filename
        self.xs = []
        self.ys = []
        self.active = False
        if load and os.path.exists(self.filename):
            P = np.load(self.filename)
            self.xs = P[:, 0].tolist()
            self.ys = P[:, 1].tolist()
            self.line.set_data(self.xs, self.ys)
            self.line.figure.canvas.draw()
        line.figure.canvas.mpl_connect("button_press_event", self.on_press)
        line.figure.canvas.mpl_connect("motion_notify_event", self.on_motion)

    def on_press(self, event):
        if event.inaxes != self.line.axes:
            return
        if not self.active:
            self.active = True
            self.xs = [event.xdata]
            self.ys = [event.ydata]
        else:
            self.active = False
            if self.save:
                P = np.c_[self.xs, self.ys]
                np.save(self.filename, P)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()

    def on_motion(self, event):
        if event.inaxes != self.line.axes or not self.active:
            return
        x, y = event.xdata, event.ydata
        d = np.sqrt((x - self.xs[-1]) ** 2 + (y - self.ys[-1]) ** 2)
        if d < 0.1:
            return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()


# The maze-path as been drawn by hand using the path tracer above
# Here we count the number of path points contained in each part
# of the same such as to set the color using a colormap
P = np.load("radial-maze-path.npy")
N = np.zeros(len(C))
for i, vertices in enumerate(C):
    codes = [path.Path.MOVETO] + [path.Path.LINETO,] * (len(vertices) - 1)
    p = path.Path(vertices, codes)
    N[i] = p.contains_points(P).sum()
N = 1 - (N - N.min()) / (N.max() - N.min())
cmap = plt.cm.get_cmap("viridis")
colors = cmap(N)

# Alternatively, you can also set colors on each arm
# colors = [] # this will be a list of n_arms * n_squares colors
# for arm in range(n_arms):
#     for square in range(n_squares+1):
#         if arm < 6:
#             color = cmap(square/n_squares)
#         else:
#             color = 0.00, 0.0, 0.00, 0.05
#         colors.append(color)

# -------------------------------------------------------
fig = plt.figure(figsize=(8, 8))
ax = plt.subplot(1, 1, 1, aspect=1, frameon=False, xticks=[], yticks=[])

# Borders
plt.plot(W[:, 0], W[:, 1], color="black", linewidth=2, zorder=10)

# Squares
collection = PolyCollection(
    C, closed=True, linewidth=2, facecolors=colors, edgecolors="white"
)
ax.add_collection(collection)

# Letters
for i in range(n_arms):
    theta = i / n_arms * 2 * np.pi
    x = (outer_radius + 1) * np.cos(theta)
    y = (outer_radius + 1) * np.sin(theta)
    ax.text(
        x,
        y,
        chr(ord("A") + i),
        weight="bold",
        rotation=i / n_arms * 360 - 90,
        va="center",
        ha="center",
        size="xx-large",
    )

# Path tracker click to start and end (clear previous path)
(line,) = ax.plot([], [], linestyle="-", color="black", linewidth=1.0, alpha=0.75)
tracer = PathTracer(line, save=False, filename="radial-maze-path.npy")

plt.tight_layout()
plt.savefig("../../figures/beyond/radial-maze.pdf")
plt.show()
