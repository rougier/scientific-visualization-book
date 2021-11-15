# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

cmaps = (
    "bone",
    "gray",
    "pink",
    "afmhot",
    "hot",
    "gist_heat",
    "copper",
    "Wistia",
    "autumn_r",
    "summer_r",
    "spring_r",
    "cool",
    "winter_r",
)

n = len(cmaps)

fig = plt.figure(figsize=(4.25, n * 0.22))
ax = plt.subplot(1, 1, 1, frameon=False, xlim=[0, 10], xticks=[], yticks=[])
fig.subplots_adjust(top=0.99, bottom=0.01, left=0.15, right=0.99)

y, dy, pad = 0, 0.5, 0.1
ticks, labels = [], []
for cmap in cmaps[::-1]:
    Z = np.linspace(0, 1, 512).reshape(1, 512)
    plt.imshow(Z, extent=[0, 10, y, y + dy], cmap=plt.get_cmap(cmap))
    ticks.append(y + dy / 2)
    labels.append(cmap)
    y = y + dy + pad

ax.set_ylim(-pad, y)
ax.set_yticks(ticks)
ax.set_yticklabels(labels)
ax.tick_params(axis="y", which="both", length=0, labelsize="small")

plt.savefig("reference-colormap-sequential-2.pdf", dpi=600)
plt.show()
