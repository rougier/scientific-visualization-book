# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import git
import numpy as np
import matplotlib

matplotlib.use("module://imgcat")
import matplotlib.pyplot as plt

from matplotlib.patches import Polygon
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


def calmap(ax, year, data, origin="upper", weekstart="sun"):
    ax.tick_params("x", length=0, labelsize="medium", which="major")
    ax.tick_params("y", length=0, labelsize="x-small", which="major")

    # Month borders
    xticks, labels = [], []

    start = datetime(year, 1, 1).weekday()

    _data = np.zeros(7 * 53) * np.nan
    _data[start : start + len(data)] = data
    data = _data.reshape(53, 7).T

    for month in range(1, 13):
        first = datetime(year, month, 1)
        last = first + relativedelta(months=1, days=-1)
        if origin == "lower":
            y0 = first.weekday()
            y1 = last.weekday()
            x0 = (int(first.strftime("%j")) + start - 1) // 7
            x1 = (int(last.strftime("%j")) + start - 1) // 7
            P = [
                (x0, y0),
                (x0, 7),
                (x1, 7),
                (x1, y1 + 1),
                (x1 + 1, y1 + 1),
                (x1 + 1, 0),
                (x0 + 1, 0),
                (x0 + 1, y0),
            ]
        else:
            y0 = 6 - first.weekday()
            y1 = 6 - last.weekday()
            x0 = (int(first.strftime("%j")) + start - 1) // 7
            x1 = (int(last.strftime("%j")) + start - 1) // 7
            P = [
                (x0, y0 + 1),
                (x0, 0),
                (x1, 0),
                (x1, y1),
                (x1 + 1, y1),
                (x1 + 1, 7),
                (x0 + 1, 7),
                (x0 + 1, y0 + 1),
            ]

        xticks.append(x0 + (x1 - x0 + 1) / 2)
        labels.append(first.strftime("%b"))
        poly = Polygon(
            P,
            edgecolor="black",
            facecolor="None",
            linewidth=1,
            zorder=20,
            clip_on=False,
        )
        ax.add_artist(poly)

    ax.set_xticks(xticks)
    ax.set_xticklabels(labels)
    ax.set_yticks(0.5 + np.arange(7))

    labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    if origin == "upper":
        labels = labels[::-1]
    ax.set_yticklabels(labels)

    ax.text(
        1.01,
        0.5,
        "{}".format(year),
        rotation=90,
        ha="left",
        va="center",
        transform=ax.transAxes,
        size="28",
        weight="bold",
        alpha=0.5,
    )

    # Showing data
    cmap = plt.cm.get_cmap("Purples")
    im = ax.imshow(
        data, extent=[0, 53, 0, 7], zorder=10, vmin=0, vmax=8, cmap=cmap, origin=origin
    )


def get_commits(year=2021, path="../.."):
    "Collect commit dates for a given year"

    n = 1 + (date(year, 12, 31) - date(year, 1, 1)).days
    C = np.zeros(n, dtype=int)
    repo = git.Repo(path)
    for commit in repo.iter_commits("master"):
        timestamp = datetime.fromtimestamp(commit.committed_date)
        if timestamp.year == year:
            day = timestamp.timetuple().tm_yday
            C[day - 1] += 1
    return C


for year in [2019, 2020, 2021]:
    fig = plt.figure(figsize=(10, 2), dpi=250, frameon=False)
    ax = plt.subplot(xticks=[], yticks=[], frameon=False)
    calmap(ax, year, get_commits(year), origin="upper", weekstart="sun")
    plt.tight_layout()
    fig.show()
