"""
A subclass of BooleanFunction that adds a method to produce an extended
translation equivalent function.


AUTHORS:

- Paul Leopardi (2016-08-23): initial version

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
from integer_bits import *


class BooleanFunctionWithTranslate(BooleanFunction):
    """
    """
    def extended_translate(self, b=0, c=0, d=0):
        """
        Extended translation equivalent function of this `BooleanFunction`.

        Given the non-negative numbers $b$, $c$ and $d$, the function
        `extended_translate` returns the function

        $x \mapsto \mathtt{self}(x + b) + \langle c, x \rangle + d$.
        """
        base2 = lambda length, num: num.digits(2, padto=length)

        m = self.nvariables()
        return lambda x: self(base2(m, x ^ b)) ^ (0 if c == 0 else inner(c, x)) ^ d
