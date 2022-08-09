.. ----------------------------------------------------------------------------
.. Title:   Scientific Visualisation - Python & Matplotlib
.. Author:  Nicolas P. Rougier
.. License: Creative Commons BY-NC-SA International 4.0
.. ----------------------------------------------------------------------------
.. _chap-layout:

Size, aspect & layout
=====================

The layout of figures and sub-figures is certainly one of the most
frustrating aspect of matplotlib and for new user, it is generally
difficult to obtain the desired layout without a lot of trials and
errors.. But this is not specific to matplotlib, it is actually
equally difficult with any software (and even worse for some). To
understand why it is difficult, it is necessary to gain a better
understanding of the underlying machinery.

Figure and axes aspect
----------------------

When you create a new figure, this figure comes with a specific size, either implicitly using defaults (as explained in the previous chapter) or explicitly through the `figsize` keyword. If we take the height divided by the width of the figure we obtain the figure aspect ratio. When you create an axes, you can also specify an aspect that will be enforced by matplotlib. And here, we hit the first difficulty. You have a container with a given aspect ratio and you want to put inside an item with a possibly different aspect ratio and matplotlib has to solve these constrains. This is illustrated on figure :ref:`figure-aspects` with different cases:

**A**: figure aspect is 1, axes aspect is 1, x and y range are equal

  .. code:: python

     fig = plt.figure(figsize=(6,6))
     ax = plt.subplot(1,1,1, aspect=1)
     ax.set_xlim(0,1), ax.set_ylim(0,1) 
     
     
**B**: figure aspect is 1/2, axes aspect is 1, x and y range are equal

  .. code:: python

     fig = plt.figure(figsize=(6,3))
     ax = plt.subplot(1,1,1, aspect=1)
     ax.set_xlim(0,1), ax.set_ylim(0,1) 
     
**C**: figure aspect is 1/2, axes aspect is 1, x and y range are different

  .. code:: python

     fig = plt.figure(figsize=(6,3))
     ax = plt.subplot(1,1,1, aspect=1)
     ax.set_xlim(0,2), ax.set_ylim(0,1) 
     
     
**D**: figure aspect is 2, axes aspect is 1, x and y range are equal

  .. code:: python

     fig = plt.figure(figsize=(3,6))
     ax = plt.subplot(1,1,1, aspect=1)
     ax.set_xlim(0,1), ax.set_ylim(0,1) 
     

**E**: figure aspect is 1, axes aspect is 1, x and y range are different

  .. code:: python

     fig = plt.figure(figsize=(6,6))
     ax = plt.subplot(1,1,1, aspect=1)
     ax.set_xlim(0,2), ax.set_ylim(0,1) 
     
     
**F**: figure aspect is 1, axes aspect is 0.5, x and y range are equal

  .. code:: python

     fig = plt.figure(figsize=(6,6))
     ax = plt.subplot(1,1,1, aspect=0.5)
     ax.set_xlim(0,1), ax.set_ylim(0,1) 
     
**G**: figure aspect is 1/2, axes aspect is 1, x and y range are different

  .. code:: python

     fig = plt.figure(figsize=(3,6))
     ax = plt.subplot(1,1,1, aspect=1)
     ax.set_xlim(0,1), ax.set_ylim(0,2) 

**H**: figure aspect is 1, axes aspect is 1, x and y range are different

  .. code:: python

     fig = plt.figure(figsize=(6,6))
     ax = plt.subplot(1,1,1, aspect=1)
     ax.set_xlim(0,1), ax.set_ylim(0,2) 
     
**I**: figure aspect is 1, axes aspect is 2, x and y range are equal

  .. code:: python

     fig = plt.figure(figsize=(6,6))
     ax = plt.subplot(1,1,1, aspect=2)
     ax.set_xlim(0,1), ax.set_ylim(0,1) 


.. figure:: layout/aspects.pdf
   :width: 100%
           
   Combination of figure and axes aspect ratio
   :label:`figure-aspects` 


The final layout of a figure results from a set of constraints that makes it  difficult to predict the end result. This is actually even more acute when you combine several axes on the same figure as shown on figures 
:ref:`figure-layout-aspect-1`, :ref:`figure-layout-aspect-2` & :ref:`figure-layout-aspect-3`. Depending on what is important in your figure (aspect, range or size), you'll privilege one of these layouts. In any case, you should now have realized that if you over-constrained your layout, it might be unsolvable and matplotlib will try to find the best compromise.

.. figure:: layout/layout-aspect-1.pdf
   :width: 100%

   Same size, same range, different aspect
   (sources :source:`layout/layout-aspect.py`)
   :label:`figure-layout-aspect-1`


