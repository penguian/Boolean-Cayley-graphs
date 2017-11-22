#!/bin/bash
qsub -v QSUB_BNBR="$1",QSUB_FNBR="$2",QSUB_C_LEN="$3" save_cast128_in_mpi_parallel.pbs

