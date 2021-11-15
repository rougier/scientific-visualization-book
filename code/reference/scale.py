# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, SymmetricalLogLocator


X = np.linspace(-2, 2, 1001)
Y = np.cos(X * 5 * 2 * np.pi)


figure = plt.figure(figsize=(6, 6))

# Style
# -----------------------------------------------------------------------------
# plt.rc('font', family="Roboto Condensed")
plt.rc("font", family="Roboto")
plt.rc("xtick", labelsize="small")
plt.rc("ytick", labelsize="small")
plt.rc("axes", labelsize="medium", titlesize="medium")


# Linear scale
# -----------------------------------------------------------------------------
ax = plt.subplot(4, 1, 1, ylim=(-3, 2))
plt.plot(X, Y, color="C1", linewidth=1.5)
ax.set_yticks([])
ax.text(
    0.01,
    0.95,
    "Linear scale",
    transform=ax.transAxes,
    weight=600,
    horizontalalignment="left",
    verticalalignment="top",
    size="medium",
)

# Respective domains for scales
plt.plot([-2, 2], [-1.5, -1.5], color="black", linewidth=1, marker="|")
ax.text(
    0,
    -1.5,
    "SymLog scale domain",
    transform=ax.transData,
    size="x-small",
    bbox=dict(facecolor="white", edgecolor="None", pad=1.0),
    horizontalalignment="center",
    verticalalignment="center",
)

plt.plot([0, 2], [-2.0, -2.0], color="black", linewidth=1, marker="|")
ax.text(
    1,
    -2,
    "Log scale domain",
    transform=ax.transData,
    size="x-small",
    bbox=dict(facecolor="white", edgecolor="None", pad=1.0),
    horizontalalignment="center",
    verticalalignment="center",
)

plt.plot([0, 1], [-2.5, -2.5], color="black", linewidth=1, marker="|")
ax.text(
    0.5,
    -2.5,
    "Logit scale domain",
    transform=ax.transData,
    size="x-small",
    bbox=dict(facecolor="white", edgecolor="None", pad=1.0),
    horizontalalignment="center",
    verticalalignment="center",
)


# Log scale (X > 0)
# -----------------------------------------------------------------------------
ax = plt.subplot(4, 1, 2, ylim=(-2, 2))
ax.set_xscale("log", basex=10)
plt.plot(X, Y, color="C1", linewidth=1.5)
ax.set_yticks([])
ax.text(
    0.01,
    0.95,
    "Log scale (x > 0)",
    transform=ax.transAxes,
    weight=600,
    horizontalalignment="left",
    verticalalignment="top",
    size="medium",
)


# SymLog scale
# -----------------------------------------------------------------------------
ax = plt.subplot(4, 1, 3, ylim=(-2, 2))
t = 0.05
ax.set_xscale("symlog", basex=10, linthreshx=t, linscalex=1)
plt.plot(X, Y, color="C1", linewidth=1.5)
ax.set_yticks([])
ax.xaxis.set_minor_locator(
    SymmetricalLogLocator(base=10, linthresh=t, subs=np.arange(2, 10))
)

ax.text(
    0.01,
    0.95,
    "Symlog scale",
    transform=ax.transAxes,
    weight=600,
    horizontalalignment="left",
    verticalalignment="top",
    size="medium",
)
ax.fill_betweenx([-2, 2], [-t, -t], [+t, +t], facecolor="black", alpha=0.1)
ax.text(
    0.50,
    0.05,
    "Linear",
    transform=ax.transAxes,
    horizontalalignment="center",
    verticalalignment="bottom",
)
ax.text(
    0.15,
    0.05,
    "Logarithmic",
    transform=ax.transAxes,
    horizontalalignment="center",
    verticalalignment="bottom",
)
ax.text(
    0.85,
    0.05,
    "Logarithmic",
    transform=ax.transAxes,
    horizontalalignment="center",
    verticalalignment="bottom",
)


# Logit (0 < X < 1)
# -----------------------------------------------------------------------------
ax = plt.subplot(4, 1, 4, ylim=(-2, 2))
ax.set_xscale("logit")
plt.plot(X, Y, color="C1", linewidth=1.5)
ax.set_yticks([])
ax.xaxis.set_minor_formatter(NullFormatter())
ax.text(
    0.01,
    0.95,
    "Logit scale (0 < x < 1)",
    transform=ax.transAxes,
    weight=600,
    horizontalalignment="left",
    verticalalignment="top",
    size="medium",
)
ax.fill_betweenx([-2, 2], [0.2, 0.2], [0.8, 0.8], facecolor="black", alpha=0.1)
ax.text(
    0.50,
    0.05,
    "Quasi linear",
    transform=ax.transAxes,
    horizontalalignment="center",
    verticalalignment="bottom",
)
ax.text(
    0.2,
    0.05,
    "Logarithmic",
    transform=ax.transAxes,
    horizontalalignment="center",
    verticalalignment="bottom",
)
ax.text(
    0.8,
    0.05,
    "Logarithmic",
    transform=ax.transAxes,
    horizontalalignment="center",
    verticalalignment="bottom",
)

# Show
plt.tight_layout()
plt.savefig("reference-scale.pdf")
plt.show()
