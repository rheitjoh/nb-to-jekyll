import setuptools

setuptools.setup(
    packages=["nbtojekyll"],
    entry_points={
        "nbconvert.exporters": [
            "jekyllmd = nbtojekyll:JekyllExporter"
        ],
        "console_scripts": [
            "jupyter-nbtojekyll = nbtojekyll.nbtojekyll:NBToJekyll.launch_instance"
        ]
    }
)
