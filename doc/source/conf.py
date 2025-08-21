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
              "autoapi.extension"]

templates_path = ['_templates']
exclude_patterns = []

# -- Autoapi extension -------------------------------------------------------
autoapi_dirs = ['../../src']

# with open("../../project.yml") as file:
#     data = yaml.safe_load(file)
#     namespace = data["revolve2-namespace"]
#     platform_dependent = [
#         f"../../{pkg}/{namespace}" for pkg in data["platform_dependent_packages"]
#     ]
#     platform_independent = [
#         f"../../{pkg}/{namespace}" for pkg in data["platform_independent_packages"]
#     ]
#     autoapi_dirs = platform_dependent + platform_independent

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



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
