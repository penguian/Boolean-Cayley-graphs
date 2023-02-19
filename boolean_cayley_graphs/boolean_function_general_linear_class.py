r"""
A boolean function class that represents a General Linear Equivalence Class
============================================================================

The ``boolean_function_general_linear_class`` module defines
the ``BooleanFunctionGeneralLinearClass`` class,
which is a subclass of BooleanFunctionImproved that represents
a general linear equivalence class of boolean functions.


AUTHORS:

- Paul Leopardi (2023-02-05): initial version

EXAMPLES:

::

    sage: from boolean_cayley_graphs.boolean_function_general_linear_class import (
    ....:     BooleanFunctionGeneralLinearClass)
    sage: bf = BooleanFunctionGeneralLinearClass([0,0,0,1])
    sage: type(bf)
    <class 'boolean_cayley_graphs.boolean_function_general_linear_class.BooleanFunctionGeneralLinearClass'>
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

from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
from boolean_cayley_graphs.saveable import Saveable

import boolean_cayley_graphs.cayley_graph_controls as controls

encoding = "UTF-8"


class BooleanFunctionGeneralLinearClass(BooleanFunctionImproved, Saveable):
    r"""
    A subclass of BooleanFunctionImproved that represents
    a general linear equivalence class of boolean functions.

    The class inherits from BooleanFunctionImproved and is initialized in the same way.
    The class inherits from Saveable to obtain load_mangled and save_mangled methods.

    EXAMPLES:

    ::

        sage: from boolean_cayley_graphs.boolean_function_general_linear_class import (
        ....:     BooleanFunctionGeneralLinearClass)
        sage: bf1 = BooleanFunctionGeneralLinearClass([0,1,0,0])
        sage: type(bf1)
        <class 'boolean_cayley_graphs.boolean_function_general_linear_class.BooleanFunctionGeneralLinearClass'>
        sage: bf1.algebraic_normal_form()
        x0*x1 + x0
        sage: bf1.truth_table()
        (False, True, False, False)

    TESTS:

    ::

        sage: from boolean_cayley_graphs.boolean_function_general_linear_class import (
        ....:     BooleanFunctionGeneralLinearClass)
        sage: bf = BooleanFunctionGeneralLinearClass([0,1,0,0])
        sage: print(bf)
        Boolean function with 2 variables

        sage: from boolean_cayley_graphs.boolean_function_general_linear_class import (
        ....:     BooleanFunctionGeneralLinearClass)
        sage: bf = BooleanFunctionGeneralLinearClass([0,1,0,0])
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

            sage: from boolean_cayley_graphs.boolean_function_general_linear_class import (
            ....:     BooleanFunctionGeneralLinearClass)
            sage: bf2 = BooleanFunctionGeneralLinearClass([0,1,0,0])
            sage: bf2_tt_buffer = bf2.tt_buffer()
            sage: bf2_test = BooleanFunctionGeneralLinearClass.from_tt_buffer(2, bf2_tt_buffer)
            sage: bf2_test.algebraic_normal_form()
            x0*x1 + x0
            sage: bf2 == bf2_test
            True
            sage: bf3 = BooleanFunctionGeneralLinearClass([0,1,0,0]*2)
            sage: bf3.nvariables()
            3
            sage: bf3_tt_buffer = bf3.tt_buffer()
            sage: bf3_test = BooleanFunctionGeneralLinearClass.from_tt_buffer(3, bf3_tt_buffer)
            sage: bf3 == bf3_test
            True
        """
        return cls(BooleanFunctionImproved.from_tt_buffer(dim, tt_buffer))


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

            sage: from boolean_cayley_graphs.boolean_function_general_linear_class import (
            ....:     BooleanFunctionGeneralLinearClass)
            sage: bf2 = BooleanFunctionGeneralLinearClass([0,1,0,0])
            sage: bf2_tt_hex = bf2.tt_hex()
            sage: bf2_test = BooleanFunctionGeneralLinearClass.from_tt_hex(2, bf2_tt_hex)
            sage: bf2_test.algebraic_normal_form()
            x0*x1 + x0
            sage: bf2 == bf2_test
            True

        TESTS:

        ::

            sage: from boolean_cayley_graphs.boolean_function_general_linear_class import (
            ....:     BooleanFunctionGeneralLinearClass)
            sage: bf1 = BooleanFunctionGeneralLinearClass([0,1])
            sage: bf1_tt_hex = bf1.tt_hex()
            sage: bf1_test = BooleanFunctionGeneralLinearClass.from_tt_hex(1, bf1_tt_hex)
            sage: bf1_test.algebraic_normal_form()
            x
            sage: bf1 == bf1_test
            True
            sage: bf3 = BooleanFunctionGeneralLinearClass([0,1,0,0]*2)
            sage: bf3.nvariables()
            3
            sage: bf3_tt_hex = bf3.tt_hex()
            sage: bf3_test = BooleanFunctionGeneralLinearClass.from_tt_hex(3, bf3_tt_hex)
            sage: bf3 == bf3_test
            True
        """
        return cls(BooleanFunctionImproved.from_tt_hex(dim, tt_hex))


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
            sage: from boolean_cayley_graphs.boolean_function_general_linear_class import (
            ....:     BooleanFunctionGeneralLinearClass)
            sage: bf2 = BooleanFunctionGeneralLinearClass([1,0,1,1])
            sage: bf2_csv_name = tmp_filename(ext='.csv')
            sage: bf2.save_as_csv(bf2_csv_name)
            sage: bf2_test = BooleanFunctionGeneralLinearClass.from_csv(bf2_csv_name)
            sage: bf2 == bf2_test
            True
            sage: os.remove(bf2_csv_name)
            sage: bf3 = BooleanFunctionGeneralLinearClass([0,1,0,0]*2)
            sage: bf3_csv_name = tmp_filename(ext='.csv')
            sage: bf3.save_as_csv(bf3_csv_name)
            sage: bf3_test = BooleanFunctionGeneralLinearClass.from_csv(bf3_csv_name)
            sage: bf3 == bf3_test
            True
        """
        return cls(BooleanFunctionImproved.from_csv(csv_file_name))


    def __eq__(self, other):
        """
        Test for equality between extended translation equivalence classes.

        WARNING:

        This test is for mathematical equivalence rather than strict equality.

        INPUT:

        - ``other`` - BooleanFunctionExtendedTranslateClassification: another equivalence class.

        OUTPUT:

        A Boolean value indicating whether ``self`` is equivalent to ``other``.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: from boolean_cayley_graphs.boolean_function_extended_translate_classification import (
            ....:     BooleanFunctionExtendedTranslateClassification as BooleanFunctionETC)
            sage: R2.<x0,x1> = BooleanPolynomialRing(2)
            sage: p = x0*x1
            sage: f1 =BooleanFunctionImproved(p)
            sage: c1 = BooleanFunctionETC.from_function(f1)
            sage: f2 =BooleanFunctionImproved([0,0,0,1])
            sage: c2 = BooleanFunctionETC.from_function(f2)
            sage: print(c2.algebraic_normal_form)
            x0*x1
            sage: print(c1 == c2)
            True
        """
        return self.is_linear_equivalent(other)


    def __invert__(self):
        """
        Return the complement Boolean function of `self`.

        INPUT:

        - ``self`` -- the current object.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_general_linear_class import BooleanFunctionGeneralLinearClass
            sage: bf0 = BooleanFunctionGeneralLinearClass([1,0,1,1])
            sage: bf1 = ~bf0
            sage: type(bf1)
            <class 'boolean_cayley_graphs.boolean_function_general_linear_class.BooleanFunctionGeneralLinearClass'>
            sage: bf1.algebraic_normal_form()
            x0*x1 + x0
            sage: bf1.truth_table()
            (False, True, False, False)
        """
        bf_self = BooleanFunctionImproved(self)
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

            sage: from boolean_cayley_graphs.boolean_function_general_linear_class import BooleanFunctionGeneralLinearClass
            sage: bf0 = BooleanFunctionGeneralLinearClass([1,0,1,0])
            sage: bf1 = BooleanFunctionGeneralLinearClass([1,1,0,0])
            sage: (bf0+bf1).truth_table(format='int')
            (0, 1, 1, 0)
            sage: S = bf0.algebraic_normal_form() + bf1.algebraic_normal_form()
            sage: (bf0+bf1).algebraic_normal_form() == S
            True

        TESTS:

        ::

            sage: bf0+BooleanFunctionGeneralLinearClass([0,1])
            Traceback (most recent call last):
            ...
            ValueError: the two Boolean functions must have the same number of variables
        """
        bf_self = BooleanFunctionImproved(self)
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

            sage: from boolean_cayley_graphs.boolean_function_general_linear_class import BooleanFunctionGeneralLinearClass
            sage: bf0 = BooleanFunctionGeneralLinearClass([1,0,1,0])
            sage: bf1 = BooleanFunctionGeneralLinearClass([1,1,0,0])
            sage: (bf0*bf1).truth_table(format='int')
            (1, 0, 0, 0)
            sage: P = bf0.algebraic_normal_form() * bf1.algebraic_normal_form()
            sage: (bf0*bf1).algebraic_normal_form() == P
            True

        TESTS:

        ::

            sage: bf0*BooleanFunctionGeneralLinearClass([0,1])
            Traceback (most recent call last):
            ...
            ValueError: the two Boolean functions must have the same number of variables
        """
        bf_self = BooleanFunctionImproved(self)
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

            sage: from boolean_cayley_graphs.boolean_function_general_linear_class import BooleanFunctionGeneralLinearClass
            sage: bf0 = BooleanFunctionGeneralLinearClass([1,0,1,0])
            sage: bf1 = BooleanFunctionGeneralLinearClass([1,1,0,0])
            sage: (bf0|bf1).truth_table(format='int')
            (1, 0, 1, 0, 1, 1, 0, 0)
            sage: C = bf0.truth_table() + bf1.truth_table()
            sage: (bf0|bf1).truth_table(format='int') == C
            True

        TESTS:

        ::

            sage: bf0|BooleanFunctionGeneralLinearClass([0,1])
            Traceback (most recent call last):
            ...
            ValueError: the two Boolean functions must have the same number of variables
        """
        bf_self = BooleanFunctionImproved(self)
        return type(self)(bf_self | other)
