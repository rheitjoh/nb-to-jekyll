import setuptools

setuptools.setup(
    entry_points={
        "nbconvert.exporters": [
            "jekyllmd = nb-to-jekyll:JekyllExporter"
        ]
    }
)
