# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: Creative Commons BY-NC-SA International 4.0
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms

fig = plt.figure(figsize=(5, 5), dpi=100)
ax = fig.add_subplot(1, 1, 1, projection="polar")
ax.set_ylim(-1, 1), ax.set_yticks([-1, -0.5, 0, 0.5, 1])

FC_to_DC = ax.transData.inverted().transform
NDC_to_FC = ax.transAxes.transform
NDC_to_DC = lambda x: FC_to_DC(NDC_to_FC(x))

P = NDC_to_DC([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])
plt.plot(
    P[:, 0],
    P[:, 1],
    clip_on=False,
    color="k",
    linewidth=1.0,
    linestyle="--",
    zorder=-10,
)
plt.scatter(P[:-1, 0], P[:-1, 1], clip_on=False, facecolor="w", edgecolor="k")

plt.tight_layout()
plt.savefig("../../figures/coordinates/transforms-polar.pdf")
plt.show()
