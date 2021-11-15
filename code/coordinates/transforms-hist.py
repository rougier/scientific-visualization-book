# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
# Illustrate rotated & translated axis (using axisartists toolkit)
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.transforms import Affine2D
import mpl_toolkits.axisartist.floating_axes as floating_axes


# Reroducibility seed
np.random.seed(123)

# Generate some data
Z = np.random.normal(0, (1.25, 0.75), (150, 2))
Z = Affine2D().rotate_deg(35).transform(Z)
Zm = Z.mean(axis=0)


# Principal components analysis
# Note that for some seeds, the PC1 and PC2 needs to be inverted
# It could be fixed by looking at the orientation but I'm lazy
W, V = np.linalg.eig(np.cov(Z.T))
PC1, PC2 = V[np.argsort(abs(W))]
rotation = 180 * np.arctan2(*PC1) / np.pi
T = np.array([PC1[1], PC1[0]])  # tangent to PCA1
O = np.array([T[1], -T[0]])  # orthogonal to PCA1


# Draw
fig = plt.figure(figsize=(5, 5))
ax1 = fig.add_axes([0.05, 0.05, 0.9, 0.9], aspect=1)

# Main scatter plot
ax1.scatter(Z[:, 0], Z[:, 1], s=50, fc="C0", ec="white", lw=0.75)
ax1.set_xlim([-3, 6])
ax1.set_xticks([-3, 6])
ax1.set_xticklabels([])
ax1.set_ylim([-3, 6])
ax1.set_yticks([-3, 6])
ax1.set_yticklabels([])
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)


# Draw main PCA axis
P = np.vstack([Zm - T * 10, Zm + T * 10])
ax1.plot(P[:, 0], P[:, 1], color="black", linestyle="--", linewidth=0.75, zorder=10)

# Compute the width of the distribution along orthogonal direction to the PCA
# main axis. This is made by rotating points and taking max on the Y axis.
transform = Affine2D().rotate_deg(-rotation)
P = transform.transform(Z - Z.mean(axis=0))
d = np.abs(P[:, 1]).max()

# Draw a rectangle surrounding the distribution & oriented along PCA main axis
P = np.vstack(
    [
        Zm - 10 * T - d * O,
        Zm + (6 - d) * T - d * O,
        Zm + (6 - d) * T + d * O,
        Zm - 10 * T + d * O,
    ]
)
ax1.add_patch(
    Polygon(
        P,
        closed=True,
        fill=True,
        edgecolor="None",
        facecolor="C0",
        alpha=0.1,
        zorder=-50,
    )
)
P = np.vstack([Zm - 10 * T, Zm + (6 - d) * T]) - d * O
plt.plot(P[:, 0], P[:, 1], color="C0", linestyle="-", linewidth=0.75, alpha=0.25)
P = np.vstack([Zm - 10 * T, Zm + (6 - d) * T]) + d * O
plt.plot(P[:, 0], P[:, 1], color="C0", linestyle="-", linewidth=0.75, alpha=0.25)

# Some markers on the axis to show the mean (we could compute exactly the delta
# for placing the marker but it is not the point of this example)
ax1.scatter(Zm[0], -2.85, s=50, color="black", marker="v", clip_on=False)
ax1.scatter(-2.85, Zm[1], s=50, color="black", marker="<", clip_on=False)


# Now the complicated stuff to orientate and translate the secondary axis

# 1. Compute the center of the histogram
C = Zm + 6 * T

# 2. Compute the coordinate and the size in normalized figure coordinates
x, y = fig.transFigure.inverted().transform(ax1.transData.transform(C))
xo, yo = fig.transFigure.inverted().transform(ax1.transData.transform(C + 2 * d * O))
h = w = np.sqrt((xo - x) ** 2 + (yo - y) ** 2)

# 3. Create the secondary axis
#    Warning: it must be squared, ie. xmax-xmin = ymax-ymin
#    It is possible to have non squared axis, but it would complicate things.
xmin, xmax = -16, 16
ymin, ymax = 0, xmax - xmin
transform = Affine2D().rotate_deg(rotation - 90)
helper = floating_axes.GridHelperCurveLinear(transform, (xmin, xmax, ymin, ymax))
ax2 = floating_axes.FloatingSubplot(fig, 111, grid_helper=helper, zorder=0)

# This auxiliary axis is necessary to draw stuff (no real idea why)
ax2_aux = ax2.get_aux_axes(transform)

# 4. We know the size of the axis we want but it is rotated. When we specify
#    the size and position, it related to the non-rotate axis and we thus need
#    to compute the bounding box. To do that, we rotate the four coordinates
#    from which we deduce the bounding box coordinates.
transform = Affine2D().rotate_deg(rotation - 90)
R = transform.transform(
    [
        (x - w / 2, y - h / 2),
        (x + w / 2, y - h / 2),
        (x - w / 2, y + h / 2),
        (x + w / 2, y + h / 2),
    ]
)
w = R[:, 0].max() - R[:, 0].min()
h = R[:, 1].max() - R[:, 1].min()
ax2.set_position((x - w / 2, y - h / 2, w, h))
fig.add_subplot(ax2)

# 5. Some decoration the secondary axis
ax2.axis["left"].major_ticklabels.set_visible(False)
ax2.axis["bottom"].major_ticklabels.set_visible(False)
ax2.axis["bottom"].major_ticks.set_tick_out(True)
ax2.axis["left"].set_visible(False)
ax2.axis["right"].set_visible(False)
ax2.axis["top"].set_visible(False)
ax2.set_xticks([0, 1])
ax2.patch.set_visible(False)

# 6. Display the histogram, taking care of the extents of the X axis
counts, bins = np.histogram(-Z @ PC1, bins=12)
X = (bins - bins[0]) / (bins[-1] - bins[0])
X = xmin + (xmax - xmin) * X
Y = np.array(counts)
ax2_aux.hist(X[:-1], X, weights=Y, facecolor="C0", edgecolor="white", linewidth=0.25)

# 7. Adding some labels
dx, dy = (X[1] - X[0]) / 2, 0.75
for x, y in zip(X, Y):
    ax2_aux.text(
        x + dx,
        y + dy,
        "%d" % y,
        ha="center",
        va="center",
        size=8,
        rotation=rotation - 90,
    )

# Save
plt.savefig("../../figures/coordinates/transforms-hist.pdf")
plt.show()
