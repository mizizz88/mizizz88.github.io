from recommonmark.parser import CommonMarkParser
import os
import sys

sys.path.insert(0, os.path.abspath('.'))

source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']
master_doc = 'index'

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ProtectHealth Documentation'
copyright = '2023, Protecthealth Corporation Sdn Bhd'
author = 'Digital Technologies, Protecthealth Corporation Sdn Bhd'
release = '2023'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser',
              'sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_path = ["_themes", ]
html_static_path = ['_static']
html_theme_options = {
    'logo_only': True,
    'navigation_depth': 5,
}
# html_logo = "media/"
html_show_sourcelink = False
html_favicon = "media/fav.png"
html_context = {
    'display_github': True,
    'github_user': 'mizizz88',
    'github_repo': 'mizizz88.github.io',
    'github_version': '',
}

pygments_style = 'sphinx'
todo_include_todos = True
