# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as patches
import matplotlib.patheffects as path_effects
from mpl_toolkits.axes_grid1 import make_axes_locatable


rows, cols = 2, 3
fig = plt.figure(figsize=(cols * 2, rows * 2.45))

for row in range(rows):
    for col in range(cols):
        index = row * cols + col + 1

        if index == cols * rows:
            ax = plt.subplot(rows, cols, index, aspect=1, frameon=False)
            ax.set_xticks([]), ax.set_yticks([])

            plt.rcParams.update(
                {"font.family": "sans-serif", "font.sans-serif": ["Helvetica"]}
            )

            ax.text(
                0,
                1.06,
                r"\begin{minipage}{4.3cm}\small "
                r"\textbf{Figure caption} "
                r"can be directly inserted from within matplotlib using the full \LaTeX~engine. To fit the axes, you can use a minipage and adjust its width to the axes. Of course, the width can be also computed automatically but from time to time it is ok to do it by trials and errors (I did). Fun part is that we could also include some tikz rendering inside the figure. "
                r"\end{minipage}\vspace{-5mm}",
                va="top",
                transform=ax.transAxes,
                clip_on=False,
                usetex=True,
            )
            continue

        ax = plt.subplot(rows, cols, index, aspect=1, frameon=True)
        ax.tick_params(which="both", direction="in")
        ax.tick_params(which="both", right=True)
        ax.set_axisbelow(True)

        ax.set_xlim(0, 10)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1.00))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
        ax.set_xticklabels([])

        ax.set_ylim(0, 10)
        ax.yaxis.set_major_locator(ticker.MultipleLocator(1.00))
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))
        ax.set_yticklabels([])

        ax.grid(color=".9", linestyle="--")

        n = 50
        x0, y0 = np.random.uniform(2, 8, 2)
        s = np.random.uniform(0.5, 2.0)
        X = np.random.normal(x0, s, n)
        Y = np.random.normal(y0, s, n)
        S = np.random.uniform(100, 200, n)
        ax.scatter(X, Y, alpha=0.5, facecolor="C0", edgecolor="None")

        Xm, Ym = X.mean(), Y.mean()
        ax.axvline(Xm, linewidth=0.5, color="black")
        text = ax.text(
            Xm,
            9.5,
            "%.1f" % Xm,
            transform=ax.transData,
            size=7,
            rotation=90,
            ha="center",
            va="top",
        )
        text.set_path_effects(
            [
                path_effects.Stroke(linewidth=2, foreground="white"),
                path_effects.Normal(),
            ]
        )

        ax.axhline(Ym, linewidth=0.5, color="black")
        text = ax.text(
            9.5,
            Ym,
            "%.1f" % Ym,
            transform=ax.transData,
            size=7,
            rotation=0,
            ha="right",
            va="center",
        )
        text.set_path_effects(
            [
                path_effects.Stroke(linewidth=2, foreground="white"),
                path_effects.Normal(),
            ]
        )

        ax.scatter([Xm], [Ym], s=10, facecolor="black", edgecolor="None")

        divider = make_axes_locatable(ax)
        cax = divider.append_axes("top", size="15%", pad=0)
        cax.get_xaxis().set_visible(False)
        cax.get_yaxis().set_visible(False)
        cax.set_facecolor("black")
        cax.text(
            0.05,
            0.45,
            "SESSION %2d" % index,
            size=10,
            color="white",
            ha="left",
            va="center",
        )
        cax.text(
            0.95,
            0.45,
            "σ=%.1f" % s,
            size=10,
            color="white",
            ha="right",
            va="center",
            weight="bold",
        )

plt.tight_layout()
plt.savefig("../../figures/ornaments/latex-text-box.png", dpi=600)
plt.show()
