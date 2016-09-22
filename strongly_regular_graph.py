
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.graphs.graph import Graph
from sage.matrix.constructor import matrix
from sage.rings.finite_rings.finite_field_constructor import GF


class StronglyRegularGraph(Graph):
    r"""
    The class `StronglyRegularGraph` is used to store a strongly regular graph
    and some of its computed properties:
    its clique polynomial and its strongly regular graph parameters.
    """
    def __init__(self, graph=None):
        Graph.__init__(self, graph)
        self.clique_polynomial   = graph.clique_polynomial()
        self.strongly_regular_parameters = graph.is_strongly_regular(parameters=True)
        self.matrix_GF2 = matrix(GF(2),self)
        self.rank = self.matrix_GF2.rank()
        self.group = self.automorphism_group()
        self.group_order = self.group.order()
