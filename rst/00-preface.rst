.. ----------------------------------------------------------------------------
.. Title:   Scientific Visualisation - Python & Matplotlib
.. Author:  Nicolas P. Rougier
.. License: Creative Commons BY-NC-SA International 4.0
.. ----------------------------------------------------------------------------
.. include:: common.rst
.. _chap-preface:

Preface
========

About the author
----------------

Nicolas P. Rougier is a full-time researcher in computational cognitive
neuroscience, located in Bordeaux, France. He's doing his research at Inria
(the French institute for computer science) and the Institute of
Neurodegenerative Diseases where he investigates decision making, learning and
cognition using computational models of the brain and distributed, numerical
and adaptive computing, a.k.a. artificial neural networks and machine
learning. His research aims to irrigate the fields of philosophy with regard to
the mind-body problem, medicine to account for the normal and pathological
functioning of the brain and the digital sciences to offer alternative
computing paradigms. Beside neuroscience and philosophy, he's also interested
in open and reproducible science (he has co-founded ReScience C with Konrad
Hinsen and ReScience X with Etienne Roesch), scientific visualization (he
created glumpy, co-created VisPy), Science outreach (e.g. The Conversation) and
computer graphics (especially digital typography).

Nicolas P. Rougier has been using Python for more than 20 years and Matplotlib
for more than 15 years for modeling in neuroscience, machine learning and for
advanced visualization. Nicolas P. Rougier is the author of several online
resources and tutorials and he's teaching Python, NumPy and scientific
visualisation at the University of Bordeaux as well as at various conferences
and schools worldwide.


About this book
---------------

This open access book has been written in reStructuredText_ converted to LaTeX
using docutils and exported to Portable Document Format using XeLaTeX. Sources
are available at `github.com/rougier/python-scientific-visualisation
<https://github.com/rougier/python-scientific-visualisation>`_


How to contribute
-----------------

If you want to contribute to this book, you can:

* Review chapters & suggest improvements 
* Report issues & correct my English 
* Star the project on GitHub & buy the printed book  


Prerequisites
-------------

This book is not a Python beginner guide and you should have an intermediate
level in Python and ideally a beginner level in NumPy. If this is not the case,
have a look at the bibliography for a curated list of resources.

Conventions
-----------

We will use usual naming conventions. If not stated explicitly, each script
should import NumPy, SciPy and Matplotlib as:

.. code:: Python

   import scipy
   import numpy as np
   import matplotlib.pyplot as plt


We'll use up-to-date versions (at the date of writing, June 2019) of the
different packages:

.. code:: Python

   >>> import sys; print(sys.version)
   3.7.4 (default, Jul  9 2019, 18:13:23)
   [Clang 10.0.1 (clang-1001.0.46.4)]
   >>> import numpy; print(numpy.__version__)
   1.16.4
   >>> import scipy; print(scipy.__version__)
   1.3.0
   >>> import matplotlib; print(matplotlib.__version__)
   3.1.0

   
License
-------

This volume is licensed under a Creative Commons Attribution Non Commercial
Share Alike 4.0 International License, which permits use, sharing, adaptation,
distribution and reproduction in any medium or format, as long as you give
appropriate credit to the original author(s) and the source, provide a link to
the Creative Commons license, and indicate if changes were made. You may not
use the material for commercial purposes. If you remix, transform, or build
upon the material, you must distribute your contributions under the same
license as the original. To learn more, visit `creativecommons.org`_.

Unless stated otherwise, all the figures are licensed under a Creative Commons
Attribution 4.0 International License and all the code is licensed under a BSD
2-clause license.

.. --- Links ------------------------------------------------------------------
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _creativecommons.org: https://creativecommons.org/
.. ----------------------------------------------------------------------------
