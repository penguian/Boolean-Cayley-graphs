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

from sage.parallel.decorate import parallel

from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
from boolean_cayley_graphs.bent_function import BentFunction


def call_in_parallel(
    f,
    list_of_tuples,
    ncpus):
    r"""
    """
    parallelize = parallel(p_iter='fork', ncpus=ncpus)
    return list(parallelize(f)(list_of_tuples))


def classify(
    n,
    form):
    r"""
    """
    return BentFunctionCayleyGraphClassification(BentFunction(form))


def classify_in_parallel(
    list_of_f,
    start=0,
    stop=None,
    ncpus=4):
    r"""
    """
    if stop == None:
        stop = len(list_of_f)
    list_of_tuples = [
        ((n, list_of_f[n]))
        for n in range(start, stop)]
    return call_in_parallel(classify, list_of_tuples, ncpus)


def save_one_classification(
    name,
    form):
    r"""
    """
    c = BentFunctionCayleyGraphClassification(BentFunction(form))
    c.save_mangled(name)
    return name


def save_classifications_in_parallel(
    name_prefix,
    list_of_f,
    start=0,
    stop=None,
    ncpus=4):
    r"""
    """
    if stop == None:
        stop = len(list_of_f)
    list_of_tuples = [
        ((name_prefix + '_' + str(n), list_of_f[n]))
        for n in range(start, stop)]
    return call_in_parallel(save_one_classification, list_of_tuples, ncpus)
