r"""
The ``bent_function`` module defines
the ``BentFunction`` class,
which represents a bent Boolean function and some of its properties.

AUTHORS:

- Paul Leopardi (2016-09-25): initial version

EXAMPLES:

::

    sage: from sage.crypto.boolean_function import BooleanFunction
    sage: bf = BooleanFunction([0,1,0,0])
    sage: bf.algebraic_normal_form()
    x0*x1 + x0
    sage: from boolean_cayley_graphs.bent_function import BentFunction
    sage: bentf = BentFunction(bf)
    sage: type(bentf)
    <class 'boolean_cayley_graphs.bent_function.BentFunction'>
    sage: bentf.algebraic_normal_form()
    x0*x1 + x0

REFERENCES:

.. Dillon [Dil1974]_, Rothaus [Rot1976]_, Tokareva [Tok2015]_.

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
from sage.misc.banner import require_version
from sage.matrix.constructor import matrix

from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved

import boolean_cayley_graphs.weight_class as wc


class BentFunction(BooleanFunctionImproved):
    r"""
    A bent Boolean function, with methods corresponding to some of its properties.

    The class inherits from BooleanFunctionImproved and is initialized
    in the same way as BooleanFunction.
    Since BooleanFunctionImproved inherits from Saveable, so does BentFunction.

    EXAMPLES:

    ::

        sage: import os
        sage: from boolean_cayley_graphs.bent_function import BentFunction
        sage: bentf = BentFunction([0,0,0,1])
        sage: bentf.algebraic_normal_form()
        x0*x1
        sage: d = tmp_dir()
        sage: bentf.save_mangled('example', directory=d)
        sage: ex = BentFunction.load_mangled('example', directory=d)
        sage: type(ex)
        <class 'boolean_cayley_graphs.bent_function.BentFunction'>
        sage: ex is bentf
        False
        sage: ex == bentf
        True
        sage: BentFunction.remove_mangled('example', directory=d)
        sage: os.rmdir(d)

    TESTS:

    ::

        sage: from sage.crypto.boolean_function import BooleanFunction
        sage: bf = BentFunction([0,1,0,0])
        sage: print(bf)
        Boolean function with 2 variables

        sage: from sage.crypto.boolean_function import BooleanFunction
        sage: bf = BentFunction([0,1,0,0])
        sage: latex(bf)
        \text{\texttt{Boolean{ }function{ }with{ }2{ }variables}}
    """


    def is_partial_spread_minus(self, certify=False):
        r"""
        Determine if a bent function is in the partial spread (-) class.

        Partial spread (-) is Dillon's :math:`\mathcal{PS}^{(-)}` class [Dil1974]_.

        INPUT:

        - ``self`` -- the current object.
        - ``certify`` -- boolean (default: False):

        OUTPUT:

        If certify is False, then return True if the bent function
        represented by ``self`` is in :math:`\mathcal{PS}^{(-)}`,
        otherwise return False.
        If certify is True then return two values,
        where the first is True or False as above,
        and if the first value is True, the second value is
        a list of intersections between maximal cliques,
        otherwie the second value is an empty list.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: bentf = BentFunction([0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,0])
            sage: bentf.is_bent()
            True
            sage: bentf.is_partial_spread_minus()
            True
            sage: bentf.is_partial_spread_minus(certify=True)
            (True, [{7, 11, 12}, {3, 13, 14}])
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
        Return the graph of the linear code corresponding to the bent function.

        INPUT:

        - ``self`` -- the current object.

        OUTPUT:

        The graph of the linear code corresponding to ``self``.
        This is a strongly regular graph [Car2010]_, [Del1972]_, [Din2015].

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: bentf = BentFunction([0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,0])
            sage: lcg = bentf.linear_code_graph()
            sage: type(lcg)
            <class 'sage.graphs.graph.Graph'>
            sage: lcg.is_strongly_regular(parameters=True)
            (16, 6, 2, 2)

        REFERENCES:

        .. Carlet [Car2010]_ Section 8.6 Proposition 8.29.

        .. Delsarte [Del1972]_.

        .. Ding [Din2015]_ Corollary 10.

        """
        L = self.linear_code()
        return strongly_regular_from_two_weight_code(L)


    def sdp_design_matrix(self):
        r"""
        Return the incidence matrix of the SDP design of the bent function.

        This method returns the incidence matrix of the design of type
        :math:`R(\mathtt{self})`, as described by Dillon and Schatz [DS1987]_.
        This is a design with the symmetric difference property [Kan1975]_.

        INPUT:

        - ``self`` -- the current object.

        OUTPUT:

        The incidence matrix of the SDP design corresponding to ``self``.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: bentf = BentFunction([0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,0])
            sage: sdp = bentf.sdp_design_matrix()
            sage: print(sdp)
            [0 0 0 1 0 0 0 1 0 0 0 1 1 1 1 0]
            [0 1 0 0 0 1 0 0 0 1 0 0 1 0 1 1]
            [0 0 1 0 0 0 1 0 0 0 1 0 1 1 0 1]
            [1 0 0 0 1 0 0 0 1 0 0 0 0 1 1 1]
            [0 0 0 1 1 1 1 0 0 0 0 1 0 0 0 1]
            [0 1 0 0 1 0 1 1 0 1 0 0 0 1 0 0]
            [0 0 1 0 1 1 0 1 0 0 1 0 0 0 1 0]
            [1 0 0 0 0 1 1 1 1 0 0 0 1 0 0 0]
            [0 0 0 1 0 0 0 1 1 1 1 0 0 0 0 1]
            [0 1 0 0 0 1 0 0 1 0 1 1 0 1 0 0]
            [0 0 1 0 0 0 1 0 1 1 0 1 0 0 1 0]
            [1 0 0 0 1 0 0 0 0 1 1 1 1 0 0 0]
            [1 1 1 0 0 0 0 1 0 0 0 1 0 0 0 1]
            [1 0 1 1 0 1 0 0 0 1 0 0 0 1 0 0]
            [1 1 0 1 0 0 1 0 0 0 1 0 0 0 1 0]
            [0 1 1 1 1 0 0 0 1 0 0 0 1 0 0 0]
            sage: from sage.combinat.designs.incidence_structures import IncidenceStructure
            sage: sdp_design = IncidenceStructure(sdp)
            sage: sdp_design.is_t_design(return_parameters=True)
            (True, (2, 16, 6, 2))

        REFERENCES:

        .. Dillon and Schatz [DS1987]_, Kantor [Kan1975]_.

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
        Return the Walsh Hadamard dual of the bent function.

        This method returns a ``BentFunction`` based on the Walsh Hadamard
        transform of ``self``. Since ``self`` is a bent function, the returned
        ``BentFunction` is well-defined and is bent, being the *dual*
        bent function [Hou1999]_ or *Fourier transform* of ``self`` [Rot1976]_.

        INPUT:

        - ``self`` -- the current object.

        OUTPUT:

        An object of class ``BentFunction``, being the dual of ``self``.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: bentf = BentFunction([0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,0])
            sage: dual_bentf = bentf.walsh_hadamard_dual()
            sage: type(dual_bentf)
            <class 'boolean_cayley_graphs.bent_function.BentFunction'>
            sage: dual_bentf.is_bent()
            True
            sage: dual_bentf.algebraic_normal_form()
            x0*x1 + x2*x3

        .. NOTE::

            Versions of Sage before 8.2 had an incorrect sign in
            ``BooleanFunction.walsh_hadamard_transform(self)``.
            See [Sage trac ticket #23931](https://trac.sagemath.org/ticket/23931)
            Previous versions of this method had ``1 + x/scale`` to compensate for
            an incorrect sign in ``BooleanFunction.walsh_hadamard_transform(self)``.
            [Since this has now been fixed in Sage 8.2](https://trac.sagemath.org/ticket/23931)
            this is now changed to ``1 - x/scale``.
        """
        dim = self.nvariables()
        scale = 2 ** (dim/2)
        coefficient = lambda x: (
                (1 - x/scale)/2
            if require_version(8,2,0)
            else
                (1 + x/scale)/2)
        return BentFunction([coefficient(x) for x in self.walsh_hadamard_transform()])


    def weight_class(self):
        r"""
        Return the weight class of the bent function.

        INPUT:

        - ``self`` -- the current object.

        OUTPUT:

        The value 0 or 1, being the weight class of ``self``.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: bentf = BentFunction([0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,0])
            sage: bentf.weight_class()
            0
        """
        length = len(self)
        weight = self.weight()
        return wc.weight_class(length, weight)
