.. ----------------------------------------------------------------------------
.. Title:   Scientific Visualisation - Python & Matplotlib
.. Author:  Nicolas P. Rougier
.. License: Creative Commons BY-NC-SA International 4.0
.. ----------------------------------------------------------------------------
.. _chap-colors:

A primer on colors
==================

Color is a `highly complex topic
<https://en.wikipedia.org/wiki/Color>`_ and a whole book would
probably not be enough to explain each and every aspect. This is the
reason why I won't try to explain everything here, the other reason
being that I'm simply not knowledgeable enough on the topic. There are
nonetheless a few things that are good to know, for example
how are colors represented on a computer. To represent a color on a
computer, we use (most of the time) the notion of a `color model
<https://en.wikipedia.org/wiki/Color_model>`_ (how do we represent a
color) and a `color space
<https://en.wikipedia.org/wiki/Color_space>`_ (what colors can be
represented). There exists several color models (RGB, HSV, HLS, CMYK,
CIEXYZ, CIELAB, etc.) and several color spaces (Adobe RGB, sRGB,
Colormatch RGB, etc.) such that you can access the same color space
using different color models. The standard for computers (since 1996)
is the `sRGB color space <https://en.wikipedia.org/wiki/SRGB>`_ where
the `s` stands for standard. This color space uses an additive color
model based on the RGB model. This means that to obtain a given color,
you need to mix different amounts of red, green, and blue light.  When
these amounts are all zero, you obtain black and when these amounts
are all at full intensity, you obtain white (D65 white point, see `CIE
1931 xy chromaticity space
<https://en.wikipedia.org/wiki/CIE_1931_color_space>`_).

Consequently, when you specify a color in matplotlib
(e.g. `"#123456"`), you need to realize that this color is implicitly
encoded in the sRGB color model and space. This draws immediate
consequences. For example, if you try to produce a gradient between
two colors using a naive approach, you'll get wrong perceptual results
because the sRGB model is not linear. This is illustrated on figure
:ref:`figure-color-gradients` where I plotted gradients using the sRGB
naive approach (first line on each gradient). You can observe that the
result is far from being satisfactory. A better way to build a
gradient is to first convert colors to the linear RGB space, apply
the gradient, and then convert it back to the sRGB color model. This is
illustrated on the second line of each gradient that are now
perceptually smoother. A third (and better) solution is to use the
`CIE Lab <https://en.wikipedia.org/wiki/CIELAB_color_space>`_ model
that has been tailored to the human perception and provides a
perceptually uniform space. It is a bit more complicated to manipulate
and you'll need external packages such as `scikit-image
<https://scikit-image.org/>`_ or `colour
<https://colour.readthedocs.io/en/develop/index.html>`_ to make the
conversion between the different models and spaces, but results are
worth the effort.

.. figure:: colors/color-gradients.pdf
   :width: 100%

   Linear color gradients using different color models
   :label:`figure-color-gradients` (sources: :source:`colors/color-gradients.py`).

Another popular model is the `HSV
<https://en.wikipedia.org/wiki/HSL_and_HSV>`_ model that stands for
Hue, Saturation and Value (see figure :ref:`figure-color-wheel`). It
provides an alternate color model to access the same color space as
the sRGB system. Matplotlib provides methods to convert to and
from the HSV model (see the `colors <https://matplotlib.org/stable/api/colors_api.html>`_ module).

.. figure:: colors/color-wheel.pdf
   :width: 100%

   Color wheel (HSV)
   :label:`figure-color-wheel` (sources: :source:`colors/color-wheel.py`).


Choosing colors
---------------

Maybe at this point the only question you have in mind is "Ok,
interesting, but how do I choose a color then? Do I even have to
choose anyway?" For this second question, you can actually let
Matplotlib choose for you. When you draw several plots at once, you
may have noticed that the plots use several different colors. These
colors are picked from what is called a color cycle:

.. code:: python

   >>> import matplotlib.pyplot as plt
   >>> print(plt.rcParams['axes.prop_cycle'].by_key()['color'])
   ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

