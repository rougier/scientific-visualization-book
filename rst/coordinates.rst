.. ----------------------------------------------------------------------------
.. Title:   Scientific Visualisation - Python & Matplotlib
.. Author:  Nicolas P. Rougier
.. License: Creative Commons BY-NC-SA International 4.0
.. ----------------------------------------------------------------------------
.. _chap-coordinates:
  
Coordinate systems
==================

In any matplotlib figure, there is at least two different coordinate systems
that co-exist anytime. One is related to the figure (FC) while the others are
related to each of the individual plots (DC). Each of these coordinate systems
exists in normalized (NxC) or native version (xC) as illustrated in figures
:ref:`fig-coordinates-cartesian` and :ref:`fig-coordinates-polar`. To convert a
coordinate from one system to the other, matplotlib provides a set of
`transform` functions:

.. code:: Python

   fig = plt.figure(figsize=(6, 5), dpi=100)
   ax = fig.add_subplot(1, 1, 1)
   ax.set_xlim(0,360), ax.set_ylim(-1,1)

   #  FC : Figure coordinates (pixels)
   # NFC : Normalized figure coordinates (0 → 1)
   #  DC : Data coordinates (data units)
   # NDC : Normalized data coordinates (0 → 1)
   
   DC_to_FC = ax.transData.transform
   FC_to_DC = ax.transData.inverted().transform

   NDC_to_FC = ax.transAxes.transform
   FC_to_NDC = ax.transAxes.inverted().transform

   NFC_to_FC = fig.transFigure.transform
   FC_to_NFC = fig.transFigure.inverted().transform


.. figure:: coordinates/coordinates-cartesian.pdf
   :width: 100%

   The co-existing coordinate systems within a figure using Cartesian
   projection. **FC**: Figure Coordinates, **NFC** Normalized Figure Coordinates,
   **DC**: Data Coordinates, **NDC**: Normalized Data Coordinates.
   :label:`fig-coordinates-cartesian`


.. figure:: coordinates/coordinates-polar.pdf
   :width: 100%
           
   The co-existing coordinate systems within a figure using Polar projection.
   **FC**: Figure Coordinates, **NFC** Normalized Figure Coordinates, **DC**:
   Data Coordinates, **NDC**: Normalized Data Coordinates.
   :label:`fig-coordinates-polar`


Let's test these functions on some specific points (corners):

.. code:: python

   # Top right corner in normalized figure coordinates
   print(NFC_to_FC([1,1]))  # (600,500)
   
   # Top right corner in normalized data coordinates
   print(NDC_to_FC([1,1]))  # (540,440)

   # Top right corner in data coordinates
   print(DC_to_FC([360,1])) # (540,440)

Since we also have the inverse functions, we can create our own transforms. For
example, from native data coordinates (DC) to normalized data coordinates (NDC):

.. code:: Python

   # Native data to normalized data coordinates
   DC_to_NDC = lambda x: FC_to_NDC(DC_to_FC(x))

   # Bottom left corner in data coordinates
   print(DC_to_NDC([0, -1]))  # (0.0, 0.0)

   # Center in data coordinates
   print(DC_to_NDC([180,0]))  # (0.5, 0.5)

   # Top right corner in data coordinates
   print(DC_to_NDC([360,1]))  # (1.0, 1.0)

When using Cartesian projection, the correspondence is quite clear between the
normalized and native data coordinates. With other kind of projection, things
work just the same even though it might appear less obvious. For example, let
us consider a polar projection where we want to draw the outer axes border. In
normalized data coordinates, we know the coordinates of the four corners,
namely `(0,0)`, `(1,0)`, `(1,1)` and `(0,1)`. We can then transform these
normalized data coordinates back to native data coordinates and draw the
border. There is however a supplementary difficulty because those coordinates
are beyond the axes limit and we'll need to tell matplotlib to not care about
the limit using the `clip_on` arguments.

.. code:: Python
          
   fig = plt.figure(figsize=(5, 5), dpi=100)
   ax = fig.add_subplot(1, 1, 1, projection='polar')
   ax.set_ylim(-1, 1), ax.set_yticks([-1, -0.5, 0, 0.5, 1])

   FC_to_DC = ax.transData.inverted().transform
   NDC_to_FC = ax.transAxes.transform
   NDC_to_DC = lambda x: FC_to_DC(NDC_to_FC(x))
   P = NDC_to_DC([[0,0], [1,0], [1,1], [0,1], [0,0]])
   
   plt.plot(P[:,0], P[:,1], clip_on=False, zorder=-10,
            color="k", linewidth=1.0, linestyle="--")
   plt.scatter(P[:-1,0], P[:-1,1],
              clip_on=False, facecolor="w", edgecolor="k")
   plt.show()

