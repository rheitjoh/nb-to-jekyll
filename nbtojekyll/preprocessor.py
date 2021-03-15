from nbconvert.preprocessors import Preprocessor, HighlightMagicsPreprocessor
from traitlets import Dict


class JekyllPreprocessor(Preprocessor):
    """Preprocessor to add Jekyll metadata"""

    def preprocess(self, nb, resources):
        """Preprocess notebook

        Extracts images and adds Jekyll metadata for YAML Front Matter.

        Args:
            nb (NotebookNode): Notebook being converted.
            resources (dict): Additional resources used by preprocessors and filters.
        Returns:
            NotebookNode: Modified notebook.
            dict: Modified resources dictionary.
        """
        name = resources["metadata"]["name"]
        # TODO: Make TOC and Mathjax be settable using cli argument
        # TODO: Use first head for title instead of name?
        metadata = {"title": name, "toc": "true", "mathjax": "true"}
        resources["metadata"]["jekyll"] = metadata

        return nb, resources


class JavaMagicsPreprocessor(HighlightMagicsPreprocessor):

    def which_magic_language(self, source):
        """
        When a cell uses another language through a magic extension,
        the other language is returned.
        If no language magic is detected, this function returns java.

        Parameters
        ----------
        source: str
            Source code of the cell to highlight
        """
        magic_language = super().which_magic_language(source)
        if magic_language is None:
            # we assume java in this case
            return "java"