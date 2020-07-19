r"""
Strongly regular graphs
=======================

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

    TESTS:

    ::

        sage: from boolean_cayley_graphs.royle_x_graph import royle_x_graph
        sage: from boolean_cayley_graphs.strongly_regular_graph import StronglyRegularGraph
        sage: g = royle_x_graph()
        sage: srg = StronglyRegularGraph(g)
        sage: print(srg)
        Graph on 64 vertices

        sage: from boolean_cayley_graphs.royle_x_graph import royle_x_graph
        sage: from boolean_cayley_graphs.strongly_regular_graph import StronglyRegularGraph
        sage: g = royle_x_graph()
        sage: srg = StronglyRegularGraph(g)
        sage: latex(srg)
        \begin{tikzpicture}
        \definecolor{cv0}{rgb}{0.0,0.0,0.0}
        ...
        \Edge[lw=0.1cm,style={color=cv0v1,},](v0)(v1)
        ...
        \Edge[lw=0.1cm,style={color=cv58v63,},](v58)(v63)
        ...
        %
        \end{tikzpicture}
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
            sage: srg.automorphism_group.as_finitely_presented_group()
            Finitely presented group < a, b, c, d, e, f, g, h | a^2, d^2, f^2, c^2, b^2, e^2, g^2, h^2, (h*d)^2, (h*a)^2, c*e*a*e, (c*a)^2, (c*d)^2, (b*d)^2, (b*g)^2, (g*a)^2, (d*a)^2, (b*a)^2, (b*f)^2, d*f*a*f, (e*f)^2, h*e*h*f*e, h*c*h*f*c*f, (g*c)^3, (b*c)^3, (h*g)^4, (g*e)^4, (b*e)^4, h*b*h*(c*f*b)^2*c, g*e*a*f*c*g*d*e*f*d, g*e*g*f*g*c*e*g*d*c*e*d, (h*g*e*g)^3, b*c*e*b*c*f*c*b*e*c*b*(c*f*a)^2 >

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
