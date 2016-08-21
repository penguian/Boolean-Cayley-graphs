"""
List with added index_append method.

Paul Leopardi.
"""

class IndexAppendList(list):
    """
    Subclass of list with an added index_append method.
    """
    def index_append(self,item):
        """
        If the usual list index method for self yields a ValueError,
        the append item to self.
        """
        try:
            result = self.index(item)
        except ValueError:
            result = len(self)
            self.append(item)
        return result
