r"""
The ``integer_bits`` module defines functions that
return bit-level properties of integers,
such as partity and bitwise inner product.

AUTHORS:

- Paul Leopardi (2016-08-21): initial version

"""
#*****************************************************************************
#       Copyright (C) 2016-2017 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************


from sage.rings.integer import Integer


base2 = lambda dim, num: Integer(num).digits(2, padto=dim)
r"""
Map ``num`` to :math:`\mathbb{F}_2^{dim}` using lexicographical ordering.

INPUT:

- ``num`` -- non-negative integer. The value to be mapped.
- ``dim`` -- positive integer. The Boolean dimension.

OUTPUT:

A list of 0,1 integer values of length ``dim``.

EXAMPLES:

::

    sage: from boolean_cayley_graphs.integer_bits import base2
    sage: base2(5,3)
    [1, 1, 0, 0, 0]
    sage: base2(3,5)
    [1, 0, 1]
    sage: base2(3,1)
    [1, 0, 0]
"""


def parity(n):
    r"""
    Return the bit parity of a non-negative integer.

    Given the non-negative number ``n``, the function ``parity`` returns 1
    if the number of 1 bits in the binary expansion is odd, otherwise 0.

    INPUT:

    - ``n`` -- non-negative integer.

    OUTPUT:

    0 or 1, being the bit parity of ``n``.

    EXAMPLES:

    ::

        sage: from boolean_cayley_graphs.integer_bits import parity
        sage: parity(0)
        0
        sage: parity(2)
        1
        sage: parity(3)
        0
    """
    result = False
    while n != 0:
        n &= n - 1
        result = not result
    return 1 if result else 0


def inner(a, b):
    r"""
    Return the inner product of two non-negative integers interpreted as Boolean vectors.

    Given the non-negative numbers ``a`` and ``b``, the function ``inner`` returns
    the Boolean inner product of their binary expansions.

    INPUT:

    - ``a`` -- non-negative integer.
    - ``b`` -- non-negative integer.

    OUTPUT:

    0 or 1, being the Boolean inner product of the Boolean vectors
    represented by ``a`` and ``b``.

    EXAMPLES:

    ::

            sage: from boolean_cayley_graphs.integer_bits import inner
            sage: inner(0,0)
            0
            sage: inner(1,1)
            1
            sage: inner(3,3)
            0
    """
    return parity(a & b)
