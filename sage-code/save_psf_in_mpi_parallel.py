r"""
"""
#*****************************************************************************
#       Copyright (C) 2017 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

import sys

from mpi4py import MPI
from sage.all_cmdline import *

from boolean_cayley_graphs.bent_function import BentFunction
from boolean_cayley_graphs.classify_in_mpi_parallel import save_class_parts_in_parallel

r"""
"""
# Check that the correct number of arguments exist.
if len(sys.argv) < 4:
    print "Usage: save_psf_in_mpi_parallel psf_seq bnbr fnbr c_len [dir]"
    sys.exit(1)

# Convert the arguments to int.
seq_nbr  = int(sys.argv[1]) # Number of the partial spread function sequence
fnbr0    = int(sys.argv[2]) # First function number within partial spread function sequence
c_len    = int(sys.argv[3]) # Number of c values per class part.
d = None
if len(sys.argv) > 4:
    d = sys.argv[4]         # Directory to save to

# Get our MPI rank.
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Load the required bent function.
load("langevin_hou_partial_spreads.sage")
psf_seq_name = "../psf/psf-"+str(seq_nbr)+".txt"
psf_seq_file = open(psf_seq_name)
anf_list = read_langevin_hou_anf_list(psf_seq_file)

# Obtain the first bent function to determine the dimension.
bentf0 = BentFunction(anf_list[fnbr0])
dim = bentf0.nvariables()
v = 2 ** dim

# This script assumes that the number of parts per bent function is
# the Integer v // c_len, and the remainder v % c_len must be 0.
nbr_parts_per_bentf, remainder_v = divmod(v, c_len)
if remainder_v != 0:
    print "c_len is not a factor of 2 ** dim. Remainder is", remainder_v
    exit(1)

# This script also assumes that size is an integer multiple of
# the number of parts per bent function.
remainder_s = size % nbr_parts_per_bentf
if remainder_s != 0:
    print "nbr_parts_per_bentf is not a factor of size. Remainder is", remainder_s
    exit(1)

# Obtain the correct bent function for this rank
fnbr = fnbr0 + (rank // nbr_parts_per_bentf)
bentf = BentFunction(anf_list[fnbr])

# Save the classification in parts with c_len matrix rows each.
save_class_parts_in_parallel(
    comm,
    "psf"+str(seq_nbr)+"_"+str(fnbr),
    bentf,
    c_len=c_len,
    dir=d)
sys.exit(0)
