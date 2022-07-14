.. ----------------------------------------------------------------------------
.. Title:   Scientific Visualisation - Python & Matplotlib
.. Author:  Nicolas P. Rougier
.. License: Creative Commons BY-NC-SA International 4.0
.. ----------------------------------------------------------------------------
.. _chap-anatomy:

Anatomy of a figure
===================

A matplotlib figure is composed of a hierarchy of elements that, when put
together, forms the actual figure as shown on figure :ref:`fig-anatomy`. Most
of the time, those elements are not created explicitly by the user but derived
from the processing of the various plot commands. Let us consider for example
the most simple matplotlib script we can write:

.. code:: python

   plt.plot(range(10))
   plt.show()

In order to display the result, matplotlib needs to create most of the elements
shown on figure :ref:`fig-anatomy`. The exact list depends on your default
settings (see chapter chap-defaults_), but the bare minimum is the creation of
a Figure_ that is the top level container for all the plot elements, an Axes_
that contains most of the figure elements and of course your actual plot, a
line in this case. The possibility to not specify everything might be
convenient but in the meantime, it limits your choices because missing elements
are created automatically, using default values. For example, in the previous
example, you have no control of the initial figure size since it has been
chosen implicitly during creation. If you want to change the figure size or
the axes aspect, you need to be more explicit:

.. code:: python
   
   fig = plt.figure(figsize=(6,6))
   ax = plt.subplot(aspect=1)
   ax.plot(range(10))
   plt.show()

.. figure:: anatomy/anatomy.pdf
   :width: 100%
         
   A matplotlib figure is composed of a hierarchy of several elements that,
   when put together, forms the actual figure (sources: :source:`anatomy/anatomy.py`).
   :label:`fig-anatomy`

In many cases, this can be further compacted using the subplots_ method.

.. code:: python
   
   fig, ax = plt.subplots(figsize=(6,6),
                          subplot_kw={"aspect": 1})
   ax.plot(range(10))
   plt.show()
   

Elements
--------

You may have noticed in the previous example that the plot_ command is attached
to `ax` instead of `plt`. The use of `plt.plot` is actually a way to tell
matplotlib that we want to plot on the current axes, that is, the last axes
that has been created, implicitly or explicitly. No need to remind that
*explicit is better than implicit* as explained in The Zen of Python, by
Tim Peters (`import this`). When you have choice, it is thus preferable to
specify exactly what you want to do. Consequently, it is important to know what
are the different elements of a figure.

Figure_:
  The most important element of a figure is the figure itself. It is created
  when you call the `figure` method and we've already seen you can specify its
  size but you can also specify a background color (`facecolor`) as well as a
  title (`suptitle`). It is important to know that the background color won't
  be used when you save the figure because the savefig_ function has also a
  `facecolor` argument (that is white by default) that will override your
  figure background color. If you don't want any background you can specify
  `transparent=True` when you save the figure.

Axes_:
  This is the second most important element that corresponds to the actual area
  where your data will be rendered. It is also called a subplot. You can have
  one to many axes per figure and each is usually surrounded by four edges
  (left, top, right and bottom) that are called **spines**. Each of these
  spines can be decorated with major and minor **ticks** (that can point inward
  or outward), **tick labels** and a **label**. By default, matplotlib
  decorates only the left and bottom spines.

Axis_:
  The decorated spines are called axis. The horizontal one is the **xaxis** and
  the vertical one is the **yaxis**. Each of them are made of a spine, major and
  minor ticks, major and minor ticks labels and an axis label. 

Spines_:
  Spines are the lines connecting the **axis** tick marks and noting the
  boundaries of the data area. They can be placed at arbitrary positions and
  may be visible or invisible.

Artist_:
  Everything on the figure, including Figure, Axes, and Axis objects, is an
  artist. This includes Text objects, Line2D objects, collection objects, Patch
  objects. When the figure is rendered, all of the artists are drawn to the
  canvas. A given artist can only be in one Axes.

  
Graphic primitives
------------------

A plot, independently of its nature, is made of patches, lines and
texts. Patches can be very small (e.g. markers) or very large (e.g. bars) and
have a range of shapes (circles, rectangles, polygons, etc.). Lines can be very
small and thin (e.g. ticks) or very thick (e.g. hatches). Text can use any font
available on your system and can also use a latex engine to render maths.

.. figure:: anatomy/bold-ticklabel.pdf
   :width: 100%

   All the graphic primitives (i.e. artists) can be accessed and modified. In
   the figure above, we modified the boldness of the X axis tick labels
   (sources: :source:`anatomy/bold-ticklabel.py`).

