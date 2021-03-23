from nbconvert.preprocessors import Preprocessor
from traitlets import Bool, Unicode


class FrontMatterPreprocessor(Preprocessor):
    """Preprocessor to add Jekyll metadata"""

    disable_toc = Bool(False).tag(config=True)
    disable_mathjax = Bool(False).tag(config=True)
    title = Unicode(
        "",
        help="Title of the Markdown page as given in the YAML Front Matter"
    ).tag(config=True)

    def preprocess(self, nb, resources):
        """Preprocess notebook

        Adds Jekyll metadata for YAML Front Matter.

        Args:
            nb (NotebookNode): Notebook being converted.
            resources (dict): Additional resources used by preprocessors and filters.
        Returns:
            NotebookNode: Modified notebook.
            dict: Modified resources dictionary.
        """
        toc = "true" if not self.disable_toc else "false"
        mathjax = "true" if not self.disable_mathjax else "false"

        metadata = {}
        metadata.update({"title": self.title, "toc": toc, "mathjax": mathjax})
        resources["metadata"]["jekyll"] = metadata

        return nb, resources