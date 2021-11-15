import glm
import plot
import numpy as np
import matplotlib as mpl
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


# Model loading
V, F = obj_load("bunny.obj")
V = glm.fit_unit_cube(V)


fig = plt.figure(figsize=(8, 8))

ax = plt.subplot(221)
camera = glm.camera(20, 45, 1.25, "perspective")
plot.axis(ax, camera, ticks=False)
plot.mesh(ax, camera, V, F, facecolor="black", edgecolor="black", linewidth=2.5)
plot.mesh(ax, camera, V, F, cmap=plt.get_cmap("magma"), edgecolor="none")
ax.text(0.99, 0.99, "Perpective", transform=ax.transAxes, ha="right", va="top")

white = (1.0, 1.0, 1.0, 0.75)
black = (0.0, 0.0, 0.0, 1.00)

ax = plt.subplot(222)
camera = glm.camera(90, 0, 2, "ortho")
plot.axis(ax, camera, ticks=False)
plot.mesh(ax, camera, V, F, linewidth=0.25, facecolor=white, edgecolor=black)
ax.text(0.99, 0.99, "Orthographic (XZ)", transform=ax.transAxes, ha="right", va="top")

ax = plt.subplot(223)
camera = glm.camera(0, 90, 2, "ortho")
plot.axis(ax, camera, ticks=False)
plot.mesh(ax, camera, V, F, linewidth=0.25, facecolor=white, edgecolor=black)
ax.text(0.99, 0.99, "Orthographic (XY)", transform=ax.transAxes, ha="right", va="top")

ax = plt.subplot(224)
camera = glm.camera(0, 0, 2, "ortho")
plot.axis(ax, camera, ticks=False)
plot.mesh(ax, camera, V, F, linewidth=0.25, facecolor=white, edgecolor=black)
ax.text(0.99, 0.99, "Orthographic (ZY)", transform=ax.transAxes, ha="right", va="top")

plt.tight_layout()
plt.show()
