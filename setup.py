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
    install_requires=["numpy","psycopg2","sagemath"],
    dependency_links=["https://pypi.org/project/"],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)

