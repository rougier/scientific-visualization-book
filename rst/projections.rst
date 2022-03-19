.. ----------------------------------------------------------------------------
.. Title:   Scientific Visualisation - Python & Matplotlib
.. Author:  Nicolas P. Rougier
.. License: BSD
.. ----------------------------------------------------------------------------
.. _chap-projection:

Scales & projections
====================

Beyond affine transforms, matplotlib also offers advanced transformations that
allows to drastically change the representation of your data without ever
modifying it. Those transformations correspond to a data preprocessing stage
that allows you to adapt the rendering to the nature of your data. As explained
in the matplotlib documentation, there are two main families of transforms:
separable transformations, working on a single dimension, are called
:nameref:`scales`, and non-separable transformations, that handle data in two
or more dimensions at once are called :nameref:`projections`.


Scales
------

Scales provide a mapping mechanism between the data and their representation
in the figure along a given dimension. Matplotlib offers four different scales
(`linear`, `log`, `symlog` and `logit`) and takes care, for each of them, of
modifying the figure such as to adapt the ticks positions and labels (see
figure :ref:`figure-scales`). Note that a scale can be applied to x axis only
(`set_xscale`), y axis only (`set_yscale`) or both.

.. figure:: scales-projections/scales-comparison.pdf
   :width: 100%

   Comparison of the linear_, log_ and logit_ scales.
   :label:`figure-scales` (sources: :source:`scales-projections/scales-comparison.py`).

The default (and implicit) scale is linear_ and it is thus generally not
necessary to specify anything. You can check if a scale is linear by comparing
the distance between three points in the figure coordinates (actually we should
compare every points but you get the idea) and check whether their difference
in data space is the same as in figure space modulo a given factor (see
:source:`scales-projections/scales-check.py`):

.. code:: python

   >>> fig = plt.figure(figsize=(6,6))
   >>> ax = plt.subplot(1, 1, 1,
                        aspect=1, xlim=[0,100], ylim=[0,100])
   >>> P0, P1, P2, P3 = (0.1, 0.1), (1,1), (10,10), (100,100)
   >>> transform = ax.transData.transform
   >>> print( (transform(P1)-transform(P0))[0] )
   4.185
   >>> print( (transform(P2)-transform(P1))[0] )
   41.85
   >>> print( (transform(P3)-transform(P2))[0] )
   418.5

Logarithmic scale (log_) is a nonlinear scale where, instead of increasing in equal
increments, each interval is increased by a factor of the base of the logarithm
(hence the name). Log scales are used for values that are strictly positive since
the logarithm is undefined for negative and null values. If we apply the previous
script to check the difference in data and figure space, you can now see the
distances are the same:

.. code:: python

   >>> fig = plt.figure(figsize=(6,6))
   >>> ax = plt.subplot(1, 1, 1,
                        aspect=1, xlim=[0.1,100], ylim=[0.1,100])
   >>> ax.set_xscale("log")
   >>> P0, P1, P2, P3 = (0.1, 0.1), (1,1), (10,10), (100,100)
   >>> transform = ax.transData.transform
   >>> print( (transform(P1)-transform(P0))[0] )
   155.0
   >>> print( (transform(P2)-transform(P1))[0] )
   155.0
   >>> print( (transform(P3)-transform(P2))[0] )
   155.0

