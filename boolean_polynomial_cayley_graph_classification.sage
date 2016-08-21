from sage.crypto.boolean_function import BooleanFunction

load("dillon_schatz_incidence_structure.sage")

load("cayley_graph_classification.sage")

load("walsh_hadamard_dual.sage")

from sage.rings.polynomial.pbori import BooleanPolynomial


class BooleanPolynomialCayleyGraphClassification(SageObject):

    def __init__(self, p):
        if not 'cayley_graph_debugging' in globals():
            debugging = False
        else:
            debugging = cayley_graph_debugging

        self.boolean_polynomial = p
        if debugging:
            print "Boolean polynomial:   ", p

        f = BooleanFunction(p)
        self.boolean_function = f

        n = f.algebraic_normal_form()
        self.algebraic_normal_form = n
        if debugging:
            print "Algebraic normal form:", n
            print "Function", ("is" if f.is_bent() else "is not"), "bent."

        dual_f = walsh_hadamard_dual(f)
        self.dual_function = dual_f
        if debugging:
            print "Dual", ("is" if dual_f.is_bent() else "is not"), "bent."

        G, D, I = dillon_schatz_incidence_structure(f)
        self.cayley_incidence_structure = G
        self.dillon_schatz_design_matrix = D
        self.dillon_schatz_incidence_structure = I
        if debugging:
            print "Dillon Schatz design",
            print ("is" if I.is_isomorphic(G) else "is not"),
            print "isomorphic to Cayley graph incidence structure."
            print "Incidence structure t-design parameters:",
            print I.is_t_design(return_parameters=True)

        fcc, srgs = cayley_graph_classification(f)
        self.cayley_graph_class_list = srgs
        self.cayley_graph_index_matrix = fcc.cayley_graph_index_matrix
        if debugging:
            print "Strongly regular parameters, rank, order"
            print "and clique polynomial"
            print "of each representative Cayley graph"
            print "in the extended affine class:"
            for s in srgs:
                print s.strongly_regular_parameters,
                print s.rank, s.group_order, s.clique_polynomial

    def mangled_name(self, name):
        return self.__class__.__name__ + "__" + name


def save_cayley_graph_classification(p, name):
    c = BooleanPolynomialCayleyGraphClassification(p)
    save(c, c.mangled_name(name))
    return c


def load_cayley_graph_classification(p, name):
    mangled_name = "BooleanPolynomialCayleyGraphClassification" + "__" + name
    load(mangled_name, c)
    return c
