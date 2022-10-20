# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
# Comment: Nicolas P. Rougier & Jehyun Lee
# kr & en: https://jehyunlee.github.io/2021/12/02/Python-DS-92-rougier01/
# ----------------------------------------------------------------------------
# Illustrate rotated & translated axis (using axisartists toolkit)
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.transforms import Affine2D
from mpl_toolkits.axes_grid1.parasite_axes import HostAxes
import mpl_toolkits.axisartist as AA


# Reproducibility seed
np.random.seed(123)

# Generate some data
Z0 = np.random.normal(0, (1.25, 0.75), (150, 2))  # Z0: 2D random points array
Z1 = Affine2D().rotate_deg(35).transform(Z0)      # Z1: rotated Z0
Zm = Z1.mean(axis=0)                              # mean of Z1. Zm = np.array([ 0.13746892, -0.02793329])


# Principal components analysis
# Note that for some seeds, the PC1 and PC2 needs to be inverted
# It could be fixed by looking at the orientation but I'm lazy
W, V = np.linalg.eig(np.cov(Z1.T))                 # W: eigenvalues, V: eigenvectors
PC1, PC2 = V[np.argsort(abs(W))]                   # PC1, PC2: 1st and 2nd Principal components
if PC2[1] < 0:                                     # to make PC2 "upwards"
    PC2 = -PC2
rotation = 180 * np.arctan2(*PC1) / np.pi

# Compute the width of the distribution along orthogonal direction to the PCA
# main axis. This is made by rotating points and taking max on the Y axis.
transform = Affine2D().rotate_deg(-rotation)

P1 = transform.transform(Z1 - Z1.mean(axis=0))     # P1 : rotated Z1, along x-axis
d = np.abs(P1[:, 1]).max()                         # d  : max. distance between P0 and Z1


# Draw
fig = plt.figure(figsize=(5, 5), num=3)
fig.clf()
ax1 = fig.add_axes([0.05, 0.05, 0.9, 0.9], aspect=1,
                   axes_class=HostAxes)
# we use HostAxes from axes_grid1.parasite axes so that we can add parasite
# axes that shares the transData of ax1.

# Main scatter plot
ax1.scatter(Z1[:, 0], Z1[:, 1], s=50, fc="C0", ec="white", lw=0.75)
ax1.set_xlim([-3, 6])
ax1.set_xticks([-3, 6])
ax1.set_xticklabels([])
ax1.set_ylim([-3, 6])
ax1.set_yticks([-3, 6])
ax1.set_yticklabels([])
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)


# Arrows on the axis to show the mean

ax1.annotate('', xy=(Zm[0], 0), xytext=(0, 5),
             xycoords=("data", "axes fraction"),
             textcoords='offset points',
             arrowprops=dict(facecolor='black', shrink=0.5,
                             headlength=5, headwidth=5))

ax1.annotate('', xy=(0, Zm[1]), xytext=(5, 0),
             xycoords=("axes fraction", "data"),
             textcoords='offset points',
             arrowprops=dict(facecolor='black', shrink=0.5,
                             headlength=5, headwidth=5))


# We define transform from the original axes to the rotated one.
transform_to_rotated = (Affine2D()
             .translate(-Zm[0], -Zm[1])
             .rotate_deg(rotation)
             .translate(0, -6+d)
             .scale(1, 10) # to reduce the height of the histogram
)

transform_from_rotated = transform_to_rotated.inverted()

# We create new parasite axes to draw a x-axis of the rotated axes. Note that
# the transData of this axes is still that of the original axes, and we cannot
# use it to draw histogram.
helper = AA.GridHelperCurveLinear(transform_from_rotated)
ax2_for_axis = AA.ParasiteAxes(ax1, viewlim_mode="equal", grid_helper=helper)
ax1.parasites.append(ax2_for_axis)

# we create new floaing axis.
xaxis = ax2_for_axis.axis["y=0"] = ax2_for_axis.new_floating_axis(1, 0)
xaxis.get_helper().set_extremes(-d, d) # limit its extents.
xaxis.toggle(ticklabels=False)
xaxis.major_ticks.set_tick_out(True)

# another parasite axes to draw histogram and others. The transData of this
# axes has that of the rotated axes.
ax2 = ax1.get_aux_axes(transform_from_rotated)

# P0: Draw main PCA axis, which is at x=0 in the rotated axes.
ax2.vlines([0], -100, 100,
           color="black", linestyle="--", linewidth=0.75, zorder=10)

# P2 : a rectangle surrounding the distribution & oriented along PCA main axis
ax2.fill_between([-d, d], -100,
                 facecolor="C0",
                 alpha=0.1,
                 zorder=-50)

# P3, P4 : edges of P2 parallel to PC1
ax2.vlines([-d, d], ymin=-100, ymax=0,
           color="C0", linestyle="-", linewidth=0.75, alpha=0.25)

# we transform the original data to the rotated axes.
Z1t = transform_to_rotated.transform(Z1)

# And draw its histogram in the rotated axes.
h, bins, _ = ax2.hist(Z1t[:, 0], bins=np.linspace(-d, d, 12))

# Adding some labels
cbins = 0.5*(bins[:-1] + bins[1:]) # center of bins
for x, y in zip(cbins, h):
    ax2.annotate(
        "%d" % y, (x, y),
        ha="center",
        va="bottom",
        size=8,
        rotation_mode="anchor",
        rotation=-rotation,
    )

# Save
plt.savefig("../../figures/coordinates/transforms-hist-alternative.pdf")
plt.show()
