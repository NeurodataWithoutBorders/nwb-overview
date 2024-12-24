# Configuration file for the Sphinx documentation builder.

# -- Project information

import sys
import os
sys.path.append(os.path.dirname(__file__))
# Import the definition of external links
from conf_extlinks import extlinks
from conf_extlinks import intersphinx_mapping
from conf_nwb_analytics import build_project_analytics
import sphinx_rtd_theme


project = 'NWB Overview'
copyright = 'Neurodata Without Borders'
author = 'Ben Dichter, Lawrence Niu, Ryan Ly, Oliver Ruebel'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    # 'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx.ext.extlinks',
    'sphinx_design',
    'sphinx_rtd_theme',
    'sphinx_tabs.tabs',
]

intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'img/favicon_96.png'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None
html_logo = 'img/logo_brain_transp.png'

html_theme_options = {
    # 'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    # 'analytics_anonymize_ip': False,
    'logo_only': False,  # Only show the NWB logo without the documentation title
    'display_version': False,  # Do not show the version of the docs
    'prev_next_buttons_location': 'bottom',  # Show previous/next button at the bottom
    'style_external_links': True,  # Add marker to indicate external links
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'black',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# these links cannot be checked in github actions
linkcheck_ignore = [
    "https://crates.io/crates/nwbview",
    r"https://.*\.incf\.org/.*",  # temporary ignore until SSL certificate issue is resolved
]

# -- Build the nwb project analytics in the current directory
build_project_analytics(target_dir=os.path.dirname(__file__))
