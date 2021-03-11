from nbconvert.exporters import MarkdownExporter

class JekyllExporter(MarkdownExporter):
    """Exports notebook to Markdown such that it can be rendered using Jekyll and Mathjax

    It
        * Replaces all single dollar sings with double dollar signs for Latex rendering
        * Replaces ```Java with ´´´java
        * Creates a valid YAML Front Matter with title and table of contents and Mathjax settings
        * Extracts images and replaces image paths
        * Generates binder link text snippet
    """

    # Name for use with "File -> Download" menu
    export_from_notebook = "JekyllMD"