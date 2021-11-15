# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import scipy.spatial
import matplotlib.pyplot as plt
import matplotlib.path as mpath
from shapely.geometry import Polygon
from matplotlib.collections import PolyCollection
from math import sqrt, ceil, floor, pi, cos, sin


def blue_noise(shape, radius, k=30, seed=None):
    """
    Generate blue noise over a two-dimensional rectangle of size (width,height)

    Parameters
    ----------

    shape : tuple
        Two-dimensional domain (width x height) 
    radius : float
        Minimum distance between samples
    k : int, optional
        Limit of samples to choose before rejection (typically k = 30)
    seed : int, optional
        If provided, this will set the random seed before generating noise,
        for valid pseudo-random comparisons.

    References
    ----------

    .. [1] Fast Poisson Disk Sampling in Arbitrary Dimensions, Robert Bridson,
           Siggraph, 2007. :DOI:`10.1145/1278780.1278807`
    """

    def sqdist(a, b):
        """ Squared Euclidean distance """
        dx, dy = a[0] - b[0], a[1] - b[1]
        return dx * dx + dy * dy

    def grid_coords(p):
        """ Return index of cell grid corresponding to p """
        return int(floor(p[0] / cellsize)), int(floor(p[1] / cellsize))

    def fits(p, radius):
        """ Check whether p can be added to the queue """

        radius2 = radius * radius
        gx, gy = grid_coords(p)
        for x in range(max(gx - 2, 0), min(gx + 3, grid_width)):
            for y in range(max(gy - 2, 0), min(gy + 3, grid_height)):
                g = grid[x + y * grid_width]
                if g is None:
                    continue
                if sqdist(p, g) <= radius2:
                    return False
        return True

    # When given a seed, we use a private random generator in order to not
    # disturb the default global random generator
    if seed is not None:
        from numpy.random.mtrand import RandomState

        rng = RandomState(seed=seed)
    else:
        rng = np.random

    width, height = shape
    cellsize = radius / sqrt(2)
    grid_width = int(ceil(width / cellsize))
    grid_height = int(ceil(height / cellsize))
    grid = [None] * (grid_width * grid_height)

    p = rng.uniform(0, shape, 2)
    queue = [p]
    grid_x, grid_y = grid_coords(p)
    grid[grid_x + grid_y * grid_width] = p

    while queue:
        qi = rng.randint(len(queue))
        qx, qy = queue[qi]
        queue[qi] = queue[-1]
        queue.pop()
        for _ in range(k):
            theta = rng.uniform(0, 2 * pi)
            r = radius * np.sqrt(rng.uniform(1, 4))
            p = qx + r * cos(theta), qy + r * sin(theta)
            if not (0 <= p[0] < width and 0 <= p[1] < height) or not fits(p, radius):
                continue
            queue.append(p)
            gx, gy = grid_coords(p)
            grid[gx + gy * grid_width] = p

    return np.array([p for p in grid if p is not None])


def bounded_voronoi(points):
    """
    Reconstruct infinite voronoi regions in a 2D diagram to finite regions.

    Parameters
    ----------
    vor : Voronoi
        Input diagram

    Returns
    -------
    regions : list of tuples
        Indices of vertices in each revised Voronoi regions.
    vertices : list of tuples
        Coordinates for revised Voronoi vertices. Same as coordinates
        of input vertices, with 'points at infinity' appended to the
        end.
    """

    vor = scipy.spatial.Voronoi(points)
    new_regions = []
    new_vertices = vor.vertices.tolist()
    center = vor.points.mean(axis=0)
    radius = vor.points.ptp().max() * 2

    # Construct a map containing all ridges for a given point
    all_ridges = {}
    for (p1, p2), (v1, v2) in zip(vor.ridge_points, vor.ridge_vertices):
        all_ridges.setdefault(p1, []).append((p2, v1, v2))
        all_ridges.setdefault(p2, []).append((p1, v1, v2))

    # Reconstruct infinite regions
    for p1, region in enumerate(vor.point_region):
        vertices = vor.regions[region]

        if all(v >= 0 for v in vertices):
            # finite region
            new_regions.append(vertices)
            continue

        # reconstruct a non-finite region
        ridges = all_ridges[p1]
        new_region = [v for v in vertices if v >= 0]

        for p2, v1, v2 in ridges:
            if v2 < 0:
                v1, v2 = v2, v1
            if v1 >= 0:
                # finite ridge: already in the region
                continue

            # Compute the missing endpoint of an infinite ridge
            t = vor.points[p2] - vor.points[p1]  # tangent
            t /= np.linalg.norm(t)
            n = np.array([-t[1], t[0]])  # normal

            midpoint = vor.points[[p1, p2]].mean(axis=0)
            direction = np.sign(np.dot(midpoint - center, n)) * n
            far_point = vor.vertices[v2] + direction * radius

            new_region.append(len(new_vertices))
            new_vertices.append(far_point.tolist())

        # sort region counterclockwise
        vs = np.asarray([new_vertices[v] for v in new_region])
        c = vs.mean(axis=0)
        angles = np.arctan2(vs[:, 1] - c[1], vs[:, 0] - c[0])
        new_region = np.array(new_region)[np.argsort(angles)]

        # finish
        new_regions.append(new_region.tolist())
    return new_regions, np.asarray(new_vertices)


