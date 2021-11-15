# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
# Illustrate multisample on data or screen space (using imshow)
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

plt.rc("font", family="Roboto")

fig = plt.figure(figsize=(2 * 4.25, 2 * 2.5 * 4.25 / 4), dpi=100)

xmin, xmax = 0 * np.pi, 5 * np.pi
ymin, ymax = -1.1, +1.1


def f(x):
    return np.sin(np.power(x, 3)) * np.sin(x)


# --- X linear space ----------------------------------------------------------
ax = plt.subplot(
    311,
    xticks=[],
    yticks=[],
    aspect=1,
    frameon=False,
    xlim=[xmin, xmax],
    ylim=[ymin, ymax],
)

X = np.linspace(xmin, xmax, 10000)
Y = f(X)
plt.plot(X, Y, linewidth=0.5, alpha=0.25, color="black")
ax.set_title("Line plot", ha="left", loc="left")

# --- X linear space ----------------------------------------------------------
ax = plt.subplot(
    312,
    xticks=[],
    yticks=[],
    aspect=1,
    frameon=False,
    xlim=[xmin, xmax],
    ylim=[ymin, ymax],
)

X = np.linspace(xmin, xmax, 10000)
Y = f(X)

segments = np.zeros((len(X) - 1, 2, 2))
segments[:, 0, 0], segments[:, 0, 1] = X[:-1], Y[:-1]
segments[:, 1, 0], segments[:, 1, 1] = X[1:], Y[1:]

ax.add_collection(LineCollection(segments, linewidths=0.5, alpha=0.25, colors="black"))
ax.set_title("Line collection", ha="left", loc="left")


# --- Multisample (screen space) ----------------------------------------------
n_samples = 8
ax = plt.subplot(
    313,
    xticks=[],
    yticks=[],
    aspect=1,
    frameon=False,
    xlim=[xmin, xmax],
    ylim=[ymin, ymax],
)
x0, y0 = ax.transAxes.transform((0, 0)).astype(int)
x1, y1 = ax.transAxes.transform((1, 1)).astype(int)
rows, cols = y1 - y0, x1 - x0
shape = n_samples * rows, n_samples * cols
Z = np.zeros(shape)

I, J = np.meshgrid(np.arange(shape[1]), np.arange(shape[0]))
# N = np.random.uniform(-0.5,0.5,I.shape)
N = np.random.normal(0, 0.5, I.shape)
X = xmin + ((I + N) / (shape[1] - 1)) * (xmax - xmin)
Y = np.floor(((f(X) - ymin) / (ymax - ymin)) * shape[0]).astype(int)
Z[Y, I] = np.minimum(np.abs(Y - J), 1)
ax.imshow(
    Z,
    extent=[xmin, xmax, ymin, ymax],
    origin="lower",
    cmap="gray_r",
    interpolation="lanczos",
    vmin=0,
    vmax=1.5,
)
ax.set_title("Multisample (imshow)", ha="left", loc="left")


plt.tight_layout()
plt.savefig("../../figures/optimization/multisample.png", dpi=600)
plt.show()


# # --- Multisample (data space) ------------------------------------------------
# ax = plt.subplot(412, xticks=[], yticks=[], aspect=1,
#                  xlim=[xmin, xmax], ylim=[ymin, ymax])

# x0, y0 = ax.transAxes.transform((0,0)).astype(int)
# x1, y1 = ax.transAxes.transform((1,1)).astype(int)
# rows, cols = y1-y0, x1-x0

# X = np.linspace(0, cols-1, n_samples*n_samples*cols) #1000)
# #X += np.random.normal(0,.5)
# X = xmin + (X/(cols-1))*(xmax-xmin)
# Y = f(X)


# #dx = (xmax-xmin)/((x1-x0) * n_samples * n_samples)
# #for i in range(n_samples*n_samples):
# #    X = np.linspace(xmin,xmax,1000)
# #    Y = f(X+dx*i/n_samples)
# plt.plot(X,Y, linewidth=0.1, alpha=1.0, color="black")
# ax.set_title("Multisample (data space)")


# # --- X log space -------------------------------------------------------------
# ax = plt.subplot(413, xticks=[], yticks=[], aspect=1,
#                  xlim=[xmin, xmax], ylim=[ymin, ymax])

# X = 1 - np.logspace(0,3,10000,endpoint=True)/1000
# X = xmin + X*(xmax-xmin)
# Y = f(X)
# plt.plot(X,Y, linewidth=0.25, alpha=0.5, color="black")
# plt.plot(X,Y, linewidth=0.25, alpha=0.5, color="black")
# ax.set_title("X log space")
