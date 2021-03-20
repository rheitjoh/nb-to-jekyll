import os

from nbconvert.nbconvertapp import NbConvertApp, nbconvert_aliases, __version__
from traitlets import default, observe, Unicode

nbtojekyll_aliases = {}
nbtojekyll_aliases.update(nbconvert_aliases)
nbtojekyll_aliases.update({
    "image-dir": "NBToJekyll.image_dir",
    "site-dir": "NBToJekyll.site_dir"
})


class NBToJekyll(NbConvertApp):

    version = __version__
    name = "jupyter-nbtojeykyll"
    description = "Convert Java Jupyter notebooks to Markdown compatible with Jekyll and Mathjax."

    aliases = nbtojekyll_aliases

    site_dir = Unicode(
        ".",
        help="The root directory of the Jekyll site."
    ).tag(config=True)

    image_dir = Unicode(
        "assets/images",
        help="""Directory in which to place extracted images. Root is the Jekyll site directory.
        For example, 'assets/images'. Path should not start with a '/'!
        """
    ).tag(config=True)

    @default("export_format")
    def _export_format_default(self):
        """Default export format"""
        return "jekyllmd"

    @observe("export_format")
    def _export_format_changed(self, change):
        """Ensures export format is jekyllmd"""
        default_format = self._export_format_default()

        if change["new"].lower() != default_format:
            raise ValueError(
                f"Invalid export format {change['new']}. Value must be {default_format}"
            )

    def init_writer(self):
        super().init_writer()
        # set build_directory to working directory to make sure images are stored based on
        # given Jekyll site dir and not the notebook dir
        if hasattr(self.writer, 'build_directory') and self.writer.build_directory == "":
            self.writer.build_directory = "."

    def init_single_notebook_resources(self, notebook_filename):
        """Initializes resources for a single notebook

        :param notebook_filename: Filename of the notebook being coverted
        :return: Fully initialized resources dictionary for notebook
        """
        resources = super().init_single_notebook_resources(notebook_filename)
        resources["image_dir"] = self.image_dir
        resources["site_dir"] = self.site_dir
        self.log.info("Image dir '%s'", str(resources["image_dir"]))
        self.log.info("Site dir '%s'", str(resources["site_dir"]))
        self.log.info("Extracted images will be stored in '%s'",
                      os.path.join(resources["site_dir"], resources["image_dir"]))

        return resources