r"""
A Graph and some of its computed properties, including its clique polynomial.

AUTHORS:

- Paul Leopardi (2016-10-05): initial version

"""
#*****************************************************************************
#       Copyright (C) 2016-17 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.graphs.graph import Graph

from boolean_cayley_graphs.saveable import Saveable


class GraphImproved(Graph, Saveable):
    r"""
    A Graph and some of its computed properties, including its clique polynomial.

    The constructor is based on the Graph constructor and takes the same arguments.

    EXAMPLES:

    ::

        sage: P = graphs.PetersenGraph()
        sage: P.clique_polynomial()
        15*t^2 + 10*t + 1
        sage: from boolean_cayley_graphs.graph_improved import GraphImproved
        sage: PI = GraphImproved(P)
        sage: PI.stored_clique_polynomial
        15*t^2 + 10*t + 1
        sage: dir = tmp_dir()
        sage: PI.save_mangled('PetersenGraph', directory=dir)
        sage: LPI = GraphImproved.load_mangled('PetersenGraph', directory=dir)
        sage: LPI.stored_clique_polynomial
        15*t^2 + 10*t + 1
        sage: GraphImproved.remove_mangled('PetersenGraph', directory=dir)
    """
    def __init__(self, graph=None, **kwargs):
        r"""
        Constructor, based on the Graph constructor.

        TESTS:

        ::

            sage: c = graphs.ClebschGraph()
            sage: c.clique_polynomial()
            40*t^2 + 16*t + 1
            sage: from boolean_cayley_graphs.graph_improved import GraphImproved
            sage: ci = GraphImproved(c)
            sage: ci.stored_clique_polynomial
            40*t^2 + 16*t + 1
        """
        Graph.__init__(self, graph, **kwargs)
        self.stored_clique_polynomial = graph.clique_polynomial()
