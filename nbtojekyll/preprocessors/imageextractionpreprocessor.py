# Based on https://gist.github.com/sglyon/5687b8455a0107afc6f4c60b5f313670
import os
from binascii import a2b_base64

from nbconvert.preprocessors import Preprocessor
from traitlets import Unicode, Set


class ImageExtractionPreprocessor(Preprocessor):
    """
    Extracts .png and .jpg images from the notebook
    """

    output_filename_template = Unicode(
        "{notebook_name}_attach_{cell_index}_{name}"
    ).tag(config=True)

    extract_output_types = Set(
        {"image/png", "image/jpeg"}
    ).tag(config=True)

    def preprocess_cell(self, cell, resources, cell_index):
        """
        Extracts images from given cell.
        """
        image_dir = resources.get("image_dir", None)
        if image_dir is None:
            self.log.debug("No image-dir specified. Skipping image extraction")
            return cell, resources

        site_dir = resources.get("site_dir", None)
        if site_dir is None:
            self.log.debug("No site-dir specified. Skipping image extraction")
            return cell, resources

        if not isinstance(resources["outputs"], dict):
            resources["outputs"] = {}

        # loop over all attachments and extract supported output types
        for name, attach in cell.get("attachments", {}).items():
            for mime, data in attach.items():
                if mime not in self.extract_output_types:
                    continue

                data = a2b_base64(data)

                filename = self.output_filename_template.format(
                    notebook_name=resources["metadata"]["name"],
                    cell_index=cell_index,
                    name=name
                )

                # filename for storage on filesystem is different
                storage_filename = os.path.join(site_dir, image_dir, filename)

                # image can be retrieved via resources dictionary
                # this is used by nbconvert to actually store the output to filesystem
                resources["outputs"][storage_filename] = data

                # Correct link in cell source
                # Link needs to be based on the Jekyll site directory as root
                filename = os.path.join("/", image_dir, filename)
                attach_str = "attachment:" + name
                if attach_str in cell.source:
                    cell.source = cell.source.replace(attach_str, filename)

        return cell, resources