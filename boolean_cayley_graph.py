"""
Cayley graph of a Boolean function.

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
from sage.graphs.graph import Graph

from boolean_function_with_translate import BooleanFunctionWithTranslate


def boolean_cayley_graph(m, f):
    r"""
    Given the non-negative number $m$ and the function `f`,
    a Boolean function that takes a non-negative integer argument,
    the function `Boolean_Cayley_graph` constructs the Cayley graph of
    `f` as a Boolean function on $\mathbb{Z}_2^m$, with the canonical ordering.
    """
    v = 2 ** m
    result = Graph(v)
    result.add_edges([(i,j) for i in xsrange(v) for j in xsrange(i) if f(i ^ j)])
    return result

def boolean_function_cayley_graph(boolf):
    m = boolf.nvariables()
    f = BooleanFunctionWithTranslate(boolf).extended_translate()
    return boolean_cayley_graph(m, f)
