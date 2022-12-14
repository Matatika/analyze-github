from setuptools import setup, find_packages

setup(
    name="analyze-github",
    version="0.1.0",
    description="Meltano project file bundle of Matatika datasets for tap-github variant meltanolabs",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/datasets/tap-github/*.yml",
            "analyze/channels/*.yml"
        ]
    },
)
