import nbformat
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a Jupyter Notebook to Jekyll Markdown.")
    parser.add_argument(metavar="notebook", nargs="+",
                        help="a notebook to convert", dest="notebooks")
    args = parser.parse_args()
    print(args.notebooks)