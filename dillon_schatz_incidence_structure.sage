load("boolean_cayley_graph.sage")
load("dillon_schatz_design_matrix.sage")

def dillon_schatz_incidence_structure(f):
    g = boolean_function_cayley_graph(f)
    G = IncidenceStructure(g.adjacency_matrix())
    D = dillon_schatz_design_matrix(f)
    I = IncidenceStructure(D)
    return G, D, I
