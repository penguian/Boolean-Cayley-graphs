#!/bin/bash
export SAGE_PKGS=$HOME/.sage
export SAGE_PATH=$(pwd)/sage-code:$(pwd)
export PYTHONPATH=$SAGE_PATH:$PYTHONPATH
PACKAGE_DIR="boolean_cayley_graphs"
POSTGRES_MODULE="boolean_cayley_graphs/classification_database_psycopg2.py"
WHOLE_PACKAGE="$PACKAGE_DIR/*.py"
PACKAGE_EXCEPT_POSTGRES=$(echo ${WHOLE_PACKAGE} | sed "s?$POSTGRES_MODULE ??")
IS_POSTGRES_RUNNING="
import psycopg2
import sys
try:
    psycopg2.connect(dbname='postgres')
except:
    sys.exit(1)
"
if python3 -c "${IS_POSTGRES_RUNNING}"
then
    sage -t ${WHOLE_PACKAGE}
else
    echo "Postgres is not running: ${POSTGRES_MODULE} will not be tested."
    sage -t ${PACKAGE_EXCEPT_POSTGRES}
fi
