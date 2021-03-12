import setuptools

setuptools.setup(
    entry_points={
        "nbconvert.exporters": [
            "jekyllmd = nbtojekyll:JekyllExporter"
        ]
    }
)
