from nbconvert.preprocessors import Preprocessor


class FrontMatterPreprocessor(Preprocessor):
    """Preprocessor to add Jekyll metadata"""

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
        name = resources["metadata"]["name"]
        # TODO: Make TOC and Mathjax be settable using cli argument
        # TODO: Use first head for title instead of name?
        metadata = {"title": name, "toc": "true", "mathjax": "true"}
        resources["metadata"]["jekyll"] = metadata

        return nb, resources