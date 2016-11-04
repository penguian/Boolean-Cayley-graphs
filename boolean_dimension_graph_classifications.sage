
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

import numpy as np


from bent_function import BentFunction
from bent_function_graph_classification import BentFunctionGraphClassification
from containers import List

import cayley_graph_controls as controls

load("bent_function_extended_affine_representative_polynomials.sage")


def save_boolean_dimension_graph_classifications(dim, start=1):
    r"""
    """
    verbose = controls.verbose

    p = bent_function_extended_affine_representative_polynomials(dim)
    c = [None]*len(p)
    for n in xrange(start, len(p)):
        if verbose:
            print n, ':'
        f = BentFunction(p[n])
        c[n] = BentFunctionGraphClassification(f)
        name_n = 'p'+str(dim)+'_'+str(n)
        c[n].save_mangled(name_n)
        if verbose:
            c[n].report()
    return c


def load_boolean_dimension_graph_classifications(dim, start=1):
    r"""
    """
    verbose = controls.verbose

    p = bent_function_extended_affine_representative_polynomials(dim)
    c = [None]*len(p)
    reclassification = [None]*len(p)
    cayley_graph_classes = List([])
    linear_graph_classes = List([])
    for n in xrange(start, len(p)):
        if verbose:
            print n, ':'
        name_n = 'p'+str(dim)+'_'+str(n)
        c[n] = BentFunctionGraphClassification.load_mangled(name_n)
        cg_class_list   = c[n].cayley_graph_class_list
        cg_index_matrix = c[n].cayley_graph_index_matrix
        lg_class_list   = c[n].linear_graph_class_list
        lg_index_matrix = c[n].linear_graph_index_matrix
        reclassification[n] = matrix(4, max(len(cg_class_list), len(lg_class_list)))

        c_class_counts = np.histogram(cg_index_matrix, range(len(cg_class_list) + 1))[0]
        for i in xrange(len(cg_class_list)):
            g = cg_class_list[i]
            reclassification[n][0, i] = cayley_graph_classes.index_append(g)
            reclassification[n][1, i] = c_class_counts[i]

        l_class_counts = np.histogram(lg_index_matrix, range(len(lg_class_list) + 1))[0]
        for i in xrange(len(lg_class_list)):
            g = lg_class_list[i]
            reclassification[n][2, i] = linear_graph_classes.index_append(g)
            reclassification[n][3, i] = l_class_counts[i]
        if verbose:
            print reclassification[n]
            c[n].report()
    return c, reclassification, cayley_graph_classes
