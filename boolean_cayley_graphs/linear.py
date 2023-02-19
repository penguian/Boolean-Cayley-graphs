r"""
Tests for GF(2) linear algebra
==============================

The ``linear`` module defines functions that
test for linearity of functions defined on
GF(2) vector spaces.

AUTHORS:

- Paul Leopardi (2023-01-16): initial version

"""
#*****************************************************************************
#       Copyright (C) 2016-2023 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************


from sage.matrix.constructor import Matrix
from sage.rings.finite_rings.finite_field_constructor import FiniteField as GF
from sage.rings.integer import Integer
from boolean_cayley_graphs.integer_bits import base2

encoding = "UTF-8"


def is_linear(dim, perm, certificate=False):
    r"""
    Check if a permutation on `range(2**dim)` is linear on `GF(2)**dim`.

    INPUT:

    - ``dim`` -- the dimension of the GF(2) linear space.
    - ``perm`` -- a function from `range(2**dim)` to iself, usually a permutation.
    - ``certificate`` -- bool (default False). If true, return the GF(2) matrix
       that corresponds to the permutation.

    OUTPUT:

    If ``certificate`` is false, a bool value.
    If ``certificate`` is true, a tuple consisting of either (False, None)
    or (True, M), where M is a GF(2) matrix that corresponds to the permutation.

    EXAMPLES:

    ::

        sage: from boolean_cayley_graphs.linear import is_linear
        sage: dim = 2
        sage: perm1 = lambda x: x*3 % 4
        sage: is_linear(dim, perm1)
        True
        sage: is_linear(dim, perm1, certificate=True)
        (
              [1 0]
        True, [1 1]
        )
        sage: perm2 = lambda x: (x+1) % 4
        sage: is_linear(dim, perm2)
        False
        sage: is_linear(dim, perm2, certificate=True)
        (False, None)
    """
    v = 2**dim

    # If perm(0) != 0 then perm cannot be linear.
    if perm(0) != 0:
        return (False, None) if certificate else False

    # Check that perm is linear on each pair of basis vectors.
    possibly_linear = True
    for a in range(dim):
        for b in range(a + 1, dim):
            if perm(2**a) ^ perm(2**b) != perm((2**a) ^ (2**b)):
                possibly_linear = False
                break
        if not possibly_linear:
            break
    if not possibly_linear:
        return (False, None) if certificate else False

    # Create the GF(2) matrix corresponding to perm, assuming linearity.
    perm_matrix = Matrix(GF(2), [
        base2(dim, Integer(perm(2**a)))
        for a in range(dim)]).transpose()
    # Check for each vector that the matrix gives the same result as perm.
    vm = Matrix(GF(2), [
         base2(dim, Integer(x))
         for x in range(v)]).transpose()
    linear = perm_matrix * vm == vm[:, [perm(x) for x in range(v)]]
    if certificate:
        return (True, perm_matrix) if linear else (False, None)
    else:
        return linear
