# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


def plot(ax):
    ax.set_xlim([-np.pi, np.pi])
    ax.set_xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
    ax.set_xticklabels(["-π", "-π/2", "0", "+π/2", "+π"])
    ax.set_ylim([-1, 1])
    ax.set_yticks([-1, 0, 1])
    ax.set_yticklabels(["-1", "0", "+1"])

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_position(("data", -3.25))
    ax.spines["bottom"].set_position(("data", -1.25))

    (plot1,) = ax.plot(X, C, label="cosine", clip_on=False)
    (plot2,) = ax.plot(X, S, label="sine", clip_on=False)

    return plot1, plot2


n = 4
fig = plt.figure(figsize=(6, n * 1.9))

X = np.linspace(-np.pi, np.pi, 400, endpoint=True)
C, S = np.cos(X), np.sin(X)

ax = plt.subplot(n, 1, 1)
plot1, plot2 = plot(ax)
ax.text(
    X[-1],
    C[-1],
    " — " + plot1.get_label(),
    size="small",
    color=plot1.get_color(),
    ha="left",
    va="center",
)
ax.text(
    X[-1],
    S[-1],
    " — " + plot2.get_label(),
    size="small",
    color=plot2.get_color(),
    ha="left",
    va="center",
)

ax = plt.subplot(n, 1, 2)
plot1, plot2 = plot(ax)
ax.text(
    X[100],
    C[100],
    " " + plot1.get_label(),
    family="Roboto Condensed",
    size="small",
    bbox=dict(facecolor="white", edgecolor="None", alpha=0.85),
    color=plot1.get_color(),
    ha="center",
    va="center",
    rotation=42.5,
)
ax.text(
    X[200],
    S[200],
    " " + plot2.get_label(),
    rotation=42.5,
    family="Roboto Condensed",
    size="small",
    bbox=dict(facecolor="white", edgecolor="None", alpha=0.85),
    color=plot2.get_color(),
    ha="center",
    va="center",
)

ax = plt.subplot(n, 1, 3)
plot1, plot2 = plot(ax)

ax.annotate(
    "cosine",
    (X[100], C[100]),
    size="small",
    color=plot1.get_color(),
    xytext=(-50, +10),
    textcoords="offset points",
    arrowprops=dict(
        arrowstyle="->", color=plot1.get_color(), connectionstyle="arc3,rad=-0.3"
    ),
)
ax.annotate(
    "sine",
    (X[200], S[200]),
    size="small",
    color=plot2.get_color(),
    xytext=(-50, +10),
    textcoords="offset points",
    arrowprops=dict(
        arrowstyle="->", color=plot2.get_color(), connectionstyle="arc3,rad=-0.3"
    ),
)

ax = plt.subplot(n, 1, 4)
plot1, plot2 = plot(ax)
index = 10
ax.scatter(
    [X[index]],
    [C[index]],
    s=100,
    marker="o",
    zorder=10,
    clip_on=False,
    linewidth=1,
    edgecolor=plot1.get_color(),
    facecolor="white",
)
ax.text(
    X[index],
    1.01 * C[index],
    "A",
    zorder=20,
    color=plot1.get_color(),
    ha="center",
    va="center",
    size="x-small",
    clip_on=False,
)

ax.scatter(
    [X[index]],
    [S[index]],
    s=100,
    marker="o",
    zorder=10,
    clip_on=False,
    linewidth=1,
    edgecolor=plot2.get_color(),
    facecolor="white",
)
ax.text(
    X[index],
    1.05 * S[index],
    "B",
    zorder=20,
    color=plot2.get_color(),
    ha="center",
    va="center",
    size="x-small",
    clip_on=False,
)


plt.tight_layout()
plt.savefig("../../figures/ornaments/legend-alternatives.pdf")
plt.show()
