"""
A subclass of BooleanFunction that adds extra methods.


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

from sage.arith.srange import xsrange
from sage.crypto.boolean_function import BooleanFunction

from boolean_cayley_graph import boolean_cayley_graph
from boolean_linear_code import boolean_linear_code
from integer_bits import inner
from saveable import Saveable


base2 = lambda dim, num: num.digits(2, padto=dim)


class BooleanFunctionImproved(BooleanFunction, Saveable):
    r"""
    """


    def cayley_graph(self):
        r"""
        """
        dim = self.nvariables()
        f = self.extended_translate()
        return boolean_cayley_graph(dim, f)


    def extended_translate(self, b=0, c=0, d=0):
        r"""
        Extended translation equivalent function.

        Given the non-negative numbers $b$, $c$ and $d$, the function
        `extended_translate` returns the function

        $x \mapsto \mathtt{self}(x + b) + \langle c, x \rangle + d$.
        """
        dim = self.nvariables()
        return lambda x: self(base2(dim, x ^ b)) ^ (0 if c == 0 else inner(c, x)) ^ d


    def linear_code(self):
        r"""
        """
        dim = self.nvariables()
        f = self.extended_translate()
        return boolean_linear_code(dim, f)


    def weight(self):
        r"""
        """
        return sum(self.truth_table(format='int'))
