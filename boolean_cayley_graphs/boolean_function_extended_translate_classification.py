r"""
Classification of boolean functions within an extended translation class
========================================================================

The ``boolean_function_extended_translate_classification`` module defines:

 * the ``BooleanFunctionExtendedTranslateClassification`` class;
   which represents the classification of the general linear classes
   within the extended translation class of a boolean function; and
 * the ``BooleanFunctionExtendedTranslateClassPart`` class,
   which represents part of an extended translate classification.

AUTHORS:

- Paul Leopardi (2023-01-26): initial version

EXAMPLES:

::

    The classification of the boolean function defined by the polynomial x2 + x1*x2.

    sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
    sage: from boolean_cayley_graphs.boolean_function_extended_translate_classification import (
    ....:     BooleanFunctionExtendedTranslateClassification as BooleanFunctionETC)
    sage: R2.<x1,x2> = BooleanPolynomialRing(2)
    sage: p = x2+x1*x2
    sage: f = BooleanFunctionImproved(p)
    sage: c = BooleanFunctionETC.from_function(f)
    sage: dict(sorted(c.__dict__.items()))
    {'algebraic_normal_form': x0*x1 + x1,
     'boolean_function_index_matrix': [0 2 1 3]
     [1 3 0 2]
     [2 0 3 1]
     [3 1 2 0],
     'boolean_function_list': [Boolean function with 2 variables,
      Boolean function with 2 variables,
      Boolean function with 2 variables,
      Boolean function with 2 variables],
     'general_linear_class_index_matrix': [0 0 1 0]
     [1 0 0 0]
     [0 0 0 1]
     [0 1 0 0],
     'general_linear_class_list': [Boolean function with 2 variables,
      Boolean function with 2 variables]}

REFERENCES:

The extended translation equivalence class and the general linear equivalence class
of a boolean function are defined by Leopardi [Leo2017]_.
"""
#*****************************************************************************
#       Copyright (C) 2016-2023 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************


from datetime import datetime
from numpy import array, argwhere
from sage.functions.log import log
from sage.graphs.graph import Graph
from sage.matrix.constructor import matrix
from sage.misc.latex import latex
from sage.misc.persist import load
from sage.plot.matrix_plot import matrix_plot
from sage.rings.integer import Integer
from sage.structure.sage_object import SageObject
from sys import stdout

import glob
import numpy as np

from boolean_cayley_graphs.boolean_function_improved import (
    BooleanFunctionImproved)
from boolean_cayley_graphs.boolean_function_general_linear_class import (
    BooleanFunctionGeneralLinearClass)
from boolean_cayley_graphs.containers import (
    BijectiveList, List, ShelveBijectiveList)
from boolean_cayley_graphs.saveable import Saveable

import boolean_cayley_graphs.cayley_graph_controls as controls
import csv
import os.path

default_algorithm = "sage"


