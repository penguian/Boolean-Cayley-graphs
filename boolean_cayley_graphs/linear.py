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

    # Define the basis of the vector space.
    basis = [2**a for a in range(dim)]

    # Create the GF(2) matrix corresponding to perm, assuming linearity.
    perm_m = Matrix(GF(2), [
            base2(dim, Integer(perm(x)))
            for x in basis])

    # If dim == 1, the permutation must be the identity.
    if dim == 1:
        return (
            (True, perm_m.transpose())
            if certificate
            else True)

    # Define some subsets of range(v)
    pairs = [2**a ^ 2**b for a in range(dim) for b in range(a+1, dim)]
    remnant = [x for x in range(1, v) if x not in basis and x not in pairs]

    # Check that perm is linear on each pair of basis vectors.
    v_m = Matrix(GF(2), [
            base2(dim, Integer(x))
            for x in pairs])
    permv_m = Matrix(GF(2), [
            base2(dim, Integer(x))
            for x in [perm(y) for y in pairs]])
    linear_on_pairs = Matrix(v_m) * Matrix(perm_m) == permv_m
    if not linear_on_pairs:
        return (False, None) if certificate else False

    # if len(remnant) == 0 then there are no vectors left to test.
    if len(remnant) == 0:
        return (
            (True, perm_m.transpose())
            if certificate
            else True)

    # Check that perm is linear on all remaining vectors.
    v_m = Matrix(GF(2), [
            base2(dim, Integer(x))
            for x in remnant])
    permv_m = Matrix(GF(2), [
            base2(dim, Integer(x))
            for x in [perm(y) for y in remnant]])
    linear = Matrix(v_m) * Matrix(perm_m) == permv_m
    return (
         ((True, perm_m.transpose()) if linear else (False, None))
         if certificate
         else linear)
