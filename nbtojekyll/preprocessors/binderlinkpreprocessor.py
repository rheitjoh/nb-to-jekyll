from nbconvert.preprocessors import Preprocessor
from traitlets import Unicode

binder_note_prefix = """\n\n---\n*Note:*\nYou can also check this page out in an
interactive Jupyter notebook by clicking the badge below:\n\n
[![Binder](https://mybinder.org/badge_logo.svg)]("""
binder_note_suffix = """)\n\n---\n"""


class BinderLinkPreprocessor(Preprocessor):

    binder_link = Unicode(
        "",  # default is to not insert binder badge
        help="""""Full link to the Jupyter notebook on Binder. Specifiying this argument will 
        induce addition of a note at the end of the first section where the user can access the 
        Binder link."""
    ).tag(config=True)

    def preprocess(self, nb, resources):
        """Adds a binder link to execute the Jupyter notebook in an interactive environment."""
        # get the repository path
        if self.binder_link != "" and len(nb.cells) > 0:
            self.log.debug("Binder link specified as '%s'", str(resources["binder_link"]))
            # insert at end of first cell
            nb.cells[0].source += binder_note_prefix + self.binder_link + binder_note_suffix
        else:
            self.log.debug("No binder link specified. Not inserting it")

        return nb, resources