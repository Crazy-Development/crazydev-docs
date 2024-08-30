# -- Project information -----------------------------------------------------
project = 'Your Project Name'
copyright = '2024, Your Name'
author = 'Your Name'

# The full version, including alpha/beta/rc tags
release = '0.1.0'

# -- General configuration ---------------------------------------------------

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# Path to source directory (relative to this file)
# This should match the structure of your documentation directory
source_suffix = '.rst'
source_dir = 'source'

# Master document (source file without extension)
master_doc = 'index'

# List of extensions to enable
extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # For Google style docstrings
    'sphinx.ext.viewcode',  # For viewing source code
    'sphinx_rtd_theme',  # Read the Docs theme
]

# Autosummary settings
autosummary_generate = True

# Paths that contain templates, relative to this directory
templates_path = ['_templates']

# List of patterns to ignore when looking for source files
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'

# Theme options
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',  # e.g. "UA-XXXXXXX-1"
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '',
}

# Paths for static files (relative to this directory)
html_static_path = ['_static']

# Additional templates that should be rendered to pages
# The default theme uses these to build the search index
html_extra_path = []


