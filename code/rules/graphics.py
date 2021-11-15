# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright INRIA
# Contributors: Wahiba Taouali (Wahiba.Taouali@inria.fr)
#               Nicolas P. Rougier (Nicolas.Rougier@inria.fr)
#
# This software is governed by the CeCILL license under French law and abiding
# by the rules of distribution of free software. You can use, modify and/ or
# redistribute the software under the terms of the CeCILL license as circulated
# by CEA, CNRS and INRIA at the following URL
# http://www.cecill.info/index.en.html.
#
# As a counterpart to the access to the source code and rights to copy, modify
# and redistribute granted by the license, users are provided only with a
# limited warranty and the software's author, the holder of the economic
# rights, and the successive licensors have only limited liability.
#
# In this respect, the user's attention is drawn to the risks associated with
# loading, using, modifying and/or developing or reproducing the software by
# the user in light of its specific status of free software, that may mean that
# it is complicated to manipulate, and that also therefore means that it is
# reserved for developers and experienced professionals having in-depth
# computer knowledge. Users are therefore encouraged to load and test the
# software's suitability as regards their requirements in conditions enabling
# the security of their systems and/or data to be ensured and, more generally,
# to use and operate it in the same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes

from projections import *

# -----------------------------------------------------------------------------
def polar_frame(ax, title=None, legend=False, zoom=False, labels=True):
    """ Draw a polar frame """

    for rho in [0, 2, 5, 10, 20, 40, 60, 80, 90]:
        lw, color, alpha = 1, "0.00", 0.25
        if rho == 90 and not zoom:
            color, lw, alpha = "0.00", 2, 1

        n = 500
        R = np.ones(n) * rho / 90.0
        T = np.linspace(-np.pi / 2, np.pi / 2, n)
        X, Y = polar_to_cartesian(R, T)
        ax.plot(X, Y, color=color, lw=lw, alpha=alpha)

        if not zoom and rho in [0, 10, 20, 40, 80] and labels:
            ax.text(
                X[-1] * 1.0 - 0.075,
                Y[-1],
                u"%d°" % rho,
                color="k",  # size=15,
                horizontalalignment="center",
                verticalalignment="center",
            )

    for theta in [-90, -60, -30, 0, +30, +60, +90]:
        lw, color, alpha = 1, "0.00", 0.25
        if theta in [-90, +90] and not zoom:
            color, lw, alpha = "0.00", 2, 1
        angle = theta / 90.0 * np.pi / 2

        n = 500
        R = np.linspace(0, 1, n)
        T = np.ones(n) * angle
        X, Y = polar_to_cartesian(R, T)
        ax.plot(X, Y, color=color, lw=lw, alpha=alpha)

        if not zoom and theta in [-90, -60, -30, +30, +60, +90] and labels:
            ax.text(
                X[-1] * 1.05,
                Y[-1] * 1.05,
                u"%d°" % theta,
                color="k",  # size=15,
                horizontalalignment="left",
                verticalalignment="center",
            )
    d = 0.01
    ax.set_xlim(0.0 - d, 1.0 + d)
    ax.set_ylim(-1.0 - d, 1.0 + d)
    ax.set_xticks([])
    ax.set_yticks([])

    if legend:
        ax.set_frame_on(True)
        ax.spines["left"].set_color("none")
        ax.spines["right"].set_color("none")
        ax.spines["top"].set_color("none")
        ax.xaxis.set_ticks_position("bottom")
        ax.spines["bottom"].set_position(("data", -1.2))
        ax.set_xticks([])
        ax.text(
            0.0,
            -1.1,
            "$\longleftarrow$ Foveal",
            verticalalignment="top",
            horizontalalignment="left",
            size=12,
        )
        ax.text(
            1.0,
            -1.1,
            "Peripheral $\longrightarrow$",
            verticalalignment="top",
            horizontalalignment="right",
            size=12,
        )
    else:
        ax.set_frame_on(False)
    if title:
        ax.title(title)


