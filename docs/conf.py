# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

# Import the version string
from testrepocomputing._version import __version__

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'testrepocomputing'
copyright = '2025, Andrea Simonelli'
author = 'Andrea Simonelli'
release = '__version__'

rst_prolog = f"""
.. |Python| replace:: `Python <https://www.python.org/>`__
.. |Sphinx| replace:: `Sphinx <https://www.sphinx-doc.org/en/master/>`__
.. |numpy| replace:: `NumPy <https://numpy.org/>`__
.. |GitHub| replace:: `GitHub <https://github.com/>`__
"""

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'undoc-members': True,
    'private-members': True
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_permalinks_icon = '<span>#</span>'
pygments_style = 'default'
pygments_dark_style = 'default'
#html_theme_options = {
#    'awesome_external_links': True,
#}
html_static_path = ['_static']
