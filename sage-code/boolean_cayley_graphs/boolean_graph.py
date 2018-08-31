r"""
The ``boolean_graph`` module defines
the ``BooleanGraph``  class,
which represents a Graph whose order is a power of 2.

AUTHORS:

- Paul Leopardi (2017-11-11): initial version

"""
#*****************************************************************************
#       Copyright (C) 2017 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from math import log

from sage.arith.srange import xsrange
from sage.graphs.graph import Graph
from sage.matrix.constructor import matrix
from sage.rings.finite_rings.finite_field_constructor import FiniteField as GF
from sage.rings.integer import Integer

from boolean_cayley_graphs.saveable import Saveable

base2 = lambda dim, num: num.digits(2, padto=dim)


class BooleanGraph(Graph, Saveable):
    """
    A Graph whose order is a power of 2.

    EXAMPLES:

    ::

        sage: from boolean_cayley_graphs.boolean_graph import BooleanGraph
        sage: g16 = BooleanGraph(16)
        sage: g16.order()
        16
    """
    def __init__(self, *args, **kwargs):
        """
        A Graph whose order is a power of 2.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_graph import BooleanGraph
            sage: g16 = BooleanGraph(8)
            sage: g16.order()
            8
        """
        super(BooleanGraph, self).__init__(*args, **kwargs)

        if not log(self.order(),2).is_integer():
            raise ValueError


    def is_linear_isomorphic(self, other, certificate=False):
        r"""
        Check that the two BooleanGraphs ``self`` and ``other`` are isomorphic
        and that the isomorphism is given by a GF(2) linear mapping on the
        vector space of vertices.

        INPUT:

        - ``self`` -- the current object.
        - ``other`` -- another object of class BooleanFunctionImproved.
        - ``certificate`` -- bool (default False). If true, return a GF(2) matrix
           that defines the isomorphism.

        OUTPUT:

        If ``certificate`` is false, a bool value.
        If ``certificate`` is true, a tuple consisting of either (False, None)
        or (True, M), where M is a GF(2) matrix that defines the isomorphism.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: from boolean_cayley_graphs.boolean_graph import BooleanGraph
            sage: bf1 = BooleanFunctionImproved([0,1,0,0])
            sage: cg1 = BooleanGraph(bf1.cayley_graph())
            sage: bf2 = BooleanFunctionImproved([0,0,1,0])
            sage: cg2 = BooleanGraph(bf2.cayley_graph())
            sage: cg1.is_linear_isomorphic(cg2)
            True
            sage: cg2.is_linear_isomorphic(cg1, certificate=True)
            (
                  [0 1]
            True, [1 0]
            )


        """

        # Check the isomorphism via canonical labels.
        # This is to work around the slow speed of is_isomorphic in some cases.
        if self.canonical_label() != other.canonical_label():
            return (False, None)

        # Obtain the mapping that defines the isomorphism.
        is_isomorphic, mapping = self.is_isomorphic(other, certificate=True)

        # If self is not isomorphic to other, it is not linear isomorphic.
        if not is_isomorphic:
            return (False,None) if certificate else False

        # Check that the mapping is linear on each pair of basis vectors.
        dim = Integer(log(self.order(), 2))
        for a in xsrange(dim):
            for b in xsrange(a + 1, dim):
                if mapping[2**a] ^ mapping[2**b] != mapping[(2**a) ^ (2**b)]:
                    return (False,None) if certificate else False

        # The mapping is linear.
        # If the caller does not want a certificate, just return True.
        if not certificate:
            return True

        # Create the G(2) matrix corresponding to the mapping.
        mapping_matrix = matrix(GF(2), [
            base2(dim, Integer(mapping[2**a]))
            for a in xsrange(dim)]).transpose()
        return (True, mapping_matrix)