class BooleanFunctionExtendedTranslateClassPart(SageObject, Saveable):
    r"""
    Partial classification of the general linear classes within the
    extended translation equivalence class of a boolean function.

    EXAMPLES:

    ::

        sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
        sage: from boolean_cayley_graphs.boolean_function_extended_translate_classification import (
        ....:     BooleanFunctionExtendedTranslateClassPart as BooleanFunctionETCPart)
        sage: R2.<x1,x2> = BooleanPolynomialRing(2)
        sage: p = x1+x2+x1*x2
        sage: f = BooleanFunctionImproved(p)
        sage: c1 = BooleanFunctionETCPart.from_function(f, c_stop=1)
        sage: print(c1)
        BooleanFunctionExtendedTranslateClassPart.from_function(BooleanFunctionImproved(x0*x1 + x0 + x1, c_start=0, c_stop=1))
        sage: latex(c1)
        \text{\texttt{BooleanFunctionExtendedTranslateClassPart.from{\char`\_}function(BooleanFunctionImproved(x0*x1{ }+{ }x0{ }+{ }x1,{ }c{\char`\_}start=0,{ }c{\char`\_}stop=1))}}

    """

    def __init__(self, *args, **kwargs):
        r"""
        Constructor from an object or from class attributes.

        INPUT:

        - ``algebraic_normal_form`` -- a polynomial of the type
          returned by ``BooleanFunction.algebraic_normal_form()``,
          representing the ``BooleanFunction`` whose classification this is.
        - ``boolean_function_index_matrix`` -- a ``Matrix` of integers,
          which are indices into ``boolean_function_list`` representing the
          distinct boolean functions.
        - ``boolean_function_list`` -- a list of boolean functions.
        - ``general_linear_class_index_matrix`` -- a ``Matrix` of integers,
          which are indices into ``general_linear_class_list`` representing the
          general linear equivalence classes.
        - ``general_linear_class_list`` -- a list of matrices representing the
          general linear equivalence classes.
        - ``c_start`` -- an integer representing the index of
          the first row of each matrix.

        OUTPUT:

        None.

        EFFECT:

        The current object ``self`` is initialized as follows.

        Each of
        - ``algebraic_normal_form``
        - ``boolean_function_index_matrix``
        - ``boolean_function_list``
        - ``general_linear_class_index_matrix``
        - ``general_linear_class_list``
        - ``c_start``
        is set to the corresponding input parameter.

        EXAMPLES:

        The partial classification of the boolean function defined by the polynomial
        :math:`x_1 + x_2 + x_1 x_2` is copied from `c1` to `c2`.

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: from boolean_cayley_graphs.boolean_function_extended_translate_classification import (
            ....:     BooleanFunctionExtendedTranslateClassPart as BooleanFunctionETCPart)
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BooleanFunctionImproved(p)
            sage: c1 = BooleanFunctionETCPart.from_function(f, c_stop=1)
            sage: c2 = BooleanFunctionETCPart(c1)
            sage: print(c1 == c2)
            True
        """
        try:
            sobj = args[0]
            self.algebraic_normal_form = sobj.algebraic_normal_form
            self.boolean_function_index_matrix = sobj.boolean_function_index_matrix
            self.boolean_function_list = sobj.boolean_function_list
            self.general_linear_class_index_matrix = sobj.general_linear_class_index_matrix
            self.general_linear_class_list = sobj.general_linear_class_list
            self.c_start=sobj.c_start
        except:
            self.algebraic_normal_form = kwargs.pop(
                'algebraic_normal_form')
            self.boolean_function_index_matrix = kwargs.pop(
                'boolean_function_index_matrix')
            self.boolean_function_list = kwargs.pop(
                'boolean_function_list')
            self.general_linear_class_index_matrix = kwargs.pop(
                'general_linear_class_index_matrix')
            self.general_linear_class_list = kwargs.pop(
                'general_linear_class_list')
            self.c_start = kwargs.pop(
                'c_start')


    def _repr_(self):
        r"""
        Sage string representation.

        INPUT:

        - ``self`` -- the current object.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: from boolean_cayley_graphs.boolean_function_extended_translate_classification import (
            ....:     BooleanFunctionExtendedTranslateClassPart as BooleanFunctionETCPart)
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BooleanFunctionImproved(p)
            sage: c1 = BooleanFunctionETCPart.from_function(f, c_stop=1)
            sage: print(c1)
            BooleanFunctionExtendedTranslateClassPart.from_function(BooleanFunctionImproved(x0*x1 + x0 + x1, c_start=0, c_stop=1))
        """
        c_stop = self.c_start + self.boolean_function_index_matrix.nrows()
        return (
            type(self).__name__ +
            ".from_function(BooleanFunctionImproved(" +
            repr(self.algebraic_normal_form) +
            ", c_start=" +
            repr(self.c_start) +
            ", c_stop=" +
            repr(c_stop) +
            "))")


    @classmethod
    def from_function(
        cls,
        boolf,
        c_start=0,
        c_stop=None,
        limited_memory=False):
        r"""
        Constructor from the ``BooleanFunction`` ``boolf``.

        INPUT:

        - ``boolf`` -- an object of class ``BooleanFunction``.
        - ``c_start`` -- integer (default: 0).
          The smallest value of `c` to use for extended translates.
        - ``c_stop`` -- integer (default: ``None``).
          One more than largest value of `c` to use for extended
          translates. ``None`` means use all remaining values.
        - ``limited_memory`` -- boolean (default: ``False``).
          A flag indicating whether the classification might be
          too large to fit into memory.

        OUTPUT:

        An object of class BooleanFunctionExtendedTranslateClassPart,
        initialized as follows.

        - ``algebraic_normal_form`` is set to ``boolf.algebraic_normal_form()``,
        - ``boolean_function_index_matrix`` -- a ``Matrix` of integers,
          which are indices into ``boolean_function_list`` representing the
          distinct boolean functions.
        - ``boolean_function_list`` -- a list of boolean functions.
        - ``general_linear_class_index_matrix`` -- a ``Matrix` of integers,
          which are indices into ``general_linear_class_list`` representing the
          general linear equivalence classes.
        - ``general_linear_class_list`` -- a list of matrices representing the
          general linear equivalence classes.
        - ``c_start`` is set to smallest value of `c` used for extended translates.

        Each entry ``boolean_function_index_matrix[c-c_start,b]`` corresponds to
        the boolean function
        :math:`x \mapsto \mathtt{boolf}(x+b) + \langle c, x \rangle + \mathtt{boolf}(b)`.
        This enumerates all of the extended translates of ``boolf`` having ``c``
        from ``c_start`` to but not including ``c_stop``.

        EXAMPLES:

        A partial classification of the boolean function defined by the polynomial
        :math:`x_1 + x_2 + x_1 x_2`.

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: from boolean_cayley_graphs.boolean_function_extended_translate_classification import (
            ....:     BooleanFunctionExtendedTranslateClassPart as BooleanFunctionETCPart)
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BooleanFunctionImproved(p)
            sage: c1 = BooleanFunctionETCPart.from_function(f,c_start=2,c_stop=4)
            sage: dict(sorted(c1.__dict__.items()))
            {'algebraic_normal_form': x0*x1 + x0 + x1,
             'boolean_function_index_matrix': [0 2 1 3]
             [1 3 0 2],
             'boolean_function_list': [Boolean function with 2 variables,
              Boolean function with 2 variables,
              Boolean function with 2 variables,
              Boolean function with 2 variables],
             'c_start': 2,
             'general_linear_class_index_matrix': [0 1 0 0]
             [0 0 0 1],
             'general_linear_class_list': [Boolean function with 2 variables,
              Boolean function with 2 variables]}
        """
        checking = controls.checking
        timing   = controls.timing

        dim = boolf.nvariables()
        v = 2 ** dim

        if c_stop == None:
            c_stop = v
        else:
            c_stop = min(c_stop, v)
        algebraic_normal_form = boolf.algebraic_normal_form()

        use_shelve = dim > 8 or (dim == 8 and limited_memory)
        boolean_function_bijection = (
            ShelveBijectiveList()
            if use_shelve else
            BijectiveList())

        c_len = c_stop - c_start
        boolean_function_index_matrix = matrix(c_len, v)
        general_linear_class_index_matrix = matrix(c_len, v)
        general_linear_class_list = List()

        f = boolf.extended_translate()
        for b in range(v):
            if timing:
                print(datetime.now(), b, end=' ')
                print(len(boolean_function_bijection.get_list()))
                stdout.flush()
            for c in range(c_start, c_stop):
                f = boolf.zero_translate(b, c)
                tt = tuple(f(x) for x in range(v))
                bf_tt = BooleanFunctionImproved(tt)
                bf_tt_index = boolean_function_bijection.index_append(bf_tt)
                boolean_function_index_matrix[c - c_start, b] = bf_tt_index

                bf_etc = BooleanFunctionGeneralLinearClass(tt)
                glc_index = general_linear_class_list.index_append(bf_etc)
                general_linear_class_index_matrix[c - c_start, b] = glc_index

                if checking:
                    pass
            boolean_function_bijection.sync()

        # Retain the list part of boolean_function_bijection, and
        # close and remove the dict part.
        boolean_function_list = boolean_function_bijection.get_list()
        boolean_function_bijection.close_dict()
        boolean_function_bijection.remove_dict()

        if checking:
            pass

        if timing:
            print(datetime.now())
            stdout.flush()

        return cls(
            algebraic_normal_form=algebraic_normal_form,
            boolean_function_index_matrix=boolean_function_index_matrix,
            boolean_function_list=boolean_function_list,
            general_linear_class_index_matrix=general_linear_class_index_matrix,
            general_linear_class_list=general_linear_class_list,
            c_start=c_start)


    def __eq__(self, other):
        """
        Test for equality between partial classifications.

        WARNING:

        This test is for strict equality rather than mathematical equivalence.

        INPUT:

        - ``other`` - BooleanFunctionExtendedTranslateClassPart: another partial classification.

        OUTPUT:

        A Boolean value indicating whether ``self`` strictly equals ``other``.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: from boolean_cayley_graphs.boolean_function_extended_translate_classification import (
            ....:     BooleanFunctionExtendedTranslateClassPart as BooleanFunctionETCPart)
            sage: R2.<x0,x1> = BooleanPolynomialRing(2)
            sage: p = x0*x1
            sage: f1 = BooleanFunctionImproved(p)
            sage: c1 = BooleanFunctionETCPart.from_function(f1, c_stop=1)
            sage: f2 = BooleanFunctionImproved([0,0,0,1])
            sage: c2 = BooleanFunctionETCPart.from_function(f2, c_stop=1)
            sage: print(c2.algebraic_normal_form)
            x0*x1
            sage: print(c1 == c2)
            True
        """
        if other is None:
            return False
        return (
            self.algebraic_normal_form == other.algebraic_normal_form and
            self.boolean_function_list == other.boolean_function_list and
            self.boolean_function_index_matrix == other.boolean_function_index_matrix and
            self.general_linear_class_list == other.general_linear_class_list and
            self.general_linear_class_index_matrix == other.general_linear_class_index_matrix and
            self.c_start == other.c_start)


