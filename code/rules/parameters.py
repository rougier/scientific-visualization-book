#!/usr/bin/env python
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

second = 1.0
millisecond = 0.001
dt = 5 * millisecond
duration = 10 * second
noise = 0.01

retina_shape = np.array([4096, 2048]).astype(int)
projection_shape = np.array([512, 512]).astype(int)
n = 128
colliculus_shape = np.array([n, n]).astype(int)

# Default stimulus
stimulus_size = 1.5  # in degrees
stimulus_intensity = 1.5

# DNF parameters (linear)
sigma_e = 0.10
A_e = 1.30
sigma_i = 1.00
A_i = 0.65
alpha = 12.5
tau = 10 * millisecond
scale = 40.0 * 40.0 / (n * n)
