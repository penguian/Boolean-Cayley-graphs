
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
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

    REFERENCE:

    Royle 2008
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
