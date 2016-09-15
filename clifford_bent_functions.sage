"""
Bent functions related to amicability relationships in the real representations of Clifford algebras.

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

from sage.crypto.boolean_function import BooleanFunction

base4 = lambda length, num: num.digits(4, padto=length)


def sigma_tau(which, m, x):
    r"""
    Given the numbers `which`, $m$ and $x$,
    `sigma_tau(0,m,x)` returns $\sigma_m(x)$, and
    `sigma_tau(1,m,x)` returns $\tau_m(x)$,
    where $\sigma_m$ and $\tau_m$ are
    two specific bent functions with disjoint support,
    defined via the properties of real monomial representation matrices
    of real Clifford algebras.
    """
    xbase4 = base4(m, x)
    nbr1 = xbase4.count(1)
    nbr2 = xbase4.count(2)
    return 0 if nbr1 + nbr2 == 0 else (nbr1 + which) % 2


clifford_sign_of_square_sigma  = lambda m, x: sigma_tau(0, m, x)
clifford_non_diag_symmetry_tau = lambda m, x: sigma_tau(1, m, x)


power_4_truth_table = lambda m, f: [
    f(m, x)
    for x in sxrange(4 ** m)]


sigma_list = lambda n: [
    BooleanFunction(power_4_truth_table(m, clifford_sign_of_square_sigma))
    for m in sxrange(n)]
r"""
The list `sigma_list(n)` contains each `BooleanFunction`
corresponding to $\sigma_m$ for $m$ from 0 to n-1.
"""


tau_list = lambda n: [
    BooleanFunction(power_4_truth_table(m, clifford_non_diag_symmetry_tau))
    for m in sxrange(n)]
r"""
The list `tau_list(n)` contains each `BooleanFunction`
corresponding to $\tau_m$ for $m$ from 0 to n-1.
"""
