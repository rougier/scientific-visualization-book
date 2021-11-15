# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure(figsize=(7, 2))
ax = plt.subplot()

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
(line1,) = ax.plot(X, C, marker="o", markevery=[-1], markeredgecolor="white")
(line2,) = ax.plot(X, S, marker="o", markevery=[-1], markeredgecolor="white")
text = ax.text(0.01, 0.95, "Test", ha="left", va="top", transform=ax.transAxes)
ax.set_xticks([])
ax.set_yticks([])


def update(frame):
    line1.set_data(X[:frame], C[:frame])
    line2.set_data(X[:frame], S[:frame])
    text.set_text("Frame %d" % frame)
    if frame in [1, 32, 128, 255]:
        plt.savefig("../../figures/animation/sine-cosine-frame-%03d.pdf" % frame)
    return line1, line2, text


plt.tight_layout()
writer = animation.FFMpegWriter(fps=30)
anim = animation.FuncAnimation(fig, update, interval=10, frames=len(X))
from tqdm.autonotebook import tqdm

bar = tqdm(total=len(X))
anim.save(
    "../../figures/animation/sine-cosine.mp4",
    writer=writer,
    dpi=100,
    progress_callback=lambda i, n: bar.update(1),
)
bar.close()
