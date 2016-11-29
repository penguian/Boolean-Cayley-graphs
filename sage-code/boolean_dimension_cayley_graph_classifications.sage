
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

import copy
import numpy as np


from boolean_cayley_graphs.bent_function import BentFunction
from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
from boolean_cayley_graphs.containers import List
from sage.structure.sage_object import register_unpickle_override

import boolean_cayley_graphs.cayley_graph_controls as controls

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

    register_unpickle_override(
        'bent_function_cayley_graph_classification',
        'BentFunctionCayleyGraphClassification',
        BentFunctionCayleyGraphClassification)
    register_unpickle_override('containers', 'List', List)

    p = bent_function_extended_affine_representative_polynomials(dim)
    c = [None]*len(p)
    for n in xrange(start, len(p)):
        if verbose:
            print n, ':'
        name_n = 'p'+str(dim)+'_'+str(n)
        c[n] = BentFunctionCayleyGraphClassification.load_mangled(name_n)
        if verbose:
            c[n].report()
    return c


def reclassify_cayley_graph_classifications(cc, start=1):
    r"""
    """
    verbose = controls.verbose

    cayley_graph_classes = List([])
    c = copy.deepcopy(cc)
    reclassification = [None]*len(c)
    for n in xsrange(start, len(c)):
        if verbose:
            print n, ':'
        cg_class_list   = c[n].cayley_graph_class_list
        cg_index_matrix = np.matrix(c[n].bent_cayley_graph_index_matrix)
        dg_index_matrix = np.matrix(c[n].dual_cayley_graph_index_matrix)
        cb_index_list   = c[n].first_matrix_index_list()
        reclassification[n] = matrix(5, len(cg_class_list))

        c_class_counts = np.histogram(cg_index_matrix,
                                      range(len(cg_class_list) + 1))[0]
        d_class_counts = np.histogram(dg_index_matrix,
                                      range(len(cg_class_list) + 1))[0]
        new_cg_index_matrix = cg_index_matrix.copy()
        for i in xrange(len(cg_class_list)):
            g = cg_class_list[i]
            reclass_index = cayley_graph_classes.index_append(g)
            reclassification[n][0, i] = reclass_index
            cb_index = cb_index_list[i]
            c_index = cb_index[0]
            b_index = cb_index[1]
            assert cg_index_matrix[c_index, b_index] == i
            new_cg_index_matrix = np.where(cg_index_matrix == i,
                                           reclass_index,
                                           new_cg_index_matrix)
            j = dg_index_matrix[c_index, b_index]
            reclassification[n][1, i] = i
            reclassification[n][2, i] = c_class_counts[i]
            reclassification[n][3, i] = j
            reclassification[n][4, i] = d_class_counts[j]
        c[n].bent_cayley_graph_index_matrix = new_cg_index_matrix
        new_dg_index_matrix = dg_index_matrix.copy()
        for i in xrange(len(cg_class_list)):
            reclass_index = reclassification[n][0, i]
            new_dg_index_matrix = np.where(dg_index_matrix == i,
                                          reclass_index,
                                          new_dg_index_matrix)
        c[n].dual_cayley_graph_index_matrix = new_dg_index_matrix
        if verbose:
            print reclassification[n]
    return cayley_graph_classes, c, reclassification
