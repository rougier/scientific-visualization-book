import numpy as np
import matplotlib.pyplot as plt


def style(index, e=0.001):
    patterns = [
        ("densely dotted", (-0.5, (e, 2 - e))),
        ("dotted", (-0.5, (e, 3 - e))),
        ("loosely dotted", (-0.5, (e, 5 - e))),
        ("densely dashed", (-0.5, (2, 3))),
        ("dashed", (-0.5, (2, 4))),
        ("loosely dashed", (-0.5, (2, 7))),
        ("densely dashdotted", (-0.5, (2, 2, e, 2 - e))),
        ("dashdotted", (-0.5, (2, 3, e, 2 - e))),
        ("loosely dashdotted", (-0.5, (2, 5, e, 5 - e))),
        ("densely dashdotdotted", (-0.5, (2, 2, e, 2 - e, e, 2 - e))),
        ("dashdotdotted", (-0.5, (2, 3, e, 3 - e, e, 3 - e))),
        ("loosely dashdotdotted", (-0.5, (2, 5, e, 5 - e, e, 5 - e))),
    ]
    return patterns[index]


fig = plt.figure(figsize=(4.25, 1.5))
ax = fig.add_axes(
    [0, 0, 1, 1],
    xlim=[-1, 23],
    ylim=[-1, 7],
    frameon=False,
    xticks=[],
    yticks=[],
    aspect=1,
)

for i in range(4):
    for j in range(3):
        name, pattern = style(i * 3 + j)
        X = np.array([j * 8, j * 8 + 6])
        Y = np.array([i * 2, i * 2])
        plt.plot(
            X,
            Y + 0.25,
            color="0.4",
            linewidth=2.0,
            dash_capstyle="projecting",
            linestyle=pattern,
        )
        plt.plot(
            X, Y, color="0.3", linewidth=2.0, dash_capstyle="round", linestyle=pattern
        )
        plt.text(j * 8 + 3, i * 2 - 0.5, name, ha="center", va="top", size="x-small")

        # Because of butt capstlye, we have to modify patterns a bit
        name, pattern = style(i * 3 + j, e=0.25)
        plt.plot(
            X,
            Y + 0.5,
            color="0.5",
            linewidth=2.0,
            dash_capstyle="butt",
            linestyle=pattern,
        )

plt.savefig("tikz-dashes.pdf")
plt.show()


# # Line width
# # -----------------------------------------------------------------------------
# y = 18
# for i,linewidth in enumerate([1,2,3,4,5]):
#     X,Y = [.5+4.25*i, .5+4.25*i+3], [y,y]
#     plt.plot(X, Y, color="black", linewidth=linewidth,  solid_capstyle="round")
#     plt.text((X[0]+X[1])/2, y-.75, "%.1f" % linewidth,
#              size="x-small", ha="center", va="top")
# plt.text(0.5, y+0.75, "Line width", size="small", ha="left", va="bottom")

# # Solid cap style
# # -----------------------------------------------------------------------------
# y = 14
# for i,capstyle in enumerate(["butt", "round", "projecting"]):
#     X,Y = [.75+7*i, .75+7*i+5.5], [y,y]
#     plt.plot(X, Y, color=".85", linewidth=8,
#              solid_capstyle="projecting")
#     plt.plot(X, Y, color="black", linewidth=8,
#              solid_capstyle=capstyle)
#     plt.plot(X, Y, color="white", linewidth=1, marker="|", markersize=5.0)
#     plt.text((X[0]+X[1])/2, y-.75, capstyle,
#              size="x-small", ha="center", va="top")
# plt.text(0.5, y+0.75, "Solid cap style", size="small", ha="left", va="bottom")

# # Dash cap style
# # -----------------------------------------------------------------------------
# y = 10
# for i,capstyle in enumerate(["butt", "round", "projecting"]):
#     X,Y = [.75+7*i, .75+7*i+5.5], [y,y]
#     plt.plot(X, Y, color=".85", linewidth=8, linestyle="--",
#             solid_capstyle=capstyle, dash_capstyle="projecting")
#     plt.plot(X, Y, color="black", linewidth=8, linestyle="--",
#             solid_capstyle=capstyle, dash_capstyle=capstyle)
#     plt.text((X[0]+X[1])/2, y-.75, capstyle,
#              size="x-small", ha="center", va="top")
# plt.text(0.5, y+0.75, "Dash cap style", size="small", ha="left", va="bottom")


# # Dash style
# # -----------------------------------------------------------------------------
# y = 6
# for i,linestyle in enumerate(["-","--",":","-.", (0,(0.01,2))]):
#     X,Y = [.5+4.25*i, .5+4.25*i+3], [y,y]
#     plt.plot(X, Y, color="black", linewidth=2.0, linestyle=linestyle,
#              solid_capstyle="round", dash_capstyle="round")
#     if isinstance(linestyle,str):
#         plt.text((X[0]+X[1])/2, y-.75, '"%s"' % str(linestyle),
#                  size="x-small", ha="center", va="top", family="monospace")
#     else:
#         plt.text((X[0]+X[1])/2, y-.75, "(0,(0.01,2))",
#                  size="x-small", ha="center", va="top")
# plt.text(0.5, y+0.75, "Classic dash style", size="small", ha="left", va="bottom")


# # Color cycle
# # -----------------------------------------------------------------------------
# y = 2
# X = np.linspace(1,20,10)
# Y = np.ones(len(X))*y
# C = ["C%d" % i for i in range(10)]
# plt.scatter(X, Y, s=200, color=C)
# for x,c in zip(X,C):
#     plt.text(x, y-0.75, '"%s"' % c,
#              size="x-small", ha="center", va="top", family="monospace")
# plt.text(0.5, y+0.75, "Color cycle", size="small", ha="left", va="bottom")


# plt.tight_layout()
# plt.savefig("reference-lines.pdf", dpi=600)
# plt.show()
