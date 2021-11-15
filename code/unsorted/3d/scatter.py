import glm
import plot
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    from matplotlib.patches import Ellipse
    from matplotlib.collections import PolyCollection

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_axes([0, 0, 1, 1])
    camera = glm.camera(25, 45, 1, "perspective")
    plot.axis(ax, camera)

    np.random.seed(1)
    n = 1024
    P = 0.2 * np.random.normal(0, 1, (n, 3))

    # Bottom shadow
    V = glm.transform(P * [1, 0, 1] - [0, 0.5, 0], camera)
    T = np.linspace(0, 2 * np.pi, 12)
    radius = 0.015
    X, Y, Z = radius * np.cos(T), np.zeros(len(T)), radius * np.sin(T)
    C = np.c_[X, Y, Z]
    polys = []
    for i in range(n):
        V = glm.transform(C + [P[i, 0], -0.5, P[i, 2]], camera)[:, :2]
        polys.append(V)

    collection = PolyCollection(
        polys, linewidths=0, alpha=0.5, zorder=+10, facecolors="0.5", edgecolor="none"
    )
    ax.add_collection(collection)

    # Actual scatter
    V = glm.transform(P, camera)
    X, Y, Z = V[:, 0], V[:, 1], V[:, 2]
    I = np.argsort(Z)
    X, Y = X[I], Y[I]
    facecolor = [
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        mpl.colors.to_rgba("C4"),
        (1, 1, 1, 0.25),
        (1, 1, 1, 1),
    ] * len(X)
    edgecolor = [
        (0, 0, 0, 0.05),
        (0, 0, 0, 0.10),
        (0, 0, 0, 0.15),
        (0, 0, 0, 1.00),
        (0, 0, 0, 0.00),
        (0, 0, 0, 0.00),
    ] * len(X)
    linewidth = [6, 4, 2, 0.5, 0.0, 0.0] * len(X)
    dX = (0, 0, 0, 0, -0.0035, -0.0035) * len(X)
    dY = (0, 0, 0, 0, +0.0025, +0.0025) * len(Y)
    size = np.array((1, 1, 1, 1, 0.25, 0.05) * len(X)) * 50
    X, Y = np.repeat(X, 6), np.repeat(Y, 6)
    ax.scatter(
        X + dX,
        Y + dY,
        s=size,
        linewidth=linewidth,
        zorder=10,
        facecolor=facecolor,
        edgecolor=edgecolor,
    )

    plt.savefig("scatter.png", dpi=300)
    plt.savefig("scatter.pdf")
    plt.show()
