from nbconvert.preprocessors import Preprocessor

binder_note_prefix = """\n\n---\n*Note:*\nYou can also check this page out in an
interactive Jupyter notebook by clicking the badge below:\n\n
[![Binder](https://mybinder.org/badge_logo.svg)]("""
binder_note_suffix = """)\n\n---\n"""


class BinderLinkPreprocessor(Preprocessor):

    def preprocess(self, nb, resources):
        """Adds a binder link to execute the Jupyter notebook in an interactive environment."""
        # get the repository path
        binder_link = resources["binder_link"]

        if binder_link != "" and len(nb.cells) > 0:
            # insert at end of first cell
            nb.cells[0].source += binder_note_prefix + binder_link + binder_note_suffix

        return nb, resources