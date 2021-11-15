# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
# Illustrate the different colorspaces (sRGB, RGB and Lab)
# ----------------------------------------------------------------------------
import math
import numpy as np
from skimage.color import rgb2lab, lab2rgb, rgb2xyz, xyz2rgb
import matplotlib.pyplot as plt

plt.rc("font", family="Roboto")


def sRGB_to_Lab(color):
    color = np.asarray(color, dtype=float)
    shape = color.shape
    if len(shape) == 1:
        color = color.reshape(1, 1, shape[0])
    elif len(shape) == 2:
        color = color.reshape(1, shape[0], shape[1])
    return rgb2lab(color)


def Lab_to_sRGB(color):
    color = np.asarray(color, dtype=float)
    shape = color.shape
    if len(shape) == 1:
        color = color.reshape(1, 1, shape[0])
    elif len(shape) == 2:
        color = color.reshape(1, shape[0], shape[1])
    return lab2rgb(color)


def sRGB_to_RGB(color):
    color = np.asarray(color, dtype=float).reshape(-1, 3)
    R, G, B = color[..., 0], color[..., 1], color[..., 2]
    R = np.where(R > 0.04045, np.power((R + 0.055) / 1.055, 2.4), R / 12.92)
    G = np.where(G > 0.04045, np.power((G + 0.055) / 1.055, 2.4), G / 12.92)
    B = np.where(B > 0.04045, np.power((B + 0.055) / 1.055, 2.4), B / 12.92)
    return np.c_[R, G, B]


def RGB_to_sRGB(color):
    color = np.asarray(color, dtype=float).reshape(-1, 3)
    R, G, B = color[..., 0], color[..., 1], color[..., 2]
    R = np.where(R > 0.0031308, 1.055 * np.power(R, 1 / 2.4) - 0.055, R * 12.92)
    G = np.where(G > 0.0031308, 1.055 * np.power(G, 1 / 2.4) - 0.055, G * 12.92)
    B = np.where(B > 0.0031308, 1.055 * np.power(B, 1 / 2.4) - 0.055, B * 12.92)
    return np.c_[R, G, B]


def gradient(color0, color1, mode="sRGB", n=256):
    T = np.linspace(0, 1, n).reshape(n, 1)
    if mode == "Lab":
        C = (1 - T) * sRGB_to_Lab(color0) + T * sRGB_to_Lab(color1)
        return Lab_to_sRGB(C)
    elif mode == "RGB":
        C = (1 - T) * sRGB_to_RGB(color0) + T * sRGB_to_RGB(color1)
        return RGB_to_sRGB(C)
    else:
        return (1 - T) * color0 + T * color1


def hex(color):
    color = (np.asarray(color) * 255).astype(int)
    r, g, b = color
    return ("#%02x%02x%02x" % (r, g, b)).upper()


def plot(ax, color0, color1, yticks=True):
    rows, cols = 16, 256
    Z = np.zeros((3, rows, cols, 3))
    Z[0] = gradient(color0, color1, "sRGB")
    Z[2] = gradient(color0, color1, "RGB")
    Z[1] = gradient(color0, color1, "Lab")

    ax.tick_params(axis="both", length=0, labelsize="xx-small")
    ax.imshow(Z.reshape(3 * rows, cols, 3), extent=[0, cols, 0, 3 * rows])

    if yticks:
        ax.set_yticks([rows // 2, rows // 2 + rows, rows // 2 + 2 * rows])
        ax.set_yticklabels(["Lab", "RGB", "sRGB"])
    else:
        ax.set_yticks([])
    ax.set_xticks([])
    plt.text(0, -2, hex(color0), ha="left", va="top", fontsize="xx-small")
    plt.text(cols, -2, hex(color1), ha="right", va="top", fontsize="xx-small")


fig = plt.figure(figsize=(4.25, 3.5))
plt.rcParams["axes.linewidth"] = 0.5

rows, cols = 6, 2

ax = plt.subplot(rows, cols, 1)
plot(ax, (1, 1, 1), (1, 0, 0))
ax = plt.subplot(rows, cols, 2)
plot(ax, (1, 0, 0), (0, 0, 0), False)

ax = plt.subplot(rows, cols, 3)
plot(ax, (1, 1, 1), (0, 1, 0))
ax = plt.subplot(rows, cols, 4)
plot(ax, (0, 1, 0), (0, 0, 0), False)

ax = plt.subplot(rows, cols, 5)
plot(ax, (1, 1, 1), (0, 0, 1))
ax = plt.subplot(rows, cols, 6)
plot(ax, (0, 0, 1), (0, 0, 0), False)

ax = plt.subplot(rows, cols, 7)
plot(ax, (1, 0, 0), (0, 1, 0))
ax = plt.subplot(rows, cols, 8)
plot(ax, (0, 1, 0), (0, 0, 1), False)

ax = plt.subplot(rows, cols, 9)
plot(ax, (1, 0, 1), (1, 1, 0))
ax = plt.subplot(rows, cols, 10)
plot(ax, (1, 1, 0), (0, 1, 1), False)

ax = plt.subplot(rows, cols, 11)
plot(ax, (1, 1, 1), (0, 0, 0))
ax = plt.subplot(rows, cols, 12)
plot(ax, (0, 0, 0), (1, 1, 1), False)

plt.tight_layout()
plt.savefig("../../figures/colors/color-gradients.pdf", dpi=600)
plt.show()
