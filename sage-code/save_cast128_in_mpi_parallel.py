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
    print "Usage: save_dim_in_mpi_parallel dim fnbr c_len"
    sys.exit(1)

# Convert the arguments to int.
bnbr  = int(sys.argv[1]) # S-box number
fnbr  = int(sys.argv[2]) # Function number within S-box
c_len = int(sys.argv[3]) # Number of c values per class part.

# Get our MPI rank.
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Load the required bent function.
load("read_cast_128_s_boxes.sage")
s_boxes = read_s_boxes_file()
bentf = s_boxes[bnbr][fnbr]

# Save the classification in parts with c_len matrix rows each.
save_class_parts_in_parallel(
    comm,
    "cast128_"+str(bnbr)+"_"+str(fnbr),
    bentf,
    c_len=c_len)
sys.exit(0)
