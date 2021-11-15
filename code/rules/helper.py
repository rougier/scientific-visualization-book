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


def disc(shape=(1024, 1024), center=(512, 512), radius=512):
    """ Generate a numpy array containing a disc. """

    def distance(x, y):
        return (x - center[0]) ** 2 + (y - center[1]) ** 2

    D = np.fromfunction(distance, shape)
    return np.where(D < radius * radius, 1.0, 0.0)


def gaussian(shape=(25, 25), width=0.5, center=0.0):
    """ Generate a gaussian of the form g(x) = height*exp(-(x-center)**2/width**2). """
    if type(shape) in [float, int]:
        shape = (shape,)
    if type(width) in [float, int]:
        width = (width,) * len(shape)
    if type(center) in [float, int]:
        center = (center,) * len(shape)
    grid = []
    for size in shape:
        grid.append(slice(0, size))
    C = np.mgrid[tuple(grid)]
    R = np.zeros(shape)
    for i, size in enumerate(shape):
        if shape[i] > 1:
            R += (((C[i] / float(size - 1)) * 2 - 1 - center[i]) / width[i]) ** 2
    return np.exp(-R / 2)


def stimulus(position, size, intensity):
    """
    Parameters
    ----------

    position : (rho,theta) (degrees)
    size :     float (degrees)
    intensity: float
    """

    x, y = cartesian(position[0] / 90.0, np.pi * position[1] / 180.0)
    Y, X = np.mgrid[0 : shape[0], 0 : shape[1]]
    X = X / float(shape[1])
    Y = 2 * Y / float(shape[0]) - 1
    R = (X - x) ** 2 + (Y - y) ** 2
    return np.exp(-0.5 * R / (size / 90.0))


def best_fft_shape(shape):
    """
    This function returns the best shape for computing a fft

    From fftw.org:
        FFTW is best at handling sizes of the form 2^a*3^b*5^c*7^d*11^e*13^f,
         where e+f is either 0 or 1,

    From http://www.netlib.org/fftpack/doc
        "the method is most efficient when n is a product of small primes."
        -> What is small ?
    """

    # fftpack (not sure of the base)
    base = [13, 11, 7, 5, 3, 2]
    # fftw
    # base = [13,11,7,5,3,2]

    def factorize(n):
        if n == 0:
            raise (RuntimeError, "Length n must be positive integer")
        elif n == 1:
            return [
                1,
            ]
        factors = []
        for b in base:
            while n % b == 0:
                n /= b
                factors.append(b)
        if n == 1:
            return factors
        return []

    def is_optimal(n):
        factors = factorize(n)
        # fftpack
        return len(factors) > 0
        # fftw
        # return len(factors) > 0 and factors[:2] not in [[13,13],[13,11],[11,11]]

    shape = np.atleast_1d(np.array(shape))
    for i in range(shape.size):
        while not is_optimal(shape[i]):
            shape[i] += 1
    return shape.astype(int)
