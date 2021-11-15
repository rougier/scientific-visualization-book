# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
from fluid import Fluid, inflow
from scipy.special import erf
import matplotlib.pyplot as plt
import matplotlib.animation as animation

shape = 256, 256
duration = 500
fluid = Fluid(shape, "dye")
inflows = [inflow(fluid, x) for x in np.linspace(-np.pi, np.pi, 8, endpoint=False)]

# Animation setup
fig = plt.figure(figsize=(5, 5), dpi=100)
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1)
ax.set_xticks([])
ax.set_ylim(0, 1)
ax.set_yticks([])
im = ax.imshow(
    np.zeros(shape),
    extent=[0, 1, 0, 1],
    vmin=0,
    vmax=1,
    origin="lower",
    interpolation="bicubic",
    cmap=plt.cm.RdYlBu,
)

# Animation scenario
scenario = []
for i in range(8):
    scenario.extend([[i]] * 20)
scenario.extend([[0, 2, 4, 6]] * 30)
scenario.extend([[1, 3, 5, 7]] * 30)

# Animation update
def update(frame):
    for i in scenario[frame % len(scenario)]:
        inflow_velocity, inflow_dye = inflows[i]
        fluid.velocity += inflow_velocity
        fluid.dye += inflow_dye
    divergence, curl, pressure = fluid.step()
    Z = curl
    Z = (erf(Z * 2) + 1) / 4

    im.set_data(Z)
    im.set_clim(vmin=Z.min(), vmax=Z.max())

    text.set_text("Frame %d" % frame)
    if frame in [30, 60, 90, 120, 150, 180, 210, 240]:
        plt.savefig("../../figures/animation/fluid-animation-%03d.png" % frame, dpi=300)

    return im, text


text = ax.text(0.01, 0.99, "Test", ha="left", va="top", transform=ax.transAxes)
anim = animation.FuncAnimation(fig, update, interval=10, frames=duration)
plt.show()
