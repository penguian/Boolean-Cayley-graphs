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

import binascii

from sage.arith.srange import xsrange
from sage.crypto.boolean_function import BooleanFunction
from sage.modules.vector_mod2_dense import vector
from sage.rings.finite_rings.finite_field_constructor import FiniteField as GF
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ

from boolean_cayley_graphs.boolean_cayley_graph import boolean_cayley_graph
from boolean_cayley_graphs.boolean_graph import BooleanGraph
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


    @classmethod
    def from_tt_buffer(
        cls,
        tt_buffer):
        r"""
        Construct an object of type BooleanFunctionImproved from the result of method tt_buffer.

        Method tt_buffer returns either:
           a result of type str representing a truth table in binary (right to left)
        or:
           a result of type buffer representing a truth table in hex.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf2 = BooleanFunctionImproved([0,1,0,0])
            sage: bf2_tt_buffer = bf2.tt_buffer()
            sage: bf2_test = BooleanFunctionImproved.from_tt_buffer(bf2_tt_buffer)
            sage: bf2_test.algebraic_normal_form()
            x0*x1 + x0
            sage: bf2 == bf2_test
            True
            sage: bf3 = BooleanFunctionImproved([0,1,0,0]*2)
            sage: bf3.nvariables()
            3
            sage: bf3_tt_buffer = bf3.tt_buffer()
            sage: bf3_test = BooleanFunctionImproved.from_tt_buffer(bf3_tt_buffer)
            sage: bf3 == bf3_test
            True

        """
        tt = (
                binascii.b2a_hex(tt_buffer)
            if isinstance(tt_buffer, buffer)
            else
                [int(bit) for bit in tt_buffer[::-1]])
        return BooleanFunctionImproved(tt)


    def __invert__(self):
        """
        Return the complement Boolean function of `self`.

        EXAMPLES

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf0 = BooleanFunctionImproved([1,0,1,1])
            sage: bf1 = ~bf0
            sage: type(bf1)
            <class 'boolean_cayley_graphs.boolean_function_improved.BooleanFunctionImproved'>
            sage: bf1.algebraic_normal_form()
            x0*x1 + x0
            sage: bf1.truth_table()
            (False, True, False, False)
        """
        bf_self = BooleanFunction(self)
        return type(self)(~bf_self)


    def __add__(self, other):
        """
        Return the element wise sum of `self`and `other` which must have the same number of variables.

        EXAMPLES

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf0 = BooleanFunctionImproved([1,0,1,0])
            sage: bf1 = BooleanFunctionImproved([1,1,0,0])
            sage: (bf0+bf1).truth_table(format='int')
            (0, 1, 1, 0)
            sage: S = bf0.algebraic_normal_form() + bf1.algebraic_normal_form()
            sage: (bf0+bf1).algebraic_normal_form() == S
            True

        TESTS

        ::

            sage: bf0+BooleanFunctionImproved([0,1])
            Traceback (most recent call last):
            ...
            ValueError: the two Boolean functions must have the same number of variables
        """
        bf_self = BooleanFunction(self)
        return type(self)(bf_self + other)


    def __mul__(self, other):
        """
        Return the elementwise multiplication of `self`and `other` which must have the same number of variables.

        EXAMPLES

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf0 = BooleanFunctionImproved([1,0,1,0])
            sage: bf1 = BooleanFunctionImproved([1,1,0,0])
            sage: (bf0*bf1).truth_table(format='int')
            (1, 0, 0, 0)
            sage: P = bf0.algebraic_normal_form() * bf1.algebraic_normal_form()
            sage: (bf0*bf1).algebraic_normal_form() == P
            True

        TESTS

        ::

            sage: bf0*BooleanFunctionImproved([0,1])
            Traceback (most recent call last):
            ...
            ValueError: the two Boolean functions must have the same number of variables
        """
        bf_self = BooleanFunction(self)
        return type(self)(bf_self * other)


    def __or__(self, other):
        """
        Return the concatenation of `self` and `other` which must have the same number of variables.

        EXAMPLES

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf0 = BooleanFunctionImproved([1,0,1,0])
            sage: bf1 = BooleanFunctionImproved([1,1,0,0])
            sage: (bf0|bf1).truth_table(format='int')
            (1, 0, 1, 0, 1, 1, 0, 0)
            sage: C = bf0.truth_table() + bf1.truth_table()
            sage: (bf0|bf1).truth_table(format='int') == C
            True

        TESTS

        ::

            sage: bf0|BooleanFunctionImproved([0,1])
            Traceback (most recent call last):
            ...
            ValueError: the two Boolean functions must have the same number of variables
        """
        bf_self = BooleanFunction(self)
        return type(self)(bf_self | other)


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


    def extended_cayley_graph(self):
        r"""
        Return the extended Cayley graph of ``self``.

        INPUT:

        - ``self`` -- the current object.

        OUTPUT:

        The extended Cayley graph of ``self`` as an object of class ``Graph``.
        This is the Cayley graph of ``self`` if ``self(0) == False``,
        otherwise it is the Cayley graph of ``~self``.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf1 = BooleanFunctionImproved([0,1,0,0])
            sage: g1 = bf1.extended_cayley_graph()
            sage: g1.adjacency_matrix()
            [0 1 0 0]
            [1 0 0 0]
            [0 0 0 1]
            [0 0 1 0]
            sage: bf2 = BooleanFunctionImproved([1,0,1,1])
            sage: g2 = bf2.extended_cayley_graph()
            sage: g2.adjacency_matrix()
            [0 1 0 0]
            [1 0 0 0]
            [0 0 0 1]
            [0 0 1 0]

        """
        return ((~self).cayley_graph()
            if self(0)
            else self.cayley_graph())


    def extended_translate(self, b=0, c=0, d=0):
        r"""
        Return an extended translation equivalent function of ``self``.

        Given the non-negative numbers `b`, `c` and `d`, the function
        `extended_translate` returns the Python function

        :math:`x \mapsto \mathtt{self}(x + b) + \langle c, x \rangle + d`,

        as decribed below.

        INPUT:

        - ``self`` -- the current object.
        - ``b`` -- non-negative integer (default: 0)
          which is mapped to :math:`\mathbb{F}_2^{dim}`.
        - ``c`` -- non-negative integer (default: 0).
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
            but rather a Python function that takes an ``Integer`` argument.

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


    def is_linear_equivalent(self, other, certificate=False):
        r"""
        Check if there is a linear equivalence between ``self`` and ``other``:

        :math:`\mathtt{other}(M x) = \mathtt{self}(x)`,

        where M is a GF(2) matrix.

        INPUT:

        - ``self`` -- the current object.
        - ``other`` -- another object of class BooleanFunctionImproved.
        - ``certificate`` -- bool (default False). If true, return a GF(2) matrix
           that defines the isomorphism.

        OUTPUT:

        If ``certificate`` is false, a bool value.
        If ``certificate`` is true, a tuple consisting of either (False, None)
        or (True, M), where M is a GF(2) matrix that defines the equivalence.

        """
        dim = self.nvariables()
        v = 2 ** dim

        self_bg  = BooleanGraph(self.cayley_graph())
        other_bg = BooleanGraph(other.cayley_graph())
        is_linear_isomorphic, M = self_bg.is_linear_isomorphic(
            other_bg,
            certificate=True)
        if not is_linear_isomorphic:
            return (False, None) if certificate else False
        self_et = self.extended_translate()
        for ix in xsrange(v):
            x = vector(GF(2),base2(dim, ix))
            if Integer(other(list(M * x))) != self_et(ix):
                return (False, None) if certificate else False
            return (True, M) if certificate else True


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


    def tt_buffer(self):
        r"""
        Return a buffer containing the binary version of the truth table.

        INPUT:

        - ``self`` -- the current object.

        OUTPUT:

        A buffer containing the binary version of the truth table of ``self``.

        EXAMPLES:

        ::

            sage: import binascii
            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf2 = BooleanFunctionImproved([0,1,0,0])
            sage: buff_bf2 = bf2.tt_buffer()
            sage: type(buff_bf2)
            <type 'str'>
            sage: print(buff_bf2)
            0010
            sage: bf3 = BooleanFunctionImproved([0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,1])
            sage: buff_bf3 = bf3.tt_buffer()
            sage: type(buff_bf3)
            <type 'buffer'>
            sage: print(binascii.b2a_hex(buff_bf3))
            c122
            sage: from_buff_bf3 = BooleanFunctionImproved.from_tt_buffer(buff_bf3)
            sage: from_buff_bf3 == buff_bf3
            False
            sage: from_buff_bf3 == bf3
            True
            sage: hex_str6 = "0123456789112345678921234567893123456789412345678951234567896123"
            sage: bf6 = BooleanFunctionImproved(hex_str6)
            sage: buff_bf6 = bf6.tt_buffer()
            sage: from_buff_bf6 = BooleanFunctionImproved.from_tt_buffer(buff_bf6)
            sage: from_buff_bf6 == bf6
            True
            sage: binascii.b2a_hex(buff_bf6) == hex_str6
            True
        """
        # Convert the truth table into an integer.
        ZZ_truth_table_2 = ZZ(self.truth_table(), 2)
        dim = self.nvariables()
        if dim < 3:
            # If dim < 3 then the truth table in hex is less than 2 hex digits long.
            # This would make the buffer less than 1 byte in length,
            # which is unusable. Return a binary string instead.
            tt = ZZ_truth_table_2.str(2)

            # Pad tt so that length in bits is a power of 2.
            buffer_len = 1 << dim
        else:
            # The following code is based on BooleanFunction.truth_table().
            # Variable tt represents truth_table in hex.
            # The code does not use truth_table(format='hex') because of
            # https://trac.sagemath.org/ticket/24282
            tt = ZZ_truth_table_2.str(16)

            # Pad tt so that length in hex digits is an even power of 2.
            # This assumes that dim is at least 2.
            buffer_len = max(2, 1 << (dim - 2))
        # Pad the tt string to the correct length.
        padding = "0" * (buffer_len - len(tt))
        tt_str = padding + tt
        # If dim < 3 then return a string, otherwise return a buffer.
        return (
                tt_str
            if dim < 3
            else
                buffer(binascii.a2b_hex(tt_str)))


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
