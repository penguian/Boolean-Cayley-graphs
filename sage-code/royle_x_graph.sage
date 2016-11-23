
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************


def royle_x_graph():
    n = 8
    order = 64

    vecs = [vector([1]*n)]
    for a in Combinations(xrange(1,n),4):
        vecs.append(vector([-1 if x in a else 1
                               for x in xrange(n)]))
    for b in Combinations(xrange(n),2):
        vecs.append(vector([-1 if x in b else 1
                               for x in xrange(n)]))

    return Graph([(i,j) for i in sxrange(order)
                        for j in sxrange(i+1,order)
                        if vecs[i]*vecs[j] == 0])
