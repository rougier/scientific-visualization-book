# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
# Illustrate polygon and clipping
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches


def circle(center, radius):
    """ Regular circle path """

    T = np.arange(0, np.pi * 2.0, 0.01)
    T = T.reshape(-1, 1)
    X = center[0] + radius * np.cos(T)
    Y = center[1] + radius * np.sin(T)
    vertices = np.hstack((X, Y))
    codes = np.ones(len(vertices), dtype=mpath.Path.code_type) * mpath.Path.LINETO
    codes[0] = mpath.Path.MOVETO
    return vertices, codes


def rectangle(center, size):
    """ Regular rectangle path """

    (x, y), (w, h) = center, size
    vertices = np.array([(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)])
    codes = np.array(
        [
            mpath.Path.MOVETO,
            mpath.Path.LINETO,
            mpath.Path.LINETO,
            mpath.Path.LINETO,
            mpath.Path.LINETO,
        ]
    )
    return vertices, codes


def patch(
    ax, path, facecolor="0.9", edgecolor="black", linewidth=1, linestyle="-", clip=None
):
    """ Build a patch with potential clipping path """
    patch = mpatches.PathPatch(
        path,
        linewidth=linewidth,
        linestyle=linestyle,
        facecolor=facecolor,
        edgecolor=edgecolor,
    )
    if clip:
        # If the path is not drawn, clipping doesn't work
        clip_patch = mpatches.PathPatch(
            clip, linewidth=0, facecolor="None", edgecolor="None"
        )
        ax.add_patch(clip_patch)
        patch.set_clip_path(clip_patch)
    ax.add_patch(patch)


def subplot(cols, rows, index, title):
    """ Shortcut to subplot to factorize options"""
    ax = plt.subplot(cols, rows, index, aspect=1)
    ax.text(-1.25, 0.75, "A", size="large", ha="center", va="center")
    ax.text(+1.25, 0.75, "B", size="large", ha="center", va="center")
    ax.set_title(title, weight="bold")
    ax.set_xlim(-1.5, +1.5), ax.set_xticks([])
    ax.set_ylim(-1, +1), ax.set_yticks([])
    return ax


V1, C1 = rectangle((-1.5, -1), size=(3, 2))
V2, C2 = circle((-0.5, 0), radius=0.75)
# For A, we use clock-wise circle vertices
A = mpath.Path(V2, C2)
# For ¬A, we use counter clock-wise circle vertices
A_ = mpath.Path(np.concatenate([V2[::-1], V1]), np.concatenate([C2, C1]))

V2, C2 = circle((+0.5, 0), radius=0.75)
# For B, we use clock-wise circle vertices
B = mpath.Path(V2, C2)
# For ¬B, we use counter clock-wise circle vertices
B_ = mpath.Path(np.concatenate([V2[::-1], V1]), np.concatenate([C2, C1]))


fig = plt.figure(figsize=(9, 5))
rows, cols = 3, 4

# A
ax = subplot(rows, cols, 1, "A")
patch(ax, A, edgecolor="None")
patch(ax, A, facecolor="None", linestyle="-", linewidth=1.5)
patch(ax, B, facecolor="None", linestyle="--", linewidth=1)

# B
ax = subplot(rows, cols, 2, "B")
patch(ax, B, edgecolor="None")
patch(ax, A, facecolor="None", linestyle="--", linewidth=1)
patch(ax, B, facecolor="None", linestyle="-", linewidth=1.4)

# ¬A
ax = subplot(rows, cols, 3, "¬A")
patch(ax, A_, edgecolor="None")
patch(ax, A, facecolor="None", linestyle="-", linewidth=1.5)
patch(ax, B, facecolor="None", linestyle="--", linewidth=1)
plt.setp(ax.spines.values(), linewidth=1.5)

# ¬B
ax = subplot(rows, cols, 4, "¬B")
patch(ax, B_, edgecolor="None")
patch(ax, A, facecolor="None", linestyle="--", linewidth=1)
patch(ax, B, facecolor="None", linestyle="-", linewidth=1.5)
plt.setp(ax.spines.values(), linewidth=1.5)

