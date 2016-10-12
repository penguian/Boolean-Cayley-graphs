
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.graphs.graph import Graph
from persistent import Persistent


class GraphImproved(Graph, Persistent):
    r"""
    The class `GraphImproved` is used to store a  graph
    and some of its computed properties, including
    its clique polynomial.
    """
    def __init__(self, graph=None, **kwargs):
        Graph.__init__(self, graph, **kwargs)
        self.clique_polynomial = graph.clique_polynomial()
