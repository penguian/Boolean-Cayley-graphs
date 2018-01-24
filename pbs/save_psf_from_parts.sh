#!/bin/bash
SEQ_NBR=$1
FNBR=$2

BCG_SITE_DIR=${BCG_SITE_DIR:-"/short/y03/pcl851/lib/python2.7/site-packages"}
BCG_DATA_DIR=${BCG_DATA_DIR:-"/g/data1a/y03/pcl851/src/sage-sandbox/Boolean-Cayley-graphs"}

mkdir -p o
qsub -v QSUB_SEQ_NBR="$SEQ_NBR",QSUB_FNBR="$FNBR",BCG_SITE_DIR="$BCG_SITE_DIR",BCG_DATA_DIR="$BCG_DATA_DIR" \
     save_psf_from_parts.pbs

