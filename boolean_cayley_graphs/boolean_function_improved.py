r"""
An improved Boolean function class
==================================

The ``boolean_function_improved`` module defines
the ``BooleanFunctionImproved`` class,
which is a subclass of BooleanFunction that adds extra methods.
One such method is ``cayley_graph``,
which returns the Cayley graph of the Boolean function.

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
import csv

from datetime import datetime
from sage.crypto.boolean_function import BooleanFunction
from sage.matrix.constructor import Matrix
from sage.rings.finite_rings.finite_field_constructor import FiniteField as GF
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sys import stdout

from boolean_cayley_graphs.boolean_cayley_graph import boolean_cayley_graph
from boolean_cayley_graphs.boolean_linear_code import boolean_linear_code
from boolean_cayley_graphs.integer_bits import base2, inner
from boolean_cayley_graphs.linear import is_linear
from boolean_cayley_graphs.saveable import Saveable

import boolean_cayley_graphs.cayley_graph_controls as controls

encoding = "UTF-8"


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

    TESTS:

    ::

        sage: from sage.crypto.boolean_function import BooleanFunction
        sage: bf = BooleanFunctionImproved([0,1,0,0])
        sage: print(bf)
        Boolean function with 2 variables

        sage: from sage.crypto.boolean_function import BooleanFunction
        sage: bf = BooleanFunctionImproved([0,1,0,0])
        sage: latex(bf)
        \text{\texttt{Boolean{ }function{ }with{ }2{ }variables}}
   """


    @classmethod
    def from_tt_buffer(
        cls,
        dim,
        tt_buffer):
        r"""
        Constructor from the buffer tt_buffer.

        The buffer tt_buffer is assumed to be the result of method tt_buffer(),
        which returns a result of type buffer representing a truth table in hex.

        INPUT:

        - ``cls`` -- the class object.
        - ``dim`` -- integer: the dimension of the Boolean function.
        - ``tt_buffer`` -- buffer: the result of the method tt_buffer()
          for the Boolean function.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf2 = BooleanFunctionImproved([0,1,0,0])
            sage: bf2_tt_buffer = bf2.tt_buffer()
            sage: bf2_test = BooleanFunctionImproved.from_tt_buffer(2, bf2_tt_buffer)
            sage: bf2_test.algebraic_normal_form()
            x0*x1 + x0
            sage: bf2 == bf2_test
            True
            sage: bf3 = BooleanFunctionImproved([0,1,0,0]*2)
            sage: bf3.nvariables()
            3
            sage: bf3_tt_buffer = bf3.tt_buffer()
            sage: bf3_test = BooleanFunctionImproved.from_tt_buffer(3, bf3_tt_buffer)
            sage: bf3 == bf3_test
            True
        """
        tt_hex = str(binascii.b2a_hex(tt_buffer), encoding)
        return cls.from_tt_hex(dim, tt_hex)


    @classmethod
    def from_tt_hex(
        cls,
        dim,
        tt_hex):
        r"""
        Constructor from the dimension dim, and the string tt_hex.

        The string tt_hex is assumed to be the result of method tt_hex(), which returns
        a string representing a truth table in hex.

        INPUT:

        - ``cls`` -- the class object.
        - ``dim`` -- integer: the dimension of the Boolean function.
        - ``tt_hex`` -- string: the result of the method tt_hex() for the Boolean function.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf2 = BooleanFunctionImproved([0,1,0,0])
            sage: bf2_tt_hex = bf2.tt_hex()
            sage: bf2_test = BooleanFunctionImproved.from_tt_hex(2, bf2_tt_hex)
            sage: bf2_test.algebraic_normal_form()
            x0*x1 + x0
            sage: bf2 == bf2_test
            True

        TESTS:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf1 = BooleanFunctionImproved([0,1])
            sage: bf1_tt_hex = bf1.tt_hex()
            sage: bf1_test = BooleanFunctionImproved.from_tt_hex(1, bf1_tt_hex)
            sage: bf1_test.algebraic_normal_form()
            x
            sage: bf1 == bf1_test
            True
            sage: bf3 = BooleanFunctionImproved([0,1,0,0]*2)
            sage: bf3.nvariables()
            3
            sage: bf3_tt_hex = bf3.tt_hex()
            sage: bf3_test = BooleanFunctionImproved.from_tt_hex(3, bf3_tt_hex)
            sage: bf3 == bf3_test
            True
        """
        if dim < 3:
            # Convert the hex character to an Integer
            tt_integer = ZZ(tt_hex, 16)
            # Convert the integer to a bit string
            v = 2 ** dim
            tt_bits = base2(v, tt_integer)
            return BooleanFunctionImproved(tt_bits)
        else:
            return BooleanFunctionImproved(tt_hex)


    @classmethod
    def from_csv(
        cls,
        csv_file_name):
        """
        Constructor from a csv file.

        The csv file is assumed to be produced by the method save_as_csv().

        INPUT:

        - ``cls`` -- the class object.
        - ``csv_file_name`` -- string: the name of the csv file to read from.

        EXAMPLES:

        ::

            sage: import csv
            sage: import os
            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf2 = BooleanFunctionImproved([1,0,1,1])
            sage: bf2_csv_name = tmp_filename(ext='.csv')
            sage: bf2.save_as_csv(bf2_csv_name)
            sage: bf2_test = BooleanFunctionImproved.from_csv(bf2_csv_name)
            sage: bf2 == bf2_test
            True
            sage: os.remove(bf2_csv_name)
            sage: bf3 = BooleanFunctionImproved([0,1,0,0]*2)
            sage: bf3_csv_name = tmp_filename(ext='.csv')
            sage: bf3.save_as_csv(bf3_csv_name)
            sage: bf3_test = BooleanFunctionImproved.from_csv(bf3_csv_name)
            sage: bf3 == bf3_test
            True
        """
        with open(csv_file_name) as csv_file:
            reader = csv.DictReader(csv_file)
            row = next(reader)
            return BooleanFunctionImproved.from_tt_hex(
                int(row["nvariables"]),
                row["tt_hex"])


    def __invert__(self):
        """
        Return the complement Boolean function of `self`.

        INPUT:

        - ``self`` -- the current object.

        EXAMPLES:

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
        Return the elementwise sum of `self`and `other` which must have the same number of variables.

        INPUT:

        - ``self`` -- the current object.
        - ``other`` -- another Boolean function.

        OUTPUT:

        The elementwise sum of `self`and `other`

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf0 = BooleanFunctionImproved([1,0,1,0])
            sage: bf1 = BooleanFunctionImproved([1,1,0,0])
            sage: (bf0+bf1).truth_table(format='int')
            (0, 1, 1, 0)
            sage: S = bf0.algebraic_normal_form() + bf1.algebraic_normal_form()
            sage: (bf0+bf1).algebraic_normal_form() == S
            True

        TESTS:

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
        Return the elementwise product of `self`and `other` which must have the same number of variables.

        INPUT:

        - ``self`` -- the current object.
        - ``other`` -- another Boolean function.

        OUTPUT:

        The elementwise product of `self`and `other`

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf0 = BooleanFunctionImproved([1,0,1,0])
            sage: bf1 = BooleanFunctionImproved([1,1,0,0])
            sage: (bf0*bf1).truth_table(format='int')
            (1, 0, 0, 0)
            sage: P = bf0.algebraic_normal_form() * bf1.algebraic_normal_form()
            sage: (bf0*bf1).algebraic_normal_form() == P
            True

        TESTS:

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

        INPUT:

        - ``self`` -- the current object.
        - ``other`` -- another Boolean function.

        OUTPUT:

        The concatenation of `self`and `other`

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf0 = BooleanFunctionImproved([1,0,1,0])
            sage: bf1 = BooleanFunctionImproved([1,1,0,0])
            sage: (bf0|bf1).truth_table(format='int')
            (1, 0, 1, 0, 1, 1, 0, 0)
            sage: C = bf0.truth_table() + bf1.truth_table()
            sage: (bf0|bf1).truth_table(format='int') == C
            True

        TESTS:

        ::

            sage: bf0|BooleanFunctionImproved([0,1])
            Traceback (most recent call last):
            ...
            ValueError: the two Boolean functions must have the same number of variables
        """
        bf_self = BooleanFunction(self)
        return type(self)(bf_self | other)


    def __hash__(self):
        r"""
        Return the hash of ``self``.
        This makes the class hashable.


        INPUT:

        - ``self`` -- the current object.

        OUTPUT:

        The hash of ``self``.

        EXAMPLES::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf1 = BooleanFunctionImproved([0,1,0,0])
            sage: hash(bf1) == hash(bf1.tt_hex())
            True
        """
        return hash(self.tt_hex())


    def cayley_graph(self):
        r"""
        Return the Cayley graph of ``self``.

        INPUT:

        - ``self`` -- the current object.

        OUTPUT:

        The Cayley graph of ``self`` as an object of class ``Graph``.

        EXAMPLES::

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

        as described below.

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

            While ``self`` is a ``BooleanFunctionImproved``, the result of
            ``extended_translate`` is *not* a ``BooleanFunctionImproved``,
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


    def zero_translate(self, b=0, c=0):
        r"""
        Return an extended translation equivalent function of ``self`` that is 0 at 0.

        Given `self` and the non-negative numbers `b` and `c`, the function
        `zero_translate` returns the Python function

        :math:`x \mapsto \mathtt{bf}(x + b) + \langle c, x \rangle + \mathtt{bf}(b)`,

        as described below.

        INPUT:

        - ``self`` -- the current object.
        - ``b`` -- non-negative integer (default: 0).
        - ``c`` -- non-negative integer (default: 0).

        OUTPUT:

        The Python function

        :math:`x \mapsto \mathtt{self}(x + b) + \langle c, x \rangle + \mathtt{bf(b)}`,

        where `b` and `c` are mapped to :math:`\mathbb{F}_2^{dim}` by the
        lexicographical ordering implied by the ``base2`` function, and
        where ``dim`` is the number of variables of ``self`` as a ``BooleanFunction.``

        .. NOTE::

            While ``self`` is a ``BooleanFunctionImproved``, the result of
            ``zero_translate`` is *not* a ``BooleanFunctionImproved``,
            but rather a Python function that takes an ``Integer`` argument.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf1 = BooleanFunctionImproved([0,1,0,0])
            sage: f001 = bf1.zero_translate(b=0,c=0)
            sage: [f001(x) for x in range(4)]
            [0, 1, 0, 0]
        """
        return self.extended_translate(b, c, self.extended_translate()(b))


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

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf1 = BooleanFunctionImproved([0,1,0,0])
            sage: bf2 = BooleanFunctionImproved([0,0,1,0])
            sage: bf1.is_linear_equivalent(bf2)
            True
            sage: bf2.is_linear_equivalent(bf1, certificate=True)
            (
                  [0 1]
            True, [1 0]
            )

        """
        self_cg  = self.cayley_graph()
        try:
            other_cg = other.cayley_graph()
        except AttributeError:
            return (False, None) if certificate else False

        # Check the isomorphism between self_cg and other_cg via canonical labels.
        # This is to work around the slow speed of is_isomorphic in some cases.
        if self_cg.canonical_label() != other_cg.canonical_label():
            return (False, None) if certificate else False

        # Obtain the mapping that defines the isomorphism.
        is_isomorphic, mapping_dict = self_cg.is_isomorphic(other_cg, certificate=True)

        # If self_cg is not isomorphic to other_cg, it is not linear equivalent.
        if not is_isomorphic:
            return (False, None) if certificate else False

        mapping = lambda x: mapping_dict[x]

        dim = self.nvariables()
        v = 2 ** dim

        # Check that mapping is linear.
        if certificate:
            linear, mapping_matrix = is_linear(dim, mapping, certificate)
        else:
            linear = is_linear(dim, mapping)
        if linear:
            return (True, mapping_matrix) if certificate else True

        # For each permutation p in the automorphism group of self_cg,
        # check that the permuted mapping:
        # 1. preserves the value of other, and
        # 2. is linear.
        self_et = self.extended_translate()
        other_et = other.extended_translate()
        auto_group = self_cg.automorphism_group()
        test_group = auto_group.stabilizer(0) if mapping(0) == 0 else auto_group
        linear = False
        for p in test_group:
            p_mapping = lambda x: p(mapping(x))
            # Check that p_mapping preserves other.
            preserved = True
            # Check the basis elements
            for a in range(dim):
                if other_et(p_mapping(2**a)) != self_et(2**a):
                    preserved = False
                    break
            if not preserved:
                continue

            # Check all elements
            for x in range(v):
                if other_et(p_mapping(x)) != self_et(x):
                    preserved = False
                    break
            if not preserved:
                continue

            # Check that p_mapping is linear.
            if certificate:
                linear, mapping_matrix = is_linear(dim, p_mapping, certificate)
            else:
                linear = is_linear(dim, p_mapping)
            # We only need to find one linear p_mapping that preserves other.
            if linear:
                break

        if certificate:
            return (True, mapping_matrix) if linear else (False, None)
        else:
            return linear


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
            sage: c2.generator_matrix().echelon_form()
            [1 0 0 0 1]
            [0 1 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 1]

        REFERENCES:

        .. Carlet [Car2010]_ Section 8.6.

        .. Ding [Ding2015]_ Corollary 10.

        """
        dim = self.nvariables()
        f = self.extended_translate()
        return boolean_linear_code(dim, f)


    def save_as_csv(self, file_name):
        """
        Save the current object as a csv file.

        INPUT:

        - ``self`` -- the current object.
        - ``file_name`` -- the file name.

        OUTPUT:

        None.

        EXAMPLES:

        ::

            sage: import csv
            sage: import os
            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf2 = BooleanFunctionImproved([0,1,0,1])
            sage: bf2_csv_name = tmp_filename(ext='.csv')
            sage: bf2.save_as_csv(bf2_csv_name)
            sage: with open(bf2_csv_name) as bf2_csv_file:
            ....:     reader = csv.DictReader(bf2_csv_file)
            ....:     for row in reader:
            ....:         print(row["nvariables"], row["tt_hex"])
            ....:
            2 a
            sage: os.remove(bf2_csv_name)
        """
        fieldnames = [
            "nvariables",
            "tt_hex"]
        with open(file_name,"w") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({
                "nvariables":
                    self.nvariables(),
                "tt_hex":
                    self.tt_hex()})


    def tt_buffer(self):
        r"""
        Return a buffer containing a compressed version of the truth table.

        INPUT:

        - ``self`` -- the current object.

        OUTPUT:

        A buffer containing a compressed version of the truth table of ``self``.

        EXAMPLES:

        ::

            sage: import binascii
            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf2 = BooleanFunctionImproved([0,1,0,0])
            sage: buff_bf2 = bf2.tt_buffer()
            sage: type(buff_bf2)
            <class 'bytes'>
            sage: encoding = "UTF-8"
            sage: print(str(binascii.b2a_hex(buff_bf2), encoding))
            02

        TESTS:

        ::

            sage: bf3 = BooleanFunctionImproved([0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,1])
            sage: buff_bf3 = bf3.tt_buffer()
            sage: type(buff_bf3)
            <class 'bytes'>
            sage: encoding = "UTF-8"
            sage: print(str(binascii.b2a_hex(buff_bf3), encoding))
            c122
            sage: from_buff_bf3 = BooleanFunctionImproved.from_tt_buffer(3, buff_bf3)
            sage: from_buff_bf3 == buff_bf3
            False
            sage: from_buff_bf3 == bf3
            True
            sage: hex_str6 = "0123456789112345678921234567893123456789412345678951234567896123"
            sage: bf6 = BooleanFunctionImproved(hex_str6)
            sage: buff_bf6 = bf6.tt_buffer()
            sage: from_buff_bf6 = BooleanFunctionImproved.from_tt_buffer(6, buff_bf6)
            sage: from_buff_bf6 == bf6
            True
            sage: str(binascii.b2a_hex(buff_bf6), encoding) == hex_str6
            True
        """
        dim = self.nvariables()

        # Use tt_hex() to otain a string representing the truth table in hex.
        tt_hex = self.tt_hex()
        # Pad tt_hex to the correct length for a buffer.
        tt_string = (
                "0" + tt_hex
            if len(tt_hex) < 2
            else
                tt_hex)
        return binascii.a2b_hex(tt_string)


    def tt_hex(self):
        r"""
        Return a hex string representing the truth table of the Boolean function.

        INPUT:

        - ``self`` -- the current object.

        OUTPUT:

        A string representing the truth table of ``self`` in hex.

        EXAMPLES:

        ::

            sage: import binascii
            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: bf2 = BooleanFunctionImproved([0,1,0,0])
            sage: str_bf2 = bf2.tt_hex()
            sage: type(str_bf2)
            <class 'str'>
            sage: print(str_bf2)
            2
            sage: bf3 = BooleanFunctionImproved([0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,1])
            sage: str_bf3 = bf3.tt_hex()
            sage: print(str_bf3)
            c122
        """
        dim = self.nvariables()
        # Convert the truth table into an integer.
        ZZ_truth_table_2 = ZZ(self.truth_table(), 2)
        # Convert the integer to a hex string.
        tt = ZZ_truth_table_2.str(16)
        if dim < 2:
            # If dim < 2 then the truth table in hex fits within 1 hex digit.
            buffer_len = 1
        else:
            # The following code is based on BooleanFunction.truth_table().
            # Variable tt represents truth_table in hex.
            # The code does not use truth_table(format='hex') because of
            # https://trac.sagemath.org/ticket/24282

            # Pad tt so that length in hex digits is a power of 2.
            # This assumes that dim is at least 2.
            buffer_len = 1 << (dim - 2)
        # Pad the tt string to the correct length.
        padding = "0" * (buffer_len - len(tt))
        return padding + tt


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
