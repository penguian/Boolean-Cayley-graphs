r"""
A subclass of BooleanFunction that includes information about relevant isomorphism classes of Cayley graphs.

<Paragraph description>
...

AUTHORS:

- Paul Leopardi (2016-08-02): initial version

...

Lots and lots of examples.
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

load("boolean_cayley_graph.sage")

load("index_append_list.sage")

load("graph_isomorphism_class.sage")

from sage.crypto.boolean_function import BooleanFunction
from datetime import datetime


class BooleanFunctionWithTranslate(BooleanFunction):
    r"""
    """
    def extended_translate(self, b=0, c=0, d=0):
        r"""
        Extended translation equivalent function of this `BooleanFunction`.

        Given the non-negative numbers $b$, $c$ and $d$, the function
        `extended_translate` returns the function

        $x \mapsto \mathtt{self}(x + b) + \langle c, x \rangle + d$.
        """
        base2 = lambda length, num: num.digits(2, padto=length)

        m = self.nvariables()
        return lambda x: self(base2(m, x ^^ b)) ^^ (0 if c == 0 else inner(c, x)) ^^ d


class BooleanFunctionCayleyGraphClassification(BooleanFunctionWithTranslate):
    r"""
    Given the `BooleanFunction` `boolf`,
    the class `BooleanFunctionCayleyGraphClassification`
    is initialized with `boolean_function` set to `boolf`,
    `cayley_graph_class_list` set to an `IndexAppendList` of `GraphIsomorphismClass`
    corresponding to the complete set of non-isomorphic Cayley graphs of the Boolean functions
    within the extended affine eqivalence class of `boolf`, and
    `cayley_graph_index_matrix` set to a matrix of indices into `cayley_graph_class_list`.

    Each entry `cayley_graph_index_matrix[c,b]` corresponds to
    the Cayley graph of the Boolean function
    $x \mapsto \mathtt{boolf}(x+b) + \langle c, x \rangle + \mathtt{boolf}(b)$.
    This enumerates all of the extended translates of `boolf`.
    """

    def __init__(self, boolf):
        r"""
        Initialize self as per the class description above.
        """
        if not 'cayley_graph_debugging' in globals():
            debugging = False
        else:
            debugging = cayley_graph_debugging

        m = boolf.nvariables()
        v = 2 ** m
        self.boolean_function = BooleanFunctionWithTranslate(boolf)
        f = self.boolean_function
        equivalent_f = f.extended_translate()
        self.cayley_graph_class_list = IndexAppendList([])
        self.cayley_graph_index_matrix = matrix(v,v)
        for b in sxrange(v):
            fb = equivalent_f(b)
            g = [GraphIsomorphismClass(boolean_cayley_graph(m, fbc)) for fbc in [f.extended_translate(b, c, fb) for c in sxrange(v)]]
            for c in sxrange(v):
                if debugging:
                    print datetime.now(), b, c,
                self.cayley_graph_index_matrix[c, b] = self.cayley_graph_class_list.index_append(g[c])
                if debugging:
                    print len(self.cayley_graph_class_list)
