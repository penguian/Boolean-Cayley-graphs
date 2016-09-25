r"""
A subclass of BentFunction that includes information about relevant isomorphism classes of Cayley graphs.


AUTHORS:

- Paul Leopardi (2016-08-02): initial version

"""

#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************


from datetime import datetime

from sage.arith.srange import xsrange
from sage.matrix.constructor import matrix
from sage.structure.sage_object import SageObject

from bent_function import BentFunction
from boolean_cayley_graph import boolean_cayley_graph
from list_with_index_append import ListWithIndexAppend
from strongly_regular_graph import StronglyRegularGraph
from weight_class import weight_class

import cayley_graph_controls as controls


class BentFunctionCayleyGraphClassification(SageObject):
    r"""
    Given the `BentFunction` `bentf`,
    the class `BentFunctionCayleyGraphClassification`
    is initialized with `bent_function` set to `bentf`,
    `cayley_graph_class_list` set to a `ListWithIndexAppend` of `Graph`
    corresponding to the complete set of non-isomorphic Cayley graphs of the Boolean functions
    within the extended affine eqivalence class of `bentf`, and
    `cayley_graph_index_matrix` set to a matrix of indices into `cayley_graph_class_list`.

    Each entry `cayley_graph_index_matrix[c,b]` corresponds to
    the Cayley graph of the Boolean function
    $x \mapsto \mathtt{bentf}(x+b) + \langle c, x \rangle + \mathtt{bentf}(b)$.
    This enumerates all of the extended translates of `bentf`.
    """

    def __init__(self, bentf):
        r"""
        Initialize self as per the class description above.
        """
        timing = controls.timing

        dim = bentf.nvariables()
        v = 2 ** dim

        self.bent_function = bentf
        self.cayley_graph_index_matrix = matrix(v,v)
        self.weight_class_matrix       = matrix(v,v)

        cayley_graph_class_list = ListWithIndexAppend([])
        f = bentf.extended_translate()
        for b in xsrange(v):
            if timing:
                print datetime.now(), b, len(cayley_graph_class_list)

            fb = f(b)
            fbc_list = [bentf.extended_translate(b, c, fb)
                        for c in xsrange(v)]
            g_list = [boolean_cayley_graph(dim, fbc).canonical_label()
                      for fbc in fbc_list]
            for c in xsrange(v):
                self.cayley_graph_index_matrix[c, b] = cayley_graph_class_list.index_append(g_list[c])
                fbc = fbc_list[c]
                weight = sum(fbc(x) for x in xsrange(v))
                self.weight_class_matrix[c, b] = weight_class(v, weight)
        self.cayley_graph_class_list = [StronglyRegularGraph(g) for g in cayley_graph_class_list]
        if timing:
            print datetime.now()
