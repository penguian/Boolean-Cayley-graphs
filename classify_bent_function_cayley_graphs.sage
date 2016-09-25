
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

import numpy as np

from bent_function_weight_classification import BentFunctionWeightClassification
from boolean_polynomial_cayley_graph_classification import BooleanPolynomialCayleyGraphClassification
from boolean_polynomial_cayley_graph_classification import load_cayley_graph_classification
from boolean_polynomial_cayley_graph_classification import save_cayley_graph_classification
from index_append_list import IndexAppendList

import cayley_graph_controls as controls

load("bent_function_extended_affine_representative_polynomials.sage")


def classify_bent_function_extended_affine_cayley_graphs(dim):
    verbose = controls.verbose

    p = bent_function_extended_affine_representative_polynomials(dim)
    c = [None]*len(p)
    for n in range(1, len(c)):
        if verbose:
            print n, ':'
        c[n] = BooleanPolynomialCayleyGraphClassification(p[n])
        save_cayley_graph_classification(c[n], 'p'+str(dim)+'_'+str(n))
    return c


def classify_bent_function_cayley_graphs(dim):
    verbose = controls.verbose

    p = bent_function_extended_affine_representative_polynomials(dim)
    classification = [None]*len(p)
    graph_classes = IndexAppendList([])
    for n in sxrange(1, len(p)):
        if verbose:
            print n, ':'
        c = load_cayley_graph_classification('p'+str(dim)+'_'+str(n))
        wc = BentFunctionWeightClassification(c)
        if verbose:
           wcm = wc.weight_class_matrix
           dsm = c.dillon_schatz_design_matrix
           print "Weight class matrix",
           print "equals" if wcm == dsm else "does not equal",
           print "Dillon Schatz design matrix."
        cg_class_list = c.cayley_graph_class_list
        cg_index_matrix = c.cayley_graph_index_matrix
        classification[n] = matrix(3,len(cg_class_list))
        class_counts = np.histogram(cg_index_matrix, range(len(cg_class_list) + 1))[0]
        for i in xrange(len(cg_class_list)):
            g = cg_class_list[i]
            classification[n][0, i] = graph_classes.index_append(g)
            classification[n][1, i] = wc.weight_class_list[i]
            classification[n][2, i] = class_counts[i]
        if verbose:
            print classification[n]
    return classification, graph_classes