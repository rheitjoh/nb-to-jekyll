from nbconvert.preprocessors import Preprocessor
from traitlets import Unicode, Set


class ImageExtractionPreprocessor(Preprocessor):

    output_filename_template = Unicode(
        "attach_{cell_index}_{name}"
    ).tag(config=True)

    extract_output_types = Set(
        {"image/png", "image/jpeg"}
    ).tag(config=True)

    def preprocess_cell(self, cell, resources, cell_index):
        pass