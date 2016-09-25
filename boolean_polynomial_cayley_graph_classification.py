
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.combinat.designs.incidence_structures import IncidenceStructure
from sage.crypto.boolean_function import BooleanFunction
from sage.structure.sage_object import SageObject, load

from bent_function import BentFunction
from bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification

import cayley_graph_controls as controls


class BooleanPolynomialCayleyGraphClassification(SageObject):


    def __init__(self, p):
        r"""
        """
        verbose = controls.verbose

        self.boolean_polynomial = p

        f = BentFunction(p)

        self.algebraic_normal_form = f.algebraic_normal_form()

        self.dillon_schatz_design_matrix = f.dillon_schatz_design_matrix()

        fcc = BentFunctionCayleyGraphClassification(f)
        self.cayley_graph_class_list   = fcc.cayley_graph_class_list
        self.cayley_graph_index_matrix = fcc.cayley_graph_index_matrix
        weight_class_matrix            = fcc.weight_class_matrix
        if weight_class_matrix != self.dillon_schatz_design_matrix:
            raise ValueError, ("weight_class_matrix != self.dillon_schatz_design_matrix" + "\n"
                               + str(weight_class_matrix) + "\n"
                               + str(self.dillon_schatz_design_matrix))
        if verbose:
            self.__print__()


    def mangled_name(self, name):
        r"""
        """
        return self.__class__.__name__ + "__" + name


    def __print__(self):
        r"""
        """
        p = self.boolean_polynomial
        print "Boolean polynomial:   ", p

        f = BooleanFunction(p)

        n = self.algebraic_normal_form
        print "Algebraic normal form:", n
        print "Function", ("is" if f.is_bent() else "is not"), "bent."

        D = self.dillon_schatz_design_matrix
        I = IncidenceStructure(D)
        print "Incidence structure t-design parameters:",
        print I.is_t_design(return_parameters=True)

        srgs = self.cayley_graph_class_list
        print "Clique polynomial,",
        print "strongly regular parameters, rank, and order",
        print "of each representative Cayley graph",
        print "in the extended affine class:"
        for s in srgs:
            print s.clique_polynomial
            print s.strongly_regular_parameters,
            print s.rank, s.group_order
            print ""
        print "Cayley graph representative index matrix:"
        print self.cayley_graph_index_matrix


def save_cayley_graph_classification(c, name):
    r"""
    """
    c.save(c.mangled_name(name))


def load_cayley_graph_classification(name):
    r"""
    """
    mangled_name = "BooleanPolynomialCayleyGraphClassification" + "__" + name
    return load(mangled_name)
