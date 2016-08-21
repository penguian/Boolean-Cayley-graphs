"""


Paul Leopardi.
"""

class IsomorphismClass(SageObject):
    def __eq__(self,rhs):
        return self.is_isomorphic(rhs)

