# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: Creative Commons BY-NC-SA International 4.0
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import ScaledTranslation

fig = plt.figure(figsize=(6, 4))

ax = fig.add_subplot(2, 1, 1)
plt.text(
    0.1,
    0.1,
    "A",
    fontsize="x-large",
    weight="bold",
    ha="left",
    va="baseline",
    transform=ax.transAxes,
)

ax = fig.add_subplot(2, 1, 2)
dx, dy = 10 / 72, 10 / 72
offset = ScaledTranslation(dx, dy, fig.dpi_scale_trans)

plt.text(
    0,
    0,
    "B",
    fontsize="x-large",
    weight="bold",
    ha="left",
    va="baseline",
    transform=ax.transAxes + offset,
)

plt.tight_layout()
plt.savefig("../../figures/coordinates/transforms-letter.pdf")
plt.show()
