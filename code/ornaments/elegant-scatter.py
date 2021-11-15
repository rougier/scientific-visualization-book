# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.size"] = 10.0
plt.rcParams["font.serif"] = ["Source Serif Pro"]
plt.rcParams["font.sans-serif"] = ["Source Sans Pro"]
plt.rcParams["font.monospace"] = ["Source Code Pro"]


fig = plt.figure(figsize=(5, 5))
ax = plt.axes()

ax.set_xlabel("Height (m)", weight="medium")
ax.set_ylabel("Weight (kg)", weight="medium")
ax.set_title(
    """Distribution of height & weight\n""" """according to sex & age (fake data)""",
    family="serif",
)

n = 250
np.random.seed(1)
X, Y = np.zeros(2 * n), np.zeros(2 * n)
S, C = np.zeros(2 * n), np.zeros(2 * n)

X[:n] = np.random.normal(1.60, 0.1, n)
Y[:n] = np.random.normal(50, 10, n)
S[:n] = np.random.uniform(25, 50, n)
C[:n] = 0

X[n:] = np.random.normal(1.75, 0.1, n)
Y[n:] = np.random.normal(75, 10, n)
S[n:] = np.random.uniform(25, 50, n)
C[n:] = 1

cmap = plt.get_cmap("RdYlBu")
scatter = plt.scatter(X, Y, s=S, edgecolor="black", linewidth=0.75, zorder=-20)
scatter = plt.scatter(X, Y, s=S, edgecolor="None", facecolor="white", zorder=-10)
scatter = plt.scatter(X, Y, c=C, s=S, cmap=cmap, edgecolor="None", alpha=0.25)

handles, labels = scatter.legend_elements(
    num=3,
    prop="sizes",
    alpha=1,
    markeredgewidth=0.5,
    markeredgecolor="black",
    markerfacecolor="None",
)
legend = plt.legend(
    handles,
    labels,
    title=" Age",
    loc=(0.6, 0.05),
    handletextpad=0.1,
    labelspacing=0.25,
    facecolor="None",
    edgecolor="None",
)
legend.get_children()[0].align = "left"
legend.get_title().set_fontweight("medium")
ax.add_artist(legend)

handles, labels = scatter.legend_elements(markeredgewidth=0.0, markeredgecolor="black")
labels = ["Female", "Male"]
legend = plt.legend(
    handles,
    labels,
    title=" Sex",
    loc=(0.75, 0.05),
    handletextpad=0.1,
    labelspacing=0.25,
    facecolor="None",
    edgecolor="None",
)
legend.get_children()[0].align = "left"
legend.get_title().set_fontweight("medium")


plt.scatter(X, [19] * len(X), marker="|", color=cmap(C), linewidth=0.5, alpha=0.25)
plt.scatter([1.3] * len(X), Y, marker="_", color=cmap(C), linewidth=0.5, alpha=0.25)

plt.savefig("../../figures/ornaments/elegant-scatter.pdf")
plt.show()
