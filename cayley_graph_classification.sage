load("boolean_function_cayley_graph_classification.sage")
load("strongly_regular_graph.sage")


def cayley_graph_classification(f):
    r"""
    """
    fcc = BooleanFunctionCayleyGraphClassification(f)
    srgs = [StronglyRegularGraph(g) for g in fcc.cayley_graph_class_list]
    return fcc, srgs


