import glm
import plot
import numpy as np
import matplotlib.pyplot as plt


def sphere(radius=1.0, slices=32, stacks=32):
    slices += 1
    stacks += 1
    n = slices * stacks
    vertices = np.zeros((n, 3))
    theta1 = np.repeat(np.linspace(0, np.pi, stacks, endpoint=True), slices)
    theta2 = np.tile(np.linspace(0, 2 * np.pi, slices, endpoint=True), stacks)

    vertices[:, 1] = np.sin(theta1) * np.cos(theta2) * radius
    vertices[:, 2] = np.cos(theta1) * radius
    vertices[:, 0] = np.sin(theta1) * np.sin(theta2) * radius

    indices = []
    for i in range(stacks - 1):
        for j in range(slices - 1):
            indices.append(i * (slices) + j)
            indices.append(i * (slices) + j + 1)
            indices.append(i * (slices) + j + slices + 1)

            indices.append(i * (slices) + j + slices + 1)
            indices.append(i * (slices) + j + slices)
            indices.append(i * (slices) + j)

    indices = np.array(indices)
    indices = indices.reshape(len(indices) // 3, 3)
    return vertices, indices


def lighting(F, direction=(1, 1, 1), color=(1, 0, 0), specular=False):

    # Faces center
    C = F.mean(axis=1)
    # Faces normal
    N = glm.normalize(np.cross(F[:, 2] - F[:, 0], F[:, 1] - F[:, 0]))
    # Relative light direction
    D = glm.normalize(C - direction)
    # Diffuse term
    diffuse = glm.clip((N * D).sum(-1).reshape(-1, 1))

    # Specular term
    if specular:
        specular = np.power(diffuse, 24)
        return np.maximum(diffuse * color, specular)

    return diffuse * color


V, F = sphere(0.5, 2 * 32, 2 * 32)
facecolor = lighting(V[F], (-1, 1, 1), (1, 0, 0), True)

fig = plt.figure(figsize=(6, 6))
ax = fig.add_axes([0, 0, 1, 1], xlim=[-1, +1], ylim=[-1, +1], aspect=1)

camera = glm.camera(20, 45, 1.15, "perspective")
plot.axis(ax, camera)
plot.mesh(
    ax,
    camera,
    V,
    F,
    mode="front",
    linewidth=0,
    facecolor=facecolor,
    edgecolor=(0, 0, 0, 0),
)
plt.show()
