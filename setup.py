from setuptools import setup, find_packages

setup(
    name="analyze-github",
    version="0.2.0",
    description="Meltano project file bundle of Matatika datasets for tap-github variant meltanolabs",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/datasets/tap-github/*.yml",
            "orchestrate/tap-github/elt.sh"
        ]
    },
)
