# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
# Illustrate rotated & translated axis (using axisartists toolkit)
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D
from matplotlib.ticker import MultipleLocator
import mpl_toolkits.axisartist.floating_axes as floating_axes


fig = plt.figure(figsize=(8, 8))

# Main axis
ax1 = plt.subplot(1, 1, 1, aspect=1, xlim=[0, 10], ylim=[0, 10])
ax1.xaxis.set_major_locator(MultipleLocator(1.00))
ax1.xaxis.set_minor_locator(MultipleLocator(0.50))
ax1.yaxis.set_major_locator(MultipleLocator(1.00))
ax1.yaxis.set_minor_locator(MultipleLocator(0.50))
ax1.grid(linewidth=0.75, linestyle="--")

# Floating axis
center = np.array([5, 5])  # data coordinates
size = np.array([5, 3])  # data coordinates
orientation = -30  # degrees
T = size / 2 * [(-1, -1), (+1, -1), (+1, +1), (-1, +1), (-1, -1)]
rotation = Affine2D().rotate_deg(orientation)
P = center + rotation.transform(T)

# Floating axis bounding box visualization
# T = rotation.transform(T)
# xmin, xmax = T[:,0].min(), T[:,0].max()
# ymin, ymax = T[:,1].min(), T[:,1].max()
# T = [(xmin, ymin), (xmin, ymax), (xmax, ymax), (xmax, ymin), (xmin, ymin)]
# P = center + T
# plt.plot(P[:,0], P[:,1], color="black", linewidth=0.75)

# Actual floating axis
DC_to_FC = ax1.transData.transform
FC_to_NFC = fig.transFigure.inverted().transform
DC_to_NFC = lambda x: FC_to_NFC(DC_to_FC(x))
xmin, ymin = DC_to_NFC((P[:, 0].min(), P[:, 1].min()))
xmax, ymax = DC_to_NFC((P[:, 0].max(), P[:, 1].max()))
transform = Affine2D().scale(1, 1).rotate_deg(orientation)
helper = floating_axes.GridHelperCurveLinear(transform, (0, size[0], 0, size[1]))
ax2 = floating_axes.FloatingSubplot(fig, 111, grid_helper=helper, zorder=0)
ax2.set_position((xmin, ymin, xmax - xmin, ymax - ymin))
fig.add_subplot(ax2)


# Cosmetic changes
ax2.axis["bottom"].major_ticks.set_tick_out(True)
ax2.axis["bottom"].major_ticklabels.set_visible(False)
ax2.axis["top"].major_ticks.set_visible(False)
ax2.axis["left"].major_ticks.set_tick_out(True)
ax2.axis["left"].major_ticklabels.set_visible(False)
ax2.axis["right"].major_ticks.set_visible(False)
aux = ax2.get_aux_axes(transform)
aux.text(
    0.1,
    0.1,
    "Floating & rotated axis",
    ha="left",
    va="bottom",
    size=10,
    rotation=orientation,
    rotation_mode="anchor",
)

aux.set_xticks([0, 1])

plt.savefig("../../figures/coordinates/transform-example.pdf")
plt.show()
