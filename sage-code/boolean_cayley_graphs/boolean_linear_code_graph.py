"""
Graph from linear code of a Boolean function.

Paul Leopardi.
"""

#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.graphs.strongly_regular_db import strongly_regular_from_two_weight_code

from boolean_linear_code import boolean_linear_code
from boolean_linear_code import linear_code_from_code_gens


def boolean_linear_code_graph(dim, f):
    r"""
    """
    L = boolean_linear_code(dim, f)
    return strongly_regular_from_two_weight_code(L)


def strongly_regular_from_code_gens(c):
    r"""
    """
    L = linear_code_from_code_gens(c)
    return strongly_regular_from_two_weight_code(L)
