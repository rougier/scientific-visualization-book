# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: Creative Commons BY-NC-SA International 4.0
# ----------------------------------------------------------------------------
# The goal is to display a metric axis whose physical size (once printed) is
# correct. The figure will be printed on A5 papersize (210x148mm) with 20mm
# margin on each side
#
# Figure width (mm) is thus 148 - 2x 20 = 108mm = 10.8cm
# Figure width (inch) (10.8/2.54) ~ 4.25 inches
#
# However, we need to have margins in our figure (or tick labels will be cut)
# so we'll have 0.125 inches margin on each side of the axis such that the axis
# will be 4 inches.
# ----------------------------------------------------------------------------
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

mpl.rcParams["font.serif"] = "Source Serif Pro"
mpl.rcParams["font.size"] = 10
mpl.rcParams["font.weight"] = 400
mpl.rcParams["font.family"] = "serif"
mpl.rcParams["axes.labelweight"] = 400

inch = 2.54
fig_width = 10.8 / inch  # ~4.252 inches
fig_height = 1.25  #  1.250 inches
margin = 0.125  #  0.125 inches

fig = plt.figure(figsize=(fig_width, fig_height))
plt.subplots_adjust(
    left=margin / fig_width,
    right=1 - margin / fig_width,
    bottom=margin / fig_height,
    top=1 - margin / fig_height,
)

ax1 = plt.subplot(1, 1, 1)
xmin, xmax = 0, 4
ymin, ymax = 0, 1

# Inches graduation
ax1 = plt.subplot(1, 1, 1, yticks=[])
ax1.spines["right"].set_visible(False)
ax1.spines["left"].set_visible(False)
ax1.spines["top"].set_visible(False)
ax1.set_xlim(xmin, xmax)
ax1.set_ylim(ymin, ymax)
ax1.spines["bottom"].set_position(("axes", 0.45))
ax1.xaxis.set_major_locator(MultipleLocator(1.00))
ax1.xaxis.set_minor_locator(MultipleLocator(0.25))
ax1.tick_params(axis="both", which="major")
ax1.set_xlabel("inch")

# Centimeter graduation
ax2 = ax1.twiny()
ax2.spines["right"].set_visible(False)
ax2.spines["left"].set_visible(False)
ax2.spines["bottom"].set_visible(False)
ax2.set_xlim(xmin * inch, xmax * inch)
ax2.spines["top"].set_position(("axes", 0.55))
ax2.xaxis.set_major_locator(MultipleLocator(1.00))
ax2.xaxis.set_minor_locator(MultipleLocator(0.10))
ax2.tick_params(axis="both", which="major", labelsize=10)
ax2.set_xlabel("cm")

plt.savefig("../../figures/anatomy/inch-cm.pdf", dpi=600)
plt.show()
