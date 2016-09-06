
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

load('bent_function_extended_affine_representative_polynomials.sage')

load('boolean_polynomial_cayley_graph_classification.sage')

import numpy as np

def classify_bent_function_extended_affine_cayley_graphs(dim):
    p = bent_function_extended_affine_representative_polynomials(dim)
    c = [None]*len(p)
    for n in range(1,len(c)):
        print n
        c[n] = BooleanPolynomialCayleyGraphClassification(p[n])
        save_cayley_graph_classification(c[n], 'p'+str(dim)+'_'+str(n))
    return c


def classify_bent_function_cayley_graphs(dim):
    p = bent_function_extended_affine_representative_polynomials(dim)
    class_indices = [None]*len(p)
    graph_classes = IndexAppendList([])
    for n in sxrange(1,len(p)):
        print n, ':'
        c = load_cayley_graph_classification('p'+str(dim)+'_'+str(n))
        cg_class_list = c.cayley_graph_class_list
        cg_index_matrix = c.cayley_graph_index_matrix
        class_indices[n] = matrix(2,len(cg_class_list))
        class_counts = np.histogram(cg_index_matrix, range(len(cg_class_list) + 1))[0]
        for i in xrange(len(cg_class_list)):
            g = cg_class_list[i]
            class_indices[n][0, i] = graph_classes.index_append(g)
            class_indices[n][1, i] = class_counts[i]
        print class_indices[n]
    return class_indices