# A ∪ B
ax = subplot(rows, cols, 5, "A ∪ B")
patch(ax, A, edgecolor="None")
patch(ax, B, edgecolor="None")
patch(ax, A, facecolor="None", linestyle="--", linewidth=1)
patch(ax, B, facecolor="None", linestyle="--", linewidth=1)
patch(ax, B, facecolor="None", edgecolor="black", clip=A_, linewidth=1.5)
patch(ax, A, facecolor="None", edgecolor="black", clip=B_, linewidth=1.5)

# A ∪ ¬B
ax = subplot(rows, cols, 6, "A ∪ ¬B")
patch(ax, A, edgecolor="None")
patch(ax, B_, edgecolor="None")
patch(ax, A, facecolor="None", linestyle="--", linewidth=1)
patch(ax, B, facecolor="None", linestyle="--", linewidth=1)
patch(ax, B, facecolor="None", edgecolor="black", clip=A_, linewidth=1.5)
patch(ax, A, facecolor="None", edgecolor="black", clip=B, linewidth=1.5)
plt.setp(ax.spines.values(), linewidth=1.5)

# ¬A ∪ B
ax = subplot(rows, cols, 7, "¬A ∪ B")
patch(ax, A_, edgecolor="None")
patch(ax, B, edgecolor="None")
patch(ax, A, facecolor="None", linestyle="--", linewidth=1)
patch(ax, B, facecolor="None", linestyle="--", linewidth=1)
patch(ax, A, facecolor="None", edgecolor="black", clip=B_, linewidth=1.5)
patch(ax, B, facecolor="None", edgecolor="black", clip=A, linewidth=1.5)
plt.setp(ax.spines.values(), linewidth=1.5)

# ¬A ∪ ¬B
ax = subplot(rows, cols, 8, "¬A ∪ ¬B")
patch(ax, A_, edgecolor="None")
patch(ax, B_, edgecolor="None")
patch(ax, A, facecolor="None", linestyle="--", linewidth=1)
patch(ax, B, facecolor="None", linestyle="--", linewidth=1)
patch(ax, A, facecolor="None", edgecolor="black", clip=B, linewidth=1.5)
patch(ax, B, facecolor="None", edgecolor="black", clip=A, linewidth=1.5)
plt.setp(ax.spines.values(), linewidth=1.5)

# A ∩ B
ax = subplot(rows, cols, 9, "A ∩ B")
patch(ax, A, edgecolor="None", clip=B)
patch(ax, A, facecolor="None", linestyle="--", linewidth=1)
patch(ax, B, facecolor="None", linestyle="--", linewidth=1)
patch(ax, A, facecolor="None", edgecolor="black", clip=B, linewidth=1.5)
patch(ax, B, facecolor="None", edgecolor="black", clip=A, linewidth=1.5)

# A ∩ ¬B
ax = subplot(rows, cols, 10, "A ∩ ¬B")
patch(ax, A, edgecolor="None", clip=B_)
patch(ax, A, facecolor="None", linestyle="--", linewidth=1)
patch(ax, B, facecolor="None", linestyle="--", linewidth=1)
patch(ax, A, facecolor="None", edgecolor="black", clip=B_, linewidth=1.5)
patch(ax, B, facecolor="None", edgecolor="black", clip=A, linewidth=1.5)


# ¬A ∩ B
ax = subplot(rows, cols, 11, "¬A ∩ B")
patch(ax, B, edgecolor="None", clip=A_)
patch(ax, A, facecolor="None", linestyle="--", linewidth=1)
patch(ax, B, facecolor="None", linestyle="--", linewidth=1)
patch(ax, B, facecolor="None", edgecolor="black", clip=A_, linewidth=1.5)
patch(ax, A, facecolor="None", edgecolor="black", clip=B, linewidth=1.5)

# ¬A ∩ ¬B
ax = subplot(rows, cols, 12, "¬A ∩ ¬B")
patch(ax, A_, edgecolor="None", clip=B_)
patch(ax, A, facecolor="None", linestyle="--", linewidth=1)
patch(ax, B, facecolor="None", linestyle="--", linewidth=1)
patch(ax, B, facecolor="None", edgecolor="black", clip=A_, linewidth=1.5)
patch(ax, A, facecolor="None", edgecolor="black", clip=B_, linewidth=1.5)
plt.setp(ax.spines.values(), linewidth=1.5)

plt.tight_layout()
plt.savefig("../../figures/beyond/polygon-clipping.pdf")
plt.show()
