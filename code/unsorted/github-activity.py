# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import os
import numpy as np
import html.parser
import urllib.request
import dateutil.parser
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def github_contrib(user, year):
    """ Get GitHub user daily contribution """

    # Check for a cached version (file)
    filename = "github-{0}-{1}.html".format(user, year)
    if os.path.exists(filename):
        with open(filename) as file:
            contents = file.read()
    # Else get file from GitHub
    else:
        url = "https://github.com/users/{0}/contributions?to={1}-12-31"
        url = url.format(user, year)
        contents = str(urllib.request.urlopen(url).read())
        with open(filename, "w") as file:
            file.write(contents)

    # Parse result (html)
    n = 1 + (date(year, 12, 31) - date(year, 1, 1)).days
    C = -np.ones(n, dtype=int)

    class HTMLParser(html.parser.HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == "rect":
                data = {key: value for (key, value) in attrs}
                date = dateutil.parser.parse(data["data-date"])
                count = int(data["data-count"])
                day = date.timetuple().tm_yday - 1
                if count > 0:
                    C[day] = count

    parser = HTMLParser()
    parser.feed(contents)
    return C


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
    ax.set_title("{}".format(year), size="medium", weight="bold")

    # Showing data
    cmap = plt.cm.get_cmap("Purples")
    ax.imshow(
        data, extent=[0, 53, 0, 7], zorder=10, vmin=0, vmax=10, cmap=cmap, origin=origin
    )


fig = plt.figure(figsize=(8, 7.5), dpi=100)
year = 2014
n = 5
for i in range(n):
    ax = plt.subplot(n, 1, i + 1, xlim=[0, 53], ylim=[0, 7], frameon=False, aspect=1)
    calmap(ax, year + i, github_contrib("rougier", year + i), origin="upper")

plt.tight_layout()

# plt.savefig("github-activity.png", dpi=300)
# plt.savefig("github-activity.pdf", dpi=600)
plt.show()
