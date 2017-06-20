r"""
Graphs corresponding to bent functions or the generators of projective two-weight codes.

AUTHORS:

- Paul Leopardi (2016-08-21): initial version

"""

#*****************************************************************************
#       Copyright (C) 2016-2017 Paul Leopardi paul.leopardi@gmail.com
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
    Return the graph corresponding to the linear code of a bent Boolean function.

    INPUT:

    - ``dim`` -- positive integer. The assumed dimension of function ``f``.
    - ``f`` -- a Python function that takes a positive integer and returns 0 or 1.
      This is assumed to represent a bent Boolean function on :math:`\mathbb{F}_2^{dim}`
      via lexicographical ordering.

    OUTPUT:

    An object of class ``Graph``, representing the graph corresponding to
    the linear code of the bent Boolean function represented by ``f``.

    .. WARNING::

        This function raises a ``ValueError`` if ``f`` is not bent.

    REFERENCES:

    .. [Car2010]_

    .. [DD2015]_ Corollary 10.

    EXAMPLES:

    Where bf is a bent function.

    ::

        sage: from sage.crypto.boolean_function import BooleanFunction
        sage: bf = BooleanFunction([0,1,0,0,0,1,0,0,0,1,0,0,1,0,1,1])
        sage: bf.is_bent()
        True
        sage: dim = bf.nvariables()
        sage: from boolean_cayley_graphs.boolean_linear_code_graph import boolean_linear_code_graph
        sage: bg = boolean_linear_code_graph(dim, bf)
        sage: bg.is_strongly_regular()
        True

    Where f is not a bent function.

    ::

        sage: from sage.crypto.boolean_function import BooleanFunction
        sage: f = BooleanFunction([0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,1])
        sage: f.is_bent()
        False
        sage: from boolean_cayley_graphs.boolean_linear_code_graph import boolean_linear_code_graph
        sage: dim = f.nvariables()
        sage: g = boolean_linear_code_graph(dim, f)
        Traceback (most recent call last):
            ...
        ValueError: too many values to unpack (expected 2)

    """
    L = boolean_linear_code(dim, f)
    return strongly_regular_from_two_weight_code(L)


def strongly_regular_from_code_gens(gens):
    r"""
    Return the strongly regular graph corresponding to a list of generators.

    INPUT:

    - ``gens`` -- list. A list of strings of 0,1 characters.
      This is assumed to represent the generators of a
      projective two-weight linear code which yields a strongly regular graph.

    OUTPUT:

    An object of class ``Graph``, representing the graph corresponding to
    the generators represented by ``gens``.

    .. WARNING::

        This function raises a ``ValueError`` if ``gens`` is not a list of
        generators of a projective two-weight linear code which yields a
        strongly regular graph.

    EXAMPLES:

    ::

        Where ``gens`` is a list of generators for a code yielding a
        strongly regular graph.

        sage: from boolean_cayley_graphs.boolean_linear_code_graph import strongly_regular_from_code_gens
        sage: gens = [
        ....: "100001",
        ....: "010100",
        ....: "001100",
        ....: "000011"]
        sage: g = strongly_regular_from_code_gens(gens)
        sage: g.is_strongly_regular()
        True

    ::

        Where ``nongens`` is a list of generators for a code that does *not*
        yield a strongly regular graph.

        sage: nongens = [
        ....: "10001",
        ....: "01000",
        ....: "00100",
        ....: "00011"]
        sage: nong = strongly_regular_from_code_gens(nongens)
        Traceback (most recent call last):
            ...
        ValueError: too many values to unpack (expected 2)

    """
    L = linear_code_from_code_gens(gens)
    return strongly_regular_from_two_weight_code(L)