These colors come from the `tab10` colormap which itself comes from
the `Tableau <https://www.tableau.com/>`_ software:

.. code:: python

   >>> import matplotlib.colors as colors
   >>> cmap = plt.get_cmap("tab10")
   >>> [colors.to_hex(cmap(i)) for i in range(10)]
   ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

These colors have been designed to be sufficiently different such as
to ease the visual perception of difference while being not too
aggressive on the eye (compared to saturated pure blue, green or red
colors for example). If you need more colors, you need first to ask
yourself whether you really need more colors. Then, and only then, you
might consider using palettes that have been designed with care. This
is the case of the open color palette (see figure
:ref:`figure-open-colors`) and the material color palette (see
:ref:`figure-material-colors`). For example, on figure
:ref:`stacked-plots`, I use two color stacks (`blue grey` and `yellow`
from the material palettes) to highlight an area of interest.


.. figure:: colors/stacked-plots.pdf
   :width: 100%

   Stacked plots using two different color stacks to better highlight
   an area of interest :label:`stacked-plots` (sources:
   :source:`colors/stacked-plots.py`).
     
    
.. figure:: colors/open-colors.pdf
   :width: 100%

   Open colors
   :label:`figure-open-colors` (sources: :source:`colors/open-colors.py`).


.. figure:: colors/material-colors.pdf
   :width: 100%

   Material colors
   :label:`figure-material-colors` (sources: :source:`colors/material-colors.py`).


Another usage is to use color stacks to identify different groups
while allowing variation inside each group. When doing this, you need
to conserve the same color semantics throughout all your subsequent
figures.

.. figure:: colors/colored-hist.pdf
   :width: 100%

   Identification of groups with internal variations using color stacks.
   :label:`figure-colored-hist` (sources: :source:`colors/colored-hist.py`).

Another popular usage of color is to show some plots associated with their standard deviation (SD) or standard error (SE). To do that, there are two different ways to do it. Either with use palettes as the one defined previously or we use transparency using the `alpha` keyword. Let's compare the results.

.. figure:: colors/alpha-vs-color.pdf
   :width: 100%

   Showing standard deviation, with or without transparency
   :label:`figure-alpha-vs-color` (sources: :source:`colors/alpha-vs-color.py`).

As you can see on the left part of figure :ref:`figure-alpha-vs-color`, using transparency results in the two plots to be somehow mixed together. This might be a useful effect since it allows you to show what is happening in shared  areas. This is not the case when using opaque colors and you thus have to decide which plot is covering the other (using `zorder`). Note that the choice of one or the other solution is up to you since it very much depends on your data.

However, it is important to note that the use of transparency is quite specific in the sense that the visual result is not specified explicitly in the script. It depends actually from the actual rendering of the figure and the way matplotlib composes the different elements. Let's consider for example a scatter plot (normal distribution) where each point is transparent (10%):

.. figure:: colors/alpha-scatter.pdf
   :width: 100%

   Semi-transparent scatter plots
   :label:`figure-alpha-scatter` (sources: :source:`colors/alpha-scatter.py`).

On the left part of figure :ref:`figure-alpha-scatter`, we can see the result with a perceptually darker area in the center. This is a direct result of rendering several small discs on top of each other in the central area. If we want to quantify this perceptual result, we need to use a trick. The trick is to render the scatter plot in an array such that we can consider the result as an image. Such image is displayed in the central part and from this, we can play with the perceptual density as shown on the right part.
          

Choosing colormaps
------------------

Colormapping corresponds to the mapping of values to colors, using a colormap that defines, for each value, the corresponding color. There are different types of colormaps (sequential, diverging, cyclic, qualitative or none of these) that correspond to different use cases. It is is important to use the right type or colormap that corresponds to your data. To pick a colormap, you can start by answering questions illustrated on figure :ref:`colormap-tree` and then choose the corresponding `colormap <https://matplotlib.org/stable/tutorials/colors/colormaps.html>`_ from the matplotlib website. 