.. figure:: layout/layout-aspect-2.pdf
   :width: 100%

   Same range, same aspect, different size
   (sources :source:`layout/layout-aspect.py`)
   :label:`figure-layout-aspect-2`
          

.. figure:: layout/layout-aspect-3.pdf
   :width: 100%

   Same size, same aspect, different range
   (sources :source:`layout/layout-aspect.py`)
   :label:`figure-layout-aspect-3`


Axes layout
-----------

Now that we know how figure and axes aspect may interact, it's time to organize our figure into subfigures. We've already seen one example in the previous section, but let's now look at the details. There exist indeed several `different methods <https://matplotlib.org/stable/tutorials/intermediate/gridspec.html>`_ to create subfigures and each have their pros and cons. Let's take a very simple example where we want to have two axes side by side. To do so, we can use `add_subplot <https://matplotlib.org/stable/api/figure_api.html?highlight=add_subplot#matplotlib.figure.Figure.add_subplot>`_, `add_axes <https://matplotlib.org/stable/api/figure_api.html?highlight=add_axes#matplotlib.figure.Figure.add_axes>`_, `GridSpec <https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html?highlight=gridspec#matplotlib.gridspec.GridSpec>`_ and `subplot_mosaic <https://matplotlib.org/stable/api/figure_api.html?#matplotlib.figure.Figure.subplot_mosaic>`_:

.. code:: python

   fig = plt.figure(figsize=(6,2))

   # Using subplots
   ax1 = fig.add_subplot(1,2,1)
   ax2 = fig.add_subplot(1,2,2)

   # Using gridspecs
   G = GridSpec(1,2)
   ax1 = fig.add_subplot(G[0,0])
   ax2 = fig.add_subplot(G[0,1])

   # Using axes
   ax1 = fig.add_axes([0.1, 0.1, 0.35, 0.8])
   ax2 = fig.add_axes([0.6, 0.1, 0.35, 0.8])
   
   # Using mosaic
   ax1, ax2 = fig.add_mosaic("AB")


As a general advice, I would encourage users to use the gridspec
approach because if offers a lot of flexibility compared to the
classical approach. For example, figure :ref:`figure-layout-classical`
shows a nice and simple 3x3 layout but does not offer much control
over the relative aspect of each axes whereas in figure
:ref:`figure-layout-gridspec`, we can very easily specify different
sizes for each axes.
           
.. figure:: layout/layout-classical.pdf
   :width: 100%

   Subplots using classical layout.
   (source :source:`layout/layout-classical.py`)
   :label:`figure-layout-classical`

.. figure:: layout/layout-gridspec.pdf
   :width: 100%

   Subplots using gridspec layout
   (source :source:`layout/layout-gridspec.py`)
   :label:`figure-layout-gridspec`

The biggest difficulty with gridspec is to get axes right, that is, at
the right position with the right size and this depends on the initial
partition of the grid spec, taking into account the different height &
width ratios. Let's consider for example figure
:ref:`figure-complex-layout` that display a moderately complex
layout. The question is: how do we partition it? Do we need a single
axis for the small image of individual axes ? Are the text on the left
part of axes or do they use their own axes. There are indeed several
solutions and figure :ref:`figure-complex-layout-bare` shows the
solution I chose to design this figure. There are individual axes for
subplots and left label. There is also a small line of axes for titles
in order to ensure that subplots have all the same size. If I had used
a title on the first row of subplots, this would have modified their
relative size compared to others. The legend on the top is using two
axes, one axes for the color legend and another for detailed
explanation. In this case, I use the central axes and write the text
outside the axes, specifying this does not need to be clipped.
                           
.. figure:: layout/complex-layout.pdf
   :width: 100%

   Complex layout
   (source :source:`layout/complex-layout.py`)
   :label:`figure-complex-layout`

.. figure:: layout/complex-layout-bare.pdf
   :width: 100%

   Complex layout structure
   (source :source:`layout/complex-layout-bare.py`)
   :label:`figure-complex-layout-bare`

          
Exercises
---------

**Standard layout 1** Using gridspec, the goal is to reproduce figure 
:ref:`figure-standard-layout-1` where the colorbar is the same size as the main axes and its width is one tenth of main axis width.
       
.. figure:: layout/standard-layout-1.pdf
   :width: 100%

   Image and colorbar
   (sources :source:`layout/standard-layout-1.py`)
   :label:`figure-standard-layout-1`

**Standard layout 2** Using gridspec, the goal is to reproduce figure 
:ref:`figure-standard-layout-2` with top and right histograms aligned with the main axes.

.. figure:: layout/standard-layout-2.pdf
   :width: 100%

   Scatter plot and histograms
   (sources :source:`layout/standard-layout-2.py`)
   :label:`figure-standard-layout-2`
