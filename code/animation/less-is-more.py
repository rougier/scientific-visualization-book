# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
# Usage:
# $ for i in `seq 1 35`; do echo $i; python less-is-more.py $i; done
# $ cp frame-35.png frame-36.png
# $ cp frame-35.png frame-37.png
# $ cp frame-35.png frame-38.png
# $ cp frame-35.png frame-39.png
# $ cp frame-35.png frame-40.png
# $ convert -delay 100 *.png less-is-more.gif

import re
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.artist import Artist


def smooth1d(x, window_len):
    s = np.r_[2 * x[0] - x[window_len:1:-1], x, 2 * x[-1] - x[-1:-window_len:-1]]
    w = np.hanning(window_len)
    y = np.convolve(w / w.sum(), s, mode="same")
    return y[window_len - 1 : -window_len + 1]


def smooth2d(A, sigma=3):
    window_len = max(int(sigma), 3) * 2 + 1
    A1 = np.array([smooth1d(x, window_len) for x in np.asarray(A)])
    A2 = np.transpose(A1)
    A3 = np.array([smooth1d(x, window_len) for x in A2])
    A4 = np.transpose(A3)
    return A4


class BaseFilter(object):
    def prepare_image(self, src_image, dpi, pad):
        ny, nx, depth = src_image.shape
        padded_src = np.zeros([pad * 2 + ny, pad * 2 + nx, depth], dtype="d")
        padded_src[pad:-pad, pad:-pad, :] = src_image[:, :, :]
        return padded_src

    def get_pad(self, dpi):
        return 0

    def __call__(self, im, dpi):
        pad = self.get_pad(dpi)
        padded_src = self.prepare_image(im, dpi, pad)
        tgt_image = self.process_image(padded_src, dpi)
        return tgt_image, -pad, -pad


class OffsetFilter(BaseFilter):
    def __init__(self, offsets=None):
        if offsets is None:
            self.offsets = (0, 0)
        else:
            self.offsets = offsets

    def get_pad(self, dpi):
        return int(max(*self.offsets) / 72.0 * dpi)

    def process_image(self, padded_src, dpi):
        ox, oy = self.offsets
        a1 = np.roll(padded_src, int(ox / 72.0 * dpi), axis=1)
        a2 = np.roll(a1, -int(oy / 72.0 * dpi), axis=0)
        return a2


class GaussianFilter(BaseFilter):
    def __init__(self, sigma, alpha=0.5, color=None):
        self.sigma = sigma
        self.alpha = alpha
        if color is None:
            self.color = (0, 0, 0)
        else:
            self.color = color

    def get_pad(self, dpi):
        return int(self.sigma * 3 / 72.0 * dpi)

    def process_image(self, padded_src, dpi):
        tgt_image = np.zeros_like(padded_src)
        aa = smooth2d(padded_src[:, :, -1] * self.alpha, self.sigma / 72.0 * dpi)
        tgt_image[:, :, -1] = aa
        tgt_image[:, :, :-1] = self.color
        return tgt_image


class DropShadowFilter(BaseFilter):
    def __init__(self, sigma, alpha=0.3, color=None, offsets=None):
        self.gauss_filter = GaussianFilter(sigma, alpha, color)
        self.offset_filter = OffsetFilter(offsets)

    def get_pad(self, dpi):
        return max(self.gauss_filter.get_pad(dpi), self.offset_filter.get_pad(dpi))

    def process_image(self, padded_src, dpi):
        t1 = self.gauss_filter.process_image(padded_src, dpi)
        t2 = self.offset_filter.process_image(t1, dpi)
        return t2


class FilteredArtistList(Artist):
    def __init__(self, artist_list, filter):
        self._artist_list = artist_list
        self._filter = filter
        Artist.__init__(self)

    def draw(self, renderer):
        renderer.start_rasterizing()
        renderer.start_filter()
        for a in self._artist_list:
            a.draw(renderer)
        renderer.stop_filter(self._filter)
        renderer.stop_rasterizing()


# -----------------------------------------------------------------------------
class RangeDict(dict):
    def __getitem__(self, item):
        if type(item) != range:
            for key in self:
                if item in key:
                    return self[key]
        else:
            return super().__getitem__(item)


