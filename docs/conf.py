#!/usr/bin/env python
#
# oleo documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#
import os
import sys
import jupytext

sys.path.insert(0, os.path.abspath(".."))

import oleo

master_doc = "index"  # The master toctree document.s
# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
add_module_names = False  # Remove namespaces from class/method signatures
autoapi_add_toctree_entry = True
autoapi_dirs = ["../oleo"]
autoapi_keep_files = True
autoapi_template_dir = "_autoapi_templates"
autosummary_generate = True  # Turn on sphinx.ext.autosummary
autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries
autodoc_inherit_docstrings = True  # If no docstring, inherit from base class
author = "Dario Quintero"
copyright = "2023, Dario Quintero"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
extensions = [
    "autoapi.extension",
    "IPython.sphinxext.ipython_console_highlighting",
    "nbsphinx",  # Integrate Jupyter Notebooks and Sphinx
    "myst_parser",
    "sphinx.ext.autodoc",  # Core Sphinx library for auto html doc generation from docstrings
    "sphinx.ext.autosummary",  # Create neat summary tables for modules/classes/methods etc
    "sphinx.ext.coverage",
    "sphinx.ext.intersphinx",  # Link to other project's documentation (see mapping below)
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",  # Add a link to the Python source code for classes, functions etc.
    "sphinx_autodoc_typehints",  # Automatically document param types (less noise in class signature)
    "sphinx_gallery.load_style",
    "sphinx-pydantic",
]

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (master_doc, "oleo.tex", "oleo Documentation", "Dario Quintero", "manual"),
]
html_show_sourcelink = (
    False  # Remove 'view source code' from top of page (for html, not python)
)
html_static_path = ["_static"]
html_theme = "alabaster"
htmlhelp_basename = "oleodoc"
man_pages = [(master_doc, "oleo", "oleo Documentation", [author], 1)]
project = "oleo"
pygments_style = "sphinx"
release = oleo.__version__
set_type_checking_flag = True  # Enable 'expensive' imports for sphinx_autodoc_typehints
source_suffix = [".rst", ".md"]
templates_path = ["_templates"]
texinfo_documents = [
    (
        master_doc,
        "oleo",
        "oleo Documentation",
        author,
        "oleo",
        "One line description of project.",
        "Miscellaneous",
    ),
]
todo_include_todos = False

mathjax3_config = {
    "tex": {"tags": "ams", "useLabelIds": True},
}
nbsphinx_allow_errors = True  # Continue through Jupyter errors
nbsphinx_custom_formats = {
    ".py": lambda s: jupytext.reads(s, ".py"),
}
version = oleo.__version__

latex_elements: dict = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}
