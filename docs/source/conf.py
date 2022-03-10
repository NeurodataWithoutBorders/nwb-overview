# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'NWB Overview'
copyright = ''
author = 'Ben Dichter, ...'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx.ext.extlinks',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'matplotlib': ('https://matplotlib.org', None),
    'h5py': ('https://docs.h5py.org/en/latest/', None),
    'hdmf': ('https://hdmf.readthedocs.io/en/latest/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
}

extlinks = {
    'incf_lesson': ('https://training.incf.org/lesson/%s', ''),
    'incf_collection': ('https://training.incf.org/collection/%s', ''),
    'nwb_extension': ('https://github.com/nwb-extensions/%s', ''),
    'pynwb': ('https://github.com/NeurodataWithoutBorders/pynwb/%s', '')
}


intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
