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


import random

from boolean_cayley_graphs.bent_function import BentFunction
from boolean_cayley_graphs.bent_function_cayley_graphs_of_c_translates import cayley_graphs_of_c_translates

import boolean_cayley_graphs.cayley_graph_controls as controls

load("langevin_hou_partial_spreads.sage")


def nbr_cayley_graphs_of_c_translates(anf_list, n):
    r"""
    """

    if controls.verbose and controls.timing:
        print n

    anf = anf_list[n]
    bentf = BentFunction(anf)
    cg_list = cayley_graphs_of_c_translates(bentf)
    len_cg_list = len(cg_list)

    if controls.verbose:
        print n, ":", len_cg_list

    return len_cg_list


def sample_nbr_cayley_graphs_of_c_translates(anf_file, sample_size, seed=None):
    r"""
    """

    random.seed(seed)
    anf_list = read_langevin_hou_anf_list(anf_file)

    nbr_bent_functions = len(anf_list)
    nbr_list = [0] * sample_size
    for n in range(sample_size):
        r = random.randint(0, nbr_bent_functions - 1)
        len_cg_list = nbr_cayley_graphs_of_c_translates(anf_list, r)
        nbr_list[n] = len_cg_list

    return nbr_list


def list_nbr_cayley_graphs_of_c_translates(anf_file, start=0):
    r"""
    """

    anf_list = read_langevin_hou_anf_list(anf_file)

    nbr_bent_functions = len(anf_list) - start
    nbr_list = [0] * nbr_bent_functions
    for n in range(start, start + nbr_bent_functions):
        len_cg_list = nbr_cayley_graphs_of_c_translates(anf_list, n)
        nbr_list[n - start] = len_cg_list

    return nbr_list
