import os

from nbconvert.nbconvertapp import NbConvertApp, nbconvert_aliases, __version__, nbconvert_flags
from traitlets import default, observe, Unicode, Bool

nbtojekyll_aliases = {}
nbtojekyll_aliases.update(nbconvert_aliases)
nbtojekyll_aliases.update({
    "image-dir": "ImageExtractionPreprocessor.image_dir",
    "site-dir": "NBToJekyll.site_dir",
    "binder-link": "BinderLinkPreprocessor.binder_link",
    "md-title": "FrontMatterPreprocessor.title"
})

nbtojekyll_flags = {}
nbtojekyll_flags.update(nbconvert_flags)
nbtojekyll_flags.update(
    {
        "disable-toc": (
            {"FrontMatterPreprocessor": {
                "disable_toc": True
            }},
            "don't enable table of contents generation in YAML Front Matter of Markdown file"
        ),
        "disable-mathjax": (
            {"FrontMatterPreprocessor": {
                "disable_mathjax": True
            }},
            "don't enable Mathjax in YAML Front Matter of Markdown file"
        )
    }
)


class NBToJekyll(NbConvertApp):
    version = __version__
    name = "jupyter-nbtojeykyll"
    description = "Convert Java Jupyter notebooks to Markdown compatible with Jekyll and Mathjax."

    aliases = nbtojekyll_aliases
    flags = nbtojekyll_flags

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
