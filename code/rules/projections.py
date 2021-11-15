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
import os
import numpy as np
from parameters import *


def cartesian_to_polar(x, y):
    """ Cartesian to polar coordinates. """

    rho = np.sqrt(x ** 2 + y ** 2)
    theta = np.arctan2(y, x)
    return rho, theta


def polar_to_cartesian(rho, theta):
    """ Polar to cartesian coordinates. """

    x = rho * np.cos(theta)
    y = rho * np.sin(theta)
    return x, y


def polar_to_logpolar(rho, theta):
    """ Polar to logpolar coordinates. """

    # Shift in the SC mapping function in deg
    A = 3.0
    # Collicular magnification along u axe in mm/rad
    Bx = 1.4
    # Collicular magnification along v axe in mm/rad
    By = 1.8
    xmin, xmax = 0.0, 4.80743279742
    ymin, ymax = -2.76745559565, 2.76745559565
    rho = rho * 90.0
    x = Bx * np.log(np.sqrt(rho * rho + 2 * A * rho * np.cos(theta) + A * A) / A)
    y = By * np.arctan(rho * np.sin(theta) / (rho * np.cos(theta) + A))
    x = (x - xmin) / (xmax - xmin)
    y = (y - ymin) / (ymax - ymin)
    return x, y


def retina_projection(Rs=retina_shape, Ps=projection_shape):
    """
    Compute the projection indices from retina to colliculus

    Parameters
    ----------

    Rs : (int,int)
        Half-retina shape

    Ps : (int,int)
        Retina projection shape (might be different from colliculus)
    """

    filename = "retina (%d,%d) - colliculus (%d,%d).npy" % (Rs[0], Rs[1], Ps[0], Ps[1])
    if os.path.exists(filename):
        return np.load(filename)

    s = 4
    rho = (np.logspace(start=0, stop=1, num=s * Rs[1], base=10) - 1) / 9.0
    theta = np.linspace(start=-np.pi / 2, stop=np.pi / 2, num=s * Rs[0])

    rho = rho.reshape((s * Rs[1], 1))
    rho = np.repeat(rho, s * Rs[0], axis=1)

    theta = theta.reshape((1, s * Rs[0]))
    theta = np.repeat(theta, s * Rs[1], axis=0)

    y, x = polar_to_cartesian(rho, theta)

    xmin, xmax = x.min(), x.max()
    x = (x - xmin) / (xmax - xmin)

    ymin, ymax = y.min(), y.max()
    y = (y - ymin) / (ymax - ymin)

    P = np.zeros((Ps[0], Ps[1], 2), dtype=int)
    xi = np.rint(x * (Rs[0] - 1)).astype(int)
    yi = np.rint((0.0 + 1.0 * y) * (Rs[1] - 1)).astype(int)

    yc, xc = polar_to_logpolar(rho, theta)
    xmin, xmax = xc.min(), xc.max()
    xc = (xc - xmin) / (xmax - xmin)
    ymin, ymax = yc.min(), yc.max()
    yc = (yc - ymin) / (ymax - ymin)
    xc = np.rint(xc * (Ps[0] - 1)).astype(int)
    yc = np.rint((0.0 + yc * 1.0) * (Ps[1] - 1)).astype(int)

    P[xc, yc, 0] = xi
    P[xc, yc, 1] = yi
    np.save(filename, P)
    return P
