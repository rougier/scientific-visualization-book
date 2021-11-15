import glm
import plot
import numpy as np
import matplotlib.pyplot as plt


# Wavefront loader (only vertices and faces)
def obj_load(filename):
    V, Vi = [], []
    with open(filename) as f:
        for line in f.readlines():
            if line.startswith("#"):
                continue
            values = line.split()
            if not values:
                continue
            if values[0] == "v":
                V.append([float(x) for x in values[1:4]])
            elif values[0] == "f":
                Vi.append([int(x) for x in values[1:4]])
    return np.array(V), np.array(Vi) - 1


fig = plt.figure(figsize=(6, 6))
ax = fig.add_axes([0, 0, 1, 1], xlim=[-1, +1], ylim=[-1, +1], aspect=1)
ax.axis("off")

camera = glm.camera(20, 45, 1.15, "perspective")
plot.axis(ax, camera)

V, F = obj_load("bunny.obj")
V = glm.fit_unit_cube(V)
plot.mesh(
    ax,
    camera,
    V,
    F,
    cmap=plt.get_cmap("magma"),
    linewidth=0.5,
    edgecolor=(0, 0, 0, 0.5),
)

plt.show()
