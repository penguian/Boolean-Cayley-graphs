
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.structure.sage_object import SageObject
from index_append_list import IndexAppendList


class BentFunctionWeightClassification(SageObject):

    def __init__(self, c):
        weight_class_list = []
        parameter_list = IndexAppendList([])
        for s in c.cayley_graph_class_list:
            weight_class_list.append(
                parameter_list.index_append(
                    s.strongly_regular_parameters))
        self.weight_class_list = weight_class_list

        weight_class_map = lambda n: weight_class_list[n]
        self.weight_class_matrix = c.cayley_graph_index_matrix.apply_map(weight_class_map)