_ax1_title = RangeDict(
    {
        range(1, 2): "Less is More",
        range(2, 5): "Remove Backgrounds",
        range(5, 10): "Remove redundant labels",
        range(10, 14): "Remove borders",
        range(14, 16): "Reduce colors",
        range(16, 19): "Remove special effects",
        range(19, 22): "Remove bolding",
        range(22, 25): "Lighten labels",
        range(25, 29): "Ligthen lines",
        range(29, 33): "Or remove lines",
        range(33, 35): "Direct label",
        range(35, 36): "Less is More",
    }
)
_bar_facecolors = RangeDict(
    {
        range(1, 15): ["#22befc", "#1dB95d", "#ca5a56", "#8b6eaa", "#fcfc38"],
        range(15, 36): ["#b2b2b2", "#b2b2b2", "#cb5958", "#b2b2b2", "#b2b2b2"],
    }
)
_bar_edgecolor = RangeDict({range(1, 13): "#000000", range(13, 36): "None"})
_bar_shadows = RangeDict({range(1, 18): True, range(18, 36): False})
_xticklabels = RangeDict(
    {
        range(1, 36): [
            "French\nFries",
            "Potato\nChips",
            "Bacon\n",
            "Pizza\n",
            "Chili Dog\n",
        ]
    }
)
_xticklines_color = RangeDict(
    {range(1, 27): "#000000", range(27, 31): "#b2b2b2", range(34, 36): "None"}
)
_yticklabels = RangeDict(
    {
        range(1, 34): ["0", "100", "200", "300", "400", "500", "600", "700"],
        range(34, 36): ["", "", "", "", "", "", "", ""],
    }
)
_yticklabels_weight = RangeDict({range(1, 21): "bold", range(21, 36): "normal"})
_yticklabels_color = RangeDict(
    {range(1, 24): "#000000", range(24, 34): "#b2b2b2", range(34, 36): "None"}
)
_yticklines_color = RangeDict(
    {range(1, 28): "#000000", range(28, 34): "#b2b2b2", range(34, 36): "None"}
)
_grid_color = RangeDict(
    {range(1, 26): "#000000", range(26, 30): "#b2b2b2", range(30, 36): "None"}
)
_ax3_title = RangeDict(
    {
        range(1, 7): "Calories per 100g for different foods",
        range(7, 36): "Calories per 100g",
    }
)
_ax3_title_weight = RangeDict({range(1, 20): "bold", range(20, 36): "normal"})
_ax3_title_color = RangeDict({range(1, 23): "#000000", range(23, 36): "#b2b2b2"})
_xlabel = RangeDict({range(1, 9): "Type of Food", range(9, 36): ""})
_ylabel = RangeDict({range(1, 8): "Number of Calories", range(8, 36): ""})
_ax2_background = RangeDict({range(1, 3): True, range(3, 36): False})
_ax3_background = RangeDict({range(1, 4): True, range(4, 36): False})
_legend = RangeDict({range(1, 6): True, range(6, 36): False})
_ax2_spines_linewidth = RangeDict(
    {range(1, 11): (2, 2, 2, 2), range(11, 36): (0, 0, 0, 0)}
)
_ax3_spines_linewidth = RangeDict(
    {
        range(1, 12): (2, 2, 2, 2),
        range(12, 31): (0, 0.75, 0.75, 0),
        range(31, 32): (0, 0, 0.75, 0),
        range(32, 36): (0, 0, 0, 0),
    }
)
_ax3_spines_color = RangeDict(
    {
        range(1, 27): ("k", "k", "k", "k"),
        range(27, 28): ("k", "#b2b2b2", "k", "k"),
        range(28, 36): ("k", "#b2b2b2", "#b2b2b2", "k"),
    }
)
_direct_label = RangeDict({range(1, 35): False, range(35, 36): True})


if len(sys.argv) > 1:
    frame = int(sys.argv[1])
else:
    frame = 1
frame = max(min(frame, 36), 1)


dpi = 100
width, height = 640, 460
values = [607, 542, 533, 296, 260]

