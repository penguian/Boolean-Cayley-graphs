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
    Call the function `f` in parallel

    INPUT:

    - ``f`` -- Function to call.
    - ``list_of_tuples`` -- A list of tuples to use as arguments to ``f``.
    - ``ncpus`` -- Integer. Default=4. The number of cpus to use in parallel.

    OUTPUT: A list of tuples. Each tuple contains an (args,keywds) pair, and a result.

    EFFECT:

    .. Note::

    See http://doc.sagemath.org/html/en/reference/parallel/sage/parallel/decorate.html

    EXAMPLE:

    ::

        sage: from boolean_cayley_graphs.classify_in_parallel import call_in_parallel
        sage: summ = lambda L: add(L)
        sage: call_in_parallel(summ,[((1,2),),((5,4),),((3,3),)],2)
        [((((1, 2),), {}), 3), ((((5, 4),), {}), 9), ((((3, 3),), {}), 6)]
    """
    parallelize = parallel(p_iter='fork', ncpus=ncpus)
    return list(parallelize(f)(list_of_tuples))


def classify(
    n,
    form):
    r"""
    Given an algebraic normal form of a bent function,
    construct the corresponding Cayley graph classification.

    INPUT:

    - ``n`` -- Integer. Tuple number.
    - ``form`` -- A Boolean function or an algebraic normal form.

    OUTPUT:

    The Cayley graph classification corresponding to the bent function
    defined by ``form``.

    .. Note::

    The parameters ``n`` and ``form`` as used here conform to the interface used by
    ``parallel``.
    See http://doc.sagemath.org/html/en/reference/parallel/sage/parallel/decorate.html

    EXAMPLE:

    ::

        sage: from boolean_cayley_graphs.bent_function import BentFunction
        sage: from boolean_cayley_graphs.classify_in_parallel import classify
        sage: bentf = BentFunction([0,0,0,1])
        sage: bentf.algebraic_normal_form()
        x0*x1
        sage: classify(0, bentf).report()
        Algebraic normal form of Boolean function: x0*x1
        Function is bent.
        <BLANKLINE>
        <BLANKLINE>
        SDP design incidence structure t-design parameters: (True, (1, 4, 1, 1))
        <BLANKLINE>
        Classification of Cayley graphs and classification of Cayley graphs of duals are the same:
        <BLANKLINE>
        There are 2 extended Cayley classes in the extended translation class.
    """
    return BentFunctionCayleyGraphClassification.from_function(BentFunction(form))


def classify_in_parallel(
    list_of_f,
    start=0,
    stop=None,
    ncpus=4):
    r"""
    In parallel, construct a list of Cayley graph classifications
    corresponding to a list of bent functions.

    INPUT:

    - ``list_of_f`` -- List of forms or bent functions.
    - ``start`` -- Integer. Default=0. Index of start position in the list.
    - ``stop`` -- Integer. Default=None. Index after end position, or ``None`` if whole remaining list.
    - ``ncpus`` -- Integer. Default=4. The number of cpus to use in parallel.

    OUTPUT: A list of tuples. Each tuple contains an (args,keywds) pair of arguments to `classify`,
    and a classification result.

    EXAMPLE:

    ::

        sage: from boolean_cayley_graphs.bent_function import BentFunction
        sage: from boolean_cayley_graphs.classify_in_parallel import classify_in_parallel
        sage: bentf0 = BentFunction([0,0,0,1])
        sage: bentf0.algebraic_normal_form()
        x0*x1
        sage: bentf1 = BentFunction([0,0,1,0])
        sage: bentf1.algebraic_normal_form()
        x0*x1 + x1
        sage: classes = classify_in_parallel([bentf0,bentf1],ncpus=2)
        sage: classes[0][1].report()
        Algebraic normal form of Boolean function: x0*x1
        Function is bent.
        <BLANKLINE>
        <BLANKLINE>
        SDP design incidence structure t-design parameters: (True, (1, 4, 1, 1))
        <BLANKLINE>
        Classification of Cayley graphs and classification of Cayley graphs of duals are the same:
        <BLANKLINE>
        There are 2 extended Cayley classes in the extended translation class.
    """
    if stop == None:
        stop = len(list_of_f)
    list_of_tuples = [
        ((n, list_of_f[n]))
        for n in range(start, stop)]
    return call_in_parallel(
        classify,
        list_of_tuples,
        ncpus)


def save_one_classification(
    name,
    form):
    r"""
    Given an algebraic normal form of a bent function,
    construct and save the corresponding Cayley graph classification.

    INPUT:

    - ``name`` -- String. Name to use with ``save_mangled`` to save the classification.
    - ``form`` -- A Boolean function or an algebraic normal form.

    OUTPUT: A copy of the string ``name``.

    EFFECT: Uses ``name`` to save the classification corresponding to ``form``.

    EXAMPLE:

    ::

        sage: import os
        sage: from boolean_cayley_graphs.bent_function import BentFunction
        sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
        sage: R2.<x1,x2> = BooleanPolynomialRing(2)
        sage: p = x1+x2+x1*x2
        sage: f = BentFunction(p)
        sage: from boolean_cayley_graphs.classify_in_parallel import save_one_classification
        sage: name = 'test_save_one_classification'
        sage: mangled_name = BentFunctionCayleyGraphClassification.mangled_name(name)
        sage: mangled_fname = mangled_name + '.sobj'
        sage: s = save_one_classification(name, f)
        sage: c = load(mangled_fname)
        sage: c.report()
        Algebraic normal form of Boolean function: x0*x1 + x0 + x1
        Function is bent.
        <BLANKLINE>
        <BLANKLINE>
        SDP design incidence structure t-design parameters: (True, (1, 4, 1, 1))
        <BLANKLINE>
        Classification of Cayley graphs and classification of Cayley graphs of duals are the same:
        <BLANKLINE>
        There are 2 extended Cayley classes in the extended translation class.
        sage: print(mangled_fname)
        BentFunctionCayleyGraphClassification__test_save_one_classification.sobj
        sage: os.remove(mangled_fname)
    """
    c = BentFunctionCayleyGraphClassification.from_function(
        BentFunction(form))
    c.save_mangled(name)
    return name


def save_classifications_in_parallel(
    name_prefix,
    list_of_f,
    start=0,
    stop=None,
    ncpus=4):
    r"""
    In parallel, construct and save a number of Cayley graph classifications
    corresponding to a list of bent functions.

    INPUT:

    - ``name_prefix`` -- String. Name prefix to use with ``save_mangled`` to save each classification.
    - ``list_of_f`` -- List of forms or bent functions.
    - ``start`` -- Integer. Default=0. Index of start position in the list.
    - ``stop`` -- Integer. Default=None. Index after end position, or ``None`` if whole remaining list.
    - ``ncpus`` -- Integer. Default=4. The number of cpus to use in parallel.

    OUTPUT:

    EFFECT: Uses ``name`` to save the classifications corresponding to ``list_of_f``.


    EXAMPLE:

    ::

        sage: from boolean_cayley_graphs.bent_function import BentFunction
        sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
        sage: from boolean_cayley_graphs.classify_in_parallel import save_classifications_in_parallel
        sage: bentf0 = BentFunction([0,0,0,1])
        sage: bentf0.algebraic_normal_form()
        x0*x1
        sage: bentf1 = BentFunction([0,0,1,0])
        sage: bentf1.algebraic_normal_form()
        x0*x1 + x1
        sage: name_prefix = 'test_save_classifications_in_parallel'
        sage: names = save_classifications_in_parallel(name_prefix, [bentf0,bentf1], ncpus=2)
        sage: mangled_name_prefix = BentFunctionCayleyGraphClassification.mangled_name(name_prefix)
        sage: mangled_fname_1 = mangled_name_prefix + '_1'
        sage: c = load(mangled_fname_1)
        sage: c.report()
        Algebraic normal form of Boolean function: x0*x1 + x1
        Function is bent.
        <BLANKLINE>
        <BLANKLINE>
        SDP design incidence structure t-design parameters: (True, (1, 4, 1, 1))
        <BLANKLINE>
        Classification of Cayley graphs and classification of Cayley graphs of duals are the same:
        <BLANKLINE>
        There are 2 extended Cayley classes in the extended translation class.
        sage: for n in range(2):
        ....:     mangled_fname = mangled_name_prefix + '_' + str(n) + '.sobj'
        ....:     print(mangled_fname)
        ....:     os.remove(mangled_fname)
        ....:
        BentFunctionCayleyGraphClassification__test_save_classifications_in_parallel_0.sobj
        BentFunctionCayleyGraphClassification__test_save_classifications_in_parallel_1.sobj
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
    Construct and save a partial Cayley graph classification
    corresponding to a given bent function.

    INPUT:

    - ``name`` -- Name to use with ``save_mangled`` to save the class part.
    - ``bentf`` -- A Bent function.
    - ``c_start`` -- smallest value of `c` to use for
        extended translates. Integer. Default is 0.
    - ``c_stop`` -- one more than largest value of `c`
        to use for extended translates. Integer.
        Default is ``None``, meaning use all remaining values.

    OUTPUT: A copy of the string ``name``.

    EFFECT: Uses ``name`` to save the partial classification corresponding to ``bentf``.

    EXAMPLE:

    ::

        sage: import os
        sage: from boolean_cayley_graphs.bent_function import BentFunction
        sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassPart
        sage: R2.<x1,x2> = BooleanPolynomialRing(2)
        sage: p = x1+x2+x1*x2
        sage: f = BentFunction(p)
        sage: from boolean_cayley_graphs.classify_in_parallel import save_one_class_part
        sage: name = 'test_save_one_class_part'
        sage: mangled_name = BentFunctionCayleyGraphClassPart.mangled_name(name)
        sage: s = save_one_class_part(name, f, c_start=1, c_stop=2)
        sage: p1=BentFunctionCayleyGraphClassPart.load_mangled(name)
        sage: p1.__dict__
        {'algebraic_normal_form': x0*x1 + x0 + x1,
        'bent_cayley_graph_index_matrix': [0 0 1 0],
        'c_start': 1,
        'cayley_graph_class_list': ['CK', 'C~'],
        'dual_cayley_graph_index_matrix': [0 0 1 0],
        'weight_class_matrix': [0 0 1 0]}
        sage: mangled_fname = mangled_name + '.sobj'
        sage: print(mangled_fname)
        BentFunctionCayleyGraphClassPart__test_save_one_class_part.sobj
        sage: os.remove(mangled_fname)
    """
    p = BentFunctionCayleyGraphClassPart.from_function(
        bentf,
        c_start=c_start,
        c_stop=c_stop)
    p.save_mangled(name)
    return name


def save_class_parts_in_parallel(
    name_prefix,
    form,
    c_len=1,
    ncpus=4):
    r"""
    In parallel, construct a complete list of the partial Cayley graph classifications
    corresponding to a given bent function or algebraic normal form.

    INPUT:

    - ``name_prefix`` -- String. Name prefix to use with ``save_mangled`` to save each class part.
    - ``form`` -- A bent function or an algebraic normal form.
    - ``c_len`` -- Integer. Default=1. The number of values of `c` to use in each class part.
    - ``ncpus`` -- Integer. Default=4. The number of cpus to use in parallel.

    OUTPUT: A list containing tuples, with names.

    EFFECT: Uses ``name_preix`` to save all partial classifications corresponding to ``bentf``.

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
        sage: name_prefix = 'test_save_class_parts_in_parallel'
        sage: mangled_name_prefix = BentFunctionCayleyGraphClassPart.mangled_name(name_prefix)
        sage: s = save_class_parts_in_parallel(name_prefix, f)
        sage: p1=BentFunctionCayleyGraphClassPart.load_mangled(name_prefix + '_1')
        sage: p1.__dict__
        {'algebraic_normal_form': x0*x1 + x0 + x1,
        'bent_cayley_graph_index_matrix': [0 0 1 0],
        'c_start': 1,
        'cayley_graph_class_list': ['CK', 'C~'],
        'dual_cayley_graph_index_matrix': [0 0 1 0],
        'weight_class_matrix': [0 0 1 0]}
        sage: for n in range(4):
        ....:     mangled_fname = mangled_name_prefix + '_' + str(n) + '.sobj'
        ....:     print(mangled_fname)
        ....:     os.remove(mangled_fname)
        ....:
        BentFunctionCayleyGraphClassPart__test_save_class_parts_in_parallel_0.sobj
        BentFunctionCayleyGraphClassPart__test_save_class_parts_in_parallel_1.sobj
        BentFunctionCayleyGraphClassPart__test_save_class_parts_in_parallel_2.sobj
        BentFunctionCayleyGraphClassPart__test_save_class_parts_in_parallel_3.sobj
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
