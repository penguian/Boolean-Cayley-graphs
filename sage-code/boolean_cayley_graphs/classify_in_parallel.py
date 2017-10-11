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
from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassPart
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


def save_one_class_part(
    name,
    bentf,
    c_start,
    c_stop):
    r"""
    """
    p = BentFunctionCayleyGraphClassPart(bentf,c_start=c_start,c_stop=c_stop)
    p.save_mangled(name)
    return name


def save_class_parts_in_parallel(
    name_prefix,
    form,
    nbr_parts=4,
    ncpus=4):
    r"""
    EXAMPLE:

    ::

        sage: from boolean_cayley_graphs.bent_function import BentFunction
        sage: R2.<x1,x2> = BooleanPolynomialRing(2)
        sage: p = x1+x2+x1*x2
        sage: f = BentFunction(p)
        sage: from boolean_cayley_graphs.classify_in_parallel import save_class_parts_in_parallel
        sage: s = save_class_parts_in_parallel('test_part', f)
        sage: p1=load("BentFunctionCayleyGraphClassPart__test_part_1.sobj")
        sage: p1.__dict__
        {'_default_filename': '/home/leopardi/sync/src/sage-sandbox/Boolean-Cayley-graphs/sage-code/BentFunctionCayleyGraphClassPart__test_part_1.sobj',
        'algebraic_normal_form': x0*x1 + x0 + x1,
        'bent_cayley_graph_index_matrix': [0 0 1 0],
        'c_start': 1,
        'cayley_graph_class_list': ['CK', 'C~'],
        'dual_cayley_graph_index_matrix': [0 0 1 0],
        'weight_class_matrix': [0 0 1 0]}
    """
    bentf = BentFunction(form)
    dim = bentf.nvariables()
    v = 2 ** dim
    c_len = v // nbr_parts
    list_of_tuples = [
        ((name_prefix + '_' + str(n), bentf, c_len * n, c_len * (n+1)))
        for n in range(nbr_parts)]
    return call_in_parallel(save_one_class_part, list_of_tuples, ncpus)
