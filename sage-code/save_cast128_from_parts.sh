#!/bin/bash
qsub -v QSUB_BNBR="$1",QSUB_FNBR="$2" save_cast128_from_parts.pbs

