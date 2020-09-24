
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

gap.load_package('grape')
gap.eval('GRAPE_NAUTY := true;')

def graphs_are_isomorphic(g_0, g_1):
    r"""
    Check that two graphs are isomorphic.
    """
    m_0 = g_0.adjacency_matrix()
    m_1 = g_1.adjacency_matrix()
    dim = str(m_0.dimensions()[0])
    gap.eval('M_0 := '+gap(m_0).str()+';')
    gap.eval('M_1 := '+gap(m_1).str()+';')
    gap.eval('GR := Group( () );')
    gap.eval('G_0 := Graph( GR, [1..' + dim +'], OnPoints, '
        + 'function(x,y) return M_0[x][y] = 1; end, true );')
    gap.eval('G_1 := Graph( GR, [1..' + dim + '], OnPoints, '
        + 'function(x,y) return M_1[x][y] = 1; end, true );')
    return gap.eval('IsIsomorphicGraph(G_0, G_1);') == 'true'


def check_graph_class_list(g_list):
    r"""
    Check that no two graphs in a list are isomorphic.
    """
    result = True
    n = len(g_list)
    for i in range(n):
        for j in range(i + 1, n):
            result &= not graphs_are_isomorphic(g_list[i], g_list[j])
    return result
