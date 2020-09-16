r"""
"""

#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.crypto.boolean_function import BooleanFunction


def read_s_box(fil):
    r"""
    """
    lis = []
    lin = fil.readline()
    if lin[0:5] != 'S-Box':
        raise IOError
    while lin not in ('','\n'):
        lin = fil.readline()
        if lin not in ('','\n'):
            for n in range(8):
                pos=n*9
                lis.append(ZZ('0x'+lin[pos:pos+8]))
    numlist = [num.digits(2,padto=32) for num in lis]
    bitmatrix = matrix(numlist)
    boolflist = [BooleanFunction(list(bitmatrix.T[n,:][0]))
                 for n in range(32)]
    return boolflist


def read_s_boxes_file(fname='../CAST-128/cast-128-s-boxes.txt'):
    r"""
    """
    s_box_functions = [None]
    fil = open(fname)
    for n in range(8):
        s_box_functions.append(read_s_box(fil))
    fil.close()
    return s_box_functions
