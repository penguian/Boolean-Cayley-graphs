#!/bin/bash
DIM=$1
FNBR=$2
C_LEN=${3:-16}
NCPUS=$((2**DIM / C_LEN))
MEM=$((NCPUS * 1))
BCG_SITE_DIR=${BCG_SITE_DIR:-"/short/y03/pcl851/lib/python2.7/site-packages"}

qsub -l ncpus=${NCPUS} -l mem=${MEM}gb \
     -v QSUB_NCPUS="$NCPUS",QSUB_DIM="$DIM",QSUB_FNBR="$FNBR",QSUB_C_LEN="$C_LEN",BCG_SITE_DIR="$BCG_SITE_DIR" \
     save_dim_in_mpi_parallel.pbs

