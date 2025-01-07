#!/bin/env python
import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

try:
    version = os.environ["BCG_RELEASE"]
except:
    version = "0.0.0.0"

setuptools.setup(
    name="boolean_cayley_graphs",
    version=version,
    author="Paul Leopardi",
    author_email="paul.leopardi@gmail.com",
    description="Investigations of Boolean functions, their Cayley graphs, and associated structures.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/penguian/Boolean-Cayley-graphs",
    packages=["boolean_cayley_graphs"],
    exclude=["CAST-128","doc","nectar","papers-talks","pbs","sage-code","sobj"],
    install_requires=[
        "numpy",
    ],
    dependency_links=["https://pypi.org/project/"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    extras_require={
        # Use one of these two
        "psycopg2": [
            "psycopg2",
        ],
        "psycopg2-binary": [
            "psycopg2-binary",
        ],
        # Use one of these two
        "sagemath": [
            #"sagemath-standard",
        ],
        "passagemath": [
            "passagemath-brial",
            "passagemath-cliquer",
            "passagemath-flint",
            "passagemath-gap",
            "passagemath-graphs",
            "passagemath-modules",
            "passagemath-pari",
            "passagemath-plot",
            "passagemath-repl",
            "passagemath-symbolics",
        ],
    },
)

