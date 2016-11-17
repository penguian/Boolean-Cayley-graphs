
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
from bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
from containers import List

import cayley_graph_controls as controls

load("bent_function_extended_affine_representative_polynomials.sage")


def save_boolean_dimension_cayley_graph_classifications(dim, start=1):
    r"""
    """
    verbose = controls.verbose

    p = bent_function_extended_affine_representative_polynomials(dim)
    c = [None]*len(p)
    for n in xrange(start, len(p)):
        if verbose:
            print n, ':'
        f = BentFunction(p[n])
        c[n] = BentFunctionCayleyGraphClassification(f)
        name_n = 'p'+str(dim)+'_'+str(n)
        c[n].save_mangled(name_n)
        if verbose:
            c[n].report()
    return c


def load_boolean_dimension_cayley_graph_classifications(dim, start=1):
    r"""
    """
    verbose = controls.verbose

    p = bent_function_extended_affine_representative_polynomials(dim)
    c = [None]*len(p)
    reclassification = [None]*len(p)
    cayley_graph_classes = List([])
    for n in xrange(start, len(p)):
        if verbose:
            print n, ':'
        name_n = 'p'+str(dim)+'_'+str(n)
        c[n] = BentFunctionCayleyGraphClassification.load_mangled(name_n)
        cg_class_list   = c[n].cayley_graph_class_list
        cg_index_matrix = c[n].bent_cayley_graph_index_matrix
        dg_index_matrix = c[n].dual_cayley_graph_index_matrix
        cb_index_list   = c[n].first_matrix_index_list()
        reclassification[n] = matrix(5, len(cg_class_list))

        c_class_counts = np.histogram(cg_index_matrix, range(len(cg_class_list) + 1))[0]
        d_class_counts = np.histogram(dg_index_matrix, range(len(cg_class_list) + 1))[0]
        for i in xrange(len(cg_class_list)):
            g = cg_class_list[i]
            reclassification[n][0, i] = cayley_graph_classes.index_append(g)
            cb_index = cb_index_list[i]
            c_index = cb_index[0]
            b_index = cb_index[1]
            assert cg_index_matrix[c_index, b_index] == i
            j = dg_index_matrix[c_index, b_index]
            reclassification[n][1, i] = i
            reclassification[n][2, i] = c_class_counts[i]
            reclassification[n][3, i] = j
            reclassification[n][4, i] = d_class_counts[j]
        if verbose:
            print reclassification[n]
            c[n].report()
    return c, reclassification, cayley_graph_classes
