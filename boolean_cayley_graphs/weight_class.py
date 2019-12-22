r"""
Classification of bent functions by their weight
================================================

The ``weight_class`` module defines the ``weight_class`` function,
which returns the weight class corresponding to a weight.

AUTHORS:

- Paul Leopardi (2016-09-25): initial version

EXAMPLES:

::

    sage: from boolean_cayley_graphs.weight_class import weight_class
    sage: weight_class(4,1)
    0
    sage: weight_class(16,10)
    1

REFERENCES:

Leopardi [Leo2017]_ Section 2.2.
"""
#*****************************************************************************
#       Copyright (C) 2016-2017 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.functions.other import sqrt


def weight_class(length, weight):
    r"""
    Return the weight class corresponding to a given length and weight.

    The length is the length of the truth table of a Boolean function.
    The weight is the Hamming weight of the Boolean function.

    INPUT:

    - ``length`` -- positive integer:
    - ``weight`` -- positive integer: the given Hamming weight.

    OUTPUT:

    An integer representing the weight class corresponding to ``length`` and
    ``weight``.

    EXAMPLES:

    ::

        sage: from boolean_cayley_graphs.weight_class import weight_class
        sage: weight_class(4,1)
        0
        sage: weight_class(16,10)
        1
        sage: weight_class(16,6)
        0
        sage: weight_class(64,36)
        1
        sage: weight_class(63,37)
        1
        sage: weight_class(65,35)
        0

    .. NOTE::

        The weight class really only makes sense for bent functions, for which
        the weight class is either 0 or 1 [Leo2017]_.

    REFERENCES:

    Leopardi [Leo2017]_ Section 2.2.

    """
    sqrtlength = sqrt(length)
    return int(((weight*2)/sqrtlength - sqrtlength + 1) / 2)
