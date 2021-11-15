# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fig = plt.figure(figsize=(4.25, 3.8))
ax = fig.add_axes(
    [0, 0, 1, 1], frameon=False, xticks=[], yticks=[], xlim=[0, 40], ylim=[0, 38]
)

y = 1

# -----------------------------------------------------------------------------
variants = {
    "normal": "/Users/rougier/Library/Fonts/Delicious-Roman.otf",
    "small-caps": "/Users/rougier/Library/Fonts/Delicious-SmallCaps.otf",
}

text = "The quick brown fox jumps over the lazy dog"
for i, variant in enumerate(variants.keys()):
    ax.text(
        1,
        y,
        text,
        size=9,
        va="center",
        fontproperties=FontProperties(fname=variants[variant]),
    )

    ax.text(
        39,
        y,
        variant,
        color="0.25",
        va="center",
        ha="right",
        size="small",
        family="Source Code Pro",
        weight=400,
    )
    y += 1.65
y += 1

# -----------------------------------------------------------------------------
styles = ["normal", "italic"]

text = "The quick brown fox jumps over the lazy dog"
for i, style in enumerate(styles):
    ax.text(1, y, text, size=9, va="center", style=style, family="Source Sans Pro")

    ax.text(
        39,
        y,
        style,
        color="0.25",
        va="center",
        ha="right",
        size="small",
        family="Source Code Pro",
        weight=400,
    )
    y += 1.65
y += 1


# -----------------------------------------------------------------------------
families = {
    "Pacifico": "cursive",
    "Source Sans Pro": "sans",
    "Source Serif Pro": "serif",
    "Source Code Pro": "monospace",
}

text = "The quick brown fox jumps over the lazy dog"
for i, family in enumerate(families):
    ax.text(1, y, text, va="center", size=9, family=family, weight="regular")

    ax.text(
        39,
        y,
        "%s" % (families[family]),
        color="0.25",
        va="center",
        ha="right",
        size="small",
        family="Source Code Pro",
        weight=400,
    )
    y += 1.65
y += 1


# -----------------------------------------------------------------------------
weights = {
    "ultralight": 100,
    "light": 200,
    "normal": 400,
    "regular": 400,
    "book": 400,
    "medium": 500,
    "roman": 500,
    "semibold": 600,
    "demibold": 600,
    "demi": 600,
    "bold": 700,
    "heavy": 800,
    "extra bold": 800,
    "black": 900,
}

text = "The quick brown fox jumps over the lazy dog"
for i, weight in enumerate(["ultralight", "normal", "semibold", "bold", "black"]):
    ax.text(1, y, text, size=9, va="center", family="Source Sans Pro", weight=weight)

    ax.text(
        39,
        y,
        "%s (%d)" % (weight, weights[weight]),
        color="0.25",
        va="center",
        ha="right",
        size="small",
        family="Source Code Pro",
        weight=400,
    )
    y += 1.65
y += 1

# -----------------------------------------------------------------------------
sizes = {
    "xx-small": 0.579,
    "x-small": 0.694,
    "small": 0.833,
    "medium": 1.0,
    "large": 1.200,
    "x-large": 1.440,
    "xx-large": 1.728,
}

text = "The quick brown fox"
for i, size in enumerate(sizes.keys()):
    ax.text(
        1,
        y,
        text,
        size=size,
        ha="left",
        va="center",
        family="Source Sans Pro",
        weight="light",
    )

    ax.text(
        39,
        y,
        "%s (%.2f)" % (size, sizes[size]),
        color="0.25",
        va="center",
        ha="right",
        size="small",
        family="Source Code Pro",
        weight=400,
    )
    y += 1.65 * max(sizes[size], sizes["small"])


plt.savefig("reference-font.pdf", dpi=600)
plt.show()
