#!/bin/bash
BNBR=$1
FNBR=$2
C_LEN=${3:-16}
NCPUS=$((256 / C_LEN))
MEM=$((NCPUS * 1))
BCG_SITE_DIR=${BCG_SITE_DIR:-"/short/y03/pcl851/lib/python2.7/site-packages"}

qsub -l ncpus=${NCPUS} -l mem=${MEM}gb \
     -v QSUB_NCPUS="$NCPUS",QSUB_BNBR="$BNBR",QSUB_FNBR="$FNBR",QSUB_C_LEN="$C_LEN",BCG_SITE_DIR="$BCG_SITE_DIR" \
     save_cast128_in_mpi_parallel.pbs

