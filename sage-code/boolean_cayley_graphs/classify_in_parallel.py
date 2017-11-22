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

from sage.functions.other import Function_ceil
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
    return BentFunctionCayleyGraphClassification.from_function(BentFunction(form))


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
    c = BentFunctionCayleyGraphClassification.from_function(BentFunction(form))
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
    p = BentFunctionCayleyGraphClassPart.from_function(bentf,c_start=c_start,c_stop=c_stop)
    p.save_mangled(name)
    return name


def save_class_parts_in_parallel(
    name_prefix,
    form,
    c_len=1,
    ncpus=4):
    r"""
    EXAMPLE:

    ::

        sage: import glob
        sage: import os
        sage: from boolean_cayley_graphs.bent_function import BentFunction
        sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassPart
        sage: R2.<x1,x2> = BooleanPolynomialRing(2)
        sage: p = x1+x2+x1*x2
        sage: f = BentFunction(p)
        sage: from boolean_cayley_graphs.classify_in_parallel import save_class_parts_in_parallel
        sage: s = save_class_parts_in_parallel('test_part', f)
        sage: p1=BentFunctionCayleyGraphClassPart.load_mangled("test_part_1.sobj")
        sage: p1.__dict__
        {'algebraic_normal_form': x0*x1 + x0 + x1,
        'bent_cayley_graph_index_matrix': [0 0 1 0],
        'c_start': 1,
        'cayley_graph_class_list': ['CK', 'C~'],
        'dual_cayley_graph_index_matrix': [0 0 1 0],
        'weight_class_matrix': [0 0 1 0]}
        sage: for n in range(4):
        ....:     fname = glob.glob("BentFunctionCayleyGraphClassPart__test_part_"+str(n)+".sobj")
        ....:     print(fname[0])
        ....:     os.remove(fname[0])
        ....:
        BentFunctionCayleyGraphClassPart__test_part_0.sobj
        BentFunctionCayleyGraphClassPart__test_part_1.sobj
        BentFunctionCayleyGraphClassPart__test_part_2.sobj
        BentFunctionCayleyGraphClassPart__test_part_3.sobj
    """
    bentf = BentFunction(form)
    dim = bentf.nvariables()
    v = 2 ** dim
    ceil = Function_ceil()
    nbr_parts = ceil(v * 1.0 / c_len)
    list_of_tuples = [
        ((name_prefix + '_' + str(n), bentf, c_len * n, c_len * (n+1)))
        for n in range(nbr_parts)]
    return call_in_parallel(save_one_class_part, list_of_tuples, ncpus)
