# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: Creative Commons BY-NC-SA International 4.0
# ----------------------------------------------------------------------------
import matplotlib.pyplot as plt


def figure(dpi):
    fig = plt.figure(figsize=(4.25, 0.2))
    ax = plt.subplot(1, 1, 1, frameon=False)
    plt.xticks([]), plt.yticks([])
    text = "A text rendered at 10pt size using {0} dpi".format(dpi)
    ax.text(
        0.5,
        0.5,
        text,
        fontname="Source Serif Pro",
        ha="center",
        va="center",
        fontsize=10,
        fontweight="light",
    )
    plt.savefig("../../figures/anatomy/figure-dpi-{0:03d}.png".format(dpi), dpi=dpi)


figure(50)
figure(100)
figure(300)
figure(600)

# Using ImageMagick
# convert -resize 2550x -append figure-dpi-*.png figure-dpi.png
