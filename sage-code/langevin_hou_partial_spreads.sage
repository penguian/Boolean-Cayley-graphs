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

import re


def read_langevin_hou_anf_list(file):
    r"""

    Classification of partial spread functions in eight variables
    http://langevin.univ-tln.fr/project/spread/psp.html

    Langevin, Philippe, and Xiang-Dong Hou.
    "Counting partial spread functions in eight variables."
    IEEE Transactions on Information Theory 57, no. 4 (2011): 2263-2269.

    """

    R8.<x1,x2,x3,x4,x5,x6,x7,x8> = BooleanPolynomialRing(8)

    anf_list = []
    line = None
    while line != '':
        line = file.readline()
        match = re.match('anf=(.*)', line)

        if match != None:
            anf_abbr = match.groups()[0]
            anf_pass1 = re.sub('([1-8])', 'x\\1', anf_abbr)
            anf = eval(re.sub('([1-8])x', '\\1*x', anf_pass1))
            anf_list.append(anf)
    return anf_list

