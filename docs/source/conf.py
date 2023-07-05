# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = 'osipi'
copyright = '2022, OSIPI'
author = 'OSIPI'
release = '0.1.1'

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones
extensions = [
    'sphinx.ext.napoleon', # parsing of NumPy and Google style docstrings
    'sphinx.ext.autodoc', # sphinx autodocumentation generation
    'sphinx.ext.autosummary', # generates function/method/attribute summary lists
    'sphinx.ext.viewcode', # viewing source code
    'sphinx.ext.intersphinx', # generate links to the documentation of objects in external projects
    'autodocsumm',
    'myst_parser', # parser for markdown language
    'sphinx_copybutton', # copy button for code blocks
    'sphinx_design', # sphinx web design components
    'sphinx_remove_toctrees', # selectively remove toctree objects from pages
]

# Add any paths that contain templates here, relative to this directory
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path
exclude_patterns = []

# -- Extension configuration -------------------------------------------------
# Map intersphinx to pre-exisiting documentation from other projects used in this project
intersphinx_mapping = {'python': ('https://docs.python.org/3/', None),
                        'numpy': ('https://numpy.org/doc/stable/', None),
                        'matplotlib': ('https://matplotlib.org/stable/', None),
                        'pydicom': ('https://pydicom.github.io/pydicom/stable/', None),
                        'nilabel': ('https://nipy.org/nibabel/', None),
                        'pandas': ('https://pandas.pydata.org/docs/', None)
                        }

autosummary_generate = True # enable autosummary extension

# Tell sphinx-autodoc-typehints to generate stub parameter annotations including
# types, even if the parameters aren't explicitly documented.
always_document_param_types = True

# Remove auto-generated API docs from sidebars.
remove_from_toctrees = ["_autosummary/*"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for a list of builtin themes
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "github_url": "https://github.com/plaresmedima/osipi",
    "collapse_navigation": True,
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css"
html_static_path = ['_static']

# The suffix(es) of source filenames.
source_suffix = ['.rst', '.md']

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'images/osipi.png'