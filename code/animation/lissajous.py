# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure(figsize=(8, 4), dpi=100)

frames = 500
n = 8

X, Y, L = [], [], []
for row in range(n // 2):
    T2 = np.linspace(0, row * 2 * np.pi, frames) if row > 0 else np.zeros(frames)

    for col in range(n):
        T1 = np.linspace(0, col * 2 * np.pi, frames) if col > 0 else np.ones(frames)

        index = n * row + col

        ax = plt.subplot(n // 2, n, 1 + index, aspect=1, frameon=False)
        ax.set_xlim([-1, +1])
        ax.set_xticks([])
        ax.set_ylim([-1, +1])
        ax.set_yticks([])

        X.append(np.cos(T1))
        Y.append(np.sin(T2))

        ax.plot(X[-1], Y[-1], color="0.95", clip_on=False, linewidth=0.75)
        (l,) = ax.plot(
            [],
            [],
            "-o",
            clip_on=False,
            markevery=[-1],
            markeredgewidth=2,
            markerfacecolor="C0",
            markeredgecolor="white",
        )
        L.append(l)


plt.subplots_adjust(left=0.0, bottom=None, right=0.95, top=None)


def animate(frame):
    for i in range(len(L)):
        L[i].set_data(X[i][:frame], Y[i][:frame])
    if frame == 150:
        plt.savefig("../../figures/animation/lissajous.pdf")


ani = animation.FuncAnimation(fig, animate, interval=5, frames=frames)
plt.show()
