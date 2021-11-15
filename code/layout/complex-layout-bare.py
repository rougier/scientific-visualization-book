# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


fig = plt.figure(figsize=(6.5, 6))
gspec = gridspec.GridSpec(
    ncols=7, nrows=7, figure=fig, height_ratios=[1, 0.25, 1, 1, 1, 1, 1]
)

plt.rc("axes", edgecolor=".75")
ax = plt.subplot(
    gspec[1, :2], frameon=True, xlim=[0, 1], xticks=[], ylim=[0, 1], yticks=[]
)
ax = plt.subplot(
    gspec[0, 2:4], frameon=True, xlim=[0, 1], xticks=[], ylim=[0, 1], yticks=[]
)
ax = plt.subplot(
    gspec[0, 5:7], frameon=True, xlim=[0, 1], xticks=[], ylim=[0, 1], yticks=[]
)
plt.rc("axes", edgecolor="black")

for col in range(2, 7):
    ax = plt.subplot(
        gspec[1, col], frameon=True, xlim=[0, 1], xticks=[], ylim=[0, 1], yticks=[]
    )

for row in range(2, 7):
    ax = plt.subplot(
        gspec[row, :2], frameon=True, xlim=[0, 1], xticks=[], ylim=[0, 1], yticks=[]
    )
    for col in range(2, 7):
        ax = plt.subplot(
            gspec[row, col],
            aspect=1,
            frameon=True,
            xlim=[0, 1],
            xticks=[],
            ylim=[0, 1],
            yticks=[],
        )


ax = plt.subplot(
    gspec[0, 4], frameon=True, aspect=1, xlim=[0, 1], xticks=[], ylim=[0, 1], yticks=[]
)

ax = plt.subplot(
    gspec[0, :2], frameon=True, xlim=[0, 10], xticks=[], ylim=[0, 4], yticks=[]
)

plt.savefig("../../figures/layout/complex-layout-bare.pdf")
plt.show()
