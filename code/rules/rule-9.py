import numpy as np

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.xkcd()

X = np.linspace(0, 2.32, 100)
Y = X * X - 5 * np.exp(-5 * (X - 2) * (X - 2))

fig = plt.figure(figsize=(12, 5), dpi=72, facecolor="white")
axes = plt.subplot(111)

plt.plot(X, Y, color="k", linewidth=2, linestyle="-", zorder=+10)

axes.set_xlim(X.min(), X.max())
axes.set_ylim(1.01 * Y.min(), 1.01 * Y.max())

axes.spines["right"].set_color("none")
axes.spines["top"].set_color("none")
axes.xaxis.set_ticks_position("bottom")
axes.spines["bottom"].set_position(("data", 0))
axes.yaxis.set_ticks_position("left")
axes.spines["left"].set_position(("data", X.min()))

axes.set_xticks([])
axes.set_yticks([])
axes.set_xlim(1.05 * X.min(), 1.10 * X.max())
axes.set_ylim(1.15 * Y.min(), 1.05 * Y.max())

t = [10, 40, 82, 88, 93, 99]
plt.scatter(X[t], Y[t], s=50, zorder=+12, c="k")

plt.text(X[t[0]] - 0.1, Y[t[0]] + 0.1, "Industrial\nRobot", ha="left", va="bottom")
plt.text(X[t[1]] - 0.15, Y[t[1]] + 0.1, "Humanoid\nRobot", ha="left", va="bottom")
plt.text(X[t[2]] - 0.25, Y[t[2]], "Zombie", ha="left", va="center")
plt.text(X[t[3]] + 0.05, Y[t[3]], "Prosthetic\nHand", ha="left", va="center")
plt.text(X[t[4]] + 0.05, Y[t[4]], "Bunraku\nPuppet", ha="left", va="center")
plt.text(X[t[5]] + 0.05, Y[t[5]], "Human", ha="left", va="center")
plt.text(X[t[2]] - 0.05, 1.5, "Uncanny\nValley", ha="center", va="center", fontsize=24)

plt.ylabel("-      Comfort Level      +", y=0.5, fontsize=20)
plt.text(0.05, -0.1, "Human Likeness ->", ha="left", va="top", color="r", fontsize=20)

X = np.linspace(0, 1.1 * 2.32, 100)
axes.fill_between(X, 0, -10, color="0.85", zorder=-1)
axes.fill_between(X, 0, +10, color=(1.0, 1.0, 0.9), zorder=-1)

# X = np.linspace(1.652,2.135,100)
X = np.linspace(1.5, 2.25, 100)
Y = X * X - 5 * np.exp(-5 * (X - 2) * (X - 2))
axes.fill_between(X, Y, +10, color=(1, 1, 1), zorder=-1)

axes.axvline(x=1.5, ymin=0, ymax=1, color=".5", ls="--")
axes.axvline(x=2.25, ymin=0, ymax=1, color=".5", ls="--")

plt.savefig("../../figures/rules/rule-9.pdf")
plt.show()
