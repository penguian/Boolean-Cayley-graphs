"""
Bit-level functions of integers.

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

def parity(n):
    """
    Given the non-negative number $n$, the function `parity` returns 1 if the number of 1 bits in the binary expansion is odd, otherwise 0.
    """
    result = False
    while n != 0:
        n &= n - 1
        result = not result
    return 1 if result else 0

def inner(a, b):
    """
    Given the non-negative numbers $a$ and $b$, the function `inner` returns the binary inner product of their binary expansions.
    """
    return parity(a & b)
