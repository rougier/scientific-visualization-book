# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
# Defaults settings / Custom defaults
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("./mystyle.txt")

X = np.linspace(-np.pi, np.pi, 257, endpoint=True)
C, S = np.cos(X), np.sin(X)

fig = plt.figure()
ax = plt.subplot(1, 1, 1, aspect=1)
ax.plot(X, C)
ax.plot(X, S)

ax.set_yticks([-1, 1])
ax.set_yticklabels(["-1", "+1"])
ax.set_xticks([-np.pi, -np.pi / 2, np.pi / 2, np.pi])
ax.set_xticklabels(["-π", "-π/2", "+π/2", "+π"])

ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

plt.tight_layout()
plt.savefig("../../figures/defaults/defaults-step-5.pdf")
plt.show()
