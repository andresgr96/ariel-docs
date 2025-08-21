# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ariel'
copyright = '2025, 0.1.0'
author = 'CI Group'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
import os
import sys
sys.path.insert(0, os.path.abspath("../../src"))

extensions = ["sphinx.ext.autodoc", 
              "sphinx.ext.apidoc", 
              "sphinx.ext.napoleon", 
              "sphinx.ext.viewcode",
              "sphinx.ext.doctest",
              "sphinx.ext.duration",
              "sphinx.ext.autosectionlabel",
              "autoapi.extension"]

templates_path = ['_templates']
exclude_patterns = []

# -- Autoapi extension -------------------------------------------------------

import os
import glob

# Dynamically find all package directories in src/ariel
ariel_base_path = "../../src/ariel"
ariel_packages = []

# Get all subdirectories in the ariel package
for item in os.listdir(ariel_base_path):
    item_path = os.path.join(ariel_base_path, item)
    # Check if it's a directory and contains Python files or has __init__.py
    if os.path.isdir(item_path):
        # Check if it's a Python package (has __init__.py or contains .py files)
        has_init = os.path.exists(os.path.join(item_path, "__init__.py"))
        has_py_files = bool(glob.glob(os.path.join(item_path, "*.py")))
        has_subdirs_with_py = any(
            glob.glob(os.path.join(item_path, "**", "*.py"), recursive=True)
        )
        
        if has_init or has_py_files or has_subdirs_with_py:
            ariel_packages.append(os.path.join(ariel_base_path, item))

# Set autoapi_dirs to include all discovered packages
autoapi_dirs = ariel_packages

print(f"AutoAPI will document the following packages: {autoapi_dirs}")

autoapi_options = [
    "members",
    "undoc-members",
    "special-members",
    "show-inheritance",
    "show-inheritance-diagram",
    "imported-members",
    "show-module-summary",
    "titles_only=True",
]
autoapi_add_toctree_entry = True
autoapi_template_dir = "_templates/autoapi"

# -- Autosectionlabel extensio -----------------------------------------------

autosectionlabel_prefix_document = True



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_logo = "../resources/ariel_logo.png"
html_favicon = "../resources/ariel.png"
html_static_path = ['_static']
