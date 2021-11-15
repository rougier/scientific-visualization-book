# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import urllib
import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def rain_update(frame):
    global E, R, scatter

    current = frame % len(E)
    i = frame % len(R)

    R["color"][:, 3] = np.maximum(0, R["color"][:, 3] - 1 / len(R))
    R["size"] += R["growth"]

    i = frame % len(R)
    R["position"][i] = E["position"][current]
    R["size"][i] = 5
    R["growth"][i] = 0.1 * np.exp(E["magnitude"][current])
    R["color"][i, 3] = 1

    scatter.set_edgecolors(R["color"])
    scatter.set_sizes(R["size"].ravel())
    scatter.set_offsets(R["position"])

    if frame == 50:
        plt.savefig("../../figures/chapter-13/earthquakes-frame-50.pdf")

    return (scatter,)


# -> http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php
feed = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/"

# Magnitude > 4.5
url = urllib.request.urlopen(feed + "4.5_month.csv")

# Reading and storage of data
data = url.read().split(b"\n")[+1:-1]
E = np.zeros(len(data), dtype=[("position", float, (2,)), ("magnitude", float, (1,))])

for i in range(len(data)):
    row = data[i].split(b",")
    E["position"][i] = float(row[2]), float(row[1])
    E["magnitude"][i] = float(row[4])

fig = plt.figure(figsize=(10, 5), dpi=75)
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()
scatter = ax.scatter(
    [],
    [],
    s=[],
    transform=ccrs.PlateCarree(),
    linewidth=0.5,
    edgecolors=[],
    facecolors="None",
)

n = 50
R = np.zeros(
    n,
    dtype=[
        ("position", float, (2,)),
        ("size", float, (1,)),
        ("growth", float, (1,)),
        ("color", float, (4,)),
    ],
)
R["position"] = np.random.uniform(0, 1, (n, 2))
R["size"] = np.linspace(0, 1, n).reshape(n, 1)
R["color"][:, 3] = np.linspace(0, 1, n)

animation = animation.FuncAnimation(fig, rain_update, interval=10, frames=200)
plt.tight_layout()
plt.show()
