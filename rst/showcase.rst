.. ----------------------------------------------------------------------------
.. Title:   Scientific Visualisation - Python & Matplotlib
.. Author:  Nicolas P. Rougier
.. License: Creative Commons BY-NC-SA International 4.0
.. ----------------------------------------------------------------------------
.. _chap-showcase:

Showtime.

:raw-latex:`\fullpagefigure{showcases/contour-dropshadow.png}`
:raw-latex:`\phantomsection \addcontentsline{toc}{chapter}{Filled contours with dropshadows}`
           
**Filled contours with dropshadows** is a nice effect that allows you
to use a sequential colormap (here Viridis) while distinguishing
positive and negative values. If you look closely at the figure, you
can see that the drop shadow is external for positive values and
internal for negative values. To achieve this result, the contours
need to be rendered individually twice. In the first pass, I render a
contour offscreen and read the resulting image into an array. I then
use a Gaussian filter to blur it a bit and transform the image to make
it full black but the alpha channel. I can then display the image
using imshow and it will gracefully blend with elements already
presents in the figure. I then add the same contour using the colormap
and I iterate the process. The trick is to start from bottom to top
such that dropshadows remain visible.

**Sources:** :source:`showcases/contour-dropshadow.py`


:raw-latex:`\fullpagefigure{showcases/domain-coloring.pdf}`
:raw-latex:`\phantomsection \addcontentsline{toc}{chapter}{Domain coloring}`
           
**Domain coloring** is a "technique for visualizing complex functions
by assigning a color to each point of the complex plane. By assigning
points on the complex plane to different colors and brightness, domain
coloring allows for a four dimensional complex function to be easily
represented and understood. This provides insight to the fluidity of
complex functions and shows natural geometric extensions of real
functions" `[Wikipedia]
<https://en.wikipedia.org/wiki/Domain_coloring>`__.  On the figure on
the left, I represented the imaginary function :math:`z +
\nicefrac{1}{z}` in the domain :math:`[-2.5, 2.5]^2`. I used the angle
of the (complex) result for setting the color and the absolute cosine
of the norm for modulating it periodically.  I could have used a cyclic
colormap such as `twilight` but I think the `Spectral` is visually
more pleasant, even though it induces some discontinuities. To draw
the grid, I used a contour plot using integer values in the real and
imaginary domain.

**Sources:** :source:`showcases/domain-coloring.py`

:raw-latex:`\fullpagefigure{showcases/escher.pdf}`
:raw-latex:`\phantomsection \addcontentsline{toc}{chapter}{Escher like projections}`
           
**Escher like projections** can be obtained using the complex exponential
function and some specific periods that can be computed quite
easily. To do the figure on the left, I mostly followed explanations
given by Craig S. Kaplan, professor at the University of Waterloo on
his blog post `Escher-like Spiral Tilings (2019)
<https://isohedral.ca/escher-like-spiral-tilings/>`_. The only
difficulty in making this figure is line thickness. If you compare this
figure with the previous one, you may have noticed that in the
previous figure, lines have a constant thickness while in this figure,
thickness varies. To achieve such effect, we have to use a polygon
made of several segment with varying thickness. This poses no real
difficulty, only some geometrical computations.
           
**Sources:** :source:`showcases/escher.py`

           
:raw-latex:`\fullpagefigure{showcases/VSOM.png}`
:raw-latex:`\phantomsection \addcontentsline{toc}{chapter}{Self-organizing maps}`
           
**Self-organizing map** (SOM) "is a type of artificial neural network
that is trained using unsupervised learning to produce a
low-dimensional (typically two-dimensional), discretized
representation of the input space of the training samples, called a
map, and is therefore a method to do dimensionality reduction"
`[Wikipedia] <https://en.wikipedia.org/wiki/Self-organizing_map>`_. I
developed with Georgios Detorakis a `randomized self-organizing map
<https://arxiv.org/pdf/2011.09534.pdf>`_ based on blue noise
distribution of neurons. The figure on the left shows the
self-organisation of the map when fed with random RGB colors. The
figure itself is made of a polygon collection where each polygon is
painted with the color of the neuron. No real difficulty, but I had to
take care of disabling antialiasing, else, thin lines appear
between polygons.

**Sources:** `github.com/rougier/VSOM <https://github.com/rougier/VSOM>`__


:raw-latex:`\fullpagefigure{showcases/waterfall-3d.pdf}`
:raw-latex:`\phantomsection \addcontentsline{toc}{chapter}{Waterfall plots}`
           
**Waterfall plot** "is a three-dimensional plot in which multiple
curves of data, typically spectra, are displayed
simultaneously. Typically the curves are staggered both across the
screen and vertically, with 'nearer' curves masking the ones
behind. The result is a series of "mountain" shapes that appear to be
side by side. The waterfall plot is often used to show how
two-dimensional information changes over time or some other variable"
`[Wikipedia] <https://en.wikipedia.org/wiki/Waterfall_plot>`__ To do
the figure, I used a 3D axis and polygons (i.e. not filled plot). The
reason to use polygon is to obtain the color gradient effect on each
curve. The only way to do that (to the best of my knowledge), is to
slice horizontally each curve in several stripes and to render the
slice using a specific color. The difficulty is to compute those
irregular slices and this is the reason I use the `Shapely library
<https://github.com/Toblerity/Shapely>`_ that allows, among many other
things, to compute the intersection between polygons.

