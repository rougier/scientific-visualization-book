# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import cartopy.crs

mpl.rcParams["font.serif"] = "Roboto Slab"
mpl.rcParams["font.size"] = 10
mpl.rcParams["font.weight"] = 400
mpl.rcParams["font.family"] = "serif"

dpi = 100
inch = 2.54
fig_width = 2 * 10.85 / inch
fig_height = fig_width * 1.25

fig = plt.figure(figsize=(fig_width, fig_height), dpi=dpi)

projections = [
    (cartopy.crs.Mercator(), "Mercator",),
    (cartopy.crs.PlateCarree(), "Plate Carree"),
    (cartopy.crs.LambertCylindrical(), "Lambert Cylindrical"),
    (cartopy.crs.Orthographic(), "Orthographic"),
    (cartopy.crs.Mollweide(), "Mollweide"),
    (cartopy.crs.EqualEarth(), "Equal Earth"),
    (cartopy.crs.LambertConformal(), "Lambert Conformal"),
    (cartopy.crs.EquidistantConic(), "Equidistant Conic"),
    (cartopy.crs.AlbersEqualArea(), "Albers Equal Area"),
    (
        cartopy.crs.NearsidePerspective(
            central_latitude=50.72, central_longitude=-3.53, satellite_height=10000000.0
        ),
        "Nearside Perspective",
    ),
    (cartopy.crs.NorthPolarStereo(), "North Polar Stereo"),
    (cartopy.crs.SouthPolarStereo(), "South Polar Stereo"),
]


for i, (projection, name) in enumerate(projections):
    ax = plt.subplot(4, 3, i + 1, projection=projection, frameon="False")
    ax.coastlines(resolution="110m", linewidth=0.5)
    ax.stock_img()
    ax.set_title(name, weight=400)

plt.savefig("../../figures/scales-projections/geo-projections.png", dpi=300)
plt.show()