Each of these graphic primitives have also a lot of other properties such as
color (facecolor and edgecolor), transparency (from 0 to 1), patterns
(e.g. dashes), styles (e.g. cap styles), special effects (e.g. shadows or
outline), antialiased (True or False), etc. Most of the time, you do not
manipulate these primitives directly. Instead, you call methods that build a
rendering using a collection of such primitives. For example, when you add a
new `Axes` to a figure, matplotlib will build a collection of line segments for
the spines and the ticks and will also add a collection of labels for the tick
labels and the axis labels. Even though this is totally transparent for you,
you can still access those elements individually if necessary. For example, to
make the X axis tick to be bold, we would write:

.. code:: Python

   fig, ax = plt.subplots(figsize=(5,2))
   for label in ax.get_xaxis().get_ticklabels():
       label.set_fontweight("bold")
   plt.show()

One important property of any primitive is the `zorder` property that indicates
the virtual depth of the primitives as shown on figure :ref:`fig-zorder`. This
zorder value is used to sort the primitives from the lowest to highest before
rendering them. This allows to control what is behind what. Most artists
possess a default zorder value such that things are rendered properly. For
example, the spines, the ticks and the tick label are generally *behind*
your actual plot.

.. figure:: anatomy/zorder.pdf
   :width: 50%

   Default rendering order of different elements and graphic primitives. The
   rendering order is from bottom to top. Note that some methods will override
   these default to position themselves properly (sources: :source:`anatomy/zorder.py`).
   :label:`fig-zorder`
 

Backends
--------

A backend is the combination of a renderer that is responsible for the actual
drawing and an optional user interface that allows to interact with a
figure. Until now, we've been using the default renderer and interface
resulting in a window being shown when the `plt.show()` method was called. To
know what is your default backend, you can type:

.. code:: Python

   import matplotlib
   print(matplotlib.get_backend())
   
In my case, the default backend is `MacOSX` but yours may be different. If you
want to test for an alternative backend, you can type:

.. code:: Python

   import matplotlib
   matplotlib.use("xxx")

If you replace `xxx` with a renderer from table :ref:`table-renderers` below,
you'll end up with a non-interactive figure, i.e. a figure that cannot be shown
on screen but only saved on disk.

.. table:: Available matplotlib renderers.
           :label:`table-renderers`
   :align: left

   ========= ================== =============================================
   Renderer  Type               Filetype
   ========= ================== =============================================
   Agg       raster             Portable Network Graphic (PNG)
   PS        vector             Postscript (PS)
   PDF       vector             Portable Document Format (PDF)
   SVG       vector             Scalable Vector Graphics (SVG)
   Cairo     raster / vector    PNG / PDF / SVG
   ========= ================== =============================================

.. table:: Available matplotlib interfaces.
   :label:`table-interfaces`
   :align: left

   ========== =============== ===============================================
   Interface  Renderer        Dependencies
   ========== =============== ===============================================
   GTK3       Agg or Cairo    PyGObject_ & Pycairo_
   Qt4        Agg             PyQt4_
   Qt5        Agg             PyQt5_
   Tk         Agg             TkInter_
   Wx         Agg             wxPython_
   MacOSX     —               OSX (obviously)
   Web        Agg             Browser
   ========== =============== ===============================================

The canonical renderer is Agg which uses the `Anti-Grain Geometry C++ library
<http://agg.sourceforge.net/antigrain.com/>`__ to make a raster image of the figure (see figure
:ref:`fig-raster-vector` to see the difference between raster and vector). Note
that even if you choose a raster renderer, you can still save the figure in a
vector format and vice-versa.

.. figure:: anatomy/raster-vector.pdf
   :width: 75%

   Zooming effect for raster graphics and vector graphics (sources:
   :source:`anatomy/raster-vector.py`). :label:`fig-raster-vector`

If you want to have some interaction with your figure, you have to combine one
of the available interfaces (see table :ref:`table-interfaces`) with a
renderer (e.g. `GTK3Cairo` that stands for GTK3 interface with Cairo
renderer).



For example, to have a rendering in a browser, you can write:

.. code:: Python

   import matplotlib
   matplotlib.use('webagg')
   import matplotlib.pyplot as plt
   plt.show()

.. warning::
   **Warning.** The `use` function must be called before importing `pyplot`.
   
Once you've chosen an interactive backend, you can decide to produce a figure
in interactive mode (figure is updated after each matplotlib command):

