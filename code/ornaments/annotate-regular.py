# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6, 4))
ax = plt.subplot(
    1,
    1,
    1,
    xlim=[-1, +1],
    xticks=[-1, 0, 1],
    ylim=[-1, +1],
    yticks=[-1, 0, 1],
    aspect=1,
)

np.random.seed(123)
X = np.random.normal(0, 0.35, 1000)
Y = np.random.normal(0, 0.35, 1000)

ax.scatter(X, Y, edgecolor="None", facecolor="C1", alpha=0.5)


I = np.random.choice(len(X), size=8, replace=False)
Px, Py = X[I], Y[I]
I = np.argsort(Y[I])[::-1]
Px, Py = Px[I], Py[I]

ax.scatter(Px, Py, edgecolor="black", facecolor="white", zorder=20)
ax.scatter(Px, Py, edgecolor="None", facecolor="C1", alpha=0.5, zorder=30)

y, dy = 1.0, 0.125
style = "arc,angleA=-0,angleB=0,armA=-100,armB=0,rad=0"

for i in range(len(I)):
    ax.annotate(
        "Point " + chr(ord("A") + i),
        xy=(Px[i], Py[i]),
        xycoords="data",
        xytext=(1.25, y - i * dy),
        textcoords="data",
        arrowprops=dict(
            arrowstyle="->",
            color="black",
            linewidth=0.75,
            shrinkA=25,
            shrinkB=5,
            patchA=None,
            patchB=None,
            connectionstyle=style,
        ),
    )

ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["left"].set_position(("data", -1.1))
ax.spines["bottom"].set_position(("data", -1.1))

# plt.tight_layout()
plt.savefig("../../figures/ornaments/legend-regular.pdf")
plt.show()
