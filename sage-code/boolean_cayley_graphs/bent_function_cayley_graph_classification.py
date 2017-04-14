r"""
The Cayley graphs within the extended translation equivalence class of a bent function.

AUTHORS:

- Paul Leopardi (2016-08-02): initial version

EXAMPLES::

    The classification of the bent function defined by the polynomial x2 + x1*x2.

    sage: from boolean_cayley_graphs.bent_function import BentFunction
    sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
    sage: R2.<x1,x2> = BooleanPolynomialRing(2)
    sage: p = x2+x1*x2
    sage: f = BentFunction(p)
    sage: c = BentFunctionCayleyGraphClassification(f)
    sage: c.__dict__
    {'algebraic_normal_form': x0*x1 + x1,
     'bent_cayley_graph_index_matrix': [0 0 1 0]
     [1 0 0 0]
     [0 0 0 1]
     [0 1 0 0],
     'cayley_graph_class_list': ['CK', 'C~'],
     'dual_cayley_graph_index_matrix': [0 0 1 0]
     [1 0 0 0]
     [0 0 0 1]
     [0 1 0 0],
     'weight_class_matrix': [0 0 1 0]
     [1 0 0 0]
     [0 0 0 1]
     [0 1 0 0]}
"""

#*****************************************************************************
#       Copyright (C) 2016-2017 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************


from datetime import datetime

from numpy import array, argwhere
from sage.arith.srange import xsrange
from sage.combinat.designs.incidence_structures import IncidenceStructure
from sage.functions.log import log
from sage.graphs.graph import Graph
from sage.matrix.constructor import matrix
from sage.plot.matrix_plot import matrix_plot
from sage.rings.integer import Integer
from sage.structure.sage_object import load, SageObject

from boolean_cayley_graphs.bent_function import BentFunction
from boolean_cayley_graphs.boolean_cayley_graph import boolean_cayley_graph
from boolean_cayley_graphs.boolean_linear_code_graph import boolean_linear_code_graph
from boolean_cayley_graphs.containers import BijectiveList
from boolean_cayley_graphs.containers import ShelveBijectiveList
from boolean_cayley_graphs.saveable import Saveable
from boolean_cayley_graphs.strongly_regular_graph import StronglyRegularGraph
from boolean_cayley_graphs.weight_class import weight_class

import boolean_cayley_graphs.cayley_graph_controls as controls


def immutable_canonical_label(g):
    r"""
    """
    return g.canonical_label().copy(immutable=True)


class BentFunctionCayleyGraphClassification(SageObject, Saveable):
    r"""
    Attributes of the Cayley graphs within the
    extended translation equivalence class of a bent function.
    """


    def __init__(self, bentf, list_dual_graphs=True):
        r"""
        Initialize `self` from the `BentFunction` `bentf`.

        INPUT:

        - `self`: the current object. Uninitialized.
        - `bentf`: an object of class `BentFunction`.
        - `list_dual_graphs`: a flag indicating whether to list dual graphs.

        OUTPUT:

        None.

        EFFECT:

        The current object `self` is initialized as follows.

        - `algebraic_normal_form` is set to `bentf.algebraic_normal_form()`,
        - `cayley_graph_class_list` is set to a list of `graph6_string` stings
          corresponding to the complete set of non-isomorphic Cayley graphs
          of the bent functions within the extended translation equivalence
          class of `bentf` (and their duals, if `list_dual_graphs` is `True`),
        - `bent_cayley_graph_index_matrix` is set to a matrix of indices
          into `cayley_graph_class_list` corresponding
          to these bent functions,
        - `dual_cayley_graph_index_matrix` is set to `None`
          if `list_dual_graphs` is `False`, otherwise it is set to
          a matrix of indices into `cayley_graph_class_list` corresponding
          to the duals of these bent functions, and
        - `weight_class_matrix` is set to the 0-1 matrix of weight classes
          corresponding to `bent_cayley_graph_index_matrix`.

        Each entry `bent_cayley_graph_index_matrix[c,b]` corresponds to
        the Cayley graph of the bent function
        $x \mapsto \mathtt{bentf}(x+b) + \langle c, x \rangle + \mathtt{bentf}(b)$.
        This enumerates all of the extended translates of `bentf`.

        EXAMPLES::

            The classification of the bent function defined by the polynomial x1 + x2 + x1*x2.

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BentFunction(p)
            sage: c1 = BentFunctionCayleyGraphClassification(f)
            sage: c1.__dict__
            {'algebraic_normal_form': x0*x1 + x0 + x1,
             'bent_cayley_graph_index_matrix': [0 1 1 1]
             [1 1 0 1]
             [1 0 1 1]
             [1 1 1 0],
             'cayley_graph_class_list': ['C~', 'CK'],
             'dual_cayley_graph_index_matrix': [0 1 1 1]
             [1 1 0 1]
             [1 0 1 1]
             [1 1 1 0],
             'weight_class_matrix': [1 0 0 0]
             [0 0 1 0]
             [0 1 0 0]
             [0 0 0 1]}

            The classification of the bent function defined by the polynomial x1 + x2 + x1*x2,
            but with list_dual_graphs=False.

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BentFunction(p)
            sage: c2 = BentFunctionCayleyGraphClassification(f,list_dual_graphs=False)
            sage: c2.__dict__
            {'algebraic_normal_form': x0*x1 + x0 + x1,
             'bent_cayley_graph_index_matrix': [0 1 1 1]
             [1 1 0 1]
             [1 0 1 1]
             [1 1 1 0],
             'cayley_graph_class_list': ['C~', 'CK'],
             'dual_cayley_graph_index_matrix': None,
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

        file_prefix=self.mangled_name(bentf.truth_table(format='hex'))
        cayley_graph_class_bijection = (
            BijectiveList()
            if dim < 8 else
            ShelveBijectiveList(file_prefix=file_prefix))

        self.bent_cayley_graph_index_matrix = matrix(v, v)
        if list_dual_graphs:
            self.dual_cayley_graph_index_matrix = matrix(v, v)
        else:
            self.dual_cayley_graph_index_matrix = None
        self.weight_class_matrix = matrix(v, v)

        f = bentf.extended_translate()
        dual_bentf = bentf.walsh_hadamard_dual()
        dual_f = dual_bentf.extended_translate()

        for b in xsrange(v):
            if timing:
                print datetime.now(), b,
                print len(cayley_graph_class_bijection)

            fb = f(b)
            for c in xsrange(v):
                fbc = bentf.extended_translate(b, c, fb)
                cg = immutable_canonical_label(boolean_cayley_graph(dim, fbc))
                cg_index = cayley_graph_class_bijection.index_append(cg.graph6_string())
                self.bent_cayley_graph_index_matrix[c, b] = cg_index

                weight = sum(fbc(x) for x in xsrange(v))
                wc = weight_class(v, weight)
                self.weight_class_matrix[c, b] = wc

                if checking:
                    if wc != 0 and wc != 1:
                        raise ValueError, (
                            "Weight class is "
                            + str(wc))
                if list_dual_graphs:
                    bentfbc = BentFunction([fbc(x) for x in xsrange(v)])

                    dual_fbc = bentfbc.walsh_hadamard_dual().extended_translate(d=wc)
                    dg = immutable_canonical_label(boolean_cayley_graph(dim, dual_fbc))
                    dg_index = cayley_graph_class_bijection.index_append(dg.graph6_string())
                    self.dual_cayley_graph_index_matrix[c, b] = dg_index

                    if checking and dim > 2:
                        blcg = boolean_linear_code_graph(dim, fbc)
                        lg = (
                            immutable_canonical_label(blcg)
                            if wc == 0
                            else immutable_canonical_label(blcg.complement()))
                        if lg != dg:
                            raise ValueError, (
                                "Cayley graph of dual does not match"
                                + "graph from linear code at "
                                + str(b) + ","
                                + str(c))
            cayley_graph_class_bijection.sync()

        # Retain the list part of cayley_graph_class_bijection, and
        # close and remove the dict part.
        self.cayley_graph_class_list = cayley_graph_class_bijection.get_list()
        cayley_graph_class_bijection.close_dict()
        cayley_graph_class_bijection.remove_dict()

        if checking:
            sdp_design_matrix = bentf.sdp_design_matrix()
            if self.weight_class_matrix != sdp_design_matrix:
                raise ValueError, (
                    "weight_class_matrix != sdp_design_matrix"
                    + "\n"
                    + str(self.weight_class_matrix)
                    + "\n"
                    + str(sdp_design_matrix))

        if timing:
            print datetime.now()


    def first_matrix_index_list(self):
        r"""
        Return a list of tuples (i_n,j_n), each of which is the first index into
        the matrix self.bent_cayley_graph_index_matrix that contains the entry n.
        The "first" is determined by argwhere.
        This function is used to obtain a representative bent function
        corresponding to each extended Cayley class.

        EXAMPLES::

            The result for the bent function defined by the polynomial x1 + x2 + x1*x2.

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BentFunction(p)
            sage: c = BentFunctionCayleyGraphClassification(f)
            sage: c.first_matrix_index_list()
            [(0, 0), (0, 1)]
        """
        nbr_cayley_graph_classes = len(self.cayley_graph_class_list)
        ci_matrix = self.bent_cayley_graph_index_matrix

        ci_array  = array(ci_matrix)
        ci_where  = [
            argwhere(ci_array == index)
            for index in xsrange(nbr_cayley_graph_classes)]
        cb_list = [
            (None
            if ci_where[index].shape[0] == 0
            else tuple(ci_where[index][0,:]))
            for index in xsrange(nbr_cayley_graph_classes)]
        return cb_list


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
        - bent_cayley_graph_index_matrix
        - dual_cayley_graph_index_matrix
          (only if this is not None and is different from bent_cayley_graph_index_matrix)
        - weight_class_matrix

        EXAMPLES::

            Report on the classification of the bent function defined by the polynomial x0+x0*x1+x2*x3.

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
            sage: R4.<x0,x1,x2,x3> = BooleanPolynomialRing(4)
            sage: p = x0+x0*x1+x2*x3
            sage: f = BentFunction(p)
            sage: c = BentFunctionCayleyGraphClassification(f)
            sage: c.report()
            Algebraic normal form of Boolean function: x0*x1 + x0 + x2*x3
            Function is bent.
            <BLANKLINE>
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
            <BLANKLINE>
            SDP design incidence structure t-design parameters: (True, (2, 16, 6, 2))
            <BLANKLINE>
            Classification of Cayley graphs and classification of Cayley graphs of duals are the same:
            <BLANKLINE>
            Matrix of indices of Cayley graphs:
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
            <BLANKLINE>
            There are 2 extended Cayley classes in the extended translation class:
            <BLANKLINE>
            For each extended Cayley class in the extended translation class:
            Clique polynomial, strongly regular parameters, rank, and order of a representative graph; and
            linear code and generator matrix for a representative bent function:
            <BLANKLINE>
            EC class 0 :
            Algebraic normal form of representative: x0*x1 + x0 + x2*x3
            Clique polynomial: 8*t^4 + 32*t^3 + 48*t^2 + 16*t + 1
            Strongly regular parameters: (16, 6, 2, 2)
            Rank: 6 Order: 1152
            <BLANKLINE>
            Linear code from representative:
            [6, 4] linear code over GF(2)
            Generator matrix:
            [1 0 0 0 0 1]
            [0 1 0 1 0 0]
            [0 0 1 1 0 0]
            [0 0 0 0 1 1]
            Linear code is projective.
            Weight distribution: {0: 1, 2: 6, 4: 9}
            <BLANKLINE>
            EC class 1 :
            Algebraic normal form of representative: x0*x1 + x0 + x1 + x2*x3
            Clique polynomial: 16*t^5 + 120*t^4 + 160*t^3 + 80*t^2 + 16*t + 1
            Strongly regular parameters: (16, 10, 6, 6)
            Rank: 6 Order: 1920
            <BLANKLINE>
            Linear code from representative:
            [10, 4] linear code over GF(2)
            Generator matrix:
            [1 0 1 0 1 0 0 1 0 0]
            [0 1 1 0 1 1 0 1 1 0]
            [0 0 0 1 1 1 0 0 0 1]
            [0 0 0 0 0 0 1 1 1 1]
            Linear code is projective.
            Weight distribution: {0: 1, 4: 5, 6: 10}

        REFERENCES:

        .. [Leo2017] "Classifying bent functions by their Cayley graphs", in preparation.

        """
        def graph_and_linear_code_report(
            bentf,
            cayley_graph_class_list,
            pair_c_b_list,
            bent_cayley_graph_index_matrix,
            dual_cayley_graph_index_matrix=None):
            r"""
            Report on the Cayley graphs and linear codes given by the
            representative bent functions in the extended translation class.
            """
            def print_compare(verb, a, b):

                print (
                    verb + " the same."
                    if a == b
                    else a),


            verbose = controls.verbose

            print ""
            print "Matrix of indices of Cayley graphs:"
            print bent_cayley_graph_index_matrix
            if dual_cayley_graph_index_matrix != None:
                print "Matrix of indices of Cayley graphs",
                print "of dual bent functions:"
                print dual_cayley_graph_index_matrix

            nbr_cayley_graph_classes = len(cayley_graph_class_list)

            print ""
            print "There are", nbr_cayley_graph_classes,
            print "extended Cayley classes in the extended translation class:"
            print ""
            print "For each extended Cayley class in the extended translation class:"
            print "Clique polynomial, strongly regular parameters,",
            print "rank, and order of a representative graph; and"
            print "linear code and generator matrix for a representative bent function:"

            for index in xsrange(nbr_cayley_graph_classes):
                print ""
                print "EC class", index, ":"
                c_b = pair_c_b_list[index]
                if c_b == None:
                    print "No such representative graph."
                else:
                    c = Integer(c_b[0])
                    b = Integer(c_b[1])
                    fb = f(b)
                    fbc = bentf.extended_translate(b, c, fb)
                    bent_fbc = BentFunction([fbc(x) for x in xsrange(v)])
                    p = bent_fbc.algebraic_normal_form()
                    print "Algebraic normal form of representative:", p
                    g = Graph(cayley_graph_class_list[index])
                    s = StronglyRegularGraph(g)
                    print "Clique polynomial:",
                    print s.stored_clique_polynomial
                    print "Strongly regular parameters:",
                    print s.strongly_regular_parameters
                    print "Rank:", s.rank,
                    print "Order:", s.group_order

                    if dual_cayley_graph_index_matrix != None:
                        dual_index = dual_cayley_graph_index_matrix[c, b]
                        if dual_index != index:
                            print "Cayley graph of dual of representative differs:"
                            print "Index is", dual_index
                            dual_g = Graph(cayley_graph_class_list[dual_index])
                            dual_s = StronglyRegularGraph(dual_g)
                            print "Clique polynomial",
                            print_compare(
                                "is",
                                dual_s.stored_clique_polynomial,
                                s.stored_clique_polynomial)
                            print ""
                            print "Strongly regular parameters",
                            print_compare (
                                "are",
                                dual_s.strongly_regular_parameters,
                                s.strongly_regular_parameters)
                            print ""
                            print "Rank",
                            print_compare ("is", dual_s.rank, s.rank)
                            print "Order",
                            print_compare (
                                "is", dual_s.group_order, s.group_order)
                            print ""
                            if verbose:
                                if log(s.group_order, Integer(2)).is_integer():
                                    print "Order is a power of 2."
                                else:
                                    print ""
                                    print "Automorphism group",
                                    dual_a = dual_s.automorphism_group
                                    print (
                                        "is"
                                        if dual_a.is_isomorphic(s.automorphism_group)
                                        else "is not"),
                                    print "isomorphic."

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
                    print dict([
                        (w,wd[w]) for w in xsrange(len(wd)) if wd[w] > 0])

        p = self.algebraic_normal_form
        print "Algebraic normal form of Boolean function:", p
        bentf = BentFunction(p)
        f = bentf.extended_translate()

        dim = bentf.nvariables()
        v = 2 ** dim

        print "Function", ("is" if bentf.is_bent() else "is not"), "bent."
        print ""
        print "Weight class matrix:"
        D = self.weight_class_matrix
        print D

        print ""
        print "SDP design incidence structure t-design parameters:",
        I = IncidenceStructure(D)
        print I.is_t_design(return_parameters=True)

        cg_list   = self.cayley_graph_class_list
        ci_matrix = self.bent_cayley_graph_index_matrix
        di_matrix = self.dual_cayley_graph_index_matrix
        cb_list   = self.first_matrix_index_list()

        print ""
        if di_matrix == None:
            print "Classification of Cayley graphs:"

            graph_and_linear_code_report(bentf, cg_list, cb_list, ci_matrix)
        else:
            print "Classification of Cayley graphs and",
            print "classification of Cayley graphs of duals",
            if ci_matrix == di_matrix:
                print "are the same:"

                graph_and_linear_code_report(bentf, cg_list, cb_list, ci_matrix)
            else:
                print "differ in matrices of indexes:"

                graph_and_linear_code_report(bentf, cg_list, cb_list, ci_matrix,
                                            di_matrix)


    def save_matrix_plots(self, figure_name, cmap='gist_stern'):
        r"""
        Use matrix_plot to plot the matrices bent_cayley_graph_index_matrix,
        dual_cayley_graph_index_matrix, and weight_class_matrix
        to a figure file.
        """
        matrix_names = (
            "bent_cayley_graph_index_matrix",
            "dual_cayley_graph_index_matrix",
            "weight_class_matrix")

        attributes = self.__dict__
        for name in matrix_names:
            graphic = matrix_plot(matrix(attributes[name]),cmap=cmap)
            graphic.save(figure_name + "_" + name + ".png")
