
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.crypto.boolean_function import BooleanFunction

load("boolean_cayley_graph.sage")


def check_bent_isomorphism(dim, k, certify=False):
    r"""
    Given the non-negative numbers $dim$ and $k$, `check_bent_isomorphism`
    checks that all of the bent functions whose truth table has $k$ bits
    set out of the $2^{dim}-1$ non-zero bits, have isomorphic Cayley graphs.
    It does so by enumerating all combinations `a` with $k$ non-zero bits set,
    testing if `a` yields a bent function, then testing the resulting
    Cayley graph for isomorphism to the first graph so obtained.

    If a non isomorphic Cayley graph is found, `check_bent_isomorphism` prints
    the combination `a`, and returns the number of bent functions found so far.
    Otherwise `check_bent_isomorphism` just returns the total number of
    bent functions found.

    The optional parameter `certify`, which defaults to `False`, prints
    the truth table `v` and Cayley graph isomorphism `iso` corresponding
    to each bent function.
    """
    v = 2 ** dim
    nbent = 0
    for a in Combinations(xrange(1, v), k):
        t = [1 if x in a else 0 for x in xrange(v)]
        f = BooleanFunction(t)
        f_is_bent = f.is_bent()
        if f_is_bent:
            nbent += 1
            g = boolean_function_cayley_graph(f)
            if nbent == 1:
                g0 = g
                print g.is_strongly_regular(parameters=True)
                if certify:
                    print t
            else:
                if certify:
                    g_is_iso, iso = g.is_isomorphic(g0, certify=True)
                else:
                    g_is_iso = g.is_isomorphic(g0)
                if not g_is_iso:
                    print a
                    return nbent
                elif certify:
                    print t, iso
    return nbent