The result is shown on figure :ref:`fig-transforms-polar`.

.. figure:: coordinates/transforms-polar.pdf
   :width: 75%
           
   Axes boundaries in polar projection using a transform from normalized data
   coordinates to data coordinates (:source:`coordinates/transform-polar.py`).
   :label:`fig-transforms-polar`

However, most of the time, you won't need to use these transform functions
explicitly but rather implicitly. For example, consider the case where you
want to add some text over a specific plot. For this, you need to use the text_
function and specify what is to be written (of course) and the coordinates
where you want to display the text. The question (for matplotlib) is how to
consider these coordinates? Are they expressed in data coordinates? normalized
data coordinates? normalized figure coordinates? The default is to consider
they are expressed in data coordinates. Consequently, if you want to us a
different system, you'll need to explicitly specify a `transform` when calling
the function. Let's say for example we want to add a letter on the bottom left
corner. We can write:

.. code:: Python

   fig = plt.figure(figsize=(6, 5), dpi=100)
   ax = fig.add_subplot(1, 1, 1)

   ax.text(0.1, 0.1, "A", transform=ax.transAxes)
   plt.show()
          
The letter will be placed at 10% from the left spine and 10% from the bottom
spine. If the two spines have the same physical size (in pixels), the letter
will be equidistant from the right and bottom spines. But, if they have
different size, this won't be true anymore and the results will not be very
satisfying (see panel A of figure :ref:`fig-transforms-letter`). What we want
to do instead is to specify a transform that is a combination of the normalized
data coordinates (0,0) plus an offset expressed in figure native units
(pixels). To do that, we need to build our own transform function to compute
the offset:

.. code:: Python

   from matplotlib.transforms import ScaledTranslation

   fig = plt.figure(figsize=(6, 4))

   ax = fig.add_subplot(2, 1, 1)
   plt.text(0.1, 0.1, "A", transform=ax.transAxes)

   ax = fig.add_subplot(2, 1, 2)
   dx, dy = 10/72, 10/72
   offset = ScaledTranslation(dx, dy, fig.dpi_scale_trans)
   plt.text(0, 0, "B", transform=ax.transAxes + offset)

   plt.show()

The result is illustrated on panel B of figure :ref:`fig-transforms-letter`.
The text is now properly positioned and will stay at the right position
independently of figure aspect ratio or data limits.

.. figure:: coordinates/transforms-letter.pdf
   :width: 100%
           
   Using transforms to position precisely a text over a plot. Top panel uses
   normalized data coordinates (0.1,0.1), bottom panel uses normalized data
   coordinates (0.0,0.0) plus an offset (10,10) expressed in figure
   coordinates (:source:`coordinates/transform-letter.py`). :label:`fig-transforms-letter`


Things can become even more complicated when you need a different transform on
the X and Y axis. Let us consider for example the case where you want to add
some text below the X tick labels. The X position of the tick labels is
expressed in data coordinates, but how do we put something under as illustrated
on figure :ref:`fig-transforms-blend`?

.. figure:: coordinates/transforms-blend.pdf
   :width: 100%
           
   Precise placement (arrows below X axis tick labels) using blended transform (:source:`coordinates/transforms-blend.py`).
   :label:`fig-transforms-blend`

The natural unit for text is point and we thus want to position our arrow using
a Y offset expressed in points. To do that, we need to use a blend transform:

.. code:: Python
          
   point = 1/72
   fontsize = 12
   dx, dy = 0, -1.5*fontsize*point
   offset = ScaledTranslation(dx, dy, fig.dpi_scale_trans)
   transform = blended_transform_factory(
                    ax.transData, ax.transAxes+offset)


