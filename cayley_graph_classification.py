
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from boolean_function_cayley_graph_classification import *
from strongly_regular_graph import *


def cayley_graph_classification(f):
    r"""
    """
    fcc = BooleanFunctionCayleyGraphClassification(f)
    srgs = [StronglyRegularGraph(g) for g in fcc.cayley_graph_class_list]
    return fcc, srgs


