# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
from matplotlib import colors
import matplotlib.pyplot as plt


def mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon=2.0):
    X = np.linspace(xmin, xmax, xn, dtype=np.float32)
    Y = np.linspace(ymin, ymax, yn, dtype=np.float32)
    C = X + Y[:, None] * 1j
    N = np.zeros(C.shape, dtype=int)
    Z = np.zeros(C.shape, np.complex64)
    for n in range(maxiter):
        I = np.less(abs(Z), horizon)
        N[I] = n
        Z[I] = Z[I] ** 2 + C[I]
    N[N == maxiter - 1] = 0
    return Z, N


xmin, xmax, xn = -2.75, +1.25, 4000
ymin, ymax, yn = -1.5, +1.5, 3000
maxiter = 200
horizon = 2.0 ** 40
log_horizon = np.log(np.log(horizon)) / np.log(2)
Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)

# Normalized recount as explained in:
# https://linas.org/art-gallery/escape/smooth.html
# https://www.ibm.com/developerworks/community/blogs/jfp/entry/My_Christmas_Gift
with np.errstate(invalid="ignore"):
    M = np.nan_to_num(N + 1 - np.log(np.log(abs(Z))) / np.log(2) + log_horizon)

width = 10
height = 10 * yn / xn
fig = plt.figure(figsize=(width, height), dpi=100)
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)

# Shaded rendering
light = colors.LightSource(azdeg=315, altdeg=10)
M = light.shade(
    M, cmap=plt.cm.hot, vert_exag=1.5, norm=colors.PowerNorm(0.3), blend_mode="hsv"
)
plt.imshow(M, extent=[xmin, xmax, ymin, ymax], interpolation="bicubic")
ax.set_xticks([])
ax.set_yticks([])
plt.savefig("mandelbrot.png", dpi=600)
plt.show()
