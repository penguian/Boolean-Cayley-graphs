#!/bin/bash
#
# To execute this script, use "sage -sh"
#
# To upload updated apidoc to leopardi@SourceForge (2017), use:
# rsync -avz --delete doc/_build/html/ leopardi@web.sourceforge.net:/home/project-web/boolean-cayley-graphs/htdocs/
#
export BCG_VERSION=${1:-"0.1"}
export BCG_RELEASE=${2:-"${BCG_VERSION}.1.1"}

# Create doc/references.rst from sage-code/boolean_cayley_graphs/references.py
pushd sage-code
sage<<EOF
from boolean_cayley_graphs.references import print_sage_references_index_rst
ref_file = open("../doc/references.rst","w")
print_sage_references_index_rst(file=ref_file)
quit
EOF
popd
pushd doc

# Use sphinx-apidoc to re-create the documentation from the Python files in ../sage-code/boolean_cayley_graphs
sphinx-apidoc -e -H "Boolean-Cayley-graphs" -A "Paul Leopardi" \
    -V ${BCG_VERSION} -R ${BCG_RELEASE} \
    -o . ../sage-code/boolean_cayley_graphs
make html
popd