class BooleanFunctionExtendedTranslateClassification(BooleanFunctionExtendedTranslateClassPart):
    r"""
    Classification of the Cayley graphs within the
    extended translation equivalence class of a boolean function.

    EXAMPLES:

    ::

        sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
        sage: from boolean_cayley_graphs.boolean_function_extended_translate_classification import (
        ....:     BooleanFunctionExtendedTranslateClassification as BooleanFunctionETC)
        sage: R2.<x1,x2> = BooleanPolynomialRing(2)
        sage: p = x1+x2+x1*x2
        sage: f = BooleanFunctionImproved(p)
        sage: c1 = BooleanFunctionETC.from_function(f)
        sage: print(c1)
        BooleanFunctionExtendedTranslateClassification.from_function(BooleanFunctionImproved(x0*x1 + x0 + x1))
        sage: latex(c1)
        \text{\texttt{BooleanFunctionExtendedTranslateClassification.from{\char`\_}function(BooleanFunctionImproved(x0*x1{ }+{ }x0{ }+{ }x1))}}
    """

    # Suffixes used by from_csv() and save_as_csv().
    bent_function_csv_suffix = "_bent_function.csv"
    cg_class_list_csv_suffix = "_cg_class_list.csv"
    matrices_csv_suffix = "_matrices.csv"


    def __init__(self, *args, **kwargs):
        r"""
        Constructor from an object or from class attributes.

        INPUT:

        - ``sobj`` -- BooleanFunctionExtendedTranslateClassification: object to copy.

        - ``algebraic_normal_form`` -- a polynomial of the type
          returned by ``BooleanFunction.algebraic_normal_form()``,
          representing the ``BooleanFunctionImproved`` whose classification this is.
        - ``boolean_function_index_matrix`` -- a ``Matrix` of integers,
          which are indices into ``boolean_function_list`` representing the
          distinct boolean functions.
        - ``boolean_function_list`` -- a list of boolean functions.
        - ``general_linear_class_index_matrix`` -- a ``Matrix` of integers,
          which are indices into ``general_linear_class_list`` representing the
          general linear equivalence classes.
        - ``general_linear_class_list`` -- a list of matrices representing the
          general linear equivalence classes.

        OUTPUT:

        None.

        EFFECT:

        The current object ``self`` is initialized as follows.

        Each of
        - ``algebraic_normal_form``
        - ``boolean_function_index_matrix``
        - ``boolean_function_list``
        - ``general_linear_class_index_matrix``
        - ``general_linear_class_list``
        is set to the corresponding input parameter.

        EXAMPLES:

        The classification of the boolean function defined by the polynomial
        :math:`x_1 + x_2 + x_1 x_2` is copied from `c1` to `c2`.

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: from boolean_cayley_graphs.boolean_function_extended_translate_classification import (
            ....:     BooleanFunctionExtendedTranslateClassification as BooleanFunctionETC)
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BooleanFunctionImproved(p)
            sage: c1 = BooleanFunctionETC.from_function(f)
            sage: c2 = BooleanFunctionETC(c1)
            sage: print(c1 == c2)
            True
        """
        try:
            sobj = args[0]
            self.algebraic_normal_form=sobj.algebraic_normal_form
            self.boolean_function_index_matrix=sobj.boolean_function_index_matrix
            self.boolean_function_list=sobj.boolean_function_list
            self.general_linear_class_index_matrix=sobj.general_linear_class_index_matrix
            self.general_linear_class_list=sobj.general_linear_class_list
        except:
            self.algebraic_normal_form = kwargs.pop(
                'algebraic_normal_form')
            self.boolean_function_index_matrix = kwargs.pop(
                'boolean_function_index_matrix')
            self.boolean_function_list = kwargs.pop(
                'boolean_function_list')
            self.general_linear_class_index_matrix = kwargs.pop(
                'general_linear_class_index_matrix')
            self.general_linear_class_list = kwargs.pop(
                'general_linear_class_list')


    def _repr_(self):
        r"""
        Sage string representation.

        INPUT:

        - ``self`` -- the current object.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: from boolean_cayley_graphs.boolean_function_extended_translate_classification import (
            ....:     BooleanFunctionExtendedTranslateClassification as BooleanFunctionETC)
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BooleanFunctionImproved(p)
            sage: c1 = BooleanFunctionETC.from_function(f)
            sage: print(c1)
            BooleanFunctionExtendedTranslateClassification.from_function(BooleanFunctionImproved(x0*x1 + x0 + x1))
        """
        return (
            type(self).__name__ +
            ".from_function(BooleanFunctionImproved(" +
            repr(self.algebraic_normal_form) +
            "))")


    @classmethod
    def from_function(
        cls,
        boolf,
        list_dual_graphs=True,
        limited_memory=False):
        r"""
        Constructor from the ``BooleanFunctionImproved`` ``boolf``.

        INPUT:

        - ``boolf`` -- an object of class ``BooleanFunctionImproved``.
        - ``list_dual_graphs`` -- boolean. a flag indicating
          whether to list dual graphs.
        - ``limited_memory`` -- boolean. A flag indicating
          whether the classification might be too large
          to fit into memory. Default is False.

        OUTPUT:

        An object of class BooleanFunctionExtendedTranslateClassification,
        initialized as follows.

        - ``algebraic_normal_form`` is set to ``boolf.algebraic_normal_form()``,
        - ``boolean_function_index_matrix`` -- a ``Matrix` of integers,
          which are indices into ``boolean_function_list`` representing the
          distinct boolean functions.
        - ``boolean_function_list`` -- a list of boolean functions.
        - ``general_linear_class_index_matrix`` -- a ``Matrix` of integers,
          which are indices into ``general_linear_class_list`` representing the
          general linear equivalence classes.
        - ``general_linear_class_list`` -- a list of matrices representing the
          general linear equivalence classes.

        Each entry ``boolean_function_index_matrix[c,b]`` corresponds to
        the Cayley graph of the boolean function
        :math:`x \mapsto \mathtt{boolf}(x+b) + \langle c, x \rangle + \mathtt{boolf}(b)`.
        This enumerates all of the extended translates of ``boolf``.

        EXAMPLES:

        The classification of the boolean function defined by the polynomial
        :math:`x_1 + x_2 + x_1 x_2`.

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: from boolean_cayley_graphs.boolean_function_extended_translate_classification import (
            ....:     BooleanFunctionExtendedTranslateClassification as BooleanFunctionETC)
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BooleanFunctionImproved(p)
            sage: c3 = BooleanFunctionETC.from_function(f)
            sage: dict(sorted(c3.__dict__.items()))
            {'algebraic_normal_form': x0*x1 + x0 + x1,
             'boolean_function_index_matrix': [0 2 1 3]
             [1 3 0 2]
             [2 0 3 1]
             [3 1 2 0],
             'boolean_function_list': [Boolean function with 2 variables,
              Boolean function with 2 variables,
              Boolean function with 2 variables,
              Boolean function with 2 variables],
             'general_linear_class_index_matrix': [0 1 1 1]
             [1 1 0 1]
             [1 0 1 1]
             [1 1 1 0],
             'general_linear_class_list': [Boolean function with 2 variables,
              Boolean function with 2 variables]}

        TESTS:

        The classification of the boolean function defined by the polynomial
        :math:`x_1 + x_2 + x_1 x_2`, but with list_dual_graphs=False.

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: from boolean_cayley_graphs.boolean_function_extended_translate_classification import (
            ....:     BooleanFunctionExtendedTranslateClassification as BooleanFunctionETC)
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BooleanFunctionImproved(p)
            sage: c4 = BooleanFunctionETC.from_function(f,list_dual_graphs=False)
            sage: dict(sorted(c4.__dict__.items()))
            {'algebraic_normal_form': x0*x1 + x0 + x1,
             'boolean_function_index_matrix': [0 2 1 3]
             [1 3 0 2]
             [2 0 3 1]
             [3 1 2 0],
             'boolean_function_list': [Boolean function with 2 variables,
              Boolean function with 2 variables,
              Boolean function with 2 variables,
              Boolean function with 2 variables],
             'general_linear_class_index_matrix': [0 1 1 1]
             [1 1 0 1]
             [1 0 1 1]
             [1 1 1 0],
             'general_linear_class_list': [Boolean function with 2 variables,
              Boolean function with 2 variables]}
        """
        cp = BooleanFunctionExtendedTranslateClassPart.from_function(
            boolf,
            limited_memory=limited_memory)
        return cls(cp)


    def __eq__(self, other):
        """
        Test for equality between classifications.

        WARNING:

        This test is for strict equality rather than mathematical equivalence.

        INPUT:

        - ``other`` - BooleanFunctionExtendedTranslateClassification: another classification.

        OUTPUT:

        A Boolean value indicating whether ``self`` strictly equals ``other``.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved
            sage: from boolean_cayley_graphs.boolean_function_extended_translate_classification import (
            ....:     BooleanFunctionExtendedTranslateClassification as BooleanFunctionETC)
            sage: R2.<x0,x1> = BooleanPolynomialRing(2)
            sage: p = x0*x1
            sage: f1 = BooleanFunctionImproved(p)
            sage: c1 = BooleanFunctionETC.from_function(f1)
            sage: f2 = BooleanFunctionImproved([0,0,0,1])
            sage: c2 = BooleanFunctionETC.from_function(f2)
            sage: print(c2.algebraic_normal_form)
            x0*x1
            sage: print(c1 == c2)
            True
        """
        if other is None:
            return False
        return (
            self.algebraic_normal_form == other.algebraic_normal_form and
            self.boolean_function_index_matrix == other.boolean_function_index_matrix and
            self.boolean_function_list == other.boolean_function_list and
            self.general_linear_class_index_matrix == other.general_linear_class_index_matrix and
            self.general_linear_class_list == other.general_linear_class_list)