.. code:: Python

   plt.ion()            # Interactive mode on 
   plt.plot([1,2,3])    # Plot is shown
   plt.xlabel("X Axis") # Label is updated
   plt.ioff()           # Interactive mode off
   
If you want to know more on backends, you can have a look at the `matplotlib
user guide <https://matplotlib.org/stable/users/explain/backends.html>`__
on the matplotlib website.


An interesting backend under OSX and `iterm2 <https://iterm2.com/>`__
terminal is the `imgcat <https://github.com/wookayin/python-imgcat>`__
backend that allows to render a figure directly inside the terminal,
emulating a kind of jupyter notebook as shown on figure
:ref:`figure-imgcat`

.. figure:: anatomy/imgcat.png
   :width: 100%

   Matplotlib imgcat backend
   :label:`figure-imgcat`
   (sources: :source:`anatomy/imgcat.py`).

.. code:: python
          
   import numpy as np
   import matplotlib
   matplotlib.use("module://imgcat")
   import matplotlib.pyplot as plt

   fig = plt.figure(figsize=(8,4), frameon=False)
   ax = plt.subplot(2,1,1)
   X = np.linspace(0, 4*2*np.pi, 500)
   line, = ax.plot(X, np.cos(X))
   ax = plt.subplot(2,1,2)
   X = np.linspace(0, 4*2*np.pi, 500)
   line, = ax.plot(X, np.sin(X))
   plt.tight_layout()
   plt.show()

For other terminals, you might need to use the `sixel <https://github.com/koppa/matplotlib-sixel>`__ backend that may work with xterm (not tested).

   
Dimensions & resolution
-----------------------

In the first example of this chapter, we specified a figure size of `(6,6)`
that corresponds to a size of 6 inches (width) by 6 inches (height) using a
default dpi (dots per inch) of 100. When displayed on a screen, dots
corresponds to pixels and we can immediately deduce that the figure size
(i.e. window size without the toolbar) will be exactly 600×600 pixels.  Same is
true if you save the figure in a bitmap format such as png (Portable Network
Graphics):

.. code:: python

   fig = plt.figure(figsize=(6,6))
   plt.savefig("output.png")

If we use the `identify` command from the ImageMagick_ graphical suite to
enquiry about the produced image, we get:
   
.. code:: bash

   $ identify -verbose output.png
   Image: output.png
     Format: PNG (Portable Network Graphics)
     Mime type: image/png
     Class: DirectClass
     Geometry: 600x600+0+0
     Resolution: 39.37x39.37
     Print size: 15.24x15.24
     Units: PixelsPerCentimeter
     Colorspace: sRGB
     ...

This confirms that the image geometry is 600×600 while the resolution is 39.37
ppc (pixels per centimeter) which corresponds to 39.37*2.54 ≈ 100 dpi (dots per
inch). If you were to include this image inside a document while keeping the
same dpi, you would need to set the size of the image to 15.24cm by 15.24cm. If
you reduce the size of the image in your document, let's say by a factor of 3,
this will mechanically increase the figure dpi to 300 in this specific
case. For a scientific article, publishers will generally request figures dpi
to be between 300 and 600. To get things right, it is thus good to know what
will be the physical dimension of your figure once inserted into your document.

.. figure:: anatomy/figure-dpi.png
   :width: 100%

   A text rendered in matplotlib and saved using different dpi (50,100,300 &
   600)  (sources: :source:`anatomy/figure-dpi.py`). :label:`figure-dpi`

For a more concrete example, let us consider this book whose format is A5
(148×210 millimeters). Right and left margins are 20 millimeters each and
images are usually displayed using the full text width. This means the physical
width of an image is exactly 108 millimeters, or approximately 4.25 inches. If
we were to use the recommended 600 dpi, we would end up with a width of 2550
pixels which might be beyond screen resolution and thus not very convenient.
Instead, we can use the default matplotlib dpi (100) when we display the figure
on the screen and only when we save it, we use a different and higher dpi:

.. code:: Python

   def figure(dpi):
       fig = plt.figure(figsize=(4.25,.2))
       ax = plt.subplot(1,1,1)
       text = "Text rendered at 10pt using %d dpi" % dpi
       ax.text(0.5, 0.5, text, ha="center", va="center",
               fontname="Source Serif Pro",
               fontsize=10, fontweight="light")
       plt.savefig("figure-dpi-%03d.png" % dpi, dpi=dpi)

   figure(50), figure(100), figure(300), figure(600)

