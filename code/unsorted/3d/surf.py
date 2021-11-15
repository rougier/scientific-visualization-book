import glm
import plot
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
if __name__ == "__main__":

    n = 24
    X, Z = np.meshgrid(
        np.linspace(-0.5 + 0.5 / n, +0.5 - 0.5 / n, n),
        np.linspace(-0.5 + 0.5 / n, +0.5 - 0.5 / n, n),
    )
    Y = 0.75 * np.exp(-10 * (X ** 2 + Z ** 2))

    cmap = plt.get_cmap("magma")
    norm = mpl.colors.Normalize(vmin=-0.25, vmax=0.75)
    facecolors = cmap(norm(Y))[..., :3]

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_axes([0, 0, 1, 1])

    camera = glm.camera(25, 45, 1, "perspective")
    plot.axis(ax, camera)
    plot.surf(ax, camera, Y, facecolors=facecolors)

plt.show()
