from setuptools import setup, find_packages
import os
import io

VERSION = "0.4.9"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="modbamtools",
    description="A set of tools to manipulate and visualize data from base modification bam files",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Roham Razaghi",
    url="https://github.com/rrazaghi/modbamtools",
    project_urls={
        "Issues": "https://github.com/rrazaghi/modbamtools/issues",
        "CI": "https://github.com/rrazaghi/modbamtools/actions",
        "Changelog": "https://github.com/rrazaghi/modbamtools/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        modbamtools=modbamtools.cli:cli
    """,
    install_requires=[
        "click>=8.1.8",
        "pysam>=0.23.3",
        "scipy>=1.10.1",
        "pandas>=2.0.3",
        "numpy>=1.24.4",
        "plotly>=6.5.0",
        "modbampy==0.5.3",
        "kaleido>=1.2.0",
        "pyBigWig>=0.3.22",
        "choreographer>=1.2.1"
        "PyPDF2",
        "pillow",
        "hdbscan",
        "tqdm",
    ],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.8, <=3.10.5",
)
