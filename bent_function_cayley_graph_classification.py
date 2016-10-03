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
from sage.structure.sage_object import load, SageObject

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
    corresponding to the complete set of non-isomorphic Cayley graphs
    of the Boolean functions within the extended affine eqivalence class
    of `bentf`, `cayley_graph_index_matrix` set to a matrix of indices
    into `cayley_graph_class_list`, and `weight_class_matrix` set to
    the 0-1 matrix of weight classes corresponding to
    `cayley_graph_index_matrix`.

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
        verbose = controls.verbose

        dim = bentf.nvariables()
        v = 2 ** dim

        self.algebraic_normal_form = bentf.algebraic_normal_form()
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

        dillon_schatz_design_matrix = bentf.dillon_schatz_design_matrix()
        if self.weight_class_matrix != dillon_schatz_design_matrix:
            raise ValueError, ("self.weight_class_matrix != dillon_schatz_design_matrix" + "\n"
                               + str(self.weight_class_matrix) + "\n"
                               + str(dillon_schatz_design_matrix))

        if timing:
            print datetime.now()


    @classmethod
    def mangled_name(cls, name):
        r"""
        """
        return cls.__name__ + "__" + name


    @classmethod
    def load_mangled(cls, name):
        r"""
        """
        return load(cls.mangled_name(name))


    def save_mangled(self, name):
        r"""
        """
        self.save(self.__class__.mangled_name(name))


