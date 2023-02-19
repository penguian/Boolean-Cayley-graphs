r"""
An improved Graph class
=======================

The ``graph_improved`` module defines
the ``GraphImproved`` class, which represents
a Graph and some of its computed properties, such as its clique polynomial.

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
    A Graph and some of its computed properties, such as its clique polynomial.

    The constructor is based on the ``Graph`` constructor and takes the same arguments.

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
        sage: PI.save_mangled('PetersenGraph', dir=dir)
        sage: LPI = GraphImproved.load_mangled('PetersenGraph', dir=dir)
        sage: LPI.stored_clique_polynomial
        15*t^2 + 10*t + 1
        sage: GraphImproved.remove_mangled('PetersenGraph', dir=dir)
        sage: os.rmdir(dir)

    TESTS:

    ::

        sage: from boolean_cayley_graphs.graph_improved import GraphImproved
        sage: P = graphs.PetersenGraph()
        sage: PI = GraphImproved(P)
        sage: print(PI)
        Petersen graph

        sage: from boolean_cayley_graphs.graph_improved import GraphImproved
        sage: P = graphs.PetersenGraph()
        sage: PI = GraphImproved(P)
        sage: latex(PI)
        \begin{tikzpicture}
        \definecolor{cv0}{rgb}{0.0,0.0,0.0}
        \definecolor{cfv0}{rgb}{1.0,1.0,1.0}
        \definecolor{clv0}{rgb}{0.0,0.0,0.0}
        ...
        \definecolor{cv6v8}{rgb}{0.0,0.0,0.0}
        \definecolor{cv6v9}{rgb}{0.0,0.0,0.0}
        \definecolor{cv7v9}{rgb}{0.0,0.0,0.0}
        %
        ...
        %
        \Edge[lw=0.1cm,style={color=cv0v1,},](v0)(v1)
        \Edge[lw=0.1cm,style={color=cv0v4,},](v0)(v4)
        \Edge[lw=0.1cm,style={color=cv0v5,},](v0)(v5)
        ...
        \Edge[lw=0.1cm,style={color=cv6v8,},](v6)(v8)
        \Edge[lw=0.1cm,style={color=cv6v9,},](v6)(v9)
        \Edge[lw=0.1cm,style={color=cv7v9,},](v7)(v9)
        %
        \end{tikzpicture}
        """


    def __init__(self, graph=None, **kwargs):
        r"""
        Constructor, based on the ``Graph`` constructor.

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
        self.stored_clique_polynomial = self.clique_polynomial()