facecolors = _bar_facecolors[frame]
edgecolor = _bar_edgecolor[frame]
labels = _xticklabels[frame]
shadow = _bar_shadows[frame]
legend = _legend[frame]
ax3_background = _ax3_background[frame]
ax2_background = _ax2_background[frame]
ax2_spines_linewidth = _ax2_spines_linewidth[frame]
ax3_spines_linewidth = _ax3_spines_linewidth[frame]
ax3_spines_color = _ax3_spines_color[frame]
ax1_title = _ax1_title[frame]
ax3_title = _ax3_title[frame]
ax3_title_weight = _ax3_title_weight[frame]
ax3_title_color = _ax3_title_color[frame]
xlabel = _xlabel[frame]
ylabel = _ylabel[frame]
grid_color = _grid_color[frame]
yticklabels = _yticklabels[frame]
yticklabels_weight = _yticklabels_weight[frame]
yticklabels_color = _yticklabels_color[frame]
yticklines_color = _yticklines_color[frame]
xticklines_color = _xticklines_color[frame]
direct_label = _direct_label[frame]


fig = plt.figure(figsize=(width / dpi, height / dpi), dpi=dpi)

ax1 = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False)
ax1.text(
    0.05,
    0.05,
    "A remake of www.darkhorseanalytics.com",
    ha="left",
    va="top",
    family="Source Sans Pro",
    weight="light",
)
ax1.text(
    0.95, 0.05, "Made with matplotlib", ha="right", va="top", family="Source Sans Pro"
)

x, y = 0.050, 0.075
w, h = 1 - 2 * x, 1 - 2 * y - 0.1
ax2 = fig.add_axes([x, y, w, h])
ax2.set_xticks([])
ax2.set_yticks([])

x, y = 0.165, 0.25
w, h = 0.585, 0.45
ax3 = fig.add_axes([x, y, w, h])
ax3.set_ylim(0, 701)
ax3.set_yticks(range(0, 701, 100))
ax3.set_xlim(0, 10)
ax3.tick_params("x", length=0, which="major", pad=12.5)


# -----------------------------------------------------------------------------
ax1.text(
    0.05,
    0.95,
    ax1_title,
    ha="left",
    va="top",
    family="Source Sans Pro",
    fontsize=32,
    weight="light",
)


# -----------------------------------------------------------------------------
if ax2_background:
    ax2.imshow(mpimg.imread("texture.jpg"))
for linewidth, axis in zip(ax2_spines_linewidth, ["top", "bottom", "left", "right"]):
    ax2.spines[axis].set_linewidth(linewidth)

# -----------------------------------------------------------------------------
if ax3_background:
    ax3.set_facecolor(".75")

for color, linewidth, axis in zip(
    ax3_spines_color, ax3_spines_linewidth, ["top", "bottom", "left", "right"]
):
    ax3.spines[axis].set_linewidth(linewidth)
    ax3.spines[axis].set_color(color)

ax3.set_xticks(range(1, 10, 2))
ax3.set_xticklabels(labels)
if ax3_spines_linewidth[1] > 0:
    locator = matplotlib.ticker.FixedLocator(range(0, 10, 2))
    ax3.xaxis.set_minor_locator(locator)
    ax3.tick_params("x", length=3.5, width=0.8, which="minor", color=xticklines_color)


for label in ax3.get_yticklabels():
    label.set_fontweight(yticklabels_weight)
    label.set_color(yticklabels_color)
ax3.tick_params(axis="y", color=yticklines_color)


ax3.set_xlabel(xlabel, weight="bold")
ax3.set_ylabel(ylabel, weight="bold")

ax3.set_title(
    ax3_title, weight=ax3_title_weight, size=12, loc="left", color=ax3_title_color
)

plt.grid(axis="y", color=grid_color)

X, Y = range(1, 10, 2), values
bars = ax3.bar(X, Y, 0.8, facecolor="w", edgecolor="k", linewidth=1.5, zorder=10)
for bar, color in zip(bars, facecolors):
    bar.set_facecolor(color)
    bar.set_edgecolor(edgecolor)
if direct_label:
    for x, y in zip(X, Y):
        ax3.text(
            x,
            y - 25,
            "%d" % y,
            ha="center",
            va="top",
            color="white",
            zorder=20,
            transform=ax3.transData,
            fontsize=9,
        )

if shadow:
    gauss = DropShadowFilter(5, alpha=0.65, offsets=(3, 1))
    shadow = FilteredArtistList(bars, gauss)
    ax3.add_artist(shadow)
    shadow.set_zorder(bars[0].get_zorder() - 0.1)

if legend:
    ax3.legend(bars, labels, edgecolor="k", loc="center left", bbox_to_anchor=(1, 0.65))

plt.savefig("frame-%02d.png" % frame, dpi=dpi)
# plt.show()
