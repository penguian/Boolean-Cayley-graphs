r"""
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
    Return the Boolean linear code corresponding to ``f``, assuming dimension ``dim``.

    INPUT:

    - ``dim`` -- positive integer. The assumed dimension of ``f``.
    - ``f`` -- a Python function that takes a positive integer and returns 0 or 1.

    OUTPUT:

    An object of class ``LinearCode`` representing the Boolean linear code
    corresponding to ``f``.

    REFERENCES:

    [Car2010]_

    [Din2015]_ Corollary 10.

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


def linear_code_from_code_gens(c):
    r"""
    """
    M = matrix(GF(2), [list(s) for s in c])
    return LinearCode(M)


def print_latex_code_parameters(c):
    r"""
    """
    print (
        "[" + str(c.length()) +
        "," + str(c.dimension()) +
        "," + str(c.minimum_distance()) + "]"),


