# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Circle, Rectangle
from matplotlib.collections import LineCollection


def line_intersect(p1, p2, P3, P4):

    p1 = np.atleast_2d(p1)
    p2 = np.atleast_2d(p2)
    P3 = np.atleast_2d(P3)
    P4 = np.atleast_2d(P4)

    x1, y1 = p1[:, 0], p1[:, 1]
    x2, y2 = p2[:, 0], p2[:, 1]
    X3, Y3 = P3[:, 0], P3[:, 1]
    X4, Y4 = P4[:, 0], P4[:, 1]

    D = (Y4 - Y3) * (x2 - x1) - (X4 - X3) * (y2 - y1)

    # Colinearity test
    C = D != 0
    UA = (X4 - X3) * (y1 - Y3) - (Y4 - Y3) * (x1 - X3)
    UA = np.divide(UA, D, where=C)
    UB = (x2 - x1) * (y1 - Y3) - (y2 - y1) * (x1 - X3)
    UB = np.divide(UB, D, where=C)

    # Test if intersections are inside each segment
    C = C * (UA > 0) * (UA < 1) * (UB > 0) * (UB < 1)

    X = np.where(C, x1 + UA * (x2 - x1), np.inf)
    Y = np.where(C, y1 + UA * (y2 - y1), np.inf)
    return np.stack([X, Y], axis=1)


class Maze:
    """
    A simple 8-maze made of straight walls (line segments)
    """

    def __init__(self):
        self.walls = np.array(
            [
                # Surrounding walls
                [(0, 0), (0, 500)],
                [(0, 500), (300, 500)],
                [(300, 500), (300, 0)],
                [(300, 0), (0, 0)],
                # Bottom hole
                [(100, 100), (200, 100)],
                [(200, 100), (200, 200)],
                [(200, 200), (100, 200)],
                [(100, 200), (100, 100)],
                # Top hole
                [(100, 300), (200, 300)],
                [(200, 300), (200, 400)],
                [(200, 400), (100, 400)],
                [(100, 400), (100, 300)],
                # Moving walls (invisible) to constraint bot path
                [(0, 250), (100, 200)],
                [(200, 300), (300, 250)],
            ]
        )

    def draw(self, ax, grid=True, margin=5):
        """
        Render the maze
        """

        # Building a filled patch from walls
        V, C, S = [], [], self.walls
        V.extend(S[0 + i, 0] for i in [0, 1, 2, 3, 0])
        V.extend(S[4 + i, 0] for i in [0, 1, 2, 3, 0])
        V.extend(S[8 + i, 0] for i in [0, 1, 2, 3, 0])
        C = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY] * 3
        path = Path(V, C)
        patch = PathPatch(
            path, clip_on=False, linewidth=1.5, edgecolor="black", facecolor="white"
        )

        # Set figure limits, grid and ticks
        ax.set_axisbelow(True)
        ax.add_artist(patch)
        ax.set_xlim(0 - margin, 300 + margin)
        ax.set_ylim(0 - margin, 500 + margin)
        if grid:
            ax.xaxis.set_major_locator(MultipleLocator(100))
            ax.xaxis.set_minor_locator(MultipleLocator(10))
            ax.yaxis.set_major_locator(MultipleLocator(100))
            ax.yaxis.set_minor_locator(MultipleLocator(10))
            ax.grid(True, "major", color="0.75", linewidth=1.00, clip_on=False)
            ax.grid(True, "minor", color="0.75", linewidth=0.50, clip_on=False)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.tick_params(axis="both", which="major", size=0)
        ax.tick_params(axis="both", which="minor", size=0)


