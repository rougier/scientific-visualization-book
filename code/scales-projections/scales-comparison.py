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
plt.rc("font", family="Roboto")
plt.rc("xtick", labelsize="small")
plt.rc("ytick", labelsize="small")
plt.rc("axes", labelsize="medium", titlesize="medium")


fig = plt.figure(figsize=(6, 2))

# Linear axis
# -----------------------------------------------------------------------------
ax = plt.subplot(3, 1, 1, xlim=[0, 1], ylim=[0, 1])
ax.patch.set_facecolor("none")
ax.text(
    0.5,
    0.1,
    "linear scale (default)",
    transform=ax.transAxes,
    horizontalalignment="center",
    verticalalignment="bottom",
)
ax.set_yticks([])
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.10))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter("%.1f"))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.02))
ax.xaxis.set_minor_formatter(plt.NullFormatter())
ax.tick_params(axis="both", which="major")


# Log axis
# -----------------------------------------------------------------------------
ax = plt.subplot(3, 1, 2, xlim=[0.1, 1.0], ylim=[0, 1])
ax.patch.set_facecolor("none")
ax.text(
    0.5,
    0.1,
    "log scale ('log')",
    transform=ax.transAxes,
    horizontalalignment="center",
    verticalalignment="bottom",
)
ax.set_xscale("log")
ax.set_yticks([])
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.10))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter("%.1f"))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.02))
ax.xaxis.set_minor_formatter(plt.NullFormatter())

# Logit axis
# -----------------------------------------------------------------------------
ax = plt.subplot(3, 1, 3, xlim=[0.1, 0.9], ylim=[0, 1])
ax.patch.set_facecolor("none")
ax.text(
    0.5,
    0.1,
    "logit scale ('logit')",
    transform=ax.transAxes,
    horizontalalignment="center",
    verticalalignment="bottom",
)
ax.set_xscale("logit")
ax.set_yticks([])
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.10))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter("%.1f"))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.02))
ax.xaxis.set_minor_formatter(plt.NullFormatter())

# Show
# -----------------------------------------------------------------------------
plt.tight_layout()
plt.savefig("../../figures/scales-projections/scales-comparison.pdf")
plt.show()
