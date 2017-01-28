r"""
"""

#*****************************************************************************
#       Copyright (C) 2017 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************


from datetime import datetime

from sage.arith.srange import xsrange

from boolean_cayley_graph import boolean_cayley_graph
from containers import List

import cayley_graph_controls as controls


def cayley_graphs_of_c_translates(bentf):
    r"""
    Obtain a List of Cayley graphs from the functions `bentf(x)+<c,x>`.

    INPUT:

    - `bentf`: an object of class `BentFunction`.

    OUTPUT:

    A List of Graph corresponding to the complete set of
    non-isomorphic Cayley graphs of the bent functions of the form
    x \mapsto \mathtt{bentf}(x) + \langle c, x \rangle$.


    EXAMPLES::

    """
    checking = controls.checking
    timing   = controls.timing

    dim = bentf.nvariables()
    v = 2 ** dim

    cayley_graph_class_list = List()

    f = bentf.extended_translate()

    if timing:
        print datetime.now()

    for c in xsrange(v):
        fc = bentf.extended_translate(0, c, 0)
        cg = boolean_cayley_graph(dim, fc).canonical_label()
        cg_index = cayley_graph_class_list.index_append(cg)

    if timing:
        print datetime.now()

    return cayley_graph_class_list
