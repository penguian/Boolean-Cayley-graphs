r"""
The ``strongly_regular_graph`` module defines the
``StronglyRegularGraph`` class, which represents
a strongly regular graph, with some of its properties,
such as its stronly regular parameters.

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

from sage.graphs.graph import Graph
from sage.matrix.constructor import matrix
from sage.misc.lazy_attribute import lazy_attribute
from sage.rings.finite_rings.finite_field_constructor import GF

from graph_improved import GraphImproved


class StronglyRegularGraph(GraphImproved):
    r"""
    A strongly regular graph, with lazy attributes for some computed properties.

    The class inherits from ``GraphImproved``, and is initialized either from a graph
    or from keyword arguments.

    EXAMPLES:

    ::

        sage: from boolean_cayley_graphs.royle_x_graph import royle_x_graph
        sage: g = royle_x_graph()
        sage: g.is_strongly_regular()
        True
        sage: from boolean_cayley_graphs.strongly_regular_graph import StronglyRegularGraph
        sage: srg = StronglyRegularGraph(g)
        sage: srg.is_strongly_regular()
        True

    """
    def __init__(self, graph=None, **kwargs):
        r"""
        Initialize either from a graph or from keyword arguments.

        TESTS::

            sage: from boolean_cayley_graphs.royle_x_graph import royle_x_graph
            sage: g = royle_x_graph()
            sage: g.is_strongly_regular()
            True
            sage: from boolean_cayley_graphs.strongly_regular_graph import StronglyRegularGraph
            sage: srg = StronglyRegularGraph(g)
            sage: srg.is_strongly_regular()
            True
        """
        GraphImproved.__init__(self, graph, **kwargs)

    @lazy_attribute
    def strongly_regular_parameters(self):
        r"""
        The strongly regular parameters of the graph.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.royle_x_graph import royle_x_graph
            sage: g = royle_x_graph()
            sage: g.is_strongly_regular(parameters=True)
            (64, 35, 18, 20)
            sage: from boolean_cayley_graphs.strongly_regular_graph import StronglyRegularGraph
            sage: srg = StronglyRegularGraph(g)
            sage: srg.is_strongly_regular()
            True
            sage: srg.strongly_regular_parameters
            (64, 35, 18, 20)
        """
        return self.is_strongly_regular(parameters=True)


    @lazy_attribute
    def matrix_GF2(self):
        r"""
        The adjacency matrix of the graph, over :math:`\mathbb{F}_2`.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: bentf = BentFunction([0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,0])
            sage: g = bentf.cayley_graph()
            sage: from boolean_cayley_graphs.strongly_regular_graph import StronglyRegularGraph
            sage: sg = StronglyRegularGraph(g)
            sage: sg.matrix_GF2
            [0 0 0 1 0 0 0 1 0 0 0 1 1 1 1 0]
            [0 0 1 0 0 0 1 0 0 0 1 0 1 1 0 1]
            [0 1 0 0 0 1 0 0 0 1 0 0 1 0 1 1]
            [1 0 0 0 1 0 0 0 1 0 0 0 0 1 1 1]
            [0 0 0 1 0 0 0 1 1 1 1 0 0 0 0 1]
            [0 0 1 0 0 0 1 0 1 1 0 1 0 0 1 0]
            [0 1 0 0 0 1 0 0 1 0 1 1 0 1 0 0]
            [1 0 0 0 1 0 0 0 0 1 1 1 1 0 0 0]
            [0 0 0 1 1 1 1 0 0 0 0 1 0 0 0 1]
            [0 0 1 0 1 1 0 1 0 0 1 0 0 0 1 0]
            [0 1 0 0 1 0 1 1 0 1 0 0 0 1 0 0]
            [1 0 0 0 0 1 1 1 1 0 0 0 1 0 0 0]
            [1 1 1 0 0 0 0 1 0 0 0 1 0 0 0 1]
            [1 1 0 1 0 0 1 0 0 0 1 0 0 0 1 0]
            [1 0 1 1 0 1 0 0 0 1 0 0 0 1 0 0]
            [0 1 1 1 1 0 0 0 1 0 0 0 1 0 0 0]

        """
        return matrix(GF(2), self)


    @lazy_attribute
    def rank(self):
        r"""
        The 2-rank of the graph.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.royle_x_graph import royle_x_graph
            sage: g = royle_x_graph()
            sage: from boolean_cayley_graphs.strongly_regular_graph import StronglyRegularGraph
            sage: srg = StronglyRegularGraph(g)
            sage: srg.rank
            64
        """
        return self.matrix_GF2.rank()


    @lazy_attribute
    def automorphism_group(self):
        r"""
        The automorphism group of the graph.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.royle_x_graph import royle_x_graph
            sage: g = royle_x_graph()
            sage: from boolean_cayley_graphs.strongly_regular_graph import StronglyRegularGraph
            sage: srg = StronglyRegularGraph(g)
            sage: srg.automorphism_group
            Permutation Group with generators [(11,21)(12,22)(13,23)(14,24)(15,25)(16,26)(17,27)(18,28)(19,29)(20,30)(36,37)(44,49)(45,50)(46,51)(47,52)(48,53), (5,11)(6,12)(7,13)(8,14)(9,15)(10,16)(27,31)(28,32)(29,33)(30,34)(37,38)(43,44)(50,54)(51,55)(52,56)(53,57), (3,4)(6,7)(8,9)(12,13)(14,15)(17,18)(22,23)(24,25)(27,28)(31,32)(41,42)(47,48)(52,53)(56,57)(59,60)(61,62), (2,3)(5,6)(9,10)(11,12)(15,16)(18,19)(21,22)(25,26)(28,29)(32,33)(40,41)(46,47)(51,52)(55,56)(58,59)(62,63), (2,5)(3,6)(4,7)(14,17)(15,18)(16,19)(24,27)(25,28)(26,29)(34,35)(38,39)(44,45)(49,50)(55,58)(56,59)(57,60), (1,2)(6,8)(7,9)(12,14)(13,15)(19,20)(22,24)(23,25)(29,30)(33,34)(39,40)(45,46)(50,51)(54,55)(59,61)(60,62), (1,20)(2,19)(3,18)(4,17)(5,16)(6,15)(7,14)(8,13)(9,12)(10,11)(37,43)(38,44)(39,45)(40,46)(41,47)(42,48), (0,1)(2,38,4,36)(3,37)(5,57,23,46)(6,53,22,51)(7,48,21,55)(8,17,26,33)(9,27,25,29)(10,31,24,19)(11,56,13,47)(12,52)(14,18,16,32)(15,28)(20,58,34,60)(30,59)(35,39)(40,43,42,49)(41,44)(45,63,54,61)(50,62)]
        """
        return Graph.automorphism_group(self)


    @lazy_attribute
    def group_order(self):
        r"""
        The order of the automorphism group of the graph.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.royle_x_graph import royle_x_graph
            sage: g = royle_x_graph()
            sage: from boolean_cayley_graphs.strongly_regular_graph import StronglyRegularGraph
            sage: srg = StronglyRegularGraph(g)
            sage: srg.group_order
            2580480
        """
        return self.automorphism_group.order()
