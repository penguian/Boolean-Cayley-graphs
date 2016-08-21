"""


Paul Leopardi.
"""

class GraphIsomorphismClass(Graph):
    def __eq__(self,rhs):
        if self.automorphism_group().order() != rhs.automorphism_group().order():
            return False
        else:
            return self.is_isomorphic(rhs)
