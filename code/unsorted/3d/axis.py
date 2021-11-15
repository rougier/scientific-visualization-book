import glm
import plot
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
if __name__ == "__main__":

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_axes([0, 0, 1, 1])
    camera = glm.camera(25, 45, 1, "perspective")
    plot.axis(ax, camera)
    plt.show()
