r"""
A subclass of BooleanFunction that adds extra methods.

AUTHORS:

- Paul Leopardi (2016-08-23): initial version

EXAMPLES:

::

    sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
    sage: bf = BooleanFunctionImproved([0,0,0,1])
    sage: type(bf)
    <class 'boolean_cayley_graphs.boolean_function_improved.BooleanFunctionImproved'>
    sage: bf.truth_table(format='int')
    (0, 0, 0, 1)

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
from sage.crypto.boolean_function import BooleanFunction

from boolean_cayley_graphs.boolean_cayley_graph import boolean_cayley_graph
from boolean_cayley_graphs.boolean_linear_code import boolean_linear_code
from boolean_cayley_graphs.integer_bits import inner
from boolean_cayley_graphs.saveable import Saveable


base2 = lambda dim, num: num.digits(2, padto=dim)
r"""
Map ``num`` to :math:`\mathbb{F}_2^{dim}` using lexicographical ordering.

INPUT:

- ``num`` -- non-negative integer. The value to be mapped.
- ``dim`` -- positive integer. The Boolean dimension.

OUTPUT:

A list of 0,1 integer values of length ``dim``.

EXAMPLES:

::

    sage: from boolean_cayley_graphs.boolean_function_improved import base2
    sage: base2(5,3)
    [1, 1, 0, 0, 0]
    sage: base2(3,5)
    [1, 0, 1]
    sage: base2(3,1)
    [1, 0, 0]
"""

class BooleanFunctionImproved(BooleanFunction, Saveable):
    r"""
    A subclass of BooleanFunction that adds extra methods.

    The class inherits from BooleanFunction is initialized in the same way.
    The class inherits from Saveable to obtain
    load_mangled and save_mangled methods.

    EXAMPLES:

    ::

        sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
        sage: bf1 = BooleanFunctionImproved([0,1,0,0])
        sage: type(bf1)
        <class 'boolean_cayley_graphs.boolean_function_improved.BooleanFunctionImproved'>
        sage: bf1.algebraic_normal_form()
        x0*x1 + x0
        sage: bf1.truth_table()
        (False, True, False, False)

    """


    def cayley_graph(self):
        r"""
        Return the Cayley graph of ``self``.

        INPUT:

        - ``self`` -- the current object.

        OUTPUT:

        The Cayley graph of ``self`` as an object of class ``Graph``.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf1 = BooleanFunctionImproved([0,1,0,0])
            sage: g1 = bf1.cayley_graph()
            sage: g1.adjacency_matrix()
            [0 1 0 0]
            [1 0 0 0]
            [0 0 0 1]
            [0 0 1 0]

        """
        dim = self.nvariables()
        f = self.extended_translate()
        return boolean_cayley_graph(dim, f)


    def extended_translate(self, b=0, c=0, d=0):
        r"""
        Return an extended translation equivalent function of ``self``.

        Given the non-negative numbers `b`, `c` and `d`, the function
        `extended_translate` returns the Python function

        :math:`x \mapsto \mathtt{self}(x + b) + \langle c, x \rangle + d`,

        as decribed below.

        INPUT:

        - ``self`` -- the current object.
        - ``b`` -- non-negtative integer (default: 0)
          which is mapped to :math:`\mathbb{F}_2^{dim}`.
        - ``c`` -- non-negtative integer (default: 0).
        - ``d`` -- integer, 0 or 1 (default: 0).

        OUTPUT:

        The Python function

        :math:`x \mapsto \mathtt{self}(x + b) + \langle c, x \rangle + d`,

        where `b` and `c` are mapped to :math:`\mathbb{F}_2^{dim}` by the
        lexicographical ordering implied by the ``base2`` function, and
        where ``dim`` is the number of variables of ``self`` as a
        ``BooleanFunction.``

        .. NOTE::

            While ``self`` is a ``BooleanFunction``, the result of
            ``extended_translate`` is *not* a ``BooleanFunction``,
            but rather a Python function that takes an ``integer`` argument.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf1 = BooleanFunctionImproved([0,1,0,0])
            sage: f001 = bf1.extended_translate(b=0,c=0,d=1)
            sage: [f001(x) for x in range(4)]
            [1, 0, 1, 1]
        """
        dim = self.nvariables()
        return lambda x: self(base2(dim, x ^ b)) ^ (0 if c == 0 else inner(c, x)) ^ d


    def linear_code(self):
        r"""
        Return the Boolean linear code corresponding to ``self``.

        INPUT:

        - ``self`` -- the current object.

        OUTPUT:

        An object of class ``LinearCode`` representing the Boolean linear code
        corresponding to self.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf2 = BooleanFunctionImproved([0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,1])
            sage: bf2.algebraic_normal_form()
            x0*x1*x2*x3 + x0*x1 + x0*x2*x3 + x0 + x1*x3 + x2*x3 + x3
            sage: c2 = bf2.linear_code()
            sage: c2.basis()
            [
            (1, 0, 0, 0, 1),
            (0, 1, 0, 0, 0),
            (0, 0, 1, 0, 0),
            (0, 0, 0, 1, 1)
            ]

        REFERENCES:

        .. [Car2010]_ Section 8.6.

        .. [DD2015]_ Corollary 10.

        """
        dim = self.nvariables()
        f = self.extended_translate()
        return boolean_linear_code(dim, f)


    def weight(self):
        r"""
        Return the Hamming weight of ``self``.

        INPUT:

        - ``self`` -- the current object.

        OUTPUT:

        A positive integer giving the number of 1 bits in the truth table of ``self``,
        in other words, the cardinality of the support of ``self`` as a
        Boolean function.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf1 = BooleanFunctionImproved([0,1,0,0])
            sage: bf2 = BooleanFunctionImproved([0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,1])
            sage: bf1.truth_table()
            (False, True, False, False)
            sage: bf1.weight()
            1
            sage: bf2.truth_table(format='int')
            (0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1)
            sage: sum([int(bf2(x)) for x in range(16)])
            5
            sage: bf2.weight()
            5
        """
        return sum(self.truth_table(format='int'))
