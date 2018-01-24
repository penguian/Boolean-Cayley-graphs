#!/bin/bash
BNBR=$1
FNBR=$2

BCG_SITE_DIR=${BCG_SITE_DIR:-"/short/y03/pcl851/lib/python2.7/site-packages"}

mkdir -p o
qsub -v QSUB_BNBR="$BNBR",QSUB_FNBR="$FNBR",BCG_SITE_DIR="$BCG_SITE_DIR" \
     save_cast128_from_parts.pbs

