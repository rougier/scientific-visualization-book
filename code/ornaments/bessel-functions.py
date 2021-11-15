# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
from scipy.special import jn, jn_zeros
import matplotlib.pyplot as plt

plt.rc("font", family="Roboto Condensed")
plt.rc("xtick", labelsize="small")
plt.rc("ytick", labelsize="small")

fig = plt.figure(figsize=(6, 3), dpi=100)
ax = plt.subplot(xlim=[0, 20], ylim=[-0.5, 1])

X = np.linspace(0, 20, 1000, endpoint=True)
n = 6
for i in range(n):
    Ji = jn(i, X)
    linewidth = 1.5 if i == 0 else 1
    linestyle = "-" if i == 0 else "-"
    color = "C1" if i == 0 else "%.2f" % (i / n)
    label = r"$J_%d$" % i

    ax.plot(X, Ji, color="white", clip_on=False, zorder=10 - i, linewidth=2.5)

    ax.plot(
        X,
        Ji,
        color=color,
        clip_on=False,
        zorder=10 - i,
        linewidth=linewidth,
        linestyle=linestyle,
        label=label,
    )

    k = np.argmax(Ji)
    ax.text(
        X[k],
        Ji[k] + 0.05,
        label,
        color=color,
        usetex=True,
        ha="center",
        va="bottom",
        size="small",
    )
    #    k = np.argmin(Ji)
    #    ax.text(X[k], Ji[k]-0.05, label, color=color,
    #            ha="center", va="top", size="small")

    Zx = [x for x in jn_zeros(i, 6) if x < 20]
    Zy = np.zeros(len(Zx))
    ax.scatter(Zx, Zy, s=15, zorder=20, edgecolor=color, facecolor="white", linewidth=1)

    if i == 0:
        ax.annotate(
            "Root",
            (Zx[0], Zy[0]),
            size="small",
            xytext=(-30, -30),
            textcoords="offset points",
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.3"),
        )

    Zy = -0.6 * np.ones(len(Zx))
    ax.scatter(
        Zx,
        Zy,
        s=30,
        zorder=20,
        clip_on=False,
        marker="|",
        facecolor="black",
        linewidth=0.5,
    )

ax.set_title(
    "Bessel functions",
    x=1,
    weight="light",
    family="Roboto Condensed",
    transform=ax.transAxes,
    ha="right",
)
ax.text(
    1,
    0.98,
    r"$J_n(x) = \frac{1}{2\pi} \int_{-\pi}^\pi e^{i(x \sin \tau -n \tau)} \,d\tau$",
    va="top",
    transform=ax.transAxes,
    size=12,
    ha="right",
    usetex=True,
)

ax.set_yticks([-0.5, 0, 0.5, 1])
ax.set_xticks([0, 10, 20])
ax.axhline(0, color="0.5", linewidth=0.5)

ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["left"].set_position(("data", -1))
ax.spines["bottom"].set_position(("data", -0.6))

plt.tight_layout()
plt.savefig("../../figures/ornaments/bessel-functions.pdf")
plt.show()
