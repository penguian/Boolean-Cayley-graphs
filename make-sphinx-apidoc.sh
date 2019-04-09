#!/bin/bash
#
# To execute this script, use "sage -sh"
#
# To upload updated apidoc to leopardi@SourceForge (2017), use:
# rsync -avz --delete doc/_build/html/ leopardi@web.sourceforge.net:/home/project-web/boolean-cayley-graphs/htdocs/
#
source ./bcg_version.sh

# Create doc/references.rst from boolean_cayley_graphs/references.py
sage<<EOF
from boolean_cayley_graphs.references import print_sage_references_index_rst
ref_file = open("doc/references.rst","w")
print_sage_references_index_rst(file=ref_file)
quit
EOF
pushd doc

# Use sphinx-apidoc to re-create the documentation from the Python files in ../boolean_cayley_graphs
sphinx-apidoc -e -H "Boolean-Cayley-graphs" -A "Paul Leopardi" \
    -V ${BCG_VERSION} -R ${BCG_RELEASE} \
    -o . ../boolean_cayley_graphs
make html
popd
