# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'my-lecture-memo'
copyright = '2025, KikuzCom1207'
author = 'KikuzCom1207'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_markdown_tables',
    'sphinx_copybutton',
    'sphinxcontrib.mermaid',
    'sphinx_diagrams',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

# ソースファイルの拡張子の設定
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Master document
master_doc = 'index'

# MyST-Parserの設定
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
]

# sphinx_copybuttonの設定
copybutton_prompt_text = '>>> '
copybutton_prompt_is_regexp = True

# sphinxcontrib-mermaidの設定
mermaid_output_format = 'svg'

# カスタムCSSの設定
html_css_files = [
    'custom.css',
]
