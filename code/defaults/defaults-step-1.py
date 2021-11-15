# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
# Defaults settings / Implicit defaults
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 257, endpoint=True)
C, S = np.cos(X), np.sin(X)
plt.plot(X, C)
plt.plot(X, S)

plt.tight_layout()
plt.savefig("../../figures/defaults/defaults-step-1.pdf")
plt.show()
