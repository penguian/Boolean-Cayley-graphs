r"""
Some binary projective two-weight codes
=======================================

The ``binary_projective_two_weight_codes`` module defines
functions that construct two types of binary projective two-weight codes
as published by Tonchev [Ton1996]_ [Ton2007]_.

AUTHORS:

- Paul Leopardi (2016-09-15): initial version

EXAMPLES:

::

    sage: from boolean_cayley_graphs.binary_projective_two_weight_codes import binary_projective_two_weight_27_6_12
    sage: c27=binary_projective_two_weight_27_6_12()
    sage: c27[1]
    ('000000000000000111111111111',
    '000000000111111000000111111',
    '000111111000011000011000011',
    '001000111011101000101000101',
    '010001011101110011101011101',
    '100010101000101001111101000')

REFERENCES:

Tonchev [Ton1996]_, [Ton2007]_.
"""
#*****************************************************************************
#       Copyright (C) 2016-2017 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************


def binary_projective_two_weight_27_6_12():
    r"""
    Return the binary projective two-weight [27,6,12] codes as published by Tonchev.

    Return a tuple that encodes the generator matrices
    of the binary projective two-weight [27,6,12] codes,
    listed as codes 1, 2, 3a, 3b and 4 in Table 1 of Tonchev [Ton1996]_,
    and repeated as codes 1 to 5 in Table 1.155 of Tonchev [Ton2007]_.

    INPUT:

    - None.

    OUTPUT:

    A tuple of tuples of strings. Each tuple of strings encodes a generator matrix
    of a binary projective two-weight code.

    EXAMPLES:

    ::

        sage: from boolean_cayley_graphs.binary_projective_two_weight_codes import binary_projective_two_weight_27_6_12
        sage: c27=binary_projective_two_weight_27_6_12()
        sage: c27[0]
        ('000000000001111111111111111',
        '000000011110000000011111111',
        '000001100110000111100001111',
        '000111111110011001100110011',
        '011010101010111011101110100',
        '101010101100001110111011101')

    REFERENCES:

    Tonchev [Ton1996]_ [Ton2007]_.
    """
    c1=("000000000001111111111111111",
        "000000011110000000011111111",
        "000001100110000111100001111",
        "000111111110011001100110011",
        "011010101010111011101110100",
        "101010101100001110111011101")
    c2=("000000000000000111111111111",
        "000000000111111000000111111",
        "000111111000011000011000011",
        "001000111011101000101000101",
        "010001011101110011101011101",
        "100010101000101001111101000")
    c3=("000000000000000111111111111",
        "000000011111111000011111111",
        "000001100001111001100001111",
        "001110100010001010101110001",
        "010110101110111110000110110",
        "100011100110011111110010011")
    c4=("000000000000000111111111111",
        "000000011111111000000001111",
        "000001100001111000011110011",
        "001110100010111011101110101",
        "010110101110001100100110000",
        "111010010100011001101010000")
    c5=("000000000000000111111111111",
        "000000000111111000000111111",
        "000000111000111000111000111",
        "000111001001001011011000011",
        "011001011010110001101001000",
        "101010110011010000010010101")

    return (c1, c2, c3, c4, c5)


def binary_projective_two_weight_35_6_16():
    r"""
    Return the binary projective two-weight [35,6,16] codes as published by Tonchev.

    Return a tuple that encodes the generator matrices
    of the binary projective two-weight [35,6,16] codes, listed
    as codes 1, 2a, 2b, 3a, 3b, 4a and 4b in Table 2 of Tonchev [Ton1996]_,
    and repeated as codes 1 to 7 in Table 1.156 of Tonchev [Ton2007]_.


    INPUT:

    - None.

    OUTPUT:

    A tuple of tuples of strings. Each tuple of strings encodes a generator matrix
    of a binary projective two-weight code.

    EXAMPLES:

    ::

        sage: from boolean_cayley_graphs.binary_projective_two_weight_codes import binary_projective_two_weight_35_6_16
        sage: c35=binary_projective_two_weight_35_6_16()
        sage: c35[2]
        ('00000000000000011111111111111111111',
        '00000000011111100000000001111111111',
        '00011111100001100001111110000111111',
        '00100011101110101110001110111000111',
        '01000101110111000010110010001011001',
        '10001010100010110100010100011101011')

    REFERENCES:

    Tonchev [Ton1996]_ [Ton2007]_.
    """
    c1=("00000000000000000001111111111111111",
        "00000000000111111110000000011111111",
        "00000111111000000110000111100001111",
        "00011000011000011110011001100110011",
        "01101001101001101010111010001000100",
        "10101010110010110100001000100011101")
    c2=("00000000000000000001111111111111111",
        "00000000011111111110000001111111111",
        "00011111100001111110000110000111111",
        "00100011100010001110001010111000111",
        "01000101100100010110111010001011001",
        "10001010101110110010011110011101011")
    c3=("00000000000000011111111111111111111",
        "00000000011111100000000001111111111",
        "00011111100001100001111110000111111",
        "00100011101110101110001110111000111",
        "01000101110111000010110010001011001",
        "10001010100010110100010100011101011")
    c4=("00000000000000000001111111111111111",
        "00000000000111111110000000011111111",
        "00000111111000011110000001100001111",
        "00111000111000101110001110100010001",
        "01011011001011100010010010001100110",
        "10001001010001110100100101100110011")
    c5=("00000000000000000001111111111111111",
        "00000000000111111110000000011111111",
        "00000111111000011110000111100000011",
        "00111000111011101110111000100011101",
        "01011011001000100011001011001101100",
        "11101101011001100110011101010110100")
    c6=("00000000000000000001111111111111111",
        "00000000000111111110000000011111111",
        "00000011111000111110000011100000111",
        "00011100111001001110001101101111011",
        "01100101001010000110110110110011000",
        "10101000011011011011011101010101101")
    c7=("00000000000000000001111111111111111",
        "00000000000111111110000000011111111",
        "00000011111000111110001111100011111",
        "00011100111001001110110001100000011",
        "01100101001010000110010010100101111",
        "10101000011011011010000110101000101")

    return (c1, c2, c3, c4, c5, c6, c7)
