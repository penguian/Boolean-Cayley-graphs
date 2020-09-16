r"""
Boolean polynomial representatives of extended affine equivalence classes
of bent functions.
"""

#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.crypto.boolean_function import BooleanFunction


def bent_function_extended_affine_representative_polynomials_dimension_2():
    r"""
    The Boolean polynomial p2[1] is the representative of the single
    extended affine equivalence class of bent functions in two variables,
    as mentioned at 7.1 of Tokareva 2015.
    """
    R2.<x1,x2> = BooleanPolynomialRing(2)
    p2 = [None]*2
    p2[1] = x1*x2
    return p2


def bent_function_extended_affine_representative_polynomials_dimension_4():
    r"""
    The Boolean polynomial p4[1] is the representative of the single
    extended affine equivalence class of bent functions in four variables,
    as mentioned at 7.1 of Tokareva 2015.
    """
    R4.<x1,x2,x3,x4> = BooleanPolynomialRing(4)
    p4 = [None]*2
    p4[1] = x1*x2 + x3*x4
    return p4


def bent_function_extended_affine_representative_polynomials_dimension_6():
    r"""
    The Boolean polynomials p6[i] for from 1 to 4 are the representatives of
    the extended affine equivalence classes of bent functions in six variables,
    as listed at 7.2 of Tokareva 2015, with citation [318] to Rothaus 1976.
    """
    R6.<x1,x2,x3,x4,x5,x6> = BooleanPolynomialRing(6)
    p6 = [None]*5
    p6[1] = x1*x2 + x3*x4 + x5*x6
    p6[2] = x1*x2*x3 + x1*x4 + x2*x5 + x3*x6
    p6[3] = x1*x2*x3 + x2*x4*x5 + x1*x2 + x1*x4 + x2*x6 + x3*x5 + x4*x5
    p6[4] = x1*x2*x3 + x2*x4*x5 + x3*x4*x6 + x1*x4 + x2*x6 + x3*x4 + x3*x5 + x3*x6 + x4*x5 + x4*x6
    return p6


def bent_function_extended_affine_representative_polynomials_dimension_8():
    r"""
    The Boolean polynomials p8[i] for from 1 to 10 are the representatives of
    the extended affine equivalence classes of bent functions in 8 variables,
    with degree up to 3, as listed at 7.3 of Tokareva 2015,
    with citation [167] to Hou 1998.
    """
    R8.<x1,x2,x3,x4,x5,x6,x7,x8> = BooleanPolynomialRing(8)
    p8 = [None]*11
    p8[1] = x1*x2 + x3*x4 + x5*x6 + x7*x8
    p8[2] = x1*x2*x3 + x1*x4 + x2*x5 + x3*x6 + x7*x8
    p8[3] = x1*x2*x3 + x2*x4*x5 + x3*x4 + x2*x6 + x1*x7 + x5*x8
    p8[4] = x1*x2*x3 + x2*x4*x5 + x1*x3 + x1*x5 + x2*x6 + x3*x4 + x7*x8
    p8[5] = x1*x2*x3 + x2*x4*x5 + x3*x4*x6 + x3*x5 + x2*x6 + x2*x5 + x1*x7 + x4*x8
    p8[6] = x1*x2*x3 + x2*x4*x5 + x3*x4*x6 + x3*x5 + x1*x3 + x1*x4 + x2*x7 + x6*x8
    p8[7] = x1*x2*x3 + x2*x4*x5 + x3*x4*x6 + x3*x5 + x2*x6 + x2*x5 + x1*x2 + x1*x3 + x1*x4 + x7*x8
    p8[8] = x1*x2*x3 + x2*x4*x5 + x3*x4*x6 + x3*x5 + x1*x6 + x2*x7 + x4*x8
    p8[9] = x1*x2*x7 + x3*x4*x7 + x5*x6*x7 + x1*x4 + x3*x6 + x2*x5 + x4*x5 + x7*x8
    p8[10] = x1*x2*x3 + x2*x4*x5 + x3*x4*x6 + x1*x4*x7 + x3*x5 + x2*x7 + x1*x5 + x1*x6 + x4*x8
    return p8


def bent_function_extended_affine_representative_polynomials(dimension):
    r"""
    Return the list of Boolean polynomial representatives of
    extended affine equivalence classes of bent functions,
    in the given dimension.
    """
    dispatcher = {
        2: bent_function_extended_affine_representative_polynomials_dimension_2,
        4: bent_function_extended_affine_representative_polynomials_dimension_4,
        6: bent_function_extended_affine_representative_polynomials_dimension_6,
        8: bent_function_extended_affine_representative_polynomials_dimension_8
    }
    return dispatcher[dimension]()


def print_latex_table_of_representative_polynomials(
    dimension, start=1, width=140):
    r"""
    For given dimension, print, in LaTeX format, the table
    of algebraic normal forms of bent functions given by
    the representative polynomials for that dimension.

    Example:

    sage: print_latex_table_of_representative_polynomials(4)
    \def\arraystretch{1.2}
    \begin{array}{|cl|}
    \hline
    \text{Class} &
    \text{Representative}
    \\
    \hline
    \,[f_{ 4 , 1 }] & f_{ 4 , 1 } :=
    \begin{array}{l}
    x_{0} x_{1} + x_{2} x_{3}
    \end{array}
    \\
    \hline
    \end{array}

    """
    print("\\def\\arraystretch{1.2}")
    print("\\begin{array}{|cl|}")
    print("\\hline")
    print("\\text{Class} &")
    print("\\text{Representative}")
    print("\\\\")
    print("\\hline")

    p = bent_function_extended_affine_representative_polynomials(dimension)

    for n in range(start, len(p)):
        boolf = BooleanFunction(p[n])
        f = boolf.algebraic_normal_form()
        print("\\,[f_{",dimension,",",n,"}] & f_{",dimension,",",n,"} :=")
        print("\\begin{array}{l}")
        lf = latex(f)
        cut = 0
        while cut >= 0 and len(lf) > width:
            cut = lf.rfind('+', 0, width)
            if cut > 0:
                print(lf[:cut])
            if cut >= 0 and cut < len(lf):
                print("\\\\")
                print("+\\,", end=' ')
            lf = lf[cut + 1:]
        print(lf)
        print("\\end{array}")
        print("\\\\")
    print("\\hline")
    print("\\end{array}")
