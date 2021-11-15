# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# Style
# -----------------------------------------------------------------------------
plt.rc("font", family="Roboto Condensed")
plt.rc("xtick", labelsize="small")
plt.rc("ytick", labelsize="small")
plt.rc("axes", labelsize="medium", titlesize="medium")

fig = plt.figure(figsize=(8, 2))

#
# -----------------------------------------------------------------------------
ax = plt.subplot(4, 1, 1, xlim=[0, 1], ylim=[0, 1])
ax.patch.set_facecolor("none")
ax.set_yticks([])
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.05))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter("%.2f"))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax.xaxis.set_minor_formatter(plt.NullFormatter())
ax.tick_params(axis="both", which="major")
labels = ax.get_xticklabels()
for i, label in enumerate(labels):
    if i in [1, 6, 11, 16, 21]:
        label.set_font("Roboto")
        label.set_size(8.5)

#
# -----------------------------------------------------------------------------
ax = plt.subplot(4, 1, 2, xlim=[0, 1], ylim=[0, 1])
ax.patch.set_facecolor("none")
ax.set_yticks([])
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.05))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter("%.2f"))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax.xaxis.set_minor_formatter(plt.NullFormatter())
labels = ax.get_xticklabels()
for i, label in enumerate(labels):
    if i not in [1, 6, 11, 16, 21]:
        label.set_size(7)

#
# -----------------------------------------------------------------------------
ax = plt.subplot(4, 1, 3, xlim=[0, 1], ylim=[0, 1])
ax.patch.set_facecolor("none")
ax.set_yticks([])
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.05))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter("%.2f"))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax.xaxis.set_minor_formatter(plt.NullFormatter())
labels = ax.get_xticklabels()
for i, label in enumerate(labels):
    if i not in [1, 6, 11, 16, 21]:
        label.set_weight(200)


#
# -----------------------------------------------------------------------------
ax = plt.subplot(4, 1, 4, xlim=[0, 1], ylim=[0, 1])
ax.patch.set_facecolor("none")
ax.set_yticks([])
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.05))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter("%.2f"))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax.xaxis.set_minor_formatter(plt.NullFormatter())

labels = ax.get_xticklabels()
for i, label in enumerate(labels):
    if i in [1, 6, 11, 16, 21]:
        label.set_color("white")
        label.set_weight(600)
        label.set_bbox(
            dict(
                boxstyle="round,pad=.25",
                linewidth=0.5,
                facecolor="black",
                edgecolor="black",
            )
        )

# Show
# -----------------------------------------------------------------------------
plt.tight_layout()
plt.savefig("../../figures/typography/tick-labels-variation.pdf")
plt.show()
