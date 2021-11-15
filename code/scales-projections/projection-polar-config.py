# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


def polar(ax, r0, rmin, rmax, rticks, tmin, tmax, tticks):
    ax.set_yticks(np.linspace(rmin, rmax, rticks))
    ax.set_yticklabels([])
    ax.set_rorigin(r0)
    ax.set_rmin(rmin)
    ax.set_rmax(rmax)

    ax.set_xticks(np.linspace(np.pi * tmin / 180, np.pi * tmax / 180, tticks))
    ax.set_xticklabels([])
    ax.set_thetamin(tmin)
    ax.set_thetamax(tmax)

    text = r"""$r_{0}=%.2f,r_{min}=%.2f,r_{max}=%.2f$""" % (r0, rmin, rmax)
    text += "\n"
    text += r"""$t_{min}=%.2f,t_{max}=%.2f$""" % (tmin, tmax)

    plt.text(
        0.5, -0.15, text, size="small", ha="center", va="bottom", transform=ax.transAxes
    )


fig = plt.figure(figsize=(8, 4))

ax = fig.add_subplot(1, 3, 1, aspect=1, projection="polar")
polar(ax, 0.00, 0.00, 1.00, 4, 0, 360, 16)

ax = fig.add_subplot(1, 3, 2, aspect=1, projection="polar")
polar(ax, 0.00, 0.25, 1.00, 8, 0, 360, 32)

ax = fig.add_subplot(1, 3, 3, aspect=1, projection="polar")
polar(ax, 0.00, 0.50, 1.00, 10, 0, 90, 20)

plt.tight_layout()
plt.savefig("../../figures/scales-projections/projection-polar-config.pdf", dpi=600)
plt.show()
