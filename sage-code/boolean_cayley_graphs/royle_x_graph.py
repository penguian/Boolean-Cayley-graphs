r"""
A strongly regular graph, as described by Royle in 2008.

AUTHORS:

- Paul Leopardi (2016-10-19): initial version

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
from sage.combinat.combination import Combinations
from sage.graphs.graph import Graph
from sage.modules.vector_integer_dense import vector


def royle_x_graph():
    r"""
    A strongly regular graph, as described by Royle in 2008.

    INPUT:

    None.

    OUTPUT:

    An object of class ``Graph``, representing Royle's X graph [Roy2008]_.

    EXAMPLES:

    ::

        sage: from boolean_cayley_graphs.royle_x_graph import royle_x_graph
        sage: g = royle_x_graph()
        sage: g.is_strongly_regular()
        True
        sage: g.is_strongly_regular(parameters=True)
        (64, 35, 18, 20)

    REFERENCES:

    .. [Roy2008]_.

    """
    n = 8
    order = 64

    vecs = [vector([1]*n)]
    for a in Combinations(xsrange(1, n), 4):
        vecs.append(vector([
            -1 if x in a else 1
               for x in xsrange(n)]))
    for b in Combinations(xsrange(n), 2):
        vecs.append(vector([
            -1 if x in b else 1
               for x in xsrange(n)]))

    return Graph([
        (i,j) for i in xsrange(order)
              for j in xsrange(i+1, order)
              if vecs[i]*vecs[j] == 0])
