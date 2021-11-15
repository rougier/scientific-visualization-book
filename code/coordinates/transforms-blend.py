# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: Creative Commons BY-NC-SA International 4.0
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import blended_transform_factory, ScaledTranslation

fig = plt.figure(figsize=(6, 4))

ax = fig.add_subplot(1, 1, 1, aspect=1)
ax.set_xlim(0, 10)
ax.set_xticks(range(11))
ax.set_ylim(0, 5)
ax.set_xticks(range(11))

point = 1 / 72
fontsize = 12
dx, dy = 0, -1.5 * fontsize * point
offset = ScaledTranslation(dx, dy, fig.dpi_scale_trans)
transform = blended_transform_factory(ax.transData, ax.transAxes + offset)

for x in range(11):
    plt.text(x, 0, "↑", transform=transform, ha="center", va="top", fontsize=fontsize)

plt.tight_layout()
plt.savefig("../../figures/coordinates/transforms-blend.pdf")
plt.show()
