r"""
Incidence matrix of designs  of type $R(\mathtt{bentf})$ described by Dillon and Schatz.

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

from bent_function import BentFunction
from walsh_hadamard_dual import walsh_hadamard_dual


def dillon_schatz_design_matrix(bentf):
    r"""
    Given a `BentFunction` `bentf`, the function `Dillon_Schatz_design_matrix`
    returns the incidence matrix of the design of type $R(\mathtt{bentf})$,
    as described by Dillon and Schatz (1987).
    """
    dim = bentf.nvariables()
    v = 2 ** dim
    result = matrix(v, v)
    dual_bentf = bentf.walsh_hadamard_dual()
    dual_f = dual_bentf.extended_translate()
    for c in xsrange(v):
        result[c,:] = matrix([bentf.extended_translate(0, c, dual_f(c))(x)
                              for x in xsrange(v)])
    return result
