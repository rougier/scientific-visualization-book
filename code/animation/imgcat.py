# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib

# Needs OSX and iterm2
matplotlib.use("module://imgcat")
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 4), frameon=False)

ax = plt.subplot(2, 1, 1)
X = np.linspace(0, 4 * 2 * np.pi, 500)
(line,) = ax.plot(X, np.cos(X))

ax = plt.subplot(2, 1, 2)
X = np.linspace(0, 4 * 2 * np.pi, 500)
(line,) = ax.plot(X, np.sin(X))

plt.tight_layout()
plt.show()
