# Configuration file for the Sphinx documentation builder.

# -- Project information

import sys
import os
sys.path.append(os.path.dirname(__file__))
# Import the definition of external links
from conf_extlinks import extlinks, intersphinx_mapping
import sphinx_rtd_theme

project = 'NWB Overview'
copyright = ''
author = 'Ben Dichter, ...'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    #'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx.ext.extlinks',
    'sphinx_rtd_theme',
]

intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# -- Options for EPUB output
epub_show_urls = 'footnote'
