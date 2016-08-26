
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.crypto.boolean_function import BooleanFunction

load("dillon_schatz_incidence_structure.sage")

load("cayley_graph_classification.sage")

load("walsh_hadamard_dual.sage")



class BooleanPolynomialCayleyGraphClassification(SageObject):

    def __init__(self, p):
        if not 'cayley_graph_debugging' in globals():
            debugging = False
        else:
            debugging = cayley_graph_debugging

        self.boolean_polynomial = p

        f = BooleanFunction(p)

        n = f.algebraic_normal_form()
        self.algebraic_normal_form = n

        G, D, I = dillon_schatz_incidence_structure(f)
        self.cayley_incidence_structure = G
        self.dillon_schatz_design_matrix = D
        self.dillon_schatz_incidence_structure = I

        fcc, srgs = cayley_graph_classification(f)
        self.cayley_graph_class_list = srgs
        self.cayley_graph_index_matrix = fcc.cayley_graph_index_matrix
        if debugging:
            self.__print__()


    def mangled_name(self, name):
        return self.__class__.__name__ + "__" + name


    def __print__(self):
        p = self.boolean_polynomial
        print "Boolean polynomial:   ", p

        f = BooleanFunction(p)

        n = self.algebraic_normal_form
        print "Algebraic normal form:", n
        print "Function", ("is" if f.is_bent() else "is not"), "bent."

        G = self.cayley_incidence_structure
        D = self.dillon_schatz_design_matrix
        I = self.dillon_schatz_incidence_structure
        print "Dillon Schatz design",
        print ("is" if I.is_isomorphic(G) else "is not"),
        print "isomorphic to Cayley graph incidence structure."
        print "Incidence structure t-design parameters:",
        print I.is_t_design(return_parameters=True)

        srgs = self.cayley_graph_class_list
        print "Strongly regular parameters, rank, order",
        print "and clique polynomial"
        print "of each representative Cayley graph",
        print "in the extended affine class:"
        for s in srgs:
            print s.strongly_regular_parameters,
            print s.rank, s.group_order, s.clique_polynomial
        print "Cayley graph representative index matrix:"
        print self.cayley_graph_index_matrix


def save_cayley_graph_classification(p, name):
    c = BooleanPolynomialCayleyGraphClassification(p)
    c._default_filename = c.mangled_name(name)
    save(c, c._default_filename)
    return c


def load_cayley_graph_classification(name):
    mangled_name = "BooleanPolynomialCayleyGraphClassification" + "__" + name
    c = load(mangled_name)
    return c
