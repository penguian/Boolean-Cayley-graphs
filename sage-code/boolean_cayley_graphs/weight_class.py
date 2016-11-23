
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.functions.other import sqrt


def weight_class(length, weight):
    r"""
    """
    sqrtlength = sqrt(length)
    return int(((weight*2)/sqrtlength - sqrtlength + 1) / 2)
