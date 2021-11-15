import imageio
import numpy as np
import matplotlib.pyplot as plt

I = imageio.imread("../data/mona-lisa.png")


def plot(ax, cmap, name=None):
    ax.imshow(I, cmap=plt.get_cmap(cmap), rasterized=True)
    ax.text(
        0.5,
        0.025,
        name or cmap,
        transform=ax.transAxes,
        color="white",
        ha="center",
        va="bottom",
        size="large",
        family="Roboto Slab",
    )
    ax.set_xticks([]), ax.set_yticks([])


rows, cols = 3, 4
plt.figure(figsize=(9, 10.25))

ax = plt.subplot(rows, cols, 1, frameon=False)
plot(ax, "cividis", "Cividis")
ax = plt.subplot(rows, cols, 2, frameon=False)
plot(ax, "viridis", "Viridis")
ax = plt.subplot(rows, cols, 3, frameon=False)
plot(ax, "magma", "Magma")
ax = plt.subplot(rows, cols, 4, frameon=False)
plot(ax, "inferno", "Inferno")

ax = plt.subplot(rows, cols, 5, frameon=False)
plot(ax, "bone")
ax = plt.subplot(rows, cols, 6, frameon=False)
plot(ax, "YlGn_r", "YlGn\n(Yellow Green)")
ax = plt.subplot(rows, cols, 7, frameon=False)
plot(ax, "RdPu_r", "RdPu\n(Red Purple)")
ax = plt.subplot(rows, cols, 8, frameon=False)
plot(ax, "OrRd_r", "OrRd\n(Orange Red)")


ax = plt.subplot(rows, cols, 9, frameon=False)
plot(ax, "Greys_r", "Greys")
ax = plt.subplot(rows, cols, 10, frameon=False)
plot(ax, "GnBu_r", "GnBu\n(Green Blue)")
ax = plt.subplot(rows, cols, 11, frameon=False)
plot(ax, "BuPu_r", "BuPu\n(Blue Purple)")
ax = plt.subplot(rows, cols, 12, frameon=False)
plot(ax, "YlOrBr_r", "YlOrBr\n(Yellow Orange Brown)")

plt.subplots_adjust(left=0, bottom=0, right=1, top=1, hspace=0.00, wspace=0.00)
plt.savefig("../../figures/colors/mona-lisa.pdf", dpi=300)
plt.show()