def poly_random_points_safe(V, n=10):
    def random_point_inside_triangle(A, B, C):
        r1 = np.sqrt(np.random.uniform(0, 1))
        r2 = np.random.uniform(0, 1)
        return (1 - r1) * A + r1 * (1 - r2) * B + r1 * r2 * C

    def triangle_area(A, B, C):
        return 0.5 * np.abs(
            (B[0] - A[0]) * (C[1] - A[1]) - (C[0] - A[0]) * (B[1] - A[1])
        )

    C = V.mean(axis=0)
    T = [(C, V[i], V[i + 1]) for i in range(len(V) - 1)]
    A = np.array([triangle_area(*t) for t in T])
    A /= A.sum()

    points = [C]
    for i in np.random.choice(len(A), size=n - 1, p=A):
        points.append(random_point_inside_triangle(*T[i]))
    return points


def poly_random_points(V, n=10):
    path = mpath.Path(V)
    xmin, xmax = V[:, 0].min(), V[:, 0].max()
    ymin, ymax = V[:, 1].min(), V[:, 1].max()
    xscale, yscale = xmax - xmin, ymax - ymin
    if xscale > yscale:
        xscale, yscale = 1, yscale / xscale
    else:
        xscale, yscale = xscale / yscale, 1
    radius = 0.85 * np.sqrt(2 * xscale * yscale / (n * np.pi))
    points = blue_noise((xscale, yscale), radius)
    points = [xmin, ymin] + points * [xmax - xmin, ymax - ymin]
    inside = path.contains_points(points)

    P = points[inside]
    if len(P) < 5:
        return poly_random_points_safe(V, n)
    np.random.shuffle(P)
    return P[:n]


def voronoi(V, npoints, level, maxlevel, color=None):
    if level == maxlevel:
        return []

    linewidths = [1.50, 1.00, 0.75, 0.50, 0.25, 0.10]
    edgecolors = [
        (0, 0, 0, 1.00),
        (0, 0, 0, 0.50),
        (0, 0, 0, 0.25),
        (0, 0, 0, 0.10),
        (0, 0, 0, 0.10),
        (0, 0, 0, 0.10),
    ]

    if level == 1:
        color = np.random.uniform(0, 1, 4)
        color[3] = 0.5

    points = poly_random_points(V, npoints - level)
    regions, vertices = bounded_voronoi(points)
    clip = Polygon(V)
    cells = []
    for region in regions:
        polygon = Polygon(vertices[region]).intersection(clip)
        polygon = np.array([point for point in polygon.exterior.coords])
        linewidth = linewidths[level]
        edgecolor = edgecolors[level]
        facecolor = "none"
        if level > 1:
            alpha = color[3] + (1 / (level + 1)) * 0.25 * np.random.uniform(-1, 0.5)
            color = color[0], color[1], color[2], min(max(alpha, 0.1), 1)
        if level == maxlevel - 1:
            facecolor = color
        zorder = -level
        cells.append((polygon, linewidth, edgecolor, facecolor, zorder))
        cells.extend(voronoi(polygon, npoints, level + 1, maxlevel, color))
    return cells


np.random.seed(12345)
T = np.linspace(0, 2 * np.pi, 100, endpoint=False)
R = 100
X, Y = R * np.cos(T), R * np.sin(T)
V = np.c_[X, Y]

V = 100 * np.array([[-1, -1], [-1, 1], [1, 1], [1, -1]])

fig = plt.figure(figsize=(8, 8))
d = R - 1
ax = fig.add_axes([0, 0, 1, 1], aspect=1, xlim=[-d, d], ylim=[-d, d])
ax.axis("off")

cells = voronoi(V, 11, level=0, maxlevel=5)
zorder = [cell[-1] for cell in cells]
cells = [cells[i] for i in np.argsort(zorder)]
polygons = [cell[0] for cell in cells]
linewidths = [cell[1] for cell in cells]
edgecolors = [cell[2] for cell in cells]
facecolors = [cell[3] for cell in cells]

collection = PolyCollection(
    polygons, linewidth=linewidths, edgecolor=edgecolors, facecolor=facecolors
)
ax.add_collection(collection)

plt.savefig("../../figures/showcases/recursive-voronoi.pdf")
plt.savefig("../../figures/showcases/recursive-voronoi.png", dpi=600)
plt.show()
