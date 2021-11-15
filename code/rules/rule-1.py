# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Matplotlib Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
#
# Author: Nicolas P. Rougier
# Source: New York Times graphics, 2007
# -> http://www.nytimes.com/imagepages/2007/07/29/health/29cancer.graph.web.html
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ----------
# Data to be represented
diseases = [
    "Kidney Cancer",
    "Bladder Cancer",
    "Esophageal Cancer",
    "Ovarian Cancer",
    "Liver Cancer",
    "Non-Hodgkin's\nlymphoma",
    "Leukemia",
    "Prostate Cancer",
    "Pancreatic Cancer",
    "Breast Cancer",
    "Colorectal Cancer",
    "Lung Cancer",
]
men_deaths = [
    10000,
    12000,
    13000,
    0,
    14000,
    12000,
    16000,
    25000,
    20000,
    500,
    25000,
    80000,
]
men_cases = [
    30000,
    50000,
    13000,
    0,
    16000,
    30000,
    25000,
    220000,
    22000,
    600,
    55000,
    115000,
]
women_deaths = [
    6000,
    5500,
    5000,
    20000,
    9000,
    12000,
    13000,
    0,
    19000,
    40000,
    30000,
    70000,
]
women_cases = [
    20000,
    18000,
    5000,
    25000,
    9000,
    29000,
    24000,
    0,
    21000,
    160000,
    55000,
    97000,
]

# ----------
# Choose some nice colors
matplotlib.rc("axes", facecolor="white")
matplotlib.rc("figure.subplot", wspace=0.65)
matplotlib.rc("grid", color="white")
matplotlib.rc("grid", linewidth=1)

# Make figure background the same colors as axes
fig = plt.figure(figsize=(12, 7), facecolor="white")


# ---WOMEN data ---
axes_left = plt.subplot(121)

# Keep only top and right spines
axes_left.spines["left"].set_color("none")
axes_left.spines["right"].set_zorder(10)
axes_left.spines["bottom"].set_color("none")
axes_left.xaxis.set_ticks_position("top")
axes_left.yaxis.set_ticks_position("right")
axes_left.spines["top"].set_position(("data", len(diseases) + 0.25))
axes_left.spines["top"].set_color("w")

# Set axes limits
plt.xlim(200000, 0)
plt.ylim(0, len(diseases))

# Set ticks labels
plt.xticks([150000, 100000, 50000, 0], ["150,000", "100,000", "50,000", "WOMEN"])
axes_left.get_xticklabels()[-1].set_weight("bold")
axes_left.get_xticklines()[-1].set_markeredgewidth(0)
for label in axes_left.get_xticklabels():
    label.set_fontsize(10)
plt.yticks([])


# Plot data
for i in range(len(women_deaths)):
    H, h = 0.8, 0.55
    # Death
    value = women_cases[i]
    p = patches.Rectangle(
        (0, i + (1 - H) / 2.0),
        value,
        H,
        fill=True,
        transform=axes_left.transData,
        lw=0,
        facecolor="red",
        alpha=0.1,
    )
    axes_left.add_patch(p)
    # New cases
    value = women_deaths[i]
    p = patches.Rectangle(
        (0, i + (1 - h) / 2.0),
        value,
        h,
        fill=True,
        transform=axes_left.transData,
        lw=0,
        facecolor="red",
        alpha=0.5,
    )
    axes_left.add_patch(p)

# Add a grid
axes_left.grid()

plt.text(165000, 8.2, "Leading Causes\nOf Cancer Deaths", fontsize=18, va="top")
plt.text(
    165000,
    7,
    """In 2007, there were more\n"""
    """than 1.4 million new cases\n"""
    """of cancer in the United States.""",
    va="top",
    fontsize=10,
)

# --- MEN data ---
axes_right = plt.subplot(122, sharey=axes_left)

# Keep only top and left spines
axes_right.spines["right"].set_color("none")
axes_right.spines["left"].set_zorder(10)
axes_right.spines["bottom"].set_color("none")
axes_right.xaxis.set_ticks_position("top")
axes_right.yaxis.set_ticks_position("left")
axes_right.spines["top"].set_position(("data", len(diseases) + 0.25))
axes_right.spines["top"].set_color("w")


# Set axes limits
plt.xlim(0, 200000)
plt.ylim(0, len(diseases))

# Set ticks labels
plt.xticks(
    [0, 50000, 100000, 150000, 200000],
    ["MEN", "50,000", "100,000", "150,000", "200,000"],
)
axes_right.get_xticklabels()[0].set_weight("bold")
for label in axes_right.get_xticklabels():
    label.set_fontsize(10)
axes_right.get_xticklines()[1].set_markeredgewidth(0)
plt.yticks([])

# Plot data
for i in range(len(men_deaths)):
    H, h = 0.8, 0.55
    # Death
    value = men_cases[i]
    p = patches.Rectangle(
        (0, i + (1 - H) / 2.0),
        value,
        H,
        fill=True,
        transform=axes_right.transData,
        lw=0,
        facecolor="blue",
        alpha=0.1,
    )
    axes_right.add_patch(p)
    # New cases
    value = men_deaths[i]
    p = patches.Rectangle(
        (0, i + (1 - h) / 2.0),
        value,
        h,
        fill=True,
        transform=axes_right.transData,
        lw=0,
        facecolor="blue",
        alpha=0.5,
    )
    axes_right.add_patch(p)

# Add a grid
axes_right.grid()

# Y axis labels
# We want them to be exactly in the middle of the two y spines
# and it requires some computations
for i in range(len(diseases)):
    x1, y1 = axes_left.transData.transform_point((0, i + 0.5))
    x2, y2 = axes_right.transData.transform_point((0, i + 0.5))
    x, y = fig.transFigure.inverted().transform_point(((x1 + x2) / 2, y1))
    plt.text(
        x,
        y,
        diseases[i],
        transform=fig.transFigure,
        fontsize=10,
        horizontalalignment="center",
        verticalalignment="center",
    )


# Devil hides in the details...
arrowprops = dict(arrowstyle="-", connectionstyle="angle,angleA=0,angleB=90,rad=0")
x = women_cases[-1]
axes_left.annotate(
    "NEW CASES",
    xy=(0.9 * x, 11.5),
    xycoords="data",
    horizontalalignment="right",
    fontsize=10,
    xytext=(-40, -3),
    textcoords="offset points",
    arrowprops=arrowprops,
)

x = women_deaths[-1]
axes_left.annotate(
    "DEATHS",
    xy=(0.85 * x, 11.5),
    xycoords="data",
    horizontalalignment="right",
    fontsize=10,
    xytext=(-50, -25),
    textcoords="offset points",
    arrowprops=arrowprops,
)

x = men_cases[-1]
axes_right.annotate(
    "NEW CASES",
    xy=(0.9 * x, 11.5),
    xycoords="data",
    horizontalalignment="left",
    fontsize=10,
    xytext=(+40, -3),
    textcoords="offset points",
    arrowprops=arrowprops,
)

x = men_deaths[-1]
axes_right.annotate(
    "DEATHS",
    xy=(0.9 * x, 11.5),
    xycoords="data",
    horizontalalignment="left",
    fontsize=10,
    xytext=(+50, -25),
    textcoords="offset points",
    arrowprops=arrowprops,
)


# Done
plt.savefig("../../figures/rules/rule-1.pdf")
plt.show()
