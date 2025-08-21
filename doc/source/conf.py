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

# Get the absolute path to the project root and then to src/ariel
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ariel_base_path = os.path.join(project_root, "src", "ariel")
ariel_packages = []

print(f"Looking for packages in: {ariel_base_path}")
print(f"Path exists: {os.path.exists(ariel_base_path)}")

if os.path.exists(ariel_base_path):
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
                ariel_packages.append(item_path)
                print(f"Found package: {item}")

    # Set autoapi_dirs to include all discovered packages
    autoapi_dirs = ariel_packages
    print(f"AutoAPI will document the following packages: {autoapi_dirs}")
else:
    print(f"Warning: {ariel_base_path} does not exist!")
    autoapi_dirs = ['../../src/ariel']  # fallback

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

# -- Autosectionlabel extension -----------------------------------------------

autosectionlabel_prefix_document = True



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_logo = "../resources/ariel_logo.png"
html_favicon = "../resources/ariel_logo.png"
html_static_path = ['_static']
