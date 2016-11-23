"""
Linear code of a Boolean function.

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

from sage.arith.srange import xsrange
from sage.coding.linear_code import LinearCode
from sage.matrix.constructor import matrix
from sage.rings.finite_rings.finite_field_constructor import FiniteField as GF

from integer_bits import inner


def boolean_linear_code(dim, f):
    r"""
    """
    v = 2 ** dim
    support = [
        y
        for y in xsrange(v)
        if f(y) == 1]
    M = matrix(GF(2), [[
        inner(x, y)
        for y in support]
        for x in xsrange(v)])
    return LinearCode(M)
