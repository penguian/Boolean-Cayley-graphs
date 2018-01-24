#!/bin/bash
SEQ_NBR=$1
FNBR_BEG=$2
NBRF=${3:-1}
C_LEN=${4:-16}
NCPUS_PER_F=$((256 / C_LEN))
NCPUS=$((NBRF * NCPUS_PER_F))
MEM=$((NCPUS * 1))

BCG_SITE_DIR=${BCG_SITE_DIR:-"/short/y03/pcl851/lib/python2.7/site-packages"}
BCG_DATA_DIR=${BCG_DATA_DIR:-"/g/data1a/y03/pcl851/src/sage-sandbox/Boolean-Cayley-graphs"}
BCG_PARTS_DIR="${BCG_DATA_DIR}/parts"

mkdir -p $BCG_PARTS_DIR
mkdir -p o
qsub -l ncpus=${NCPUS} -l mem=${MEM}gb \
     -v QSUB_NCPUS="$NCPUS",QSUB_SEQ_NBR="$SEQ_NBR",QSUB_FNBR_BEG="$FNBR_BEG",QSUB_NBRF="$NBRF",QSUB_C_LEN="$C_LEN",BCG_PARTS_DIR="$BCG_PARTS_DIR",BCG_SITE_DIR="$BCG_SITE_DIR" \
     save_psf_in_mpi_parallel.pbs

