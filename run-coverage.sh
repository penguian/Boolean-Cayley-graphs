#!/bin/bash
export SAGE_PATH=$(pwd)/sage-code
export PYTHONPATH=$SAGE_PATH:$PYTHONPATH
sage --coverage sage-code/boolean_cayley_graphs/*.py
