# nbtojekyll
Converts Jupyter Java notebooks to Markdown that can be rendered using Jekyll, Kramdown, and Mathjax.

Currently Work in Progress.

Inspired by the [JekyllNB](https://github.com/klane/jekyllnb) package.

## Features

- Converts single dollar signs $ to double dollar signs $$ as required by Kramdown for correct 
  Latex rendering. Also inserts newlines before and after existing $$ to support math blocks.
    
- \`\`\`Java is converted to \`\`\`java to allow for correct syntax highlighting

- Extraction of images included in the notebook

- Automatic addition of a YAML Front Matter with title, table of contents, and mathjax enabled.

## Quickstart

Python 3 is required for installation. You will also need Jupyter and nbconvert for usage.

### Installation

The library is currently not hosted on PyPI, so you will have to install it locally.
To do that, clone this repository, open a terminal with working directory in this repository's
root folder and execute
```bash
python -m pip install --upgrade --force-reinstall --no-deps --no-cache-dir .
```
This will install the library for the Python version given by your `python` executable.
The rest of the arguments are to ensure that the package is reinstalled even if the version number
stays the same.

### Usage

There are two ways to use nbtojekyll: Via nbconvert or directly.

To use via nbconvert, simply specify `jekyllmd` as the format to export to (via nbconvert's `--to`)
parameter. However, this does not support image extraction.

Direct usage follows this template:
```bash
jupyter nbtojekyll <ARGUMENTS>
```
nbtojekyll uses nbconvert under the hood and therefore supports all the commandline arguments that
nbconvert supports.
It additionally adds the following options:

- `--site-dir SITE_DIR`: If specified, SITE_DIR should be the path to the root of the Jekyll site
  to which the converted notebook belongs. This path is used to construct the paths where the
  extracted images will be stored on your local filesystem. Default is the current working directory
  when executing nbtojekyll.
  
- `--image-dir IMAGE_DIR`: If specified, IMAGE_DIR should be the path where the extracted images 
  should be stored relative to the Jekyll site root path. The path should be given without a leading
  separator. Default is `assets/images`.
  
These arguments are optional. 
However, make sure that the Jekyll site root directory is the current working directory when 
executing without them. 
Otherwise, the images might not be stored where you want them to.
  

 