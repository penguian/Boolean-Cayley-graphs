r"""
The ``boolean_linear_code`` module defines the functions:

 * ``boolean_linear_code_graph``;
   which returns the Boolean linear code corresponding to a Boolean function,
 * ``linear_code_from_code_gens``;
   which return the Boolean linear code corresponding to a list of generators; and
 * ``print_latex_code_parameters``,
   which prints the standard parameters of a linear code.

AUTHORS:

- Paul Leopardi (2016-10-28): initial version

"""
#*****************************************************************************
#       Copyright (C) 2016-2017 Paul Leopardi paul.leopardi@gmail.com
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

from boolean_cayley_graphs.integer_bits import inner


def boolean_linear_code(dim, f):
    r"""
    Return the Boolean linear code corresponding to a Boolean function.

    INPUT:

    - ``dim`` -- positive integer. The assumed dimension of function ``f``.
    - ``f`` -- a Python function that takes a positive integer and returns 0 or 1.
      This is assumed to represent a Boolean function on :math:`\mathbb{F}_2^{dim}`
      via lexicographical ordering.

    OUTPUT:

    An object of class ``LinearCode``, representing the Boolean linear code
    corresponding to the Boolean function represented by ``f``.

    EXAMPLES:

    ::

        sage: from sage.crypto.boolean_function import BooleanFunction
        sage: bf = BooleanFunction([0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,1])
        sage: dim = bf.nvariables()
        sage: from boolean_cayley_graphs.boolean_linear_code import boolean_linear_code
        sage: bc = boolean_linear_code(dim, bf)
        sage: bc.characteristic_polynomial()
        -2/3*x + 2
        sage: bc.generator_matrix().echelon_form()
        [1 0 0 0 1]
        [0 1 0 0 0]
        [0 0 1 0 0]
        [0 0 0 1 1]

    REFERENCES:

    .. Carlet [Car2010]_.

    .. Calderbank and Kantor [CalK1986]_.

    .. Ding [Din2015]_ Corollary 10.

    """
    v = 2 ** dim
    support = [
        y
        for y in xsrange(v)
        if f(y) == 1]
    M = matrix(GF(2), [[
        inner(2 ** k, y)
        for y in support]
        for k in xsrange(dim)])
    return LinearCode(M)


def linear_code_from_code_gens(gens):
    r"""
    Return the Boolean linear code corresponding to a list of generators.

    INPUT:

    - ``gens`` -- list. A list of strings of 0,1 characters.
      This is assumed to represent the generators of a linear code.

    OUTPUT:

    An object of class ``LinearCode`` representing the Boolean linear code
    corresponding to the generators represented by ``gens``.

    EXAMPLE:

    ::

        sage: from boolean_cayley_graphs.boolean_linear_code import linear_code_from_code_gens
        sage: gens = (
        ....: "10001",
        ....: "01000",
        ....: "00100",
        ....: "00011")
        sage: c = linear_code_from_code_gens(gens)
        sage: c.basis()
        [
        (1, 0, 0, 0, 1),
        (0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0),
        (0, 0, 0, 1, 1)
        ]
    """
    M = matrix(GF(2), [list(s) for s in gens])
    return LinearCode(M)


def print_latex_code_parameters(c):
    r"""
    Print the standard parameters of a linear code.

    INPUT:

    - ``c`` -- ``LinearCode``.

    OUTPUT:

    A string representing the standard parameters of the linear code ``c``.

    EXAMPLE:

    ::

        sage: from boolean_cayley_graphs.boolean_linear_code import linear_code_from_code_gens
        sage: from boolean_cayley_graphs.boolean_linear_code import print_latex_code_parameters
        sage: gens = (
        ....: "10001",
        ....: "01000",
        ....: "00100",
        ....: "00011")
        sage: c = linear_code_from_code_gens(gens)
        sage: print_latex_code_parameters(c)
        [5,4,1]
    """
    print (
        "[" + str(c.length()) +
        "," + str(c.dimension()) +
        "," + str(c.minimum_distance()) + "]"),
