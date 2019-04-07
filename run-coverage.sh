#!/bin/bash
export SAGE_PATH=$(pwd)/sage-code:$(pwd)
export PYTHONPATH=$SAGE_PATH:$PYTHONPATH
sage --coverage boolean_cayley_graphs/*.py