.. figure:: colors/colormap-tree.pdf
   :width: 100%

   How to choose a colormap?
   :label:`colormap-tree` 

Problem is, for each type, there exist several colormaps. But if you pick the right type, the choice is yours and depends mostly on you aesthetic taste. As long as you choose the right type, you cannot be wrong. Figure :ref:`figure-mona-lisa` a few choices associated with sequential colormaps and they all look good. In this case, one selection criterion could be the fact that the image represents a human being and we may prefer a colormap close to skin tones.

.. figure:: colors/mona-lisa.pdf
   :width: 100%

   Variations on Mona Lisa (Leonardo da Vinci, 1503).
   :label:`figure-mona-lisa` (sources: :source:`colors/mona-lisa.py`).

Diverging colormaps needs special care because they are really composed of two gradients with a special central value. By default, this central value is mapped to 0.5 in the normalized linear mapping and this works pretty well as long as the absolute minimum and maximum value of your data are the same. Now, consider the situation illustrated on figure :ref:`figure-colormap-transform`. Here we have a small domain with negative values and a larger domain with positive values. Ideally, we would like the negative values to be mapped with blueish colors and positive values with yellowish colors. If we use a diverging colormap without any precaution, there's no guarantee that we'll obtain the result we want. To fix the problem, we thus need to tell matplotlib what is the central value and to do this, we need to use a `Two Slope norm <https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.TwoSlopeNorm.html#matplotlib.colors.TwoSlopeNorm>`_ instead of a `Linear norm <https://matplotlib.org/stable/tutorials/colors/colormapnorms.html#>`_.

.. figure:: colors/colormap-transform.pdf
   :width: 100%

   Colormap with linear norm vs two slopes norm.
   :label:`figure-colormap-transform` 

          
.. code:: python

   >>> import matplotlib.pyplot as plt
   >>> import matplotlib.colors as colors
   >>> cmap = plt.get_cmap("Spectral")
   
   >>> norm = mpl.colors.Normalize(vmin=-3, vmax=10)
   >>> Print(norm(0))
   0.23076923076923078
   >>> print(cmap(norm(0)))
   (0.968, 0.507, 0.300, 1.0)
   
   >>> norm = mpl.colors.TwoSlopeNorm(vmin=-3, vcenter=0, vmax=10)
   >>> print(norm(0))
   0.5
   >>> cmap = plt.get_cmap("Spectral")
   >>> print(cmap(norm(0)))
   (0.998, 0.999, 0.746, 1.0)


Exercises
---------

**Exercise 1** The goal is to reproduce the figure :ref:`figure-colored-plot`. The trick is to split each line is small segments such that they can each have their own colors since it is not possible to do that with a regular plot. However, for performance reasons, you'll need to use `LineCollection <https://matplotlib.org/stable/gallery/shapes_and_collections/line_collection.html>`_. You can start from the following code:

.. code:: python
          
   X = np.linspace(-5*np.pi, +5*np.pi, 2500)
   for d in np.linspace(0,1,15):
       dx, dy = 1 + d/3, d/2 + (1-np.abs(X)/X.max())**2
       Y = dy * np.sin(dx*X) + 0.1*np.cos(3+5*X) 

.. figure:: colors/colored-plot.pdf
   :width: 100%

   (Too much) colored line plots  (sources :source:`colors/colored-plot.py`)
   :label:`figure-colored-plot` 


**Exercise 2** This exercise is a bit tricky and requires the usage of `PolyCollection <https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection>`_. The tricky part is to define, in a generic way, each polygon depending on the number of branches and sections. It is mostly trigonometry. I advise to start by drawing only the main lines and then create the small patches. The color part should then be easy because it depends only on the angle and you can thus use HSV encoding.
          
.. figure:: colors/flower-polar.pdf
   :width: 100%

   Flower polar (sources :source:`colors/flower-polar.py`)
   :label:`figure-flower-polar` 
