r"""
Classification in parallel using MPI
====================================

The ``classify_in_mpi_parallel`` module defines functions that
use MPI to save Cayley graph classifications or partial classifications in parallel.

AUTHORS:

- Paul Leopardi (2017-10-13)

"""
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from builtins import str
from builtins import range
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
    stop=None,
    directory=None):
    r"""
    Using MPI, construct and save a number of Cayley graph classifications
    corresponding to a list of bent functions.

    INPUT:

    - ``comm`` -- MPI communicator.
    - ``name_prefix`` -- String. Name prefix to use with ``save_mangled`` to save each classification.
    - ``list_of_f`` -- List of forms or bent functions.
    - ``start`` -- Integer. Default=0. Index of start position in the list.
    - ``stop`` -- Integer. Default=None. Index after end position, or ``None`` if whole remaining list.
    - ``directory`` -- string, optional. The directory where the object
      is to be saved. Default is None, meaning the current directory.

    OUTPUT: None.

    EFFECT: Uses ``name`` to save the classifications corresponding to ``list_of_f``.
    """
    rank = comm.Get_rank()
    size = comm.Get_size()

    if stop == None:
        stop = len(list_of_f)
    for n in range(start + rank, stop, size):
        name = name_prefix + '_' + str(n)
        form = BooleanFunction(list_of_f[n]).truth_table(format='hex')
        save_one_classification(
            name,
            form,
            directory=directory)


def save_class_parts_in_parallel(
    comm,
    name_prefix,
    form,
    c_len=1,
    directory=None):
    r"""
    Using MPI, construct a complete list of the partial Cayley graph classifications
    corresponding to a given bent function or algebraic normal form.

    INPUT:

    - ``comm`` -- MPI communicator.
    - ``name_prefix`` -- String. Name prefix to use with ``save_mangled`` to save each class part.
    - ``form`` -- A bent function or an algebraic normal form.
    - ``c_len`` -- Integer. Default=1. The number of values of `c` to use in each class part.
    - ``directory`` -- string, optional. The directory where the object
      is to be saved. Default is None, meaning the current directory.

    OUTPUT: None.

    EFFECT: Uses ``name_prefix`` to save all partial classifications corresponding to ``bentf``.
    """
    rank = comm.Get_rank()
    size = comm.Get_size()

    bentf = BentFunction(form)
    dim = bentf.nvariables()
    v = 2 ** dim
    ceil = Function_ceil()
    nbr_parts = ceil(v * 1.0 / c_len)

    # Include the case where size > nbr_parts and therefore
    # this function is being applied to many bent functions in parallel.
    if size > nbr_parts:
        beg_n = rank % nbr_parts
        end_n = beg_n + 1
    else:
        beg_n = rank
        end_n = nbr_parts

    nbr_digits = ceil(log(nbr_parts, 10))
    for n in range(beg_n, end_n, size):
        n_str = '{0:0={width}}'.format(n, width=nbr_digits)
        save_one_class_part(
            name=name_prefix + '_' + n_str,
            bentf=bentf,
            c_start=c_len * n,
            c_stop=c_len * (n + 1),
            directory=directory)