We can also use transformations to a totally different usage as shown
on figure :ref:`figure-collage`. To obtain such figure, I rewrote the
`imshow
<https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html>`__
function to apply translation, scaling and rotation and I call the
function 200 times with random values (check :source:`coordinates/collage.py` for full code, I'm only giving main details below).

.. code:: python
          
   def imshow(ax, I, position=(0,0), scale=1, angle=0):
       height, width = I.shape
       extent = scale * np.array([-width/2, width/2,
                                  -height/2, height/2])
       im = ax.imshow(I, extent=extent, zorder=zorder)
       t = transforms.Affine2D().rotate_deg(angle).translate(*position)
       im.set_transform(t + ax.transData)


.. figure:: coordinates/collage.png
   :width: 100%

   Collage
   :label:`figure-collage`
   (sources: :source:`coordinates/collage.py`).

   
Transformations are quite powerful tools even though you won't manipulate them
too often in your daily life. But there are a few cases where you'll be
happy to know about them. You can read further on transforms and coordinates
with the `Transformation tutorial`_ on the matplotlib website.


Real case usage
---------------

Let's now study a real case of transforms as shown on figure
:ref:`fig-transforms-hist`. This is a simple scatter plot showing some Gaussian
data, with two principal axis. I added a histogram that is orthogonal to the
first principal component axis to show the distribution on the main axis.
This figure might appear simple (a scatter plot and an oriented histogram) but
the reality is quite different and rendering such a figure is far from
obvious. The main difficulty is to have the histogram at the right position,
size and orientation knowing that position must be set in data coordinates,
size must be given in figure normalized coordinates and orientation in
degrees. To complicate things, we want to express the elevation of the text
above the histogram bars in data points. |newline|

.. figure:: coordinates/transforms-hist.pdf
   :width: 100%
           
   Rotated histogram aligned with second main PCA axis
   (:source:`coordinates/transforms-hist.py`). :label:`fig-transforms-hist`

You can have a look at the sources for the complete story but let's concentrate
on the main difficulty, that is adding a rotated floating axis. Let us start with
a simple figure:
   
.. code:: Python

   import numpy as np
   import matplotlib.pyplot as plt
   from matplotlib.transforms import Affine2D
   import mpl_toolkits.axisartist.floating_axes as floating

   fig = plt.figure(figsize=(8,8))
   ax1 = plt.subplot(1,1,1, aspect=1,
                     xlim=[0,10], ylim=[0,10])

Let's imagine we want to have a floating axis whose center is (5,5) in data
coordinates, size is (5,3) in data coordinates and orientation is -30 degrees:

.. code:: Python

   center = np.array([5,5])
   size = np.array([5,3])
   orientation = -30
   T = size/2*[(-1,-1), (+1,-1), (+1,+1), (-1,+1)]
   rotation = Affine2D().rotate_deg(orientation)
   P = center + rotation.transform(T)

In the code above, we defined the four points delimiting the extent of our new
axis and we took advantage of matplotlib affine transforms to do the actual
rotation. At this point, we have thus four points describing the border of the
axis in data coordinates and we need to transform them in figure normalized
coordinates because the floating axis requires normalized figure coordinates.

.. code:: Python

   DC_to_FC = ax1.transData.transform
   FC_to_NFC = fig.transFigure.inverted().transform
   DC_to_NFC = lambda x: FC_to_NFC(DC_to_FC(x))

We have one supplementary difficulty because the position of a floating axis
needs to be defined in terms of the non-rotated bounding box:

.. code:: Python

   xmin, ymin = DC_to_NFC((P[:,0].min(), P[:,1].min()))
   xmax, ymax = DC_to_NFC((P[:,0].max(), P[:,1].max()))

We now have all the information to add our new axis:

.. code:: Python

   transform = Affine2D().rotate_deg(orientation)
   helper = floating.GridHelperCurveLinear(
                 transform, (0, size[0], 0, size[1]))
   ax2 = floating.FloatingSubplot(
                 fig, 111, grid_helper=helper, zorder=0)
   ax2.set_position((xmin, ymin, xmax-xmin, ymax-ymin))
   fig.add_subplot(ax2)

The result is shown on figure :ref:`fig-transforms-floating-axis`.


Exercise
--------

**Exercise 1** When you specify the size of markers in a scatter plot, this
size is expressed in points. Try to make a scatter plot whose size is expressed
in data points such as to obtain figure :ref:`fig-transforms-exercise-1`.

.. figure:: coordinates/transforms-exercise-1.pdf
   :width: 100%
           
   A scatter plot whose marker size is expressed in data coordinates instead of points
   (:source:`coordinates/transforms-exercise-1.py`).
   :label:`fig-transforms-exercise-1`
          

.. figure:: coordinates/transforms-floating-axis.pdf
   :width: 100%
           
   A floating and rotated floating axis with controlled position size and
   rotation (:source:`coordinates/transforms-floating-axis.py`).
   :label:`fig-transforms-floating-axis`


.. --- Links ------------------------------------------------------------------
.. _text:  https://matplotlib.org/api/_as_gen/matplotlib.pyplot.text.html
.. _Transformation tutorial: https://matplotlib.org/tutorials/advanced/transforms_tutorial.html
.. ----------------------------------------------------------------------------


