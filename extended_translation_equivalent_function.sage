"""
Extended translation equivalent function.

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

load("integer_bits.sage")

base2 = lambda length, num: num.digits(2, padto=length)

def extended_translation_equivalent_function(boolf, b=0, c=0, d=0):
    """
    Given a `BooleanFunction` `boolf` and non-negative numbers $b$, $c$ and $d$,
    the function `extended_translation_equivalent_function` returns the function

    $x \mapsto \mathtt{boolf}(x + b) + \langle c, x \rangle + d$.
    """
    m = boolf.nvariables()
    return lambda x: boolf(base2(m, x ^^ b)) ^^ (0 if c == 0 else inner(c, x)) ^^ d
