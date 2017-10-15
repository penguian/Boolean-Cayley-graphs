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

from mpi4py import MPI
from sage.all_cmdline import *

from boolean_cayley_graphs.classify_in_mpi_parallel import save_class_parts_in_parallel

r"""
"""
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

load("bent_function_extended_affine_representative_polynomials.sage")
list_of_f = bent_function_extended_affine_representative_polynomials_dimension_6()
bentf = list_of_f[4]

save_class_parts_in_parallel(comm, 'p6_4_n_str_test', bentf, c_len=4)
quit
