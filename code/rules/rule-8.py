import numpy as np
import matplotlib.pyplot as plt

# Data
# -----------------------------------------------------------------------------
p, n = 7, 32
X = np.linspace(0, 2, n)
Y = np.random.uniform(-0.75, 0.5, (p, n))

# -----------------------------------------------------------------------------
fig = plt.figure(figsize=(20, 8))
ax = plt.subplot(1, 2, 1, aspect=1)
ax.patch.set_facecolor((1, 1, 0.75))
for i in range(p):
    plt.plot(X, Y[i], label="Series %d     " % (1 + i), lw=2)
plt.xlim(0, 2)
plt.ylim(-1, 1)
plt.yticks(np.linspace(-1, 1, 18))
plt.xticks(np.linspace(0, 2, 18))
plt.legend()
plt.grid()

# -----------------------------------------------------------------------------
ax = plt.subplot(1, 2, 2, aspect=1)
Yy = p - (np.arange(p) + 0.5)
Xx = [p,] * p
rects = plt.barh(
    Yy, Xx, align="center", height=0.75, color=".95", ec="None", zorder=-20
)
plt.xlim(0, p), plt.ylim(0, p)

for i in range(p):
    label = "Series %d" % (1 + i)
    plt.text(-0.1, Yy[i], label, ha="right", fontsize=16)
    plt.axvline(0, (Yy[i] - 0.4) / p, (Yy[i] + 0.4) / p, c="k", lw=3)
    plt.axvline(
        0.25 * p, (Yy[i] - 0.375) / p, (Yy[i] + 0.375) / p, c=".5", lw=0.5, zorder=-15
    )
    plt.axvline(
        0.50 * p, (Yy[i] - 0.375) / p, (Yy[i] + 0.375) / p, c=".5", lw=0.5, zorder=-15
    )
    plt.axvline(
        0.75 * p, (Yy[i] - 0.375) / p, (Yy[i] + 0.375) / p, c=".5", lw=0.5, zorder=-15
    )
    plt.plot(X * p / 2, i + 0.5 + 2 * Y[i] / p, c="k", lw=2)
    for j in range(p):
        if i != j:
            plt.plot(X * p / 2, i + 0.5 + 2 * Y[j] / p, c=".5", lw=0.5, zorder=-10)
plt.text(0.25 * p, 0, "0.5", va="top", ha="center", fontsize=10)
plt.text(0.50 * p, 0, "1.0", va="top", ha="center", fontsize=10)
plt.text(0.75 * p, 0, "1.5", va="top", ha="center", fontsize=10)
plt.axis("off")

plt.savefig("../../figures/rules/rule-8.pdf")
plt.show()
