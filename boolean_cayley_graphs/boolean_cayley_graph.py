r"""
Cayley graph of a Boolean function
==================================

The ``boolean_cayley_graph`` module defines
a function that contructs the Cayley graph of a Boolean function.

AUTHORS:

- Paul Leopardi (2016-08-21): initial version

EXAMPLES:

::

    sage: from boolean_cayley_graphs.boolean_cayley_graph import boolean_cayley_graph
    sage: f = lambda n: (n // 2) % 2
    sage: [f(i) for i in range(4)]
    [0, 0, 1, 1]
    sage: g = boolean_cayley_graph(2, f)
    sage: g.adjacency_matrix()
    [0 0 1 1]
    [0 0 1 1]
    [1 1 0 0]
    [1 1 0 0]

REFERENCES:

Bernasconi and Codenotti [BC1999]_.
"""
#*****************************************************************************
#       Copyright (C) 2016-2017 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************


from sage.graphs.graph import Graph


def boolean_cayley_graph(dim, f):
    r"""
    Construct the Cayley graph of a Boolean function.

    Given the non-negative integer ``dim`` and the function ``f``,
    a Boolean function that takes a non-negative integer argument,
    the function ``Boolean_Cayley_graph`` constructs the Cayley graph of ``f``
    as a Boolean function on :math:`\mathbb{F}_2^{dim}`,
    with the lexicographica ordering.
    The value ``f(0)`` is assumed to be ``0``, so the graph is always simple.

    INPUT:

    - ``dim`` -- integer. The Boolean dimension of the given function.
    - ``f`` -- function. A Boolean function expressed as a Python function
      taking non-negative integer arguments.

    OUTPUT:

    A ``Graph`` object representing the Cayley graph of ``f``.

    .. SEEALSO:
        :module:`sage.graphs.graph`

    EXAMPLES:

    The Cayley graph of the function ``f`` where :math:`f(n) = n \mod 2`.

    ::

        sage: from boolean_cayley_graphs.boolean_cayley_graph import boolean_cayley_graph
        sage: f = lambda n: n % 2
        sage: g = boolean_cayley_graph(2, f)
        sage: g.adjacency_matrix()
        [0 1 0 1]
        [1 0 1 0]
        [0 1 0 1]
        [1 0 1 0]

    """
    return Graph([range(2 ** dim), lambda i, j: f(i ^ j)],
                 format="rule",
                 immutable=True)
