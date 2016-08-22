
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

load("boolean_cayley_graph.sage")
load("dillon_schatz_design_matrix.sage")

def dillon_schatz_incidence_structure(f):
    g = boolean_function_cayley_graph(f)
    G = IncidenceStructure(g.adjacency_matrix())
    D = dillon_schatz_design_matrix(f)
    I = IncidenceStructure(D)
    return G, D, I
