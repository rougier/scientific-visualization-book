# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: Creative Commons BY-NC-SA International 4.0
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib
from matplotlib import ticker
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

plt.figure(figsize=(8, 5), dpi=100)

ax = plt.subplot(2, 1, 1, aspect=0.25)
ax.text(
    0.5,
    0.5,
    "Typography matters",
    family="Times New Roman",
    size=60,
    color=".85",
    horizontalalignment="center",
    verticalalignment="center",
)
ax.set_title(
    "Typography is an important dimension of a scientific figure",
    x=0,
    y=0.965,
    horizontalalignment="left",
    verticalalignment="baseline",
)
ax.set_xticks(np.linspace(0, 1, 21))


ax = plt.subplot(2, 1, 2, aspect=0.25)
font = matplotlib.font_manager.FontProperties(
    family="Roboto Condensed", weight="regular", size=9
)
ax.set_xticks(np.linspace(0, 1, 21))
ax.set_yticks(np.linspace(0, 1, 5))

for label in ax.get_xticklabels():
    label.set_fontproperties(font)
for label in ax.get_yticklabels():
    label.set_fontproperties(font)

for label in ax.get_xticklabels()[1:-1:2]:
    label.set_size(7.5)
    label.set_weight("light")

for label in ax.get_yticklabels()[1:-1:]:
    label.set_size(7.5)
    label.set_weight("light")

ax.text(
    0.5,
    0.5,
    "Typography",
    family="Times New Roman",
    size=80,
    color=".85",
    horizontalalignment="center",
    verticalalignment="center",
)
ax.text(
    0.8375,
    0.725,
    "matters",
    family="Times New Roman",
    size=30,
    color="0.25",
    horizontalalignment="center",
    verticalalignment="center",
)

font = matplotlib.font_manager.FontProperties(
    family="Roboto Slab", weight="regular", size=15
)
text = ax.set_title(
    "Typography is an important dimension of a scientific figure",
    fontproperties=font,
    x=0,
    y=0.975,
    horizontalalignment="left",
    verticalalignment="baseline",
)
text.set_path_effects(
    [path_effects.Stroke(linewidth=2, foreground="white"), path_effects.Normal()]
)


plt.tight_layout()
plt.savefig("../../figures/typography/typography-matters.pdf", dpi=100)
plt.savefig("../../figures/typography/typography-matters.png", dpi=300)
plt.show()
