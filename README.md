# py_volanalytics

`py_volanalytics` is a python library containing robust implementations of algorithms, analytical formulae and semi-analytical results used for volatility modeling. It also offers implementations of the core blocks one needs for such tasks - optimizers, fourier transforms, characteristic functions, FFT etc.

Over time, the cost of writing my own library and the understanding and flexibility that comes with it will hopefully outweigh the sunk cost of building things ground up. 

Cookbooks
--------
 - [Implementing *Arbitrage free smoothing of IVS*, Mathias Fengler](./cookbooks/fengler_volatility_smoothing.ipynb)
 - [Interpolators](./cookbooks/interpolators_ex.ipynb)
 
Installation
-------------
The easiest way to install `py_volanalytics` is by using `pip`:

```
# to install the latest release (from PyPI)
pip install py_volanalytics

# to install the latest release (using Conda)
conda install -c conda-forge py_volanalytics

# to install the latest commit (from GitHub)
pip install git+https://github.com/quasar-chunawala/py_volanalytics

# to clone and install from a local copy
git clone https://github.com/quasar-chunawala/py_volanlytics.git
cd py_volanalytics
pip install -e .
```

PyPi package
------------
[py_volanalytics](https://pypi.org/project/py-volanalytics/0.1.0/)

References
----------
- [The local volatility surface](https://emanuelderman.com/wp-content/uploads/1996/06/gs-local_volatility_surface.pdf), *Emanuel Derman, 1996*
