r"""
Bent Boolean functions.

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

import weight_class as wc
from boolean_function_improved import BooleanFunctionImproved


class BentFunction(BooleanFunctionImproved):
    r"""
    """


    def walsh_hadamard_dual(self):
        r"""
        The function `walsh_hadamard_dual` returns a `BentFunction`
        based on the Walsh Hadamard transform of `self`.
        Since `self` is a bent function, the returned `BentFunction` is
        well-defined and is bent, being the *dual* bent function (Hou 1999)
        or *Fourier transform* of `self` (Rothaus 1976).

        *NOTE* The use of `1 + x/scale` here is to compensate for
        an incorrect sign in BooleanFunction.walsh_hadamard_transform(self).
        If this is ever fixed, then this must be changed to `1 - x/scale`.
        """
        m = self.nvariables()
        scale = 2 ** (m/2)
        return BentFunction([(1 + x/scale)/2 for x in self.walsh_hadamard_transform()])


    def weight_class(self):
        r"""
        """
        length = len(self)
        weight = self.weight()
        return wc.weight_class(length, weight)
