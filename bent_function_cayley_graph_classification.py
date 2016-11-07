r"""
The Cayley graphs within the extended translation equivalence class of a bent function.

AUTHORS:

- Paul Leopardi (2016-08-02): initial version

EXAMPLES::

    The classification of the bent function defined by the polynomial x2 + x1*x2.

    sage: from bent_function import BentFunction
    sage: from bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
    sage: R2.<x1,x2> = BooleanPolynomialRing(2)
    sage: p = x2+x1*x2
    sage: f = BentFunction(p)
    sage: c = BentFunctionCayleyGraphClassification(f)
    sage: c.__dict__
    {'algebraic_normal_form': x0*x1 + x1,
     'cayley_graph_class_list': [Graph on 4 vertices, Graph on 4 vertices],
     'cayley_graph_index_matrix': [0 0 1 0]
     [1 0 0 0]
     [0 0 0 1]
     [0 1 0 0],
     'cayley_pair_c_b_list': [(0, 0), (1, 0)],
     'dual_c_graph_index_matrix': [0 0 1 0]
     [1 0 0 0]
     [0 0 0 1]
     [0 1 0 0],
     'dual_c_pair_c_b_list': [(0, 0), (1, 0)],
     'weight_class_matrix': [0 0 1 0]
     [1 0 0 0]
     [0 0 0 1]
     [0 1 0 0]}
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
from sage.combinat.designs.incidence_structures import IncidenceStructure
from sage.matrix.constructor import matrix
from sage.structure.sage_object import load, SageObject

from bent_function import BentFunction
from boolean_cayley_graph import boolean_cayley_graph
from boolean_linear_code_graph import boolean_linear_code_graph
from containers import List
from graph_improved import GraphImproved
from persistent import Persistent
from strongly_regular_graph import StronglyRegularGraph
from weight_class import weight_class

import cayley_graph_controls as controls



class BentFunctionCayleyGraphClassification(SageObject, Persistent):
    r"""
    Attributes of the Cayley graphs within the extended translation equivalence class of a bent function.

    """

    def __init__(self, bentf):
        r"""
        Initialize `self` from the `BentFunction` `bentf`.

        INPUT:

        - `self`: the current object. Uninitialized.
        - `bentf`: an object of class `BentFunction`.

        OUTPUT:

        None.

        EFFECT:

        The current object `self` is initialized as follows.

        - `algebraic_normal_form` is set to `bentf.algebraic_normal_form()`,
        - `cayley_graph_index_matrix` is set to a matrix of indices
          into `cayley_graph_class_list`,
        - `weight_class_matrix` is set to the 0-1 matrix of weight classes
          corresponding to `cayley_graph_index_matrix`,
        - `cayley_graph_class_list` is set to a `List` of `GraphImproved`
          corresponding to the complete set of non-isomorphic Cayley graphs
          of the bent functions within the extended translation equivalence
          class of `bentf`, and
        - `cayley_pair_c_b_list` is set to a `list` of each of the first
          2-tuples (c, b) found such that if
          `index == cayley_graph_index_matrix[c, b]` then
          `cayley_graph_class_list[index]` is not isomorphic to any Cayley
          graph previously generated, and `cayley_pair_c_b_list[index] == (c,b)`.

        Each entry `cayley_graph_index_matrix[c,b]` corresponds to
        the Cayley graph of the bent function
        $x \mapsto \mathtt{bentf}(x+b) + \langle c, x \rangle + \mathtt{bentf}(b)$.
        This enumerates all of the extended translates of `bentf`.

        EXAMPLES::

            The classification of the bent function defined by the polynomial x1 + x2 + x1*x2.

            sage: from bent_function import BentFunction
            sage: from bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BentFunction(p)
            sage: c = BentFunctionCayleyGraphClassification(f)
            sage: c.__dict__
            {'algebraic_normal_form': x0*x1 + x0 + x1,
             'cayley_graph_class_list': [Graph on 4 vertices, Graph on 4 vertices],
             'cayley_graph_index_matrix': [0 1 1 1]
             [1 1 0 1]
             [1 0 1 1]
             [1 1 1 0],
             'cayley_pair_c_b_list': [(0, 0), (1, 0)],
             'dual_c_graph_index_matrix': [0 1 1 1]
             [1 1 0 1]
             [1 0 1 1]
             [1 1 1 0],
             'dual_c_pair_c_b_list': [(0, 0), (1, 0)],
             'weight_class_matrix': [1 0 0 0]
             [0 0 1 0]
             [0 1 0 0]
             [0 0 0 1]}
        """
        checking = controls.checking
        timing   = controls.timing

        dim = bentf.nvariables()
        v = 2 ** dim

        self.algebraic_normal_form = bentf.algebraic_normal_form()

        self.cayley_graph_class_list = List([])

        self.cayley_pair_c_b_list = []
        self.dual_c_pair_c_b_list = []

        self.cayley_graph_index_matrix = matrix(v,v)
        self.dual_c_graph_index_matrix = matrix(v,v)

        self.weight_class_matrix       = matrix(v,v)

        f = bentf.extended_translate()
        dual_bentf = bentf.walsh_hadamard_dual()
        dual_f = dual_bentf.extended_translate()

        max_cg_index = -1
        max_dg_index = -1
        for b in xsrange(v):
            if timing:
                print datetime.now(), b,
                print len(self.cayley_graph_class_list)

            fb = f(b)
            for c in xsrange(v):
                fbc = bentf.extended_translate(b, c, fb)
                cg = boolean_cayley_graph(dim, fbc).canonical_label()
                cg_index = self.cayley_graph_class_list.index_append(cg)
                self.cayley_graph_index_matrix[c, b] = cg_index

                if cg_index > max_cg_index:
                    max_cg_index = cg_index
                    self.cayley_pair_c_b_list.append((c, b))

                weight = sum(fbc(x) for x in xsrange(v))
                wc = weight_class(v, weight)
                self.weight_class_matrix[c, b] = wc

                if checking:
                    if wc != 0 and wc != 1:
                        raise ValueError, (
                            "Weight class is "
                            + str(wc))

                bentfbc = BentFunction([fbc(x) for x in xsrange(v)])

                dual_fbc = bentfbc.walsh_hadamard_dual().extended_translate(
                    d=wc)
                dg = boolean_cayley_graph(dim, dual_fbc).canonical_label()
                dg_index = self.cayley_graph_class_list.index_append(dg)
                self.dual_c_graph_index_matrix[c, b] = dg_index

                if dg_index > max_dg_index:
                    max_dg_index = dg_index
                    self.dual_c_pair_c_b_list.append((c, b))

                if checking and dim > 2:
                    blcg = boolean_linear_code_graph(dim, fbc)
                    lg = (
                        blcg.canonical_label()
                        if wc == 0
                        else blcg.complement().canonical_label())
                    if cg != lg:
                        raise ValueError, (
                            "Cayley graph does not match graph from linear code at "
                            + str(b) + ","
                            + str(c))

        if checking:
            dillon_schatz_design_matrix = bentf.dillon_schatz_design_matrix()
            if self.weight_class_matrix != dillon_schatz_design_matrix:
                raise ValueError, (
                    "weight_class_matrix != dillon_schatz_design_matrix"
                    + "\n"
                    + str(self.weight_class_matrix)
                    + "\n"
                    + str(dillon_schatz_design_matrix))

        if timing:
            print datetime.now()


    def report(self):
        r"""
        Print a report on the attributes of `self`.

        This includes various computed quantities.

        INPUT:

        `self`: the current object.

        OUTPUT:

        (To standard output)
        A report on the following attributes of `self`:
        - algebraic_normal_form
        - cayley_graph_class_list
        - cayley_graph_index_matrix
        - weight_class_matrix

        Each Cayley graph in cayley_graph_class_list is converted to
        a StronglyRegularGraph, and the following attributes are reported:
        - clique_polynomial, strongly_regular_parameters, rank, group_order.
        Each corresponding (c, b) pair in cayley_pair_c_b_list is converted to
        a BentFunction, and the corresponding LinearCode and generator matrix
        are reported.

        EXAMPLES::

            Report on the classification of the bent function defined by the polynomial x1 + x1*x2.

            sage: from bent_function import BentFunction
            sage: from bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
            sage: R4.<x1,x2,x3,x4> = BooleanPolynomialRing(4)
            sage: p = x1+x1*x2+x3*x4
            sage: f = BentFunction(p)
            sage: c = BentFunctionCayleyGraphClassification(f)
            sage: c.report()
            Algebraic normal form: x0*x1 + x0 + x2*x3
            Function is bent.
            Dillon-Schatz incidence structure t-design parameters: (True, (2, 16, 6, 2))
            Classification of Cayley graphs and classification of Cayley graphs of duals are the same:

            Clique polynomial, strongly regular parameters, rank, and order
            of each representative graph in the extended translation class;
            linear code and generator matrix for a representative bent function from each graph class:
            0 :
            Algebraic normal form of representative: x0*x1 + x0 + x2*x3
            Clique polynomial 8*t^4 + 32*t^3 + 48*t^2 + 16*t + 1
            Strongly regular parameters (16, 6, 2, 2)
            Rank 6 Order 1152

            Linear code from representative:
            Linear code of length 6, dimension 4 over Finite Field of size 2
            Generator matrix:
            [1 0 0 0 0 1]
            [0 1 0 1 0 0]
            [0 0 1 1 0 0]
            [0 0 0 0 1 1]
            Linear code is projective.
            Weight distribution: {0: 1, 2: 6, 4: 9}

            1 :
            Algebraic normal form of representative: x0*x1 + x0 + x1 + x2*x3
            Clique polynomial 16*t^5 + 120*t^4 + 160*t^3 + 80*t^2 + 16*t + 1
            Strongly regular parameters (16, 10, 6, 6)
            Rank 6 Order 1920

            Linear code from representative:
            Linear code of length 10, dimension 4 over Finite Field of size 2
            Generator matrix:
            [1 0 1 0 1 0 0 1 0 0]
            [0 1 1 0 1 1 0 1 1 0]
            [0 0 0 1 1 1 0 0 0 1]
            [0 0 0 0 0 0 1 1 1 1]
            Linear code is projective.
            Weight distribution: {0: 1, 4: 5, 6: 10}

            Graph index matrix:
            [0 1 0 0 0 1 0 0 0 1 0 0 1 0 1 1]
            [0 0 0 1 0 0 0 1 0 0 0 1 1 1 1 0]
            [1 0 0 0 1 0 0 0 1 0 0 0 0 1 1 1]
            [0 0 1 0 0 0 1 0 0 0 1 0 1 1 0 1]
            [0 1 0 0 1 0 1 1 0 1 0 0 0 1 0 0]
            [0 0 0 1 1 1 1 0 0 0 0 1 0 0 0 1]
            [1 0 0 0 0 1 1 1 1 0 0 0 1 0 0 0]
            [0 0 1 0 1 1 0 1 0 0 1 0 0 0 1 0]
            [0 1 0 0 0 1 0 0 1 0 1 1 0 1 0 0]
            [0 0 0 1 0 0 0 1 1 1 1 0 0 0 0 1]
            [1 0 0 0 1 0 0 0 0 1 1 1 1 0 0 0]
            [0 0 1 0 0 0 1 0 1 1 0 1 0 0 1 0]
            [1 0 1 1 0 1 0 0 0 1 0 0 0 1 0 0]
            [1 1 1 0 0 0 0 1 0 0 0 1 0 0 0 1]
            [0 1 1 1 1 0 0 0 1 0 0 0 1 0 0 0]
            [1 1 0 1 0 0 1 0 0 0 1 0 0 0 1 0]
            Weight class matrix:
            [0 1 0 0 0 1 0 0 0 1 0 0 1 0 1 1]
            [0 0 0 1 0 0 0 1 0 0 0 1 1 1 1 0]
            [1 0 0 0 1 0 0 0 1 0 0 0 0 1 1 1]
            [0 0 1 0 0 0 1 0 0 0 1 0 1 1 0 1]
            [0 1 0 0 1 0 1 1 0 1 0 0 0 1 0 0]
            [0 0 0 1 1 1 1 0 0 0 0 1 0 0 0 1]
            [1 0 0 0 0 1 1 1 1 0 0 0 1 0 0 0]
            [0 0 1 0 1 1 0 1 0 0 1 0 0 0 1 0]
            [0 1 0 0 0 1 0 0 1 0 1 1 0 1 0 0]
            [0 0 0 1 0 0 0 1 1 1 1 0 0 0 0 1]
            [1 0 0 0 1 0 0 0 0 1 1 1 1 0 0 0]
            [0 0 1 0 0 0 1 0 1 1 0 1 0 0 1 0]
            [1 0 1 1 0 1 0 0 0 1 0 0 0 1 0 0]
            [1 1 1 0 0 0 0 1 0 0 0 1 0 0 0 1]
            [0 1 1 1 1 0 0 0 1 0 0 0 1 0 0 0]
            [1 1 0 1 0 0 1 0 0 0 1 0 0 0 1 0]

        REFERENCES:

        .. [Leo2017] "Classifying bent functions by their Cayley graphs", in preparation.

        """
        def graph_and_linear_code_report(
            bentf,
            graph_class_list,
            pair_c_b_list,
            graph_index_matrix):
            r"""
            """
            verbose = controls.verbose

            print ""
            print "Clique polynomial,",
            print "strongly regular parameters, rank, and order"
            print "of each representative graph",
            print "in the extended translation class;"
            print "linear code and generator matrix",
            print "for a representative bent function from each graph class:"
            for index in xsrange(len(graph_class_list)):
                print index, ":"
                c_b = pair_c_b_list[index]
                c = c_b[0]
                b = c_b[1]
                fb = f(b)
                fbc = bentf.extended_translate(b, c, fb)
                bent_fbc = BentFunction([fbc(x) for x in xsrange(v)])
                p = bent_fbc.algebraic_normal_form()
                print "Algebraic normal form of representative:", p
                g = graph_class_list[index]
                s = StronglyRegularGraph(g)
                print "Clique polynomial", s.stored_clique_polynomial
                print "Strongly regular parameters", s.strongly_regular_parameters
                print "Rank", s.rank,
                print "Order", s.group_order

                print ""
                print "Linear code from representative:"
                lc = bent_fbc.linear_code()
                print lc
                print "Generator matrix:"
                print lc.generator_matrix()
                print "Linear code",
                print "is" if lc.is_projective() else "is not",
                print "projective."
                print "Weight distribution:",
                wd = lc.weight_distribution()
                print dict([(w,wd[w]) for w in xsrange(len(wd)) if wd[w] > 0])
                print ""
            print "Graph index matrix:"
            print graph_index_matrix


        p = self.algebraic_normal_form
        print "Algebraic normal form:", p
        bentf = BentFunction(p)
        f = bentf.extended_translate()

        dim = bentf.nvariables()
        v = 2 ** dim

        print "Function", ("is" if bentf.is_bent() else "is not"), "bent."

        D = self.weight_class_matrix
        I = IncidenceStructure(D)
        print "Dillon-Schatz incidence structure t-design parameters:",
        print I.is_t_design(return_parameters=True)

        cg_list   = self.cayley_graph_class_list
        ccb_list  = self.cayley_pair_c_b_list
        ci_matrix = self.cayley_graph_index_matrix
        dcb_list  = self.dual_c_pair_c_b_list
        di_matrix = self.dual_c_graph_index_matrix

        print "Classification of Cayley graphs and",
        print "classification of Cayley graphs of duals",
        if ci_matrix == di_matrix:
            print "are the same:"
            graph_and_linear_code_report(bentf, cg_list, ccb_list, ci_matrix)
        else:
            cb_lists_differ = ccb_list != dcb_list
            i_matrices_differ = ci_matrix != di_matrix
            print "differ in",
            if cb_lists_differ:
                print "lists of first (c,b) pairs;",
            if i_matrices_differ:
                print "matrices of indexes;",
            print ""
            if i_matrices_differ:
                print ""
                print "Cayley graphs:"
                graph_and_linear_code_report(bentf, cg_list, ccb_list, ci_matrix)
                print ""
                print "Graphs from linear codes:"
                graph_and_linear_code_report(bentf, cg_list, dcb_list, di_matrix)

        print "Weight class matrix:"
        print D