If your data has negative values, you have to use a symmetric log scale (symlog_)
that is a composition of both a linear and a logarithmic scale. More precisely,
values around 0 use a linear scale and values outside the vicinity of zero uses
a logarithmic scale. You can of course specify the extent of the linear zone
when you set the scale. The logit_ scale is used for values in the range ]0,1[
and uses a logarithmic scale on the "border" and a quasi-linear scale in the
middle (around 0.5). If none of these scales suit your needs, you still have
the option to define your own custom scale:

.. code:: python

   def forward(x):
       return x**(1/2)
   def inverse(x):
       return x**2

   ax.set_xscale('function', functions=(forward, inverse))

In such case, you have to provide both the forward and inverse function that
allows to transform your data. The inverse function is used when displaying
coordinates under the mouse pointer.

.. figure:: scales-projections/scales-custom.pdf
   :width: 100%

   Custom (user defined) scales.
   :label:`figure-scales-custom` (sources: :source:`scales-projections/scales-custom.py`).

Finally, if you need a custom scale with complex transforms, you may need to
write a proper scale object as it is explained on the `matplotlib documentation
<https://matplotlib.org/gallery/scales/custom_scale.html>`_.

Projections
-----------

Projections are a bit more complex than scales but in the meantime much more
powerful. Projections allows you to apply arbitrary transformation to your data
before rendering them in a figure. There is no real limit on the kind of
transformation you can apply as long as you know how to transform your data into
something that will be 2 dimensional (the figure space) and reciprocally. In
other words, you need to define a forward and an inverse
transformation. Matplotlib comes with only a few standard projections but offers
all the machinery to create new domain-dependent projection such as for example
cartographic projection. You might wonder why there are so few native
projections. The answer is that it would be too time-consuming and too difficult
for the developers to implement and maintain each and every projections that
are domain specific. They chose instead to restrict projection to the most
generic ones, namely polar_ and 3d_.

We've already seen the polar projection in the previous chapter. The most simple
and straightforward way to use is to specify the projection when you create an
axis:

.. code:: Python

   ax = plt.subplot(1, 1, 1, projection='polar')

This axis is now equipped with a polar projection. This means that any plotting
command you apply is pre-processed such as to apply (automatically) the forward
transformation on the data. In the case of a polar projection, the forward
transformation must specify how to go from polar coordinates :math:`(\rho,
\theta)` to Cartesian coordinates :math:`(x,y) = (\rho cos(\theta), \rho
sin(\theta))`. When you declare a polar axis, you can specify limits of the axis
as we've done previously but we have also some dedicated settings such as
`set_thetamin`, `set_thetamax`, `set_rmin`, `set_rmax` and more specifically
`set_rorigin`. This allows you to have fine control over what is actually shown as illustrated on the figure :ref:`figure-projection-polar-config`.

.. figure:: scales-projections/projection-polar-config.pdf
   :width: 100%

   Polar projection
   :label:`figure-projection-polar-config`
   (sources: :source:`scales-projections/projection-polar-config.py`).


If you now try to do some plots (e.g. plot, scatter, bar), you'll see that
everything is transformed but a few elements. More precisely, the shape of
markers is not transformed (a disc marker will remains a disc visually), the
text is not transformed (such that it remains readable) and the width of lines
is kept constant. Let's have a look at a more elaborate figure to see what it
means more precisely. On figure :ref:`figure-projection-polar-histogram`, I
plotted a simple signal using mostly `fill_between
<https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.fill_between.html>`_
command. The concentric grey/white colored rings are made using the
`fill_between` command between two different :math:`\rho` values while the
histogram is made with various :math:`\rho` values. If you now look more closely
at the :math:`\rho` axis with ticks ranging from 100 to 900, you can observe
that the ticks have the same vertical size. It is indeed an *anomaly* I
introduced deliberately for purely aesthetic reasons. If I had specified these
ticks using a plot command, the length of each tick would correspond to a
difference of angle (for the vertical size) and they would become taller and
taller as we move away from the center. To have regulars ticks, we thus have to
do some computations using the inverse transform (remember, a projection is a
forward and an inverse transform). I won't give all the details here but you can
read the code (:source:`projection-polar-histogram.py`) to see how it is
made. Note that the actual role of the inverse transformation is to link mouse
coordinates (in Cartesian 2D coordinates) back to your data.

.. figure:: scales-projections/projection-polar-histogram.pdf
   :width: 95%

   Polar projection with better defaults.
   :label:`figure-projection-polar-histogram`
   (sources: :source:`scales-projections/projection-polar-histogram.py`).

Conversely, there are some situations were we might be interested in having
the text and the markers to be transformed as illustrated on figure
:ref:`figure-text-polar`.

.. figure:: scales-projections/text-polar.pdf
   :width: 90%

   Polar projection with transformation of text and markers.
   :label:`figure-text-polar`
   (sources: :source:`scales-projections/text-polar.py`).

On this example, both the markers and the text have been transformed
manually. For the markers, the trick is to use `Ellipses
<https://matplotlib.org/api/_as_gen/matplotlib.patches.Ellipse.html>`_ that are
approximated as a sequence of small line segments, each of them being
transformed. In the corresponding code, I only specify the center, and the size
of the pseudo-marker and the pre-processing stage takes care of applying the
polar projection to each individual parts composing the marker (ellipse),
resulting in a slightly curved ellipse. For the text, the process is the same
but it is a bit more complicated since we need first to convert the text into a
path that can be transformed (we'll see that in more detail in the next
chapter).


The second projection that matplotlib offers is the 3d projection, that is the
projection from a 3D Cartesian space to a 2 Cartesian space. To start using 3D
projection, you'll need to use the `Axis3D
<https://matplotlib.org/api/toolkits/mplot3d.html>`_ toolkit that is generally
shipped with matplotlib:

.. code:: python

   from mpl_toolkits.mplot3d import Axes3D
   ax = plt.subplot(1, 1, 1, projection='3d')

With this 3D axis, you can use regular plotting commands with a big difference
though: you need now to provide 3 coordinates (x,y,z) where you previously
provided only two (x,y) as illustrated on figure
:ref:`figure-projection-3d-frame`. Note that this figure is quite different from
the default 3D axis you may get from matplotlib. Here, I tweaked every setting
I can think of to try to improve the default look and to show how things can be
changed. Have a look at the corresponding code and try to modify some settings to
see the actual effect. The `3D Axis API
<https://matplotlib.org/mpl_toolkits/mplot3d/api.html>`_ is fairly well
documented on the matplotlib website and I won't explain each and every command.

.. note:: **Note** The 3D axis projection is limited by the absence of a proper
    `depth-buffer <https://en.wikipedia.org/wiki/Z-buffering>`_. This is not a
    bug (nor a feature) and this results in some glitches between the elements
    composing a figure.

.. figure:: scales-projections/projection-3d-frame.pdf
   :width: 80%

   Three dimensional projection
   :label:`figure-projection-3d-frame`
   (sources: :source:`scales-projections/projection-3d-frame.py`).

For other type of projections, you'll need to install third-party packages
depending on the type of projection you intend to use:

`Cartopy <https://scitools.org.uk/cartopy/docs/latest/>`_
  is a Python package
  designed for geospatial data processing in order to produce maps and other
  geospatial data analyses. Cartopy makes use of the powerful PROJ.4, NumPy and
  Shapely libraries and includes a programmatic interface built on top of
  Matplotlib for the creation of publication quality maps.

`GeoPandas <https://geopandas.org/>`_
  is an open source project to make working
  with geospatial data in python easier. GeoPandas extends the data types used by
  pandas to allow spatial operations on geometric types. Geometric operations
  are performed by Shapely. Geopandas further depends on fiona for file access
  and descartes and matplotlib for plotting.

`Python-ternary <https://github.com/marcharper/python-ternary>`_
  is a plotting library for use with matplotlib to make ternary plots in
  the two dimensional simplex projected onto a two dimensional plane. The
  library provides functions for plotting projected lines, curves
  (trajectories), scatter plots, and heatmaps. There are several examples and a
  short tutorial below.

`pySmithPlot <https://github.com/vMeijin/pySmithPlot>`_
  is a matplotlib extension providing a projection class for creating high
  quality Smith Charts with Python. The generated plots blend seamlessly into
  matplotlib's style and support almost the full range of customization options.

`Matplotlib-3D <https://github.com/rougier/matplotlib-3d>`_
  is an experimental project that attempts to provide a better and more
  versatile 3d axis for Matplotlib.

  ..
   .. figure:: scales-projections/geo-projections.pdf
      :width: 100%

      Some of the standard and not so standard geographic projections
      :label:`figure-geo-projections` (sources: :source:`scales-projections/geo-projections.py`).

If you're still not satisfied with existing projections, your last option is to
create your own projection but this is quite an advanced operation even though
the matplotlib documentation provides some `examples
<https://matplotlib.org/devel/add_new_projection.html>`_


Exercises
---------

**Exercise 1** Considering functions :math:`f(x) = 10^x`, :math:`f(x) = x` and
:math:`f(x) = log_{10}(x)`, try to reproduce figure :ref:`figure-scales-log-log`.

.. figure:: scales-projections/scales-log-log.pdf
   :width: 100%

   Combining linear and logarithmic scales.
   :label:`figure-scales-log-log` (sources: :source:`scales-projections/scales-log-log.py`).


**Exercise 2** The goal is to produce a figure showing `microphone
polar patterns
<https://en.wikipedia.org/wiki/Microphone#Polar_patterns>`__
(omnidirectional, subcardioid, cardioid, supercardioid, bidirectional
and shotgun). The first five patterns are simple functions where
radius evolves with angle, while the last pattern may require some
work.

.. figure:: scales-projections/polar-patterns.pdf
   :width: 100%

   Microphone polar patterns
   :label:`figure-polar-patterns`
   (sources: :source:`scales-projections/polar-patterns.py`).




.. --- Links ------------------------------------------------------------------
.. _linear: https://matplotlib.org/api/scale_api.html?#matplotlib.scale.LinearScale
.. _log: https://matplotlib.org/api/scale_api.html?#matplotlib.scale.LogScale
.. _symlog: https://matplotlib.org/api/scale_api.html?#matplotlib.scale.SymmetricalLogScale
.. _logit: https://matplotlib.org/api/scale_api.html?#matplotlib.scale.LogitScale
.. _polar: https://matplotlib.org/api/projections_api.html#module-matplotlib.projections.polar
.. _3d: https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
.. ----------------------------------------------------------------------------

