r"""
The ``bent_function_cayley_graph_classification`` module defines:

 * the ``BentFunctionCayleyGraphClassification`` class;
   which represents the classification of the Cayley graphs
   within the extended translation class of a bent function; and
 * the ``BentFunctionCayleyGraphClassPart`` class,
   which represents part of a Cayley graph classification.

AUTHORS:

- Paul Leopardi (2016-08-02): initial version

EXAMPLES:

::

    The classification of the bent function defined by the polynomial x2 + x1*x2.

    sage: from boolean_cayley_graphs.bent_function import BentFunction
    sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
    sage: R2.<x1,x2> = BooleanPolynomialRing(2)
    sage: p = x2+x1*x2
    sage: f = BentFunction(p)
    sage: c = BentFunctionCGC.from_function(f)
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

REFERENCES:

The extended translation equivalence class and the extended Cayley equivalence class
of a bent function are defined by Leopardi [Leo2017]_.
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
from sage.coding.linear_code import LinearCode
from sage.combinat.designs.incidence_structures import IncidenceStructure
from sage.functions.log import log
from sage.graphs.graph import Graph
from sage.graphs.strongly_regular_db import strongly_regular_from_two_weight_code
from sage.matrix.constructor import matrix
from sage.misc.latex import latex
from sage.plot.matrix_plot import matrix_plot
from sage.rings.integer import Integer
from sage.structure.sage_object import load, SageObject
from sys import stdout

import glob
import numpy as np

from boolean_cayley_graphs.bent_function import BentFunction
from boolean_cayley_graphs.binary_projective_two_weight_codes import binary_projective_two_weight_27_6_12
from boolean_cayley_graphs.binary_projective_two_weight_codes import binary_projective_two_weight_35_6_16
from boolean_cayley_graphs.boolean_cayley_graph import boolean_cayley_graph
from boolean_cayley_graphs.boolean_linear_code import linear_code_from_code_gens
from boolean_cayley_graphs.boolean_linear_code import print_latex_code_parameters
from boolean_cayley_graphs.boolean_linear_code_graph import boolean_linear_code_graph
from boolean_cayley_graphs.containers import BijectiveList
from boolean_cayley_graphs.containers import ShelveBijectiveList
from boolean_cayley_graphs.saveable import Saveable
from boolean_cayley_graphs.strongly_regular_graph import StronglyRegularGraph
from boolean_cayley_graphs.weight_class import weight_class

import boolean_cayley_graphs.cayley_graph_controls as controls
import csv
import os.path


class BentFunctionCayleyGraphClassPart(SageObject, Saveable):
    r"""
    Partial classification of the Cayley graphs within the
    extended translation equivalence class of a bent function.
    """

    def __init__(self, *args, **kwargs):
        r"""
        Constructor from an object or from class attributes.

        INPUT:

        - ``algebraic_normal_form`` -- a polynomial of the type
          returned by ``BooleanFunction.algebraic_normal_form()``,
          representing the ``BentFunction`` whose classification this is.
        - ``cayley_graph_class_list`` -- a list of ``graph6_string`` strings
          corresponding to the complete set of non-isomorphic Cayley graphs of
          the bent functions within the extended translation equivalence class
          of the ``BentFunction`` represented by ``algebraic_normal_form``,
          and their duals, if ``dual_cayley_graph_index_matrix`` is not ``None``,
        - ``bent_cayley_graph_index_matrix`` -- a ``Matrix` of integers,
          which are indices into ``cayley_graph_class_list`` representing the
          correspondence between bent functions and their Cayley graphs.
        - ``dual_cayley_graph_index_matrix`` -- a ``Matrix` of integers,
          which are indices into ``cayley_graph_class_list`` representing the
          correspondence between dual bent functions and their Cayley graphs.
        - ``weight_class_matrix`` -- a ``Matrix` of integers with value 0 or 1
          corresponding to the weight class of each bent function.
        - ``c_start`` -- an integer representing the Boolean vector
          corresponding to the first row of each matrix.

        OUTPUT:

        None.

        EFFECT:

        The current object ``self`` is initialized as follows.

        Each of
        - ``algebraic_normal_form``
        - ``cayley_graph_class_list``
        - ``bent_cayley_graph_index_matrix``
        - ``dual_cayley_graph_index_matrix``
        - ``weight_class_matrix``
        - ``c_start``
        is set to the corresponding input parameter.

        EXAMPLES:

        The partial classification of the bent function defined by the polynomial
        :math:`x_1 + x_2 + x_1 x_2` is copied from `c1` to `c2`.

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassPart as BentFunctionCGCP
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BentFunction(p)
            sage: c1 = BentFunctionCGCP.from_function(f, c_stop=1)
            sage: c2 = BentFunctionCGCP(c1)
            sage: print(c1 == c2)
            True
        """
        try:
            sobj = args[0]
            self.algebraic_normal_form=sobj.algebraic_normal_form
            self.cayley_graph_class_list=sobj.cayley_graph_class_list
            self.bent_cayley_graph_index_matrix=sobj.bent_cayley_graph_index_matrix
            self.dual_cayley_graph_index_matrix=sobj.dual_cayley_graph_index_matrix
            self.weight_class_matrix=sobj.weight_class_matrix
            self.c_start=sobj.c_start
        except:
            self.algebraic_normal_form          = kwargs.pop(
                'algebraic_normal_form')
            self.cayley_graph_class_list        = kwargs.pop(
                'cayley_graph_class_list')
            self.bent_cayley_graph_index_matrix = kwargs.pop(
                'bent_cayley_graph_index_matrix')
            self.dual_cayley_graph_index_matrix = kwargs.pop(
                'dual_cayley_graph_index_matrix', None)
            self.weight_class_matrix            = kwargs.pop(
                'weight_class_matrix')
            self.c_start                        = kwargs.pop(
                'c_start')


    @classmethod
    def from_function(
        cls,
        bentf,
        list_dual_graphs=True,
        c_start=0,
        c_stop=None,
        limited_memory=False):
        r"""
        Constructor from the ``BentFunction`` ``bentf``.

        INPUT:

        - ``bentf`` -- an object of class `BentFunction`.
        - ``list_dual_graphs`` -- boolean. A flag indicating
          whether to list dual graphs. Default is True.
        - ``c_start`` -- smallest value of `c` to use for
          extended translates. Integer. Default is 0.
        - ``c_stop`` -- one more than largest value of `c`
          to use for extended translates. Integer.
          Default is ``None``, meaning use all remaining values.
        - ``limited_memory`` -- boolean. A flag indicating
          whether the classification might be too large
          to fit into memory. Default is False.

        OUTPUT:

        An object of class BentFunctionCayleyGraphClassPart,
        initialized as follows.

        - ``algebraic_normal_form`` is set to ``bentf.algebraic_normal_form()``,
        - ``cayley_graph_class_list`` is set to a list of ``graph6_string`` stings
          corresponding to the complete set of non-isomorphic Cayley graphs
          of the bent functions within the extended translation equivalence
          class of ``bentf`` (and their duals, if ``list_dual_graphs`` is ``True``),
        - ``bent_cayley_graph_index_matrix`` is set to a matrix of indices
          into ``cayley_graph_class_list`` corresponding to these bent functions,
        - ``dual_cayley_graph_index_matrix`` is set to ``None``
          if ``list_dual_graphs`` is ``False``, otherwise it is set to
          a matrix of indices into `cayley_graph_class_list` corresponding
          to the duals of these bent functions, and
        - ``weight_class_matrix`` is set to the 0-1 matrix of weight classes
          corresponding to ``bent_cayley_graph_index_matrix``,
        - ``c_start`` is set to smallest value of c used for extended translates.

        Each entry ``bent_cayley_graph_index_matrix[c-c_start,b]`` corresponds to
        the Cayley graph of the bent function
        :math:`x \mapsto \mathtt{bentf}(x+b) + \langle c, x \rangle + \mathtt{bentf}(b)`.
        This enumerates all of the extended translates of ``bentf`` having ``c``
        from ``c_start`` to but not including ``c_stop``.

        EXAMPLES:

        A partial classification of the bent function defined by the polynomial
        :math:`x_1 + x_2 + x_1 x_2`.

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassPart as BentFunctionCGCPart
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BentFunction(p)
            sage: c1 = BentFunctionCGCPart.from_function(f,c_start=2,c_stop=4)
            sage: c1.__dict__
            {'algebraic_normal_form': x0*x1 + x0 + x1,
            'bent_cayley_graph_index_matrix': [0 1 0 0]
            [0 0 0 1],
            'c_start': 2,
            'cayley_graph_class_list': ['CK', 'C~'],
            'dual_cayley_graph_index_matrix': [0 1 0 0]
            [0 0 0 1],
            'weight_class_matrix': [0 1 0 0]
            [0 0 0 1]}

        A partial classification of the bent function defined by the polynomial
        :math:`x_1 + x_2 + x_1 x_2`, but with list_dual_graphs=False.

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BentFunction(p)
            sage: c2 = BentFunctionCGCPart.from_function(f,list_dual_graphs=False,c_start=0,c_stop=2)
            sage: c2.__dict__
            {'algebraic_normal_form': x0*x1 + x0 + x1,
            'bent_cayley_graph_index_matrix': [0 1 1 1]
            [1 1 0 1],
            'c_start': 0,
            'cayley_graph_class_list': ['C~', 'CK'],
            'dual_cayley_graph_index_matrix': None,
            'weight_class_matrix': [1 0 0 0]
            [0 0 1 0]}
        """
        checking = controls.checking
        timing   = controls.timing

        dim = bentf.nvariables()
        v = 2 ** dim
        c_start
        if c_stop == None:
            c_stop = v
        else:
            c_stop = min(c_stop, v)
        algebraic_normal_form = bentf.algebraic_normal_form()

        cayley_graph_class_bijection = (
            ShelveBijectiveList()
            if dim > 8 or (dim == 8 and limited_memory) else
            BijectiveList())

        c_len = c_stop - c_start
        bent_cayley_graph_index_matrix = matrix(c_len, v)
        if list_dual_graphs:
            dual_cayley_graph_index_matrix = matrix(c_len, v)
        else:
            dual_cayley_graph_index_matrix = None
        weight_class_matrix = matrix(c_len, v)

        f = bentf.extended_translate()
        dual_bentf = bentf.walsh_hadamard_dual()
        dual_f = dual_bentf.extended_translate()

        for b in xsrange(v):
            if timing:
                print datetime.now(), b,
                print len(cayley_graph_class_bijection)
                stdout.flush()

            fb = f(b)
            for c in xsrange(c_start, c_stop):
                fbc = bentf.extended_translate(b, c, fb)
                cg = boolean_cayley_graph(dim, fbc).canonical_label()
                cg_index = cayley_graph_class_bijection.index_append(cg.graph6_string())
                bent_cayley_graph_index_matrix[c - c_start, b] = cg_index

                weight = sum(fbc(x) for x in xsrange(v))
                wc = weight_class(v, weight)
                weight_class_matrix[c - c_start, b] = wc

                if checking:
                    if wc != 0 and wc != 1:
                        raise ValueError, (
                            "Weight class is "
                            + str(wc))
                if list_dual_graphs:
                    bentfbc = BentFunction([fbc(x) for x in xsrange(v)])

                    dual_fbc = bentfbc.walsh_hadamard_dual().extended_translate(d=wc)
                    dg = boolean_cayley_graph(dim, dual_fbc).canonical_label()
                    dg_index = cayley_graph_class_bijection.index_append(dg.graph6_string())
                    dual_cayley_graph_index_matrix[c - c_start, b] = dg_index

                    if checking and dim > 2:
                        blcg = boolean_linear_code_graph(dim, fbc)
                        lg = (
                            blcg.canonical_label()
                            if wc == 0 else
                            blcg.complement().canonical_label())
                        if lg != dg:
                            raise ValueError, (
                                "Cayley graph of dual does not match"
                                + "graph from linear code at "
                                + str(b) + ","
                                + str(c))
            cayley_graph_class_bijection.sync()

        # Retain the list part of cayley_graph_class_bijection, and
        # close and remove the dict part.
        cayley_graph_class_list = cayley_graph_class_bijection.get_list()
        cayley_graph_class_bijection.close_dict()
        cayley_graph_class_bijection.remove_dict()

        if checking:
            sdp_design_matrix = bentf.sdp_design_matrix()
            if weight_class_matrix != sdp_design_matrix:
                raise ValueError, (
                    "weight_class_matrix != sdp_design_matrix"
                    + "\n"
                    + str(weight_class_matrix)
                    + "\n"
                    + str(sdp_design_matrix))

        if timing:
            print datetime.now()
            stdout.flush()

        return cls(
            algebraic_normal_form=algebraic_normal_form,
            cayley_graph_class_list=cayley_graph_class_list,
            bent_cayley_graph_index_matrix=bent_cayley_graph_index_matrix,
            dual_cayley_graph_index_matrix=dual_cayley_graph_index_matrix,
            weight_class_matrix=weight_class_matrix,
            c_start=c_start)


    def __eq__(self, other):
        """
        Test for equality between partial classifications.

        WARNING:

        This test is for strict equality rather than mathematical equivalence.

        INPUT:

        - ``other`` - BentFunctionCayleyGraphClassPart: another partial classification.

        OUTPUT:

        A Boolean value indicating whether ``self`` strictly equals ``other``.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassPart as BentFunctionCGCP
            sage: R2.<x0,x1> = BooleanPolynomialRing(2)
            sage: p = x0*x1
            sage: f1 = BentFunction(p)
            sage: c1 = BentFunctionCGCP.from_function(f1, c_stop=1)
            sage: f2 = BentFunction([0,0,0,1])
            sage: c2 = BentFunctionCGCP.from_function(f2, c_stop=1)
            sage: print(c2.algebraic_normal_form)
            x0*x1
            sage: print(c1 == c2)
            True
        """
        return (
            self.algebraic_normal_form == other.algebraic_normal_form and
            self.cayley_graph_class_list == other.cayley_graph_class_list and
            self.bent_cayley_graph_index_matrix == other.bent_cayley_graph_index_matrix and
            self.dual_cayley_graph_index_matrix == other.dual_cayley_graph_index_matrix and
            self.weight_class_matrix == other.weight_class_matrix and
            self.c_start == other.c_start)


class BentFunctionCayleyGraphClassification(BentFunctionCayleyGraphClassPart):
    r"""
    Classification of the Cayley graphs within the
    extended translation equivalence class of a bent function.
    """

    # Suffixes used by from_csv() and save_as_csv().
    bent_function_csv_suffix = "_bent_function.csv"
    cg_class_list_csv_suffix = "_cg_class_list.csv"
    matrices_csv_suffix = "_matrices.csv"


    def __init__(self, *args, **kwargs):
        r"""
        Constructor from an object or from class attributes.

        INPUT:

        - ``sobj`` -- BentFunctionCayleyGraphClassification: object to copy.

        - ``algebraic_normal_form`` -- a polynomial of the type
          returned by ``BooleanFunction.algebraic_normal_form()``,
          representing the ``BentFunction`` whose classification this is.
        - ``cayley_graph_class_list`` -- a list of ``graph6_string`` strings
          corresponding to the complete set of non-isomorphic Cayley graphs of
          the bent functions within the extended translation equivalence class
          of the ``BentFunction`` represented by ``algebraic_normal_form``,
          and their duals, if ``dual_cayley_graph_index_matrix`` is not ``None``,
        - ``bent_cayley_graph_index_matrix`` -- a ``Matrix` of integers,
          which are indices into ``cayley_graph_class_list`` representing the
          correspondence between bent functions and their Cayley graphs.
        - ``dual_cayley_graph_index_matrix`` -- a ``Matrix` of integers,
          which are indices into ``cayley_graph_class_list`` representing the
          correspondence between dual bent functions and their Cayley graphs.
        - ``weight_class_matrix`` -- a ``Matrix` of integers with value 0 or 1
          corresponding to the weight class of each bent function.

        OUTPUT:

        None.

        EFFECT:

        The current object ``self`` is initialized as follows.

        Each of
        - ``algebraic_normal_form``
        - ``cayley_graph_class_list``
        - ``bent_cayley_graph_index_matrix``
        - ``dual_cayley_graph_index_matrix``
        - ``weight_class_matrix``
        is set to the corresponding input parameter.

        EXAMPLES:

        The classification of the bent function defined by the polynomial
        :math:`x_1 + x_2 + x_1 x_2` is copied from `c1` to `c2`.

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BentFunction(p)
            sage: c1 = BentFunctionCGC.from_function(f)
            sage: c2 = BentFunctionCGC(c1)
            sage: print(c1 == c2)
            True
        """
        try:
            sobj = args[0]
            self.algebraic_normal_form=sobj.algebraic_normal_form
            self.cayley_graph_class_list=sobj.cayley_graph_class_list
            self.bent_cayley_graph_index_matrix=sobj.bent_cayley_graph_index_matrix
            self.dual_cayley_graph_index_matrix=sobj.dual_cayley_graph_index_matrix
            self.weight_class_matrix=sobj.weight_class_matrix
        except:
            self.algebraic_normal_form          = kwargs.pop(
                'algebraic_normal_form')
            self.cayley_graph_class_list        = kwargs.pop(
                'cayley_graph_class_list')
            self.bent_cayley_graph_index_matrix = kwargs.pop(
                'bent_cayley_graph_index_matrix')
            self.dual_cayley_graph_index_matrix = kwargs.pop(
                'dual_cayley_graph_index_matrix', None)
            self.weight_class_matrix            = kwargs.pop(
                'weight_class_matrix')


    @classmethod
    def cg_class_list_from_csv(
        cls,
        file_name):
        """
        Read a Cayley graph class list from a csv file.

        The csv file is assumed to be created by the method
        save_cg_class_list_as_csv().

        INPUT:

        - ``file_name`` -- the name of the csv file.

        OUTPUT:

        A list of Cayley graphs in graph6_string format.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: import os
            sage: bf2 = BentFunction([1,0,1,1])
            sage: c2 = BentFunctionCGC.from_function(bf2)
            sage: csv_name = tmp_filename(ext=".csv")
            sage: c2.save_cg_class_list_as_csv(csv_name)
            sage: cgcl_saved = BentFunctionCGC.cg_class_list_from_csv(csv_name)
            sage: print(cgcl_saved == c2.cayley_graph_class_list)
            True
            sage: os.remove(csv_name)

        """
        cg_list = []
        with open(file_name) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                cg_list.append(row["canonical_label"])
        return cg_list


    @classmethod
    def matrices_from_csv(
        cls,
        dim,
        file_name):
        r"""
        Read three matrices from a csv file.

        The csv file is assumed to be created by the method
        save_matrices_as_csv().

        INPUT:

        - ``dim`` -- integer: the dimension of the bent function.
        - ``file_name`` -- the name of the csv file.

        OUTPUT:

        A tuple of matrices,

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: import os
            sage: bf2 = BentFunction([1,1,0,1])
            sage: dim = bf2.nvariables()
            sage: c2 = BentFunctionCGC.from_function(bf2)
            sage: csv_name = tmp_filename(ext=".csv")
            sage: c2.save_matrices_as_csv(csv_name)
            sage: (ci_matrix,di_matrix,wc_matrix) = BentFunctionCGC.matrices_from_csv(dim, csv_name)
            sage: print(c2.bent_cayley_graph_index_matrix == ci_matrix)
            True
            sage: print(c2.dual_cayley_graph_index_matrix == di_matrix)
            True
            sage: print(c2.weight_class_matrix == wc_matrix)
            True
            sage: os.remove(csv_name)

        TESTS:

            Test the case where list_dual_graphs==False and dual_cayley_graph_index_matrix is None.

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: import os
            sage: bf = BentFunction([1,1,0,1])
            sage: dim = bf.nvariables()
            sage: c = BentFunctionCGC.from_function(bf, list_dual_graphs=False)
            sage: csv_name = tmp_filename(ext=".csv")
            sage: c.save_matrices_as_csv(csv_name)
            sage: (ci_matrix,di_matrix,wc_matrix) = BentFunctionCGC.matrices_from_csv(dim, csv_name)
            sage: print(c.bent_cayley_graph_index_matrix == ci_matrix)
            True
            sage: print(c.dual_cayley_graph_index_matrix == di_matrix)
            True
            sage: print(c.weight_class_matrix == wc_matrix)
            True
            sage: os.remove(csv_name)
        """
        v = 2 ** dim
        with open(file_name) as csv_file:
            reader = csv.DictReader(csv_file)
            fieldnames = reader.fieldnames
            ci_matrix = matrix(v, v)
            wc_matrix = matrix(v, v)
            di_matrix = (
                    matrix(v, v)
                if "dual_cayley_graph_index" in fieldnames
                else
                    None)
            for row in reader:
                c = int(row["c"])
                b = int(row["b"])
                ci_matrix[c, b] = row["bent_cayley_graph_index"]
                wc_matrix[c, b] = row["weight_class"]
                if "dual_cayley_graph_index" in fieldnames:
                    di_matrix[c, b] = row["dual_cayley_graph_index"]

        return (ci_matrix, di_matrix, wc_matrix)


    @classmethod
    def from_csv(
        cls,
        file_name_prefix):
        r"""
        Constructor from three csv files.

        INPUT:

        - ``file_name_prefix`` -- string: the common prefix to use for file names.

        OUTPUT:

        None.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: import os
            sage: bf2 = BentFunction([1,1,0,1])
            sage: c2 = BentFunctionCGC.from_function(bf2)
            sage: prefix = tmp_filename()
            sage: c2.save_as_csv(prefix)
            sage: c2_saved = BentFunctionCGC.from_csv(prefix)
            sage: print(c2 == c2_saved)
            True
            sage: bent_function_csv_name = prefix + BentFunctionCGC.bent_function_csv_suffix
            sage: os.remove(bent_function_csv_name)
            sage: cg_class_list_csv_name = prefix + BentFunctionCGC.cg_class_list_csv_suffix
            sage: os.remove(cg_class_list_csv_name)
            sage: matrices_csv_name = prefix + BentFunctionCGC.matrices_csv_suffix
            sage: os.remove(matrices_csv_name)

        """
        bentf = BentFunction.from_csv(
            file_name_prefix + cls.bent_function_csv_suffix)
        algebraic_normal_form = bentf.algebraic_normal_form()
        cayley_graph_class_list = cls.cg_class_list_from_csv(
            file_name_prefix + cls.cg_class_list_csv_suffix)
        dim = bentf.nvariables()
        (
            bent_cayley_graph_index_matrix,
            dual_cayley_graph_index_matrix,
            weight_class_matrix) = cls.matrices_from_csv(
                dim,
                file_name_prefix + cls.matrices_csv_suffix)

        return cls(
            algebraic_normal_form=algebraic_normal_form,
            cayley_graph_class_list=cayley_graph_class_list,
            bent_cayley_graph_index_matrix=bent_cayley_graph_index_matrix,
            dual_cayley_graph_index_matrix=dual_cayley_graph_index_matrix,
            weight_class_matrix=weight_class_matrix)


    @classmethod
    def from_function(
        cls,
        bentf,
        list_dual_graphs=True,
        limited_memory=False):
        r"""
        Constructor from the ``BentFunction`` ``bentf``.

        INPUT:

        - ``bentf`` -- an object of class `BentFunction`.
        - ``list_dual_graphs`` -- boolean. a flag indicating
          whether to list dual graphs.
        - ``limited_memory`` -- boolean. A flag indicating
          whether the classification might be too large
          to fit into memory. Default is False.

        OUTPUT:

        An object of class BentFunctionCayleyGraphClassification,
        initialized as follows.

        - ``algebraic_normal_form`` is set to ``bentf.algebraic_normal_form()``,
        - ``cayley_graph_class_list`` is set to a list of ``graph6_string``
          strings corresponding to the complete set of non-isomorphic Cayley graphs
          of the bent functions within the extended translation equivalence
          class of ``bentf`` (and their duals, if ``list_dual_graphs`` is ``True``),
        - ``bent_cayley_graph_index_matrix`` is set to a matrix of indices
          into ``cayley_graph_class_list`` corresponding to these bent functions,
        - ``dual_cayley_graph_index_matrix`` is set to ``None``
          if ``list_dual_graphs`` is ``False``, otherwise it is set to
          a matrix of indices into `cayley_graph_class_list` corresponding
          to the duals of these bent functions, and
        - ``weight_class_matrix`` is set to the 0-1 matrix of weight classes
          corresponding to ``bent_cayley_graph_index_matrix``.

        Each entry ``bent_cayley_graph_index_matrix[c,b]`` corresponds to
        the Cayley graph of the bent function
        :math:`x \mapsto \mathtt{bentf}(x+b) + \langle c, x \rangle + \mathtt{bentf}(b)`.
        This enumerates all of the extended translates of ``bentf``.

        EXAMPLES:

        The classification of the bent function defined by the polynomial
        :math:`x_1 + x_2 + x_1 x_2`.

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BentFunction(p)
            sage: c3 = BentFunctionCGC.from_function(f)
            sage: c3.__dict__
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

        TESTS:

        The classification of the bent function defined by the polynomial
        :math:`x_1 + x_2 + x_1 x_2`, but with list_dual_graphs=False.

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BentFunction(p)
            sage: c4 = BentFunctionCGC.from_function(f,list_dual_graphs=False)
            sage: c4.__dict__
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
        cp = BentFunctionCayleyGraphClassPart.from_function(
            bentf,
            list_dual_graphs=list_dual_graphs,
            limited_memory=limited_memory)
        return cls(cp)


    @classmethod
    def from_parts(
        cls,
        prefix_basename,
        directory=None,
        limited_memory=False):
        """
        Constructor from saved class parts.

        INPUTS:

        - ``prefix_basename`` -- string. The prefix to use with mangled_name()
          to obtain the file names of the saved class parts.
        - ``limited_memory`` -- boolean, default is False.
          A flag indicating whether the classification might be too large to
          fit into memory.

        OUTPUT:

        An object of class BentFunctionCayleyGraphClassification,
        constructed from the saved class parts.

        EXAMPLES:

        A classification of the bent function defined by the polynomial
        :math:`x_1 + x_2 + x_1 x_2`.

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassPart as BentFunctionCGCPart
            sage: import os.path
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BentFunction(p)
            sage: prefix = tmp_filename()
            sage: prefix_dirname = os.path.dirname(prefix)
            sage: prefix_basename = os.path.basename(prefix)
            sage: for row in xsrange(4):
            ....:     c = BentFunctionCGCPart.from_function(f, c_start=row,c_stop=row+1)
            ....:     part_prefix = prefix_basename + "_" + str(row)
            ....:     c.save_mangled(
            ....:         part_prefix,
            ....:         directory=prefix_dirname)
            sage: cl1 = BentFunctionCGC.from_parts(
            ....:    prefix_basename,
            ....:    directory=prefix_dirname)
            sage: cl1.report(report_on_matrix_details=True)
            Algebraic normal form of Boolean function: x0*x1 + x0 + x1
            Function is bent.
            <BLANKLINE>
            Weight class matrix:
            [1 0 0 0]
            [0 0 1 0]
            [0 1 0 0]
            [0 0 0 1]
            <BLANKLINE>
            SDP design incidence structure t-design parameters: (True, (1, 4, 1, 1))
            <BLANKLINE>
            Classification of Cayley graphs and classification of Cayley graphs of duals are the same:
            <BLANKLINE>
            There are 2 extended Cayley classes in the extended translation class.
            <BLANKLINE>
            Matrix of indices of Cayley graphs:
            [0 1 1 1]
            [1 1 0 1]
            [1 0 1 1]
            [1 1 1 0]
            sage: for row in xsrange(4):
            ....:     part_prefix = prefix_basename + "_" + str(row)
            ....:     BentFunctionCGCPart.remove_mangled(
            ....:         part_prefix,
            ....:         directory=prefix_dirname)
        """
        mangled_part_prefix = BentFunctionCayleyGraphClassPart.mangled_name(
            prefix_basename,
            directory=directory)
        file_name_list = glob.glob(mangled_part_prefix + "_[0-9]*.sobj")
        file_name_list.sort()

        # Load the first part to see how large the matrices need to be.
        part_nbr = 0
        part = load(file_name_list[part_nbr])
        algebraic_normal_form = part.algebraic_normal_form
        bentf = BentFunction(algebraic_normal_form)
        dim = bentf.nvariables()
        v = 2 ** dim

        # If the number of columns in the part must match
        # (be 2 to the power of) the number of variables of the bent function.
        if part.bent_cayley_graph_index_matrix.ncols() != v:
            raise ValueError

        # Initialize the graph class bijection to be empty.
        cayley_graph_class_bijection = (
            ShelveBijectiveList()
            if dim > 8 or (dim == 8 and limited_memory) else
            BijectiveList())

        # Initialize the matrix attributes to be empty and of the right size.
        bent_cayley_graph_index_matrix = matrix(v, v)
        list_dual_graphs = part.dual_cayley_graph_index_matrix != None
        if list_dual_graphs:
            dual_cayley_graph_index_matrix = matrix(v, v)
        else:
            dual_cayley_graph_index_matrix = None
        weight_class_matrix = matrix(v,v)

        for part_nbr in range(len(file_name_list)):
            # In the main loop, map each part classification into
            # the whole classification.
            if part_nbr > 0:
                part = load(file_name_list[part_nbr])
            whole_cg_index = dict()
            for part_cg_index in range(len(part.cayley_graph_class_list)):
                cg_index = cayley_graph_class_bijection.index_append(
                    part.cayley_graph_class_list[part_cg_index])
                whole_cg_index[part_cg_index] = cg_index
            c_len = part.bent_cayley_graph_index_matrix.nrows()
            for part_c in range(c_len):
                c = part.c_start + part_c
                for b in range(v):
                    bent_cayley_graph_index_matrix[c, b] = (
                        whole_cg_index[
                            part.bent_cayley_graph_index_matrix[part_c, b]])
                    dual_cayley_graph_index_matrix[c, b] = (
                        whole_cg_index[
                            part.dual_cayley_graph_index_matrix[part_c, b]])
                    weight_class_matrix[c, b] = (
                        part.weight_class_matrix[part_c, b])

        # Retain the list part of cayley_graph_class_bijection, and
        # close and remove the dict part.
        cayley_graph_class_list = cayley_graph_class_bijection.get_list()
        cayley_graph_class_bijection.close_dict()
        cayley_graph_class_bijection.remove_dict()

        return cls(
            algebraic_normal_form=algebraic_normal_form,
            cayley_graph_class_list=cayley_graph_class_list,
            bent_cayley_graph_index_matrix=bent_cayley_graph_index_matrix,
            dual_cayley_graph_index_matrix=dual_cayley_graph_index_matrix,
            weight_class_matrix=weight_class_matrix)


    def __eq__(self, other):
        """
        Test for equality between classifications.

        WARNING:

        This test is for strict equality rather than mathematical equivalence.

        INPUT:

        - ``other`` - BentFunctionCayleyGraphClassification: another classification.

        OUTPUT:

        A Boolean value indicating whether ``self`` strictly equals ``other``.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: R2.<x0,x1> = BooleanPolynomialRing(2)
            sage: p = x0*x1
            sage: f1 = BentFunction(p)
            sage: c1 = BentFunctionCGC.from_function(f1)
            sage: f2 = BentFunction([0,0,0,1])
            sage: c2 = BentFunctionCGC.from_function(f2)
            sage: print(c2.algebraic_normal_form)
            x0*x1
            sage: print(c1 == c2)
            True
        """
        return (
            self.algebraic_normal_form == other.algebraic_normal_form and
            self.cayley_graph_class_list == other.cayley_graph_class_list and
            self.bent_cayley_graph_index_matrix == other.bent_cayley_graph_index_matrix and
            self.dual_cayley_graph_index_matrix == other.dual_cayley_graph_index_matrix and
            self.weight_class_matrix == other.weight_class_matrix)


    def first_matrix_index_list(self):
        r"""
        Obtain a representative bent function corresponding to each extended Cayley class.

        INPUT:

        - ``self`` -- the current object.

        OUTPUT:

        A list of tuples `(i_n,j_n)`, each of which is the first index into
        the matrix `self.bent_cayley_graph_index_matrix` that contains the entry `n`.
        The first index is determined by `argwhere`.

        EXAMPLES:

        The result for the bent function defined by the polynomial :math:`x_1 + x_2 + x_1 x_2`.

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: R2.<x1,x2> = BooleanPolynomialRing(2)
            sage: p = x1+x2+x1*x2
            sage: f = BentFunction(p)
            sage: c = BentFunctionCGC.from_function(f)
            sage: c.first_matrix_index_list()
            [(0, 0), (0, 1)]
        """
        tot_cayley_graph_classes = len(self.cayley_graph_class_list)
        ci_matrix = self.bent_cayley_graph_index_matrix

        ci_array  = array(ci_matrix)
        ci_where  = [
            argwhere(ci_array == index)
            for index in xsrange(tot_cayley_graph_classes)]
        cb_list = [
            (None
            if ci_where[index].shape[0] == 0
            else tuple(ci_where[index][0,:]))
            for index in xsrange(tot_cayley_graph_classes)]
        return cb_list


    def report(
        self,
        report_on_matrix_details=False,
        report_on_graph_details=False):
        r"""
        Print a report on the classification.

        The report includes attributes and various computed quantities.

        INPUT:

        - ``self`` -- the current object.
        - ``report_on_matrix_details`` -- optional, Boolean (default: False).
           If True, print each matrix.
        - ``report_on_graph_details`` -- optional, Boolean (default: False).
           If True, produce a detailed report for each Cayley graph.

        OUTPUT:

        (To standard output)
        A report on the following attributes of ``self``:
        - ``algebraic_normal_form``
        - ``cayley_graph_class_list``
        - If report_on_matrix_details is ``True``:
        -- ``bent_cayley_graph_index_matrix``
        -- ``dual_cayley_graph_index_matrix``
        (only if this is not ``None`` and is different from
        ``bent_cayley_graph_index_matrix``)
        -- ``weight_class_matrix``
        - If report_on_graph_details is ``True``:
        details of each graph in ``cayley_graph_class_list``.

        EXAMPLES:

        Report on the classification of the bent function defined by
        the polynomial :math:`x_0 + x_0 x_1 + x_2 x_3`.

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: R4.<x0,x1,x2,x3> = BooleanPolynomialRing(4)
            sage: p = x0+x0*x1+x2*x3
            sage: f = BentFunction(p)
            sage: c = BentFunctionCGC.from_function(f)
            sage: c.report(report_on_matrix_details=True, report_on_graph_details=True)
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
            There are 2 extended Cayley classes in the extended translation class.
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

        - [Leo2017]_.
        """
        def graph_and_linear_code_report(
            bentf,
            report_on_matrix_details,
            report_on_graph_details,
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

            nbr_bent_cayley_graph_classes = len(
                np.unique(bent_cayley_graph_index_matrix))
            print ""
            print "There are", nbr_bent_cayley_graph_classes,
            print "extended Cayley classes in the extended translation class."

            tot_cayley_graph_classes = len(cayley_graph_class_list)

            if dual_cayley_graph_index_matrix != None:
                nbr_dual_cayley_graph_classes = len(
                    np.unique(dual_cayley_graph_index_matrix))
                print "There are", nbr_dual_cayley_graph_classes,
                print "extended Cayley classes of dual bent functions",
                print "in the extended translation class,"
                print "and", tot_cayley_graph_classes,
                print "extended Cayley classes in the union of the two."

            if report_on_matrix_details:
                print ""
                print "Matrix of indices of Cayley graphs:"
                print bent_cayley_graph_index_matrix

                if dual_cayley_graph_index_matrix != None:
                    print "Matrix of indices of Cayley graphs",
                    print "of dual bent functions:"
                    print dual_cayley_graph_index_matrix

            if not report_on_graph_details:
                return

            print ""
            print "For each extended Cayley class in the extended translation class:"
            print "Clique polynomial, strongly regular parameters,",
            print "rank, and order of a representative graph; and"
            print "linear code and generator matrix for a representative bent function:"

            for index in xsrange(tot_cayley_graph_classes):
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
        D = self.weight_class_matrix
        if report_on_matrix_details:
            print "Weight class matrix:"
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

            graph_and_linear_code_report(
                bentf,
                report_on_matrix_details,
                report_on_graph_details,
                cg_list,
                cb_list,
                ci_matrix)
        else:
            print "Classification of Cayley graphs and",
            print "classification of Cayley graphs of duals",
            if ci_matrix == di_matrix:
                print "are the same:"

                graph_and_linear_code_report(
                    bentf,
                    report_on_matrix_details,
                    report_on_graph_details,
                    cg_list,
                    cb_list,
                    ci_matrix)
            else:
                print "differ in matrices of indexes:"

                graph_and_linear_code_report(
                    bentf,
                    report_on_matrix_details,
                    report_on_graph_details,
                    cg_list,
                    cb_list,
                    ci_matrix,
                    di_matrix)


    def print_latex_table_of_cayley_classes(self, width=40, rows_per_table=6):
        r"""
        Print a table of Cayley classes in LaTeX format.

        For a given classification, print, in LaTeX format, the table
        of selected properties of the Cayley classes of that classification.

        INPUT:

        - ``self`` -- the current object.
        - ``width`` -- integer (default: 40): the table width.
        - ``rows_per_table`` -- integer (default: 6): the number of rows to
          include before starting a new table.

        OUTPUT:

        (To standard output.) A table in LaTeX format.

        EXAMPLES:

        Print the table of Cayley classes for the classification of the bent
        function defined by the polynomial :math:`x_0 + x_0 x_1 + x_2 x_3`.

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: R4.<x0,x1,x2,x3> = BooleanPolynomialRing(4)
            sage: p = x0+x0*x1+x2*x3
            sage: f = BentFunction(p)
            sage: c = BentFunctionCGC.from_function(f)
            sage: c.print_latex_table_of_cayley_classes()
            \small{}
            \begin{align*}
            \def\arraystretch{1.2}
            \begin{array}{|cccl|}
            \hline
            \text{Class} &
            \text{Parameters} &
            \text{2-rank} &
            \text{Clique polynomial}
            \\
            \hline
            0 &
            (16, 6, 2, 2) &
            6 &
            \begin{array}{l}
            8t^{4} + 32t^{3} + 48t^{2} + 16t + 1
            \end{array}
            \\
            1 &
            (16, 10, 6, 6) &
            6 &
            \begin{array}{l}
            16t^{5} + 120t^{4} + 160t^{3}
            \,+
            \\
            80t^{2} + 16t + 1
            \end{array}
            \\
            \hline
            \end{array}
            \end{align*}
        """
        def print_latex_header():
            print "\\small{}"
            print "\\begin{align*}"
            print "\\def\\arraystretch{1.2}"
            print "\\begin{array}{|cccl|}"
            print "\\hline"
            print "\\text{Class} &"
            print "\\text{Parameters} &"
            print "\\text{2-rank} &"
            print "\\text{Clique polynomial}"
            print "\\\\"
            print "\\hline"


        def print_latex_footer():
            print "\\hline"
            print "\\end{array}"
            print "\\end{align*}"

        print_latex_header()
        cg_list = self.cayley_graph_class_list
        for n in xsrange(len(cg_list)):
            if n > 0 and n % rows_per_table == 0:
                print_latex_footer()
                print "\\newpage"
                print_latex_header()

            print n, "&"
            g = Graph(cg_list[n])
            srg = StronglyRegularGraph(g)
            print srg.strongly_regular_parameters, "&"
            print srg.rank, "&"
            cp = srg.stored_clique_polynomial
            print "\\begin{array}{l}"
            lf = latex(cp)
            cut = 0
            while cut >= 0 and len(lf) > width:
                cut = lf.rfind('+', 0, width)
                if cut > 0:
                    print lf[:cut]
                if cut >= 0 and cut < len(lf):
                    print "\\,+"
                    print "\\\\"
                lf = lf[cut + 1:]
            print lf
            print "\\end{array}"
            print "\\\\"

        print_latex_footer()


    def print_latex_table_of_tonchev_graphs(self, width=40):
        r"""
        Print a table comparing Cayley graphs with graphs from Tonchev's codes.

        Tonchev's codes are binary projective two-weight codes
        as published by Tonchev [Ton1996]_, [Ton2007]_.

        INPUT:

        - ``self`` -- the current object.
        - ``width`` -- integer (default: 40): the table width.

        OUTPUT:

        (To standard output.) A table in LaTeX format.

        .. NOTE::

            The comparison displayed in this table really only makes sense for
            bent functions in 6 dimensions.

        EXAMPLES:

        The classification for the bent function defined by the polynomial
        :math:`x_0 x_1 + x_2 x_3 + x_4 x_5`.

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: R6.<x0,x1,x2,x3,x4,x5> = BooleanPolynomialRing(6)
            sage: p = x0*x1 + x2*x3 + x4*x5
            sage: f = BentFunction(p)
            sage: c = BentFunctionCGC.from_function(f) # long time (60 seconds)
            sage: c.print_latex_table_of_tonchev_graphs() # long time (depends on line above)
            \begin{align*}
            \def\arraystretch{1.2}
            \begin{array}{|ccl|}
            \hline
            \text{Class} &
            \text{Parameters} &
            \text{Reference}
            \\
            \hline
            0 & [35,6,16] & \text{Table 1.156 1 (complement)}
            \\
            0 & [35,6,16] & \text{Table 1.156 2 (complement)}
            \\
            1 & [27,6,12] & \text{Table 1.155 1 }
            \\
            \hline
            \end{array}
            \end{align*}

        REFERENCES:

        - [Ton1996]_.

        - [Ton2007]_.
        """
        print "\\begin{align*}"
        print "\\def\\arraystretch{1.2}"
        print "\\begin{array}{|ccl|}"
        print "\\hline"
        print "\\text{Class} &"
        print "\\text{Parameters} &"
        print "\\text{Reference}"
        print "\\\\"
        print "\\hline"

        tw_155 = binary_projective_two_weight_27_6_12()
        lc_155 = [
            linear_code_from_code_gens(tw)
            for tw in tw_155]
        sr_155 = [
            strongly_regular_from_two_weight_code(lc).canonical_label().graph6_string()
            for lc in lc_155]

        tw_156 = binary_projective_two_weight_35_6_16()
        lc_156 = [
            linear_code_from_code_gens(tw)
            for tw in tw_156]
        sr_156 = [
            strongly_regular_from_two_weight_code(lc).complement().canonical_label().graph6_string()
            for lc in lc_156]

        cg_list = self.cayley_graph_class_list
        for n in xsrange(len(cg_list)):
            cg = cg_list[n]
            for k in xsrange(len(sr_155)):
                if cg == sr_155[k]:
                    print n, "&",
                    print_latex_code_parameters(lc_155[k])
                    print "& \\text{Table 1.155",
                    print k + 1,
                    print "}"
                    print "\\\\"
            for k in xsrange(len(sr_156)):
                if cg == sr_156[k]:
                    print n, "&",
                    print_latex_code_parameters(lc_156[k])
                    print "& \\text{Table 1.156",
                    print k + 1,
                    print "(complement)}"
                    print "\\\\"

        print "\\hline"
        print "\\end{array}"
        print "\\end{align*}"


    def save_matrix_plots(self, figure_name, cmap='gist_stern'):
        r"""
        Plot the matrix attributes to figure files.

        Use ``matrix_plot`` to plot the matrix attributes
        ``bent_cayley_graph_index_matrix``, ``dual_cayley_graph_index_matrix``,
        and ``weight_class_matrix`` to corresponding figure files.

        INPUT:

        - ``self`` -- the current object.
        - ``figure_name`` -- string: the prefix to use in the file names for
          the figures.
        - ``cmap`` -- string (default: 'gist_stern'): the colormap to use with
          ``matrixplot``.

        OUTPUT:

        (To figure files:
        ``figure_name`` + ``"_bent_cayley_graph_index_matrix.png"``,
        ``figure_name`` + ``"_dual_cayley_graph_index_matrix.png"``,
        ``figure_name`` + ``"_weight_class_matrix.png"``) Plots of the corresponding
        matrix attributes.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: import glob
            sage: import os
            sage: bf = BentFunction([1,1,0,1])
            sage: dim = bf.nvariables()
            sage: c = BentFunctionCGC.from_function(bf)
            sage: figure_name = tmp_filename()
            sage: c.save_matrix_plots(figure_name)
            sage: figure_list = glob.glob(figure_name+"*.png")
            sage: for figure in figure_list:
            ....:     print(
            ....:         "_bent_cayley_graph_index_matrix.png" in figure or
            ....:         "_dual_cayley_graph_index_matrix.png" in figure or
            ....:         "_weight_class_matrix.png" in figure)
            ....:     print(os.path.isfile(figure))
            ....:     os.remove(figure)
            True
            True
            True
            True
            True
            True
        """
        matrix_names = (
            "bent_cayley_graph_index_matrix",
            "dual_cayley_graph_index_matrix",
            "weight_class_matrix")

        attributes = self.__dict__
        for name in matrix_names:
            graphic = matrix_plot(matrix(attributes[name]),cmap=cmap)
            graphic.save(figure_name + "_" + name + ".png")


    def save_cg_class_list_as_csv(self, file_name):
        """
        Save the Cayley graph class list to a csv file.

        INPUT:

        - ``file_name`` -- the name of the csv file.

        OUTPUT:

        None.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: import os
            sage: bf2 = BentFunction([1,0,1,1])
            sage: c2 = BentFunctionCGC.from_function(bf2)
            sage: csv_name = tmp_filename(ext=".csv")
            sage: c2.save_cg_class_list_as_csv(csv_name)
            sage: cgcl_saved = BentFunctionCGC.cg_class_list_from_csv(csv_name)
            sage: print(cgcl_saved == c2.cayley_graph_class_list)
            True
            sage: os.remove(csv_name)
        """
        cg_list = self.cayley_graph_class_list

        fieldnames = [
            "cayley_graph_index",
            "canonical_label"]
        with open(file_name, "w") as cg_class_file:
            writer = csv.DictWriter(
                cg_class_file,
                fieldnames=fieldnames)
            writer.writeheader()
            for n in xsrange(len(cg_list)):
                    writer.writerow({
                        "cayley_graph_index":
                            n,
                        "canonical_label":
                            cg_list[n]})


    def save_matrices_as_csv(self, file_name):
        """
        Save the matrices bent_cayley_graph_index_matrix,
        dual_cayley_graph_index_matrix and weight_class_matrix to a csv file.

        INPUT:

        - ``file_name`` -- the name of the csv file.

        OUTPUT:

        None.

        EXAMPLES::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: import os
            sage: bf2 = BentFunction([0,1,1,1])
            sage: dim = bf2.nvariables()
            sage: c2 = BentFunctionCGC.from_function(bf2)
            sage: csv_name = tmp_filename(ext=".csv")
            sage: c2.save_matrices_as_csv(csv_name)
            sage: (ci_matrix,di_matrix,wc_matrix) = BentFunctionCGC.matrices_from_csv(dim, csv_name)
            sage: print(c2.bent_cayley_graph_index_matrix == ci_matrix)
            True
            sage: print(c2.dual_cayley_graph_index_matrix == di_matrix)
            True
            sage: print(c2.weight_class_matrix == wc_matrix)
            True
            sage: os.remove(csv_name)

        TESTS:

            Test the case where list_dual_graphs=False and dual_cayley_graph_index_matrix is None.

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: import os
            sage: bf = BentFunction([1,0,1,1])
            sage: dim = bf.nvariables()
            sage: c = BentFunctionCGC.from_function(bf, list_dual_graphs=False)
            sage: csv_name = tmp_filename(ext=".csv")
            sage: c.save_matrices_as_csv(csv_name)
            sage: (ci_matrix,di_matrix,wc_matrix) = BentFunctionCGC.matrices_from_csv(dim, csv_name)
            sage: print(c.bent_cayley_graph_index_matrix == ci_matrix)
            True
            sage: print(c.dual_cayley_graph_index_matrix == di_matrix)
            True
            sage: print(c.weight_class_matrix == wc_matrix)
            True
            sage: os.remove(csv_name)

        """
        bentf = BentFunction(self.algebraic_normal_form)
        dim = bentf.nvariables()
        v = 2 ** dim

        ci_matrix = self.bent_cayley_graph_index_matrix
        di_matrix = self.dual_cayley_graph_index_matrix
        wc_matrix = self.weight_class_matrix

        fieldnames = [
            "b",
            "c",
            "bent_cayley_graph_index",
            "weight_class"]
        if di_matrix is not None:
            fieldnames.append(
                "dual_cayley_graph_index")
        with open(file_name, "w") as matrix_file:
            writer = csv.DictWriter(
                matrix_file,
                fieldnames=fieldnames)
            writer.writeheader()

            for c in xsrange(v):
                for b in xsrange(v):
                    row_dict = {
                        "b":
                            b,
                        "c":
                            c,
                        "bent_cayley_graph_index":
                            ci_matrix[c, b],
                        "weight_class":
                            wc_matrix[c, b]}
                    if di_matrix is not None:
                        row_dict[
                            "dual_cayley_graph_index"] = di_matrix[c, b]
                    writer.writerow(row_dict)


    def save_as_csv(self, file_name_prefix):
        """
        Save the classification as three csv files with a common prefix.

        INPUT:

        - ``self`` -- the current object.
        - ``file_name_prefix`` -- string: the common prefix to use for file names.

        OUTPUT:

        None.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.bent_function import BentFunction
            sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification as BentFunctionCGC
            sage: import os
            sage: bf2 = BentFunction([0,0,0,1])
            sage: c2 = BentFunctionCGC.from_function(bf2)
            sage: prefix = tmp_filename()
            sage: c2.save_as_csv(prefix)
            sage: c2_saved = BentFunctionCGC.from_csv(prefix)
            sage: print(c2 == c2_saved)
            True
            sage: bent_function_csv_name = prefix + BentFunctionCGC.bent_function_csv_suffix
            sage: os.remove(bent_function_csv_name)
            sage: cg_class_list_csv_name = prefix + BentFunctionCGC.cg_class_list_csv_suffix
            sage: os.remove(cg_class_list_csv_name)
            sage: matrices_csv_name = prefix + BentFunctionCGC.matrices_csv_suffix
            sage: os.remove(matrices_csv_name)
        """
        cls = type(self)
        bentf = BentFunction(self.algebraic_normal_form)
        bentf.save_as_csv(
            file_name_prefix + cls.bent_function_csv_suffix)

        self.save_cg_class_list_as_csv(
            file_name_prefix + cls.cg_class_list_csv_suffix)

        self.save_matrices_as_csv(
            file_name_prefix + cls.matrices_csv_suffix)
