r"""
Walsh Hadamard dual of a Boolean function.

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

from sage.crypto.boolean_function import BooleanFunction


def walsh_hadamard_dual(boolf):
    r"""
    Given a `BooleanFunction` `boolf`, the function `walsh_hadamard_dual`
    returns a `BooleanFunction` based on the Walsh Hadamard transform of `boolf`.
    If `boolf` is a bent function, then the returned `BooleanFunction` is
    well-defined and is also bent, being the *dual* bent function (Hou 1999) or
    *Fourier transform* of `boolf` (Rothaus 1976).

    *NOTE* The use of `1 + x/scale` here is to compensate for
    an incorrect sign in walsh_hadamard_transform().
    If this is ever fixed, then this must be changed to `1 - x/scale`.
    """
    m = boolf.nvariables()
    scale = 2 ** (m/2)
    return BooleanFunction([(1 + x/scale)/2 for x in boolf.walsh_hadamard_transform()])
