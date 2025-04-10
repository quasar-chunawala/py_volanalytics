# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('../../src/py_volanalytics/'))

project = 'py_volanalytics'
copyright = '2025, Quasar Chunawala'
author = 'Quasar Chunawala'
release = '0.1.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Optional: For Google/NumPy-style docstrings
    'sphinx.ext.viewcode',  # Optional: Adds links to source code
    'sphinx.ext.mathjax',
    'myst_parser',
    #'sphinx-copybutton',
    #'sphinxext-rediraffe',
    'sphinx_pyscript',
    #'sphinx-togglebutton',
]

myst_enable_extensions = [
    "amsmath",  # Enables support for $$ math blocks
    "dollarmath"  # Enables support for inline and block math using $ and $$
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
