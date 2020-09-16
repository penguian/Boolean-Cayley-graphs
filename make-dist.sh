#!/bin/bash
#
# To execute this script, use "sage -sh"
#
# To upload the dist to Pypi, use:
# twine upload "dist/boolean_cayley_graphs-${BCG_RELEASE}-py3-none-any.whl"
#
source ./bcg_version.sh

sage -python setup.py bdist_wheel
