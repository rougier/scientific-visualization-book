# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, SymmetricalLogLocator


fig = plt.figure(figsize=(6, 6))
ax = plt.subplot(1, 1, 1, aspect=1, xlim=[0, 100], ylim=[0, 100])
P0, P1, P2, P3 = (0.1, 0.1), (1, 1), (10, 10), (100, 100)
transform = ax.transData.transform
print("Linear scale")
print(
    " -> distance({0:5.1f},{1:5.1f}) = {2:.2f}".format(
        P0[0], P1[0], abs((transform(P1) - transform(P0))[0])
    )
)
print(
    " -> distance({0:5.1f},{1:5.1f}) = {2:.2f}".format(
        P1[0], P2[0], abs((transform(P2) - transform(P1))[0])
    )
)
print(
    " -> distance({0:5.1f},{1:5.1f}) = {2:.2f}".format(
        P2[0], P3[0], abs((transform(P3) - transform(P2))[0])
    )
)
print()

fig = plt.figure(figsize=(6, 6))
ax = plt.subplot(1, 1, 1, aspect=1, xlim=[0.1, 100], ylim=[0.1, 100])
ax.set_xscale("log")
transform = ax.transData.transform

P0, P1, P2, P3 = (0.1, 0.1), (1, 1), (10, 10), (100, 100)
print("Log scale")
print(
    " -> distance({0:5.1f},{1:5.1f}) = {2:.2f}".format(
        P0[0], P1[0], abs((transform(P1) - transform(P0))[0])
    )
)
print(
    " -> distance({0:5.1f},{1:5.1f}) = {2:.2f}".format(
        P1[0], P2[0], abs((transform(P2) - transform(P1))[0])
    )
)
print(
    " -> distance({0:5.1f},{1:5.1f}) = {2:.2f}".format(
        P2[0], P3[0], abs((transform(P3) - transform(P2))[0])
    )
)
