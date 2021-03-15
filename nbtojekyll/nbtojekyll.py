from nbconvert.nbconvertapp import NbConvertApp
from traitlets import default, observe


class NBToJekyll(NbConvertApp):

    @default("export_format")
    def _export_format_default(self):
        """Default export format"""
        return "jekyllmd"

    @observe("export_format")
    def _export_format_changed(self, change):
        """Ensure export format is jekyllmd"""
        default_format = self._export_format_default()

        if change["new"].lower() != default_format:
            raise ValueError(
                f"Invalid export format {change['new']}, value must be {default_format}"
            )