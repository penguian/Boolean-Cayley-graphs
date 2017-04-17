r"""
Bent Boolean functions.

Paul Leopardi.
"""

#*****************************************************************************
#       Copyright (C) 2016-2017 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************


from sage.arith.srange import xsrange
from sage.graphs.graph import Graph
from sage.graphs.strongly_regular_db import strongly_regular_from_two_weight_code
from sage.matrix.constructor import matrix

from boolean_function_improved import BooleanFunctionImproved
from walsh_hadamard_dual import walsh_hadamard_dual

import weight_class as wc


class BentFunction(BooleanFunctionImproved):
    r"""
    """


    def is_partial_spread_minus(self, certify=False):
        r"""
        """
        dim = self.nvariables()
        reqd_clique_size = 2 ** (dim / 2)
        cayley = self.cayley_graph()
        cliques_0 = cayley.cliques_containing_vertex(0)
        reqd_cliques = [
            set(clique)
            for clique in cliques_0
            if (len(clique) >= reqd_clique_size)]
        nbr_cliques = len(reqd_cliques)
        if nbr_cliques == 0:
            if certify:
                return False, []
            else:
                return False
        clique_matrix = matrix(nbr_cliques)
        for j in range(nbr_cliques):
            for k in range(j + 1, nbr_cliques):
                clique_matrix[j, k] = clique_matrix[k, j] = (
                    1
                    if reqd_cliques[j] & reqd_cliques[k] == {0} else
                    0)

        clique_graph = Graph(clique_matrix)
        clique_max = clique_graph.clique_maximum()
        if len(clique_max) == reqd_clique_size // 2:
            if certify:
                part = [
                    reqd_cliques[j] - {0}
                    for j in clique_max]
                return True, part
            else:
                return True
        else:
            if certify:
                intersections = []
                for j in range(nbr_cliques):
                    for k in range(j + 1, nbr_cliques):
                        intersections.append(
                            ((j,k), reqd_cliques[j] & reqd_cliques[k]))
                return False, intersections
            else:
                return False


    def linear_code_graph(self):
        r"""
        """
        L = self.linear_code()
        return strongly_regular_from_two_weight_code(L)


    def sdp_design_matrix(self):
        r"""
        The function `sdp_design_matrix` returns
        the incidence matrix of the design of type $R(\mathtt{self})$,
        as described by Dillon and Schatz (1987).
        """
        dim = self.nvariables()
        v = 2 ** dim
        result = matrix(v, v)
        dual_self = self.walsh_hadamard_dual()
        dual_f = dual_self.extended_translate()
        for c in xsrange(v):
            result[c,:] = matrix([self.extended_translate(0, c, dual_f(c))(x)
                                for x in xsrange(v)])
        return result


    def walsh_hadamard_dual(self):
        r"""
        The function `walsh_hadamard_dual` returns a `BentFunction`
        based on the Walsh Hadamard transform of `self`.
        Since `self` is a bent function, the returned `BentFunction` is
        well-defined and is bent, being the *dual* bent function (Hou 1999)
        or *Fourier transform* of `self` (Rothaus 1976).

        *NOTE* The use of `1 + x/scale` here is to compensate for
        an incorrect sign in BooleanFunction.walsh_hadamard_transform(self).
        If this is ever fixed, then this must be changed to `1 - x/scale`.
        """
        dim = self.nvariables()
        scale = 2 ** (dim/2)
        return BentFunction([(1 + x/scale)/2 for x in self.walsh_hadamard_transform()])


    def weight_class(self):
        r"""
        """
        length = len(self)
        weight = self.weight()
        return wc.weight_class(length, weight)
