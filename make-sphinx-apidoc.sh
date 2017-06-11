#!/bin/bash
BCG_VERSION=${1:-"0.0"}
BCG_RELEASE=${2:-${BCG_VERSION}.1}
sphinx-apidoc -e -F -H "Boolean-Cayley-graphs" -A "Paul Leopardi" -V ${BCG_VERSION} -R ${BCG_RELEASE} -o doc sage-code
cd doc
make html
