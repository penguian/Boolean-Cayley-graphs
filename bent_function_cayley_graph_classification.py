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
    sage: f.is_bent()
    True
    sage: c = BentFunctionCayleyGraphClassification(f)
    sage: c.__dict__
    {'algebraic_normal_form': x0*x1 + x1,
    'cayley_graph_class_list': [Graph on 4 vertices, Graph on 4 vertices],
    'cayley_graph_index_matrix': [0 0 1 0]
    [1 0 0 0]
    [0 0 0 1]
    [0 1 0 0],
    'pair_c_b_list': [(0, 0), (1, 0)],
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
        - `pair_c_b_list` is set to a `list` of each of the first
          2-tuples (c, b) found such that if
          `index == cayley_graph_index_matrix[c, b]` then
          `cayley_graph_class_list[index]` is not isomorphic to any Cayley
          graph previously generated, and `pair_c_b_list[index] == (c,b)`.

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
            sage: f.is_bent()
            True
            sage: c = BentFunctionCayleyGraphClassification(f)
            sage: c.__dict__
            {'algebraic_normal_form': x0*x1 + x0 + x1,
            'cayley_graph_class_list': [Graph on 4 vertices, Graph on 4 vertices],
            'cayley_graph_index_matrix': [0 1 1 1]
            [1 1 0 1]
            [1 0 1 1]
            [1 1 1 0],
            'pair_c_b_list': [(0, 0), (1, 0)],
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
        self.cayley_graph_index_matrix = matrix(v,v)
        self.weight_class_matrix       = matrix(v,v)

        cayley_graph_class_list = List([])
        self.pair_c_b_list = []
        f = bentf.extended_translate()
        max_index = -1
        for b in xsrange(v):
            if timing:
                print datetime.now(), b, len(cayley_graph_class_list)

            fb = f(b)
            fbc_list = [bentf.extended_translate(b, c, fb)
                        for c in xsrange(v)]
            g_list = [boolean_cayley_graph(dim, fbc).canonical_label()
                      for fbc in fbc_list]
            for c in xsrange(v):
                g = g_list[c]
                index = cayley_graph_class_list.index_append(g)
                self.cayley_graph_index_matrix[c, b] = index
                fbc = fbc_list[c]
                weight = sum(fbc(x) for x in xsrange(v))
                wc = weight_class(v, weight)
                self.weight_class_matrix[c, b] = wc
                if index > max_index:
                    max_index = index
                    self.pair_c_b_list.append((c, b))
                    if checking:
                        if wc != 0 and wc != 1:
                            raise ValueError, (
                                "Weight class is "
                                + str(wc))

        self.cayley_graph_class_list = [GraphImproved(g)
                                        for g in cayley_graph_class_list]

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
        Each corresponding (c, b) pair in pair_c_b_list is converted to
        a BentFunction, and the corresponding LinearCode and generator matrix
        are reported.

        EXAMPLES::

            Report on the classification of the bent function defined by the polynomial x1 + x1*x2.

            sage: from bent_function import BentFunction
            sage: from bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p=x1+x1*x2
            sage: f=BentFunction(p)
            sage: c=BentFunctionCayleyGraphClassification(f)
            sage: c.report()
            Algebraic normal form: x0*x1 + x0
            Function is bent.
            Dillon-Schatz incidence structure t-design parameters: (True, (1, 4, 1, 1))

            Clique polynomial, strongly regular parameters, rank, and order of each representative Cayley graph in the extended affine class;
            linear code and generator matrix for one of the bent functions in the Cayley class:
            Polynomial 2*t^2 + 4*t + 1
            Parameters (4, 1, 0, 0)
            Rank 4 Order 8
            Linear code of length 1, dimension 1 over Finite Field of size 2
            Generator matrix:
            [1]
            Linear code is projective.
            Weight distribution {0: 1, 1: 1}

            Polynomial t^4 + 4*t^3 + 6*t^2 + 4*t + 1
            Parameters False
            Rank 4 Order 24
            Linear code of length 3, dimension 2 over Finite Field of size 2
            Generator matrix:
            [1 0 1]
            [0 1 1]
            Linear code is projective.
            Weight distribution {0: 1, 2: 3}

            Cayley graph index matrix:
            [0 1 0 0]
            [0 0 0 1]
            [1 0 0 0]
            [0 0 1 0]
            Weight class matrix:
            [0 1 0 0]
            [0 0 0 1]
            [1 0 0 0]
            [0 0 1 0]

        REFERENCES:

        .. [Leo2017] "Classifying bent functions by their Cayley graphs", in preparation.

        """
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

        g_list = self.cayley_graph_class_list
        cb_list = self.pair_c_b_list
        print ""
        print "Clique polynomial,",
        print "strongly regular parameters, rank, and order",
        print "of each representative Cayley graph",
        print "in the extended affine class;"
        if dim > 2:
            print "linear code, generator matrix, and corresponding",
            print "clique polynomial,",
            print "strongly regular parameters, rank, and order",
        else:
            print "linear code and generator matrix",
        print "for one of the bent functions in the Cayley class:"
        for index in xsrange(len(g_list)):
            g = g_list[index]
            s = StronglyRegularGraph(g)
            print "Polynomial", s.stored_clique_polynomial
            print "Parameters", s.strongly_regular_parameters
            print "Rank", s.rank, "Order", s.group_order
            c_b = cb_list[index]
            c = c_b[0]
            b = c_b[1]
            fb = f(b)
            fbc = bentf.extended_translate(b, c, fb)
            bent_fbc = BentFunction([fbc(x) for x in xsrange(v)])
            if dim > 2:
                h = (    bent_fbc.strongly_regular_graph()
                    if   bent_fbc.weight_class() == 0
                    else bent_fbc.strongly_regular_graph().complement())
                t = StronglyRegularGraph(h.canonical_label())
                if s == t:
                    print "Strongly regular graph from code",
                    print "is isomorphic to Cayley graph."
                else:
                    print "Polynomial", t.stored_clique_polynomial
                    print "Parameters", t.strongly_regular_parameters
                    print "Rank", t.rank, "Order", t.group_order
            lc = bent_fbc.linear_code()
            print lc
            print "Generator matrix:"
            print lc.generator_matrix()
            print "Linear code",
            print "is" if lc.is_projective() else "is not",
            print "projective."
            print "Weight distribution",
            wd = lc.weight_distribution()
            print dict([(w,wd[w]) for w in xsrange(len(wd)) if wd[w] > 0])
            print ""

        print "Cayley graph index matrix:"
        print self.cayley_graph_index_matrix
        print "Weight class matrix:"
        print D
