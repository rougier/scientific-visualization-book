# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(4.25, 6 * 0.55))
ax = fig.add_axes(
    [0, 0, 1, 1], xlim=[0, 11], ylim=[0.5, 6.5], frameon=False, xticks=[], yticks=[]
)
y = 6


def split(n_segment):
    width = 9
    segment_width = 0.75 * (width / n_segment)
    segment_pad = (width - n_segment * segment_width) / (n_segment - 1)
    X0 = 1 + np.arange(n_segment) * (segment_width + segment_pad)
    X1 = X0 + segment_width
    return X0, X1


# Color
# ----------------------------------------------------------------------------
X0, X1 = split(10)
for i, (x0, x1) in enumerate(zip(X0, X1)):
    ax.plot([x0, x1], [y, y], color="C%d" % i, linewidth=10, solid_capstyle="butt")
    plt.text(
        (x0 + x1) / 2,
        y - 0.2,
        '"C%d"' % i,
        size="x-small",
        ha="center",
        va="top",
        family="monospace",
    )
ax.text(X0[0] - 0.25, y + 0.2, "Line color", size="small", ha="left", va="baseline")
ax.text(
    X1[-1] + 0.25,
    y + 0.2,
    "color / c",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)

y -= 1

# Line width
# ----------------------------------------------------------------------------
X0, X1 = split(5)
LW = np.arange(1, 6)
for x0, x1, lw in zip(X0, X1, LW):
    ax.plot([x0, x1], [y, y], color="black", linewidth=lw, solid_capstyle="round")
    plt.text((x0 + x1) / 2, y - 0.2, "%d" % lw, size="x-small", ha="center", va="top")
ax.text(X0[0] - 0.25, y + 0.2, "Line width", size="small", ha="left", va="baseline")
ax.text(
    X1[-1] + 0.25,
    y + 0.2,
    "linewidth / lw",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1

# Solid capstyle
# ----------------------------------------------------------------------------
X0, X1 = split(3)
styles = "butt", "round", "projecting"
for x0, x1, style in zip(X0, X1, styles):
    ax.plot([x0, x1], [y, y], color=".85", solid_capstyle="projecting", linewidth=7)
    ax.plot([x0, x1], [y, y], color="black", solid_capstyle=style, linewidth=7)
    ax.text(
        (x0 + x1) / 2,
        y - 0.2,
        '"%s"' % style,
        size="x-small",
        ha="center",
        va="top",
        family="monospace",
    )

ax.text(X0[0] - 0.25, y + 0.2, "Cap style", size="small", ha="left", va="baseline")
ax.text(
    X1[-1] + 0.25,
    y + 0.2,
    "solid_capstyle",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1

# Dash capstyle
# ----------------------------------------------------------------------------
X0, X1 = split(3)
styles = "butt", "round", "projecting"
for x0, x1, style in zip(X0, X1, styles):
    ax.plot(
        [x0, x1],
        [y, y],
        color=".85",
        dash_capstyle="projecting",
        linewidth=7,
        linestyle="--",
    )
    ax.plot(
        [x0, x1],
        [y, y],
        color="black",
        linewidth=7,
        linestyle="--",
        dash_capstyle=style,
    )
    ax.text(
        (x0 + x1) / 2,
        y - 0.2,
        '"%s"' % style,
        size="x-small",
        ha="center",
        va="top",
        family="monospace",
    )
ax.text(X0[0] - 0.25, y + 0.2, "Dash cap style", size="small", ha="left", va="baseline")
ax.text(
    X1[-1] + 0.25,
    y + 0.2,
    "dash_capstyle",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1

# Line style
# ----------------------------------------------------------------------------
X0, X1 = split(5)
styles = "-", ":", "--", "-.", (0, (0.01, 2))

for x0, x1, style in zip(X0, X1, styles):
    ax.plot(
        [x0, x1],
        [y, y],
        color="black",
        linestyle=style,
        solid_capstyle="round",
        dash_capstyle="round",
        linewidth=3,
    )
    if isinstance(style, str):
        text = '"%s"' % style
    else:
        text = "%s" % str(style)

    ax.text(
        (x0 + x1) / 2,
        y - 0.2,
        text,
        size="x-small",
        ha="center",
        va="top",
        family="monospace",
    )
ax.text(X0[0] - 0.25, y + 0.2, "Line style", size="small", ha="left", va="baseline")
ax.text(
    X1[-1] + 0.25,
    y + 0.2,
    "linestyle / ls",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)
y -= 1


# Color
# ----------------------------------------------------------------------------
X0, X1 = split(2)
for i, (x0, x1) in enumerate(zip(X0, X1)):

    X = np.linspace(x0, x1, 500)
    Y = y + 0.1 * np.cos(5 * np.pi * (X - x0) / (x1 - x0))

    ax.plot(X, Y, color="black", linewidth=0.75, antialiased=i, rasterized=1 - i)
    plt.text(
        (x0 + x1) / 2,
        y - 0.2,
        "%s" % bool(i),
        size="x-small",
        ha="center",
        va="top",
        family="monospace",
    )

ax.text(X0[0] - 0.25, y + 0.2, "Antialias", size="small", ha="left", va="baseline")
ax.text(
    X1[-1] + 0.25,
    y + 0.2,
    "antialiased",
    color="blue",
    size="small",
    ha="right",
    va="baseline",
    family="monospace",
)

y -= 1

plt.savefig("reference-line.pdf", dpi=200)
plt.show()
