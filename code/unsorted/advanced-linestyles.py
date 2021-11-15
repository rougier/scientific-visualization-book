import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(4.25, 6))
ax = plt.subplot(111, aspect=1, frameon=False, xticks=[], yticks=[])

X = np.linspace(0, 2 * np.pi, 100)
Y = 0.5 * np.sin(X)
yticks, ylabels = [], []


# 1
# -----------------------------------------------------------------------------
y = 1
yticks.append(y), ylabels.append("%d" % y)
ax.plot(X, y + Y, "black", linewidth=1)
ax.plot(
    X,
    y + Y,
    "black",
    linewidth=10,
    solid_capstyle="butt",
    dash_capstyle="butt",
    linestyle=(0.0, (0.1, 1.0)),
)

# 2
# -----------------------------------------------------------------------------
y += 1
yticks.append(y), ylabels.append("%d" % y)
ax.plot(
    X,
    y + Y,
    ".25",
    linewidth=5,
    solid_capstyle="butt",
    dash_capstyle="butt",
    linestyle=(0.0, (0.1, 0.45)),
)
ax.plot(X, y + Y, "black", linewidth=1)
ax.plot(
    X,
    y + Y,
    "black",
    linewidth=10,
    solid_capstyle="butt",
    dash_capstyle="butt",
    linestyle=(0.0, (0.1, 1.0)),
)

# 3
# -----------------------------------------------------------------------------
y += 1
yticks.append(y), ylabels.append("%d" % y)
ax.plot(X, y + Y, "black", linewidth=8, solid_capstyle="round")
ax.plot(X, y + Y, "white", linewidth=6, solid_capstyle="round")
ax.plot(X, y + Y, "black", linewidth=1, solid_capstyle="round")

# 4
# -----------------------------------------------------------------------------
y += 1
yticks.append(y), ylabels.append("%d" % y)
ax.plot(
    X,
    y + Y,
    "black",
    linewidth=8,
    solid_capstyle="round",
    dash_capstyle="round",
    linestyle=(0.0, (0.01, 1.5)),
)

# 5
# -----------------------------------------------------------------------------
y += 1
yticks.append(y), ylabels.append("%d" % y)
ax.plot(
    X, y + Y, "black", linewidth=1.5, marker="o", markevery=10, mec="black", mfc="white"
)

# 6
# -----------------------------------------------------------------------------
y += 1
yticks.append(y), ylabels.append("%d" % y)
ax.plot(
    X, y + Y, "black", linewidth=1.5, marker="o", markevery=10, mec="white", mfc="black"
)

# 7
# -----------------------------------------------------------------------------
y += 1
yticks.append(y), ylabels.append("%d" % y)
ax.plot(
    X,
    y + Y,
    "black",
    linewidth=1.5,
    markersize=10,
    mew=2.5,
    mec="white",
    mfc="white",
    marker="$↑$",
    markevery=10,
)
ax.plot(
    X,
    y + Y,
    "black",
    linewidth=0.0,
    markersize=10,
    mew=0.5,
    mec="black",
    mfc="black",
    marker="$↑$",
    markevery=10,
)

# 8
# -----------------------------------------------------------------------------
y += 1
yticks.append(y), ylabels.append("%d" % y)
for i in range(9):
    ax.plot(
        X,
        y + Y,
        "%.2f" % (i / 10),
        linewidth=4,
        solid_capstyle="round",
        dash_capstyle="round",
        linestyle=(i + 1, (0.01, 9.0)),
    )

# 9
# -----------------------------------------------------------------------------
y += 1
yticks.append(y), ylabels.append("%d" % y)
Y = Y.mean() + 0 * Y
ax.plot(
    X,
    y + Y,
    marker=(3, 0, -90),
    mew=2.5,
    mec="black",
    mfc="black",
    markersize=7,
    linestyle="None",
    markevery=2,
)
ax.plot(
    X,
    y + Y,
    marker=(3, 0, -90),
    mew=1,
    mec="white",
    mfc="white",
    markersize=7,
    linestyle="None",
    markevery=2,
)

# 10
# -----------------------------------------------------------------------------
y += 0.5
yticks.append(y), ylabels.append("%d" % (y + 0.5))
ax.plot(
    X,
    y + Y,
    "black",
    linewidth=6,
    solid_capstyle="butt",
    ms=10,
    mew=1.5,
    mec="white",
    mfc="None",
    marker=5,
    markevery=(5, 10),
)

# 11
# -----------------------------------------------------------------------------
y += 0.5
yticks.append(y), ylabels.append("%d" % (y + 1))
ax.plot(
    X,
    y + Y,
    "black",
    linewidth=1,
    linestyle="--",
    marker="$✁$",
    markevery=(10, 1000),
    ms=20,
    mew=0.75,
    mec="black",
    mfc="white",
)

ax.set_yticks(yticks)
ax.set_yticklabels(ylabels)
ax.tick_params(axis="both", which="both", length=0)

plt.tight_layout()
plt.savefig("advanced-linestyles.pdf")
plt.show()
