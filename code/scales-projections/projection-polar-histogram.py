# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

# Setup
fig = plt.figure(figsize=(6, 6))
ax = plt.subplot(1, 1, 1, projection="polar", frameon=True)
ax.set_thetalim(0, 2 * np.pi)
ax.set_rlim(0, 1000)
ax.set_xticks([])
ax.set_xticklabels([])
ax.set_yticks(np.linspace(100, 1000, 10))
ax.set_yticklabels([])
ax.tick_params("both", grid_alpha=0.50, grid_zorder=-10, grid_linewidth=0.5)


# Theta ticks
radius = ax.get_rmax()
length = 0.025 * radius
for i in range(360):
    angle = np.pi * i / 180
    plt.plot(
        [angle, angle],
        [radius, radius - length],
        linewidth=0.50,
        color="0.75",
        clip_on=False,
    )
for i in range(0, 360, 5):
    angle = np.pi * i / 180
    plt.plot(
        [angle, angle],
        [radius, radius - 2 * length],
        linewidth=0.75,
        color="0.75",
        clip_on=False,
    )
for i in range(0, 360, 15):
    angle = np.pi * i / 180
    plt.plot([angle, angle], [radius, 100], linewidth=0.5, color="0.75")
    plt.plot(
        [angle, angle],
        [radius + length, radius],
        zorder=500,
        linewidth=1.0,
        color="0.00",
        clip_on=False,
    )
    plt.text(
        angle,
        radius + 4 * length,
        "%d°" % i,
        zorder=500,
        rotation=i - 90,
        rotation_mode="anchor",
        va="top",
        ha="center",
        size="small",
        family="Roboto",
        color="black",
    )
for i in range(0, 360, 90):
    angle = np.pi * i / 180
    plt.plot([angle, angle], [radius, 0], zorder=500, linewidth=1.00, color="0.0")


# Radius ticks
def polar_to_cartesian(theta, radius):
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    return np.array([x, y])


def cartesian_to_polar(x, y):
    radius = np.sqrt(x ** 2 + y ** 2)
    theta = np.arctan2(y, x)
    return np.array([theta, radius])


for i in range(0, 1000, 10):
    P0 = 0, i
    P1 = cartesian_to_polar(*(polar_to_cartesian(*P0) + [0, 0.75 * length]))
    plt.plot([P0[0], P1[0]], [P0[1], P1[1]], linewidth=0.50, color="0.75")

for i in range(100, 1000, 100):
    P0 = 0, i
    P1 = cartesian_to_polar(*(polar_to_cartesian(*P0) + [0, +1.0 * length]))
    plt.plot([P0[0], P1[0]], [P0[1], P1[1]], zorder=500, linewidth=0.75, color="0.0")
    P1 = cartesian_to_polar(*(polar_to_cartesian(*P0) + [0, -1.0 * length]))
    text = ax.text(
        P1[0],
        P1[1],
        "%d" % i,
        zorder=500,
        va="top",
        ha="center",
        size="x-small",
        family="Roboto",
        color="black",
    )
    text.set_path_effects(
        [path_effects.Stroke(linewidth=2, foreground="white"), path_effects.Normal()]
    )

# Circular bands
n = 1000
T = np.linspace(0, 2 * np.pi, n)
color = "0.95"
ax.fill_between(T, 0, 100, color=color, zorder=-50)
ax.fill_between(T, 200, 300, color=color, zorder=-50)
ax.fill_between(T, 400, 500, color=color, zorder=-50)
ax.fill_between(T, 600, 700, color=color, zorder=-50)
ax.fill_between(T, 800, 900, color=color, zorder=-50)
plt.scatter([0], [0], 20, facecolor="white", edgecolor="black", zorder=1000)


# Actual plot
np.random.seed(123)
n = 145
T = 2 * np.pi / n + np.linspace(0, 2 * np.pi, n)
T[1::2] = T[0:-1:2]
R = np.random.uniform(400, 800, n)
R[-1] = R[0]
R[1:-1:2] = R[2::2]
ax.fill(T, R, color="C1", zorder=150, alpha=0.1)
ax.plot(T, R, color="white", zorder=200, linewidth=3.5)
ax.plot(T, R, color="C1", zorder=250, linewidth=1.5)


plt.tight_layout()
plt.savefig("../../figures/scales-projections/projection-polar-histogram.pdf")
plt.show()
