# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, MultipleLocator

X = np.linspace(0.001, 90, 5000)
figure = plt.figure(figsize=(6, 6))

# Style
# -----------------------------------------------------------------------------
plt.rc("font", family="Roboto")
plt.rc("xtick", labelsize="small")
plt.rc("ytick", labelsize="small")
plt.rc("axes", labelsize="medium", titlesize="medium")


# X-linear Y-linear
# -----------------------------------------------------------------------------
ax1 = plt.subplot(2, 2, 1, xlim=(0.0, 10), ylim=(0.0, 10))
ax1.plot(X, 10 ** X, color="C0")
ax1.plot(X, X, color="C1")
ax1.plot(X, np.log10(X), color="C2")
ax1.set_ylabel("Linear")
ax1.xaxis.set_major_locator(MultipleLocator(2.0))
ax1.xaxis.set_minor_locator(MultipleLocator(0.4))
ax1.yaxis.set_major_locator(MultipleLocator(2.0))
ax1.yaxis.set_minor_locator(MultipleLocator(0.4))
ax1.grid(True, "minor", color="0.85", linewidth=0.50, zorder=-20)
ax1.grid(True, "major", color="0.65", linewidth=0.75, zorder=-10)
ax1.tick_params(which="both", labelbottom=False, bottom=False)

ax1.text(1.25, 8.50, "$f(x) = 10^x$", color="C0")
ax1.text(5.75, 5.00, "$f(x) = x$", color="C1")
ax1.text(5.50, 1.50, "$f(x) = log_{10}(x)$", color="C2")
ax1.set_title("X linear - Y linear")


# X-log Y-linear
# -----------------------------------------------------------------------------
ax2 = plt.subplot(2, 2, 2, xlim=(0.001, 100), ylim=(0.0, 10), sharey=ax1)
ax2.set_xscale("log")
ax2.tick_params(which="both", labelbottom=False, bottom=False)
ax2.tick_params(which="both", labelleft=False, left=False)
ax2.plot(X, 10 ** X, color="C0")
ax2.plot(X, X, color="C1")
ax2.plot(X, np.log10(X), color="C2")
ax2.grid(True, "minor", color="0.85", linewidth=0.50, zorder=-20)
ax2.grid(True, "major", color="0.65", linewidth=0.75, zorder=-10)
ax2.set_title("X logarithmic - Y linear")


# X-linear Y-log
# -----------------------------------------------------------------------------
ax3 = plt.subplot(2, 2, 3, xlim=(0.0, 10), ylim=(0.001, 100), sharex=ax1)
ax3.set_yscale("log")
ax3.plot(X, 10 ** X, color="C0")
ax3.plot(X, X, color="C1")
ax3.plot(X, np.log10(X), color="C2")
ax3.set_ylabel("Logarithmic")
ax3.set_xlabel("Linear")
ax3.grid(True, "minor", color="0.85", linewidth=0.50, zorder=-20)
ax3.grid(True, "major", color="0.65", linewidth=0.75, zorder=-10)
ax3.set_title("X linear - Y logarithmic")

# X-log Y-log
# -----------------------------------------------------------------------------
ax4 = plt.subplot(2, 2, 4, xlim=(0.001, 100), ylim=(0.001, 100), sharex=ax2, sharey=ax3)
ax4.set_xscale("log")
ax4.set_yscale("log")
ax4.tick_params(which="both", labelleft=False, left=False)
ax4.plot(X, 10 ** X, color="C0")
ax4.plot(X, X, color="C1")
ax4.plot(X, np.log10(X), color="C2")
ax4.set_xlabel("Logarithmic")
ax4.grid(True, "minor", color="0.85", linewidth=0.50, zorder=-20)
ax4.grid(True, "major", color="0.65", linewidth=0.75, zorder=-10)
ax4.set_title("X logarithmic - Y logarithmic")


# Show
# -----------------------------------------------------------------------------
plt.tight_layout()
plt.savefig("../../figures/scales-projections/scales-log-log.pdf")
plt.show()
