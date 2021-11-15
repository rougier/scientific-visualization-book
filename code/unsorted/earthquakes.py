# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import urllib
import numpy as np
import cartopy
import matplotlib.pyplot as plt
from datetime import datetime


# -> http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php
feed = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/"

# Significant earthquakes in the past 30 days
# url = urllib.request.urlopen(feed + "significant_month.csv")

# Earthquakes of magnitude > 4.5 in the past 30 days
url = urllib.request.urlopen(feed + "4.5_month.csv")

# Earthquakes of magnitude > 2.5 in the past 30 days
# url = urllib.request.urlopen(feed + "2.5_month.csv")

# Earthquakes of magnitude > 1.0 in the past 30 days
# url = urllib.request.urlopen(feed + "1.0_month.csv")

# Read data
data = (url.read().decode()).split("\n")
E = np.genfromtxt(
    data, delimiter=",", names=True, usecols=("latitude", "longitude", "mag")
)
X, Y, M = E["longitude"], E["latitude"], E["mag"]
M = 25 * (M - 4) ** 3

# Plot data
fig = plt.figure(figsize=(8, 6))
ax = plt.subplot(1, 1, 1, projection=cartopy.crs.EqualEarth())
ax.set_global()

ax.add_feature(cartopy.feature.OCEAN, zorder=0, facecolor="blue", alpha=0.1)
ax.add_feature(
    cartopy.feature.LAND, zorder=0, facecolor="white", edgecolor="0.25", linewidth=0.5
)

# Visual effect for a more salient information
ax.scatter(
    X, Y, M, lw=1, ec="black", alpha=1, zorder=10, transform=cartopy.crs.PlateCarree()
)
ax.scatter(
    X,
    Y,
    M - 1,
    ec="none",
    fc="white",
    alpha=1,
    zorder=20,
    transform=cartopy.crs.PlateCarree(),
)
ax.scatter(
    X,
    Y,
    M - 1,
    ec="none",
    fc="red",
    alpha=0.25,
    zorder=20,
    transform=cartopy.crs.PlateCarree(),
)
ax.scatter(
    X,
    Y,
    2,
    ec="none",
    fc="black",
    alpha=1,
    zorder=30,
    transform=cartopy.crs.PlateCarree(),
)

# Title & subtitles
ax.text(
    0.5,
    1.01,
    "Earthquakes with magnitude > 4.5 in the past 30 days",
    va="bottom",
    ha="center",
    transform=ax.transAxes,
    family="Source Serif Pro",
    size=12,
    weight=600,
)
ax.text(
    0.5,
    -0.01,
    datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    + " - data from http://earthquake.usgs.gov",
    va="top",
    ha="center",
    transform=ax.transAxes,
    family="Source Serif Pro",
    size=12,
    weight=400,
)

plt.tight_layout()
plt.savefig("earthquakes.pdf", dpi=600)
plt.show()
