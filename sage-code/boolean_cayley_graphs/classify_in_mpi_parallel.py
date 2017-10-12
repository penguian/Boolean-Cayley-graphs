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

from sage.crypto.boolean_function import BooleanFunction
from sage.functions.other import Function_ceil

from boolean_cayley_graphs.bent_function import BentFunction
from boolean_cayley_graphs.classify_in_parallel import save_one_classification
from boolean_cayley_graphs.classify_in_parallel import save_one_class_part


def scatter_functions_to_classify(
    comm,
    list_of_f,
    list_start,
    list_stop):
    r"""
    """
    size = comm.Get_size()
    nbr_workers = size - 1

    len_list = len(list_of_f)
    list_stop = (
        len_list
        if list_stop == None
        else min(list_stop, len_list))
    comm.bcast(list_stop, root=0)

    for start in range(list_start, list_stop, nbr_workers):
        stop = min(start + nbr_workers, list_stop)
        tuples_to_scatter = [
            (n, BooleanFunction(list_of_f[n]).truth_table(format='hex'))
            for n in range(start, stop)]

        list_to_scatter = [None] * size
        list_to_scatter[1 : 1 + stop - start] = tuples_to_scatter
        comm.scatter(list_to_scatter, root=0)


def save_some_classifications(
    comm,
    name_prefix):
    r"""
    """
    rank = comm.Get_rank()
    size = comm.Get_size()
    nbr_workers = size - 1

    list_stop  = comm.bcast(None, root=0)
    more = True
    while more:
        table_tuple = comm.scatter(None, root=0)

        if table_tuple == None:
            more = False
        else:
            n = table_tuple[0]
            name = name_prefix + '_' + str(n)
            table = table_tuple[1]
            save_one_classification(name, table)

            start = n - rank + 1
            more = start + nbr_workers < list_stop


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
    nbr_workers = size - 1

    if rank == 0:
        scatter_functions_to_classify(comm, list_of_f, start, stop)
    else:
        save_some_classifications(comm, name_prefix)


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
    for n in range(rank, nbr_parts, size):
        c_start = c_len * n
        c_stop  = c_len * (n + 1)
        name = name_prefix + '_' + str(n)
        save_one_class_part(
            name=name_prefix + '_' + str(n),
            bentf=bentf,
            c_start=c_len * n,
            c_stop=c_len * (n + 1))
