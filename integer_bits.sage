"""
Bit-level functions of integers.

Paul Leopardi.
"""

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
