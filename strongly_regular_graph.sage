
class StronglyRegularGraph(Graph):
    """
    The class `StronglyRegularGraph` is used to store a strongly regular graph and some of its computed properties: its clique polynomial and its strongly regular graph parameters.
    """
    def __init__(self, graph=None):
        Graph.__init__(self, graph)
        self.clique_polynomial   = graph.clique_polynomial()
        self.strongly_regular_parameters = graph.is_strongly_regular(parameters=True)
        self.matrix_GF2 = matrix(GF(2),self)
        self.rank = self.matrix_GF2.rank()
        self.group = self.automorphism_group()
        self.group_order = self.group.order()
