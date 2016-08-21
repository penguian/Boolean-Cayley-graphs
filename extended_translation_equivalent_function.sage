"""
Extended translation equivalent function.

Paul Leopardi.
"""

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
