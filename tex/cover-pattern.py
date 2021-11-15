import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection

inch = 25.4
width = 2*148 + 10 +2*3
height = 210 + 2*3

fig = plt.figure(figsize=(width/inch,height/inch))
ax = fig.add_axes([0,0,1,1], aspect=1, frameon=False)

radius = 25
patches = []
for y in range(11,-1,-1):
    for x in range(8,-1,-1):
        center = 2*x*radius + y%2*radius, y*radius
        for i,r in enumerate(np.linspace(25, 2.5, 10)):
            patches.append(plt.Circle(center, r))

collection = PatchCollection(patches, edgecolors="0.1", facecolors='black')
ax.add_collection(collection)

ax.set_xlim(0, width)
ax.set_ylim(0, height)

plt.savefig("cover-pattern.pdf")
plt.savefig("cover-pattern.png", dpi=600)
plt.show()
