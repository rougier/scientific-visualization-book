import numpy as np
import matplotlib.pyplot as plt

n = 20
Z = np.linspace(0, 1, n * n).reshape(n, n)
Z = (Z - Z.min()) / (Z.max() - Z.min())
Z += np.random.uniform(0, 1, (n, n))

plt.figure(figsize=(20, 8))

ax = plt.subplot(1, 2, 1, aspect=1)
values = [30.0, 20.0, 15.0, 10.0]
x, y = 0.0, 0.5
for value in values:
    r1 = 0.5 * (value / values[0])
    r2 = 0.5 * ((np.sqrt(value / np.pi)) / (np.sqrt(values[0] / np.pi)))
    ax.add_artist(plt.Circle((x + r2, y), r1, color="r"))
    ax.add_artist(plt.Circle((x + r2, 1.5 + y), r2, color="k"))
    fontsize = 2 * value
    #    plt.text(x+r2, y, "%d" % value, color="white", family = "Times New Roman",
    #             fontsize=fontsize, ha="center", va="center")
    #    plt.text(x+r2, 1.5+y, "%d" % value, color="white", family = "Times New Roman",
    #             fontsize=fontsize, ha="center", va="center")
    x += 2 * r2 + 0.05
plt.axhline(1.25, c="k")
plt.text(
    0.0,
    1.25 + 0.05,
    "Relative size using disc area",
    ha="left",
    va="bottom",
    color=".25",
)
plt.text(
    0.0,
    1.25 - 0.05,
    "Relative size using disc radius",
    ha="left",
    va="top",
    color=".25",
)
plt.xlim(-0.05, 3.5)
plt.ylim(-0.05, 2.6)
plt.axis("off")


ax = plt.subplot(1, 2, 2, aspect=1)

plt.axhline(5, c="k")
plt.text(
    0.0, 5 + 0.15, "Relative size using full range", ha="left", va="bottom", color=".25"
)
plt.text(
    0.0, 5 - 0.15, "Relative size using partial range", ha="left", va="top", color=".25"
)


n = 10
np.random.seed(123)
X = 0.25 + np.arange(n)
Y = 2 + np.random.uniform(0.75, 0.85, n)

plt.bar(X, 5 * (Y - 2.2), 0.9, color="k", ec="None", bottom=6)
plt.bar(X, 20 * (Y - 2.75), 0.9, color="r", ec="None", bottom=1)

plt.xlim(-0.05, 10.5)
plt.ylim(-0.05, 10.5)
plt.axis("off")

plt.savefig("../../figures/rules/rule-7.pdf")
plt.show()
