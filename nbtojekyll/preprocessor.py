from nbconvert.preprocessors import Preprocessor


class JekyllPreprocessor(Preprocessor):
    """Preprocessor to add Jekyll metadata"""

    def preprocess(self, nb, resources):
        """Preprocess notebook

        Extracts images and adds


        Args:
            nb (NotebookNode): Notebook being converted.
            resources (dict): Additional resources used by preprocessors and filters.
        Returns:
            NotebookNode: Modified notebook.
            dict: Modified resources dictionary.
        """
        pass