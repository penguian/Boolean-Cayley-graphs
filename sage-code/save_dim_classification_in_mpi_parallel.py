r"""
"""
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

import sys

from mpi4py import MPI
from sage.all_cmdline import *

from boolean_cayley_graphs.classify_in_mpi_parallel import save_class_parts_in_parallel

r"""
"""
# Check that the correct number arguments exist.
if len(sys.argv) != 4:
    print("Usage: save_dim_in_mpi_parallel dim fnbr c_len")
    sys.exit(1)

# Convert the arguments to int.
dim   = int(sys.argv[1])
fnbr  = int(sys.argv[2])
c_len = int(sys.argv[3])

# Get our MPI rank.
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Load the required bent function.
load("bent_function_extended_affine_representative_polynomials.sage")
list_of_f = bent_function_extended_affine_representative_polynomials(dim)
bentf = list_of_f[fnbr]

# Save the classification in parts with c_len matrix rows each.
save_class_parts_in_parallel(comm, "p"+str(dim)+"_"+str(fnbr)+"_test", bentf, c_len=c_len)
sys.exit(0)