**Sources:** :source:`showcases/waterfall-3d.py`


:raw-latex:`\fullpagefigure{showcases/windmap.png}`
:raw-latex:`\phantomsection \addcontentsline{toc}{chapter}{Streamlines}`
           
**Streamlines** are a "family of curves that are instantaneously
tangent to the velocity vector of the flow. These show the direction
in which a massless fluid element will travel at any point in time"
`[Wikipedia]
<https://en.wikipedia.org/wiki/Streamlines,_streaklines,_and_pathlines>`__. The
figure on the left shows such stream lines and is actually a still
from an animation. Each streamline has been split into line segments
and gathered in a line collection such that each segment has its own
color. From there, it is easy to suggest stream direction using
gradients. Note that I could have used a single line collection for
all streamlines. Strangely enough, the only difficulty in this figure
are the line round caps. For the reason explained `here
<https://stackoverflow.com/questions/11578760>`_, I had to create a
specific graphic context such as to have round caps.

**Sources:** :source:`showcases/windmap.py`


:raw-latex:`\fullpagefigure{showcases/mandelbrot.png}`
:raw-latex:`\phantomsection \addcontentsline{toc}{chapter}{Mandelbrot set}`
           
The **Mandelbrot set** "is the set of complex numbers :math:`c`for
which the function :math:`f_{c}(z) = z^{2} + c` does not diverge when
iterated from :math:`z = 0`, i.e., for which the sequence
:math:`f_{c}(0)`, :math:`f_{c}(f_{c}(0))`, etc., remains bounded in
absolute value `[Wikipedia]
<https://en.wikipedia.org/wiki/Mandelbrot_set>`__.  To plot the figure
on the left, I used a regular imshow with shading and normalized
recounts that is explained on this post `Smooth Shading for the
Mandelbrot Exterior
<https://linas.org/art-gallery/escape/smooth.html>`__. The script is
also present in the matplotlib gallery which I contributed some years
ago.

**Sources:** :source:`showcases/mandelbrot.py`


:raw-latex:`\fullpagefigure{showcases/recursive-voronoi.pdf}`
:raw-latex:`\phantomsection \addcontentsline{toc}{chapter}{Recursive Voronoi}`
           
This **recursive Voronoi set** has been quite painful to design
because it requires some quite precise settings to obtain what I think
is a beautiful result. These settings are the placement of random
points with good visual properties and for that, I use the `Fast
Poisson Disk Sampling
<https://www.cct.lsu.edu/~fharhad/ganbatte/siggraph2007/CD2/content/sketches/0250.pdf>`__
by Robert Bridson which is simple and fast. I also use quite
extensively the shapely library to clip he different polygons and I
discovered in the meantime how to draw random points inside a
polygon. Finally, I played with lines thickness, polygons color and
transparency to achieve this result, involving 5 levels of
recursion. On my computer, it takes around 1 minute to compute.

**Sources:** :source:`showcases/recursive-voronoi.py`

:raw-latex:`\fullpagefigure{showcases/elevation.png}`
:raw-latex:`\phantomsection \addcontentsline{toc}{chapter}{3D Heightmap}`
           
A **3D heightmap** of Mount St Helens after it exploded. This has been
made with my `experimental 3D axis
<https://github.com/rougier/matplotlib-3d>`__. Nothing really
complicated here, just a bit slow because it needs to sort a bunch of
triangles.


:raw-latex:`\fullpagefigure{showcases/mosaic.pdf}`
:raw-latex:`\phantomsection \addcontentsline{toc}{chapter}{Voronoi mosaic}`

This **Voronoi mosaic** is based on blue noise distribution where each
Voronoi cell has been painted according to the color of the center of
the Voronoi cell in the original image. This results in a cheap
stained glass window effect.

**Sources:** :source:`showcases/mosaic.py`


:raw-latex:`\fullpagefigure{showcases/text-shadow.png}`
:raw-latex:`\phantomsection \addcontentsline{toc}{chapter}{Text shadow}`

This **shadowed text** is harder to design than it seems. I started
from a text path object and iterated over the segments composing the
path in order to create sheared rectangles that constitute the shadow. To
make the shadow disappear in the background, I created an image with a
vertical gradient using semi-transparent color (fully transparent on
top and fully opaque on the bottom). This results in a nice fading
shadow effect.
           
**Sources:** :source:`showcases/text-shadow.py`


:raw-latex:`\fullpagefigure{showcases/text-spiral.pdf}`
:raw-latex:`\phantomsection \addcontentsline{toc}{chapter}{Text spiral}`


This **spiral text** has been made using an `Archimedean spiral
<https://en.wikipedia.org/wiki/Archimedean_spiral>`__ (:math:`r =
a + b\theta`) that guarantees a constant speed along a line that
rotates with constant angular velocity. Said differently, successive
turnings of the spiral have a constant separation distance. Starting
from a very long text path representing some of the decimals of pi
(using the `mpmath <https://github.com/fredrik-johansson/mpmath>`__
library), it's then only a matter of transforming the vertices to
follow the spiral.
           
**Sources:** :source:`showcases/text-spiral.py`
