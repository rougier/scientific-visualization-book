# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 1.25))
ax = plt.subplot(frameon=False)
ax.set_xlim(0.5, 7.5), ax.set_xticks([])
ax.set_ylim(0, 1.5), ax.set_yticks([])


X, Y = [1], [1]
alpha = 1
ax.scatter(X, Y, 256, marker="o", facecolor="black", edgecolor="None", alpha=alpha)
text = "{:d} point\nalpha={:.2f}".format(len(X), alpha)
ax.text(X[0], 0.75, text, ha="center", va="top", size="small")

X, Y = [2], [1]
alpha = 0.1
ax.scatter(X, Y, 256, marker="o", facecolor="black", edgecolor="None", alpha=alpha)
text = "{:d} point\nalpha={:.3f}".format(len(X), alpha)
ax.text(X[0], 0.75, text, ha="center", va="top", size="small")

X, Y = [3] * 10, [1] * 10
alpha = 0.1
ax.scatter(X, Y, 256, marker="o", facecolor="black", edgecolor="None", alpha=alpha)
text = "{:d} point(s)\nalpha={:.3f}".format(len(X), alpha)
ax.text(X[0], 0.75, text, ha="center", va="top", size="small")

X, Y = [4] * 25, [1] * 25
alpha = 0.1
ax.scatter(X, Y, 256, marker="o", facecolor="black", edgecolor="None", alpha=alpha)
text = "{:d} point(s)\nalpha={:.3f}".format(len(X), alpha)
ax.text(X[0], 0.75, text, ha="center", va="top", size="small")

X, Y = [5] * 10, [1] * 10
alpha = 0.002
ax.scatter(X, Y, 256, marker="o", facecolor="black", edgecolor="None", alpha=alpha)
text = "{:d} point(s)\nalpha={:.3f}".format(len(X), alpha)
ax.text(X[0], 0.75, text, ha="center", va="top", size="small")

X, Y = [6] * 64, [1] * 64
alpha = 0.002
ax.scatter(X, Y, 256, marker="o", facecolor="black", edgecolor="None", alpha=alpha)
text = "{:d} point(s)\nalpha={:.3f}".format(len(X), alpha)
ax.text(X[0], 0.75, text, ha="center", va="top", size="small")

X, Y = [7] * 512, [1] * 512
alpha = 0.002
ax.scatter(X, Y, 256, marker="o", facecolor="black", edgecolor="None", alpha=alpha)
text = "{:d} point(s)\nalpha={:.3f}".format(len(X), alpha)
ax.text(X[0], 0.75, text, ha="center", va="top", size="small")


plt.tight_layout()
plt.savefig("../../figures/optimization/transparency.pdf")
plt.show()
