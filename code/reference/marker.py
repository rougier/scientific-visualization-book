# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(4.25, 8 * 0.55))
ax = fig.add_axes(
    [0, 0, 1, 1], xlim=[0, 11], ylim=[0.5, 8.5], frameon=False, xticks=[], yticks=[]
)  # , aspect=1)

X = np.linspace(1, 10, 10)
Y = np.zeros(len(X))
y = 8

# Marker edge color
# ----------------------------------------------------------------------------
C = ["C%d" % i for i in range(10)]
plt.scatter(X, y + Y, s=200, facecolor="white", edgecolor=C, linewidth=1.5)
for x, c in zip(X, C):
    plt.text(
        x,
        y - 0.25,
        '"%s"' % c,
        size="x-small",
        ha="center",
        va="top",
        family="monospace",
    )
plt.text(
    X[0] - 0.25, y + 0.25, "Marker edge color", size="small", ha="left", va="baseline"
)
plt.text(
    X[-1] + 0.25,
    y + 0.25,
    "mec / ec",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1


# Marker face color
# ----------------------------------------------------------------------------
C = ["C%d" % i for i in range(10)]
plt.scatter(X, y + Y, s=200, facecolor=C, edgecolor="None")
for x, c in zip(X, C):
    plt.text(
        x,
        y - 0.25,
        '"%s"' % c,
        size="x-small",
        ha="center",
        va="top",
        family="monospace",
    )
plt.text(
    X[0] - 0.25, y + 0.25, "Marker face color", size="small", ha="left", va="baseline"
)
plt.text(
    X[-1] + 0.25,
    y + 0.25,
    "mfc / fc",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1

# Marker edge width
# ----------------------------------------------------------------------------
LW = 1 + np.arange(10) / 2
plt.scatter(X, y + Y, s=100, facecolor="white", edgecolor="black", linewidth=LW)
for x, lw in zip(X, LW):
    plt.text(
        x,
        y - 0.25,
        "%.1f" % lw,
        size="x-small",
        ha="center",
        va="top",
        family="monospace",
    )
plt.text(
    X[0] - 0.25, y + 0.25, "Marker edge width", size="small", ha="left", va="baseline"
)
plt.text(
    X[-1] + 0.25,
    y + 0.25,
    "mew / lw",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1

# Marker edge width
# ----------------------------------------------------------------------------
S = (1 + np.arange(10)) * 25
plt.scatter(X, y + Y, s=S, facecolor="black", edgecolor="None")
for x, s in zip(X, S):
    plt.text(
        x, y - 0.25, "%d" % s, size="x-small", ha="center", va="top", family="monospace"
    )
plt.text(X[0] - 0.25, y + 0.25, "Marker size", size="small", ha="left", va="baseline")
plt.text(
    X[-1] + 0.25,
    y + 0.25,
    "ms / s",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1


X = np.linspace(1, 10, 12)

# Filled markers
# -----------------------------------------------------------------------------
M = [".", "o", "s", "P", "X", "*", "p", "D", "<", ">", "^", "v"]
for x, marker in zip(X, M):
    plt.scatter(x, y, s=256, color="black", marker="s", fc=".9", ec="none")
    plt.scatter(
        x,
        y,
        s=100,
        color="black",
        marker=marker,
        fc="white",
        ec="black",
        linewidth=0.75,
    )
    plt.text(
        x,
        y - 0.25,
        '"%s"' % marker,
        size="x-small",
        ha="center",
        va="top",
        family="monospace",
    )
plt.text(
    X[0] - 0.25, y + 0.25, "Filled markers", size="small", ha="left", va="baseline"
)
plt.text(
    X[-1] + 0.25,
    y + 0.25,
    "marker",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1

# Unfilled markers
# -----------------------------------------------------------------------------
M = ["1", "2", "3", "4", "+", "x", "|", "_", 4, 5, 6, 7]
for x, marker in zip(X, M):
    if isinstance(marker, str):
        text = '"%s"' % marker
    else:
        text = "%s" % marker

    plt.scatter(x, y, s=256, color="black", marker="s", fc=".9", ec="none")
    plt.scatter(
        x, y, s=100, color="black", marker=marker, fc="none", ec="black", linewidth=0.75
    )
    plt.text(
        x, y - 0.25, text, size="x-small", ha="center", va="top", family="monospace"
    )
plt.text(
    X[0] - 0.25, y + 0.25, "Unfilled markers", size="small", ha="left", va="baseline"
)
plt.text(
    X[-1] + 0.25,
    y + 0.25,
    "marker",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1

# Unicode markers
# -----------------------------------------------------------------------------
M = ["♠", "♣", "♥", "♦", "→", "←", "↑", "↓", "◐", "◑", "◒", "◓"]
for x, marker in zip(X, M):
    ax.scatter(x, y, s=256, color="black", marker="s", fc=".9", ec="none")
    ax.scatter(
        x,
        y,
        s=100,
        color="black",
        marker="$" + marker + "$",
        fc="black",
        ec="none",
        linewidth=0.5,
    )
    ax.text(
        x,
        y - 0.25,
        '"\$%s\$"' % marker,
        size="x-small",
        ha="center",
        va="top",
        family="monospace",
    )
ax.text(
    X[0] - 0.25, y + 0.25, "Unicode markers", size="small", ha="left", va="baseline"
)
ax.text(
    X[-1] + 0.25,
    y + 0.25,
    "marker",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1

# Spacing
# -----------------------------------------------------------------------------
n_segment = 4
width = 9
segment_width = 0.75 * (width / n_segment)
segment_pad = (width - n_segment * segment_width) / (n_segment - 1)
X0 = 1 + np.arange(n_segment) * (segment_width + segment_pad)
marks = [10, [0, -1], (25, 5), [0, 25, -1]]

for x0, mark in zip(X0, marks):
    X = np.linspace(x0, x0 + segment_width, 50)
    Y = y * np.ones(len(X))
    ax.plot(
        X,
        Y,
        linewidth=1,
        color="black",
        marker=".",
        mfc="white",
        mec="black",
        mew="1",
        markevery=mark,
    )

    ax.text(
        (X[0] + X[-1]) / 2,
        y - 0.1,
        "%s" % str(mark),
        size="x-small",
        ha="center",
        va="top",
    )


ax.text(1 - 0.25, y + 0.25, "Marker spacing", size="small", ha="left", va="baseline")
ax.text(
    X[-1] + 0.25,
    y + 0.25,
    "markevery",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)


plt.savefig("reference-marker.pdf", dpi=600)
plt.show()
