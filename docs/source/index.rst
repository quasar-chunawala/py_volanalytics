.. py_volanalytics documentation master file, created by
   sphinx-quickstart on Wed Apr  9 21:46:17 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

``py_volanalytics`` documentation
=================================

``py_volanalytics`` is a python library containing robust implementations of algorithms, analytical formulae and semi-analytical results used for volatility modeling. It also offers implementations of the core blocks one needs for such tasks - optimizers, fourier transforms, characteristic functions, FFT etc.

Currently, *py_volanalytics* supports the following features:



Installation
============
The easiest way to install ``py_volanalytics`` is by using ``pip``:

.. code:: none

   # to install the latest release (from PyPI)
   pip install py_volanalytics

   # to install the latest release (using Conda)
   conda install -c conda-forge py_volanalytics

   # to install the latest commit (from GitHub)
   pip install git+https://github.com/quasar-chunawala/py_volanalytics

   # to clone and install from a local copy
   git clone https://github.com/quasar-chunawala/py_volanlyticss.git
   cd py_volanalytics
   pip install -e .


.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   short_rate_models
   the_hjm_framework
   modules

.. automodule:: py_volanalytics
   :members:
   :undoc-members:
   :show-inheritance:

