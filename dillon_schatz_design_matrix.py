r"""
Incidence matrix of designs  of type $R(\mathtt{boolf})$ described by Dillon and Schatz.

Paul Leopardi.
"""

#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.arith.srange import xsrange
from sage.matrix.constructor import matrix

from walsh_hadamard_dual import *
from boolean_function_with_translate import *


def dillon_schatz_design_matrix(boolf):
    r"""
    Given a `BooleanFunction` `boolf`, the function `Dillon_Schatz_design_matrix`
    returns the incidence matrix of the design of type $R(\mathtt{boolf})$,
    as described by Dillon and Schatz (1987).
    """
    m = boolf.nvariables()
    v = 2 ** m
    result = matrix(v,v)
    dual_boolf = walsh_hadamard_dual(boolf)
    dual_f = BooleanFunctionWithTranslate(dual_boolf).extended_translate()
    boolft = BooleanFunctionWithTranslate(boolf)
    for c in xsrange(v):
        result[c,:] = matrix([boolft.extended_translate(0,c,dual_f(c))(x) for x in xsrange(v)])
    return result
