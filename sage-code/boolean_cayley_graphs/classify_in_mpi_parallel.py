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

from math import log
from sage.crypto.boolean_function import BooleanFunction
from sage.functions.other import Function_ceil

from boolean_cayley_graphs.bent_function import BentFunction
from boolean_cayley_graphs.classify_in_parallel import save_one_classification
from boolean_cayley_graphs.classify_in_parallel import save_one_class_part


def save_classifications_in_parallel(
    comm,
    name_prefix,
    list_of_f,
    start=0,
    stop=None):
    r"""
    """
    rank = comm.Get_rank()
    size = comm.Get_size()

    if stop == None:
        stop = len(list_of_f)
    for n in range(start + rank, stop, size):
        name = name_prefix + '_' + str(n)
        form = BooleanFunction(list_of_f[n]).truth_table(format='hex')
        save_one_classification(name, form)


def save_class_parts_in_parallel(
    comm,
    name_prefix,
    form,
    c_len=1):
    r"""
    """
    rank = comm.Get_rank()
    size = comm.Get_size()

    bentf = BentFunction(form)
    dim = bentf.nvariables()
    v = 2 ** dim
    ceil = Function_ceil()
    nbr_parts = ceil(v * 1.0 / c_len)
    nbr_digits = ceil(log(nbr_parts, 10))
    for n in range(rank, nbr_parts, size):
        n_str = '{0:0={width}}'.format(n, width=nbr_digits)
        save_one_class_part(
            name=name_prefix + '_' + n_str,
            bentf=bentf,
            c_start=c_len * n,
            c_stop=c_len * (n + 1))