class Bot:
    def __init__(self):
        self.size = 10
        self.position = 150, 250
        self.orientation = 0
        self.n_sensors = 8
        A = np.linspace(-np.pi / 2, +np.pi / 2, self.n_sensors + 2, endpoint=True)[1:-1]
        self.sensors = {
            "angle": A,
            "range": 75 * np.ones((self.n_sensors, 1)),
            "value": np.ones((self.n_sensors, 1)),
        }

    def draw(self, ax):

        # Sensors
        n = 2 * len(self.sensors["angle"])
        sensors = LineCollection(
            np.zeros((n, 2, 2)),
            colors=["0.75", "0.00"] * n,
            linewidths=[0.75, 1.00] * n,
            linestyles=["--", "-"] * n,
        )
        # Body
        body = Circle(
            self.position,
            self.size,
            zorder=20,
            edgecolor="black",
            facecolor=(1, 1, 1, 0.75),
        )

        # Head
        P = np.zeros((1, 2, 2))
        P[0, 0] = self.position
        P[0, 1] = P[0, 1] + self.size * np.array(
            [np.cos(self.orientation), np.sin(self.orientation)]
        )
        head = LineCollection(P, colors="black", zorder=30)

        # List of artists to be rendered (sensors, body, head)
        self.artists = [sensors, body, head]
        ax.add_collection(sensors)
        ax.add_artist(body)
        ax.add_artist(head)

    def update(self, maze):

        sensors, body, head = self.artists

        # Sensors
        verts = sensors.get_segments()
        linewidths = sensors.get_linewidth()
        A = self.sensors["angle"] + self.orientation
        T = np.stack([np.cos(A), np.sin(A)], axis=1)
        P1 = self.position + self.size * T
        P2 = P1 + self.sensors["range"] * T
        P3, P4 = maze.walls[:, 0], maze.walls[:, 1]
        for i, (p1, p2) in enumerate(zip(P1, P2)):
            verts[2 * i] = verts[2 * i + 1] = p1, p2
            linewidths[2 * i + 1] = 1
            C = line_intersect(p1, p2, P3, P4)
            index = np.argmin(((C - p1) ** 2).sum(axis=1))
            p = C[index]
            if p[0] < np.inf:
                verts[2 * i + 1] = p1, p
                self.sensors["value"][i] = np.sqrt(((p1 - p) ** 2).sum())
                self.sensors["value"][i] /= self.sensors["range"][i]
            else:
                self.sensors["value"][i] = 1
        sensors.set_verts(verts)
        sensors.set_linewidths(linewidths)

        # Body
        body.set_center(self.position)

        # Head
        P = np.zeros((1, 2, 2))
        P[0, 0] = self.position
        P[0, 1] = P[0, 0] + self.size * np.array(
            [np.cos(self.orientation), np.sin(self.orientation)]
        )
        head.set_verts(P)


# ------------------------------------------------------------------------------
if __name__ == "__main__":
    from matplotlib.gridspec import GridSpec
    import matplotlib.animation as animation

    maze = Maze()
    bot = Bot()
    bot.position = 150, 250
    bot.orientation = 0
    bot.sensors["range"][3:5] *= 1.25

    fig = plt.figure(figsize=(10, 5), frameon=False)
    G = GridSpec(8, 2, width_ratios=(1, 2))
    ax = plt.subplot(G[:, 0], aspect=1, frameon=False)

    # Maze + bot
    maze.draw(ax, grid=True, margin=15)
    bot.draw(ax)

    # Sensor plots
    plots = []
    P = np.zeros((500, 2))
    (trace,) = ax.plot([], [], color="0.5", zorder=10, linewidth=1, linestyle=":")
    for i in range(bot.n_sensors):
        ax = plt.subplot(G[i, 1])
        ax.set_xticks([]), ax.set_yticks([])
        ax.set_ylabel("Sensor %d" % (i + 1), fontsize="x-small")
        (plot,) = ax.plot([], [], linewidth=0.75)
        ax.set_xlim(0, 500)
        ax.set_ylim(0, 1.1)
        plots.append(plot)
    X = np.arange(500)
    Y = np.zeros((bot.n_sensors, 500))

    def update(frame):

        # Update bot position according to sensors
        dv = (bot.sensors["value"].ravel() * [-4.0, -3, -2, -1, 1, 2, 3, 4]).sum()
        if abs(dv) > 0.5:
            bot.orientation += 0.01 * dv
        bot.position += 2 * np.array([np.cos(bot.orientation), np.sin(bot.orientation)])
        bot.update(maze)

        # Alternate wall moving to bias bot behavior
        if bot.position[1] < 100:
            maze.walls[12:] = [[(0, 250), (100, 300)], [(200, 200), (300, 250)]]
        elif bot.position[1] > 400:
            maze.walls[12:] = [[(0, 250), (100, 200)], [(200, 300), (300, 250)]]

        # Sensor plots
        n = len(bot.sensors["angle"])
        if frame < 500:
            P[frame] = bot.position
            trace.set_xdata(P[:frame, 0])
            trace.set_ydata(P[:frame, 1])
            for i in range(n):
                Y[i, frame] = bot.sensors["value"][i]
                plots[i].set_ydata(Y[i, :frame])
                plots[i].set_xdata(X[:frame])
        else:
            P[:-1] = P[1:]
            P[-1] = bot.position
            trace.set_xdata(P[:, 0])
            trace.set_ydata(P[:, 1])
            Y[:, 0:-1] = Y[:, 1:]
            for i in range(n):
                Y[i, -1] = bot.sensors["value"][i]
                plots[i].set_ydata(Y[i])
                plots[i].set_xdata(X)

        return bot.artists, trace, plots

    anim = animation.FuncAnimation(fig, update, frames=100_000, interval=10)
    plt.tight_layout()

    # Animation saving
    if 0:
        fig.set_frameon(True)
        anim = animation.FuncAnimation(fig, update, frames=1000, interval=10)
        import tqdm

        writer = animation.FFMpegWriter(fps=30)
        print("Encoding animation (maze.mp4")
        bar = tqdm.tqdm(total=1000)
        anim.save(
            "maze.mp4",
            writer=writer,
            dpi=100,
            progress_callback=lambda i, n: bar.update(1),
        )
        bar.close()
        fig.set_frameon(False)

    plt.show()
