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

from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
from boolean_cayley_graphs.bent_function import BentFunction


def classify(n, form):
    r"""
    """
    import boolean_cayley_graphs.cayley_graph_controls as controls
    controls.timimg = True
    return BentFunctionCayleyGraphClassification(BentFunction(form))


def classify_in_parallel(list_of_forms, ncpus=4):
    r"""
    """
    do_in_parallel = parallel(p_iter='fork', ncpus=ncpus)
    list_of_form_tuples = [
        ((n, list_of_forms[n]))
        for n in range(len(list_of_forms))]
    return list(do_in_parallel(classify)(list_of_form_tuples))
