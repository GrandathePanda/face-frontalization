Face Frontalization
===================

This is a Python port of the Face Frontalization code provided by
Hassner *et al.* at
http://www.openu.ac.il/home/hassner/projects/frontalize

The original code was written in Matlab and was ported to Python using
Numpy and OpenCV.

.. figure:: https://raw.githubusercontent.com/dougsouza/face-frontalization/master/example.png
   :alt: alt tag

   alt tag

Dependencies
~~~~~~~~~~~~

`Dlib Python Wraper <http://dlib.net>`__ >= 18.17

`OpenCV Python Wraper <http://opencv.org/downloads.html>`__ = 3.0.0

`SciPy <http://www.scipy.org/install.html>`__

-  Windows x64: I have provided compiled binaries for OpenCV 3.0.0 and
   Dlib 18.18
   `here <https://drive.google.com/file/d/0B7pvh2tbCWLLdElLYURTODdZSzg/view?usp=sharing>`__.
   Just drag the files to your python packages folder (e.g.
   site-packages). If they don't work, you'll have to compile them
   yourself.
-  Linux/OSX: You'll have to compile OpenCV and Dlib yourself.

Other Dependencies
~~~~~~~~~~~~~~~~~~

To run demo.py you must have:

`Matplotlib <http://matplotlib.org/>`__

Citation
~~~~~~~~

If you find this code useful please cite:

Tal Hassner, Shai Harel, Eran Paz and Roee Enbar, *Effective Face
Frontalization in Unconstrained Images*, IEEE Conf. on Computer Vision
and Pattern Recognition (CVPR), Boston, June 2015
