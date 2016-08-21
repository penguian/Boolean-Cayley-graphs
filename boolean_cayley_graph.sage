"""
Cayley graph of a Boolean function.

Paul Leopardi.
"""

def boolean_cayley_graph(m, f):
    """
    Given the non-negative number $m$ and the function `f`,
    a Boolean function that takes a non-negative integer argument,
    the function `Boolean_Cayley_graph` constructs the Cayley graph of
    `f` as a Boolean function on $\mathbb{Z}_2^m$, with the canonical ordering.
    """
    v = 2 ** m
    result = Graph(v)
    result.add_edges([(i,j) for i in sxrange(v) for j in sxrange(i) if f(i ^^ j)])
    return result

load("extended_translation_equivalent_function.sage")

def boolean_function_cayley_graph(boolf):
    m = boolf.nvariables()
    return boolean_cayley_graph(m, extended_translation_equivalent_function(boolf))
