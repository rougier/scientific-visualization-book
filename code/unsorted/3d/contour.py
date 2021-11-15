import glm
import plot
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
if __name__ == "__main__":

    n = 32
    X, Z = np.meshgrid(
        np.linspace(-0.5 + 0.5 / n, +0.5 - 0.5 / n, n),
        np.linspace(-0.5 + 0.5 / n, +0.5 - 0.5 / n, n),
    )
    Y = 0.75 * np.exp(-10 * (X ** 2 + Z ** 2))

    def f(x, y):
        return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-(x ** 2) - y ** 2)

    n = 100
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)
    X, Y = np.meshgrid(x, y)
    Z = 0.5 * f(X, Y)

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_axes([0, 0, 1, 1])

    camera = glm.camera(25, 45, 1, "perspective")
    plot.axis(ax, camera)
    plot.contour(ax, camera, Z)

plt.show()
