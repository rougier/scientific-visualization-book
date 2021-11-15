# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: Creative Commons BY-NC-SA International 4.0
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(8, 2))

ymin, ymax = [0, 2]
xmin, xmax = [0, 8]
ax = plt.subplot(1, 1, 1, aspect=1, xlim=[xmin, xmax], ylim=[ymin, ymax])
point = fig.dpi / 72
X = 0.5 + np.arange(8)
Y = np.ones(len(X))

# Marker size is expressed in point^2 and a point is defined as fig.dpi/72
# This means that a size of 10 really means (10*point)^2
# Problem is thus to convert points into data coordinates:
# PT_to_DC = lambda x: x * ax.get_window_extent().width / (xmax-xmin)
# Note that the DC_to_PR is validonly for a given window size

DC_to_PT = lambda x: x * ax.get_window_extent().width / (xmax - xmin) / point
S = DC_to_PT(1) ** 2
plt.scatter(X, Y, s=S, facecolor="none", edgecolor="black", linewidth=1)

plt.savefig("../../figures/coordinates/transforms-exercise-1.pdf")
plt.show()