Figure :ref:`figure-dpi` shows the output for the different dpi. Only the 600
dpi output is acceptable. Note that when it is possible, it is preferable to
save the result in PDF (Portable Document Format) because it is a vector format
that will adapt flawlessly to any resolution. However, even if you save your
figure in a vector format, you still need to indicate a dpi for figure elements
that cannot be vectorized (e.g .images).

Finally, you may have noticed that the font size on figure :ref:`figure-dpi`
appears to be the same as the font size of the text you're currently
reading. This is not by accident since this Latex document uses a font size of
10 points and the matplotlib figure also uses a font size of 10 points. But
what is a point exactly? In Latex, a point (pt) corresponds to 1/72.27 inches
while in matplotlib it corresponds to 1/72 inches.

To help you visualize the exact dimension of your figure, it is
possible to add a ruler to a figure such that it displays current
figure dimension as shown on figure :ref:`figure-ruler`. If you
manually resize the figure, you'll see that the actual dimension of
the figure changes while if you only change the dpi, the size will
remain the same. Usage is really simple:

.. code:: python

   import ruler
   import numpy as np
   import matplotlib.pyplot as plt
          
   fig,ax = plt.subplots()
   ruler = ruler.Ruler(fig)
   plt.show()


   
.. figure:: anatomy/ruler.pdf
   :width: 100%

   Interactive ruler :label:`figure-ruler`
   (:source:`anatomy/ruler.py`).

   
Exercise
--------

It's now time to try to make some simple exercises gathering all the concepts
we've seen so far (including finding the relevant documentation).

**Exercise 1** Try to produce a figure with a given (and exact) pixel size
(e.g. 512x512 pixels). How would you specify the size and save the figure?

.. figure:: anatomy/pixel-font.png
   :width: 100%

   Pixel font text using exact image size :label:`figure-pixel-font`
   (:source:`anatomy/pixel-font.py`).

   
**Exercise 2**
The goal is to make the figure :ref:`figure-inch-cm` that shows a dual axis, one
in inches and one in centimeters. The difficulty is that we want the
centimeters and inched to be physically correct when printed. This requires
some simple computations for finding the right size and some trials and errors
to make the actual figure. Don't pay too much attention to all the details, the
essential part is to get the size right. 

.. figure:: anatomy/inch-cm.pdf
   :width: 100%

   Inches/centimeter conversion :label:`figure-inch-cm`
   (**solution**: :source:`anatomy/inch-cm.py`).


**Exercise 3**

Here we'll try to reproduce the figure :ref:`figure-zorder-plots`. If you look
at the figure, you'll realize that each curve is partially covering other
curves and it is thus important to set a proper zorder for each curve such that
the rendering will be independent of drawing order. For the actual curves, you can start from the following code:

.. code:: Python
          
   def curve():
       n = np.random.randint(1,5)
       centers = np.random.normal(0.0,1.0,n)
       widths = np.random.uniform(5.0,50.0,n)
       widths = 10*widths/widths.sum()
       scales = np.random.uniform(0.1,1.0,n)
       scales /= scales.sum()    
       X = np.zeros(500)
       x = np.linspace(-3,3,len(X))
       for center, width, scale in zip(centers, widths, scales):
           X = X + scale*np.exp(- (x-center)*(x-center)*width)
       return X

.. figure:: anatomy/zorder-plots.pdf
   :width: 100%

   Multiple plots partially covering each other :label:`figure-zorder-plots`
   (**solution**: :source:`anatomy/zorder-plots.py`).


.. --- Links ------------------------------------------------------------------
.. _Figure: https://matplotlib.org/api/figure_api.html
.. _Axes:   https://matplotlib.org/api/axes_api.html
.. _plot:   https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
.. _ImageMagick: https://imagemagick.org
.. _savefig: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html
.. _subplots: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots.html
.. _Axis:  https://matplotlib.org/api/axis_api.html
.. _Axes:  https://matplotlib.org/api/axes_api.html
.. _Ticks: https://matplotlib.org/api/ticker_api.html
.. _Spines: https://matplotlib.org/api/spines_api.html
.. _Artist: https://matplotlib.org/tutorials/intermediate/artists.html
.. _pygobject: https://pygobject.readthedocs.io/en/latest/
.. _pycairo: https://pycairo.readthedocs.io/en/latest/
.. _pyqt4: https://www.riverbankcomputing.com/software/pyqt/intro
.. _pyqt5: https://www.riverbankcomputing.com/software/pyqt/intro
.. _tkinter: https://wiki.python.org/moin/TkInter
.. _wxpython: https://www.wxpython.org/
.. ----------------------------------------------------------------------------


