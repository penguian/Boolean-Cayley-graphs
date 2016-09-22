
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.graphs.strongly_regular_db import strongly_regular_from_two_weight_code


def linear_code_from_code_gens(c):
    M = matrix(GF(2), [list(s) for s in c])
    return LinearCode(M)

def strongly_regular_from_code_gens(c):
    """
    Given the tuple of strings `c` which encodes the generators of a two-weight code,
    the function `strongly_regular_from_code_gens`
    returns the corresponding strongly regular graph `G`.
    """
    return strongly_regular_from_two_weight_code(linear_code_from_code_gens(c))
