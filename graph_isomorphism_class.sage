"""


Paul Leopardi.
"""

#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

class GraphIsomorphismClass(Graph):
    def __eq__(self,rhs):
        if self.automorphism_group().order() != rhs.automorphism_group().order():
            return False
        else:
            return self.is_isomorphic(rhs)