# -----------------------------------------------------------------------------
def logpolar_frame(ax, title=None, legend=False, labels=True):
    """ Draw a log polar frame """

    for rho in [2, 5, 10, 20, 40, 60, 80, 90]:
        lw, color, alpha = 1, "0.00", 0.25
        if rho == 90:
            color, lw, alpha = "0.00", 2, 1

        n = 500
        R = np.ones(n) * rho / 90.0
        T = np.linspace(-np.pi / 2, np.pi / 2, n)
        X, Y = polar_to_logpolar(R, T)
        X, Y = X * 2, 2 * Y - 1
        ax.plot(X, Y, color=color, lw=lw, alpha=alpha)
        if labels and rho in [2, 5, 10, 20, 40, 80]:
            ax.text(
                X[-1],
                Y[-1] + 0.05,
                u"%d°" % rho,
                color="k",  # size=15,
                horizontalalignment="right",
                verticalalignment="bottom",
            )

    for theta in [-90, -60, -30, 0, +30, +60, +90]:
        lw, color, alpha = 1, "0.00", 0.25
        if theta in [-90, +90]:
            color, lw, alpha = "0.00", 2, 1
        angle = theta / 90.0 * np.pi / 2

        n = 500
        R = np.linspace(0, 1, n)
        T = np.ones(n) * angle
        X, Y = polar_to_logpolar(R, T)
        X, Y = X * 2, 2 * Y - 1
        ax.plot(X, Y, color=color, lw=lw, alpha=alpha)
        if labels:
            ax.text(
                X[-1] * 1.0 + 0.05,
                Y[-1] * 1.0,
                u"%d°" % theta,
                color="k",  # size=15,
                horizontalalignment="left",
                verticalalignment="center",
            )

    d = 0.01
    ax.set_xlim(0.0 - d, 2.0 + d)
    ax.set_ylim(-1.0 - d, 1.0 + d)
    ax.set_xticks([])
    ax.set_yticks([])
    if legend:
        ax.set_frame_on(True)
        ax.spines["left"].set_color("none")
        ax.spines["right"].set_color("none")
        ax.spines["top"].set_color("none")
        ax.xaxis.set_ticks_position("bottom")
        ax.spines["bottom"].set_position(("data", -1.2))
        ax.set_xticks([0, 2])
        ax.set_xticklabels(["0", "4.8 (mm)"])
        ax.text(
            0.0,
            -1.1,
            "$\longleftarrow$ Rostral",
            verticalalignment="top",
            horizontalalignment="left",
            size=12,
        )
        ax.text(
            2,
            -1.1,
            "Caudal $\longrightarrow$",
            verticalalignment="top",
            horizontalalignment="right",
            size=12,
        )
    else:
        ax.set_frame_on(False)
    if title:
        ax.title(title)


# -----------------------------------------------------------------------------
def polar_imshow(axis, Z, *args, **kwargs):
    kwargs["interpolation"] = kwargs.get("interpolation", "nearest")
    kwargs["cmap"] = kwargs.get("cmap", plt.cm.gray_r)
    # kwargs['vmin'] = kwargs.get('vmin', Z.min())
    # kwargs['vmax'] = kwargs.get('vmax', Z.max())
    kwargs["vmin"] = kwargs.get("vmin", 0)
    kwargs["vmax"] = kwargs.get("vmax", 1)
    kwargs["origin"] = kwargs.get("origin", "lower")
    axis.imshow(Z, extent=[0, 1, -1, 1], *args, **kwargs)


# -----------------------------------------------------------------------------
def logpolar_imshow(axis, Z, *args, **kwargs):
    kwargs["interpolation"] = kwargs.get("interpolation", "nearest")
    kwargs["cmap"] = kwargs.get("cmap", plt.cm.gray_r)
    # kwargs['vmin'] = kwargs.get('vmin', Z.min())
    # kwargs['vmax'] = kwargs.get('vmax', Z.max())
    kwargs["vmin"] = kwargs.get("vmin", 0)
    kwargs["vmax"] = kwargs.get("vmax", 1)
    kwargs["origin"] = kwargs.get("origin", "lower")
    im = axis.imshow(Z, extent=[0, 2, -1, 1], *args, **kwargs)
    # axins = inset_axes(axis, width='25%', height='5%', loc=3)
    # vmin, vmax = Z.min(), Z.max()
    # plt.colorbar(im, cax=axins, orientation='horizontal', ticks=[vmin,vmax], format = '%.2f')
    # axins.xaxis.set_ticks_position('bottom')
