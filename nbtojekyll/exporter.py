import os

from nbconvert.exporters import MarkdownExporter
from traitlets import default


class JekyllExporter(MarkdownExporter):
    """Exports notebook to Markdown such that it can be rendered using Jekyll and Mathjax

    It
        * Replaces all single dollar sings with double dollar signs for Latex rendering
        * Replaces ```Java with ´´´java
        * Creates a valid YAML Front Matter with title and table of contents and Mathjax settings
        * Extracts images and replaces image paths
        * Generates binder link text snippet
    """

    # name for use with "File -> Download" menu
    export_from_notebook = "JekyllMD"

    # path to available template files
    extra_template_basedirs = [
        os.path.join(os.path.dirname(__file__), "templates")
    ]

    @default("template_name")
    def _template_name_default(self):
        """Default template name"""
        return "jekyllmd"

