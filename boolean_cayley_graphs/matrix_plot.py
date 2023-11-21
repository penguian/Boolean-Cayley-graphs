r"""
Convenience functions for plotting matrices
===========================================

The ``matrix_plot`` module defines some convenience functions that make
matrix plots of integer matrices more useful.

AUTHORS:

- Paul Leopardi (2023-11-20): initial version

"""
#*****************************************************************************
#       Copyright (C) 2023 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.plot.matrix_plot import matrix_plot

def matrix_plot_with_colorbar(mat, xrange=None, yrange=None, **options):
    r"""
    Plot a matrix with a colorbar that sensibly depends on the matrix
    minimum and maximum values.

    EXAMPLE:

    ::
        sage: from boolean_cayley_graphs.matrix_plot import matrix_plot_with_colorbar
        sage: mat = Matrix([[1, 2], [3, 4]])
        sage: matrix_plot_with_colorbar(mat, cmap='bone')
        Graphics object consisting of 1 graphics primitive
    """
    try:
        matmin = int(mat.min())
        matmax = int(mat.max())
    except AttributeError:
        matmin = int(mat.numpy().min())
        matmax = int(mat.numpy().max())

    ncolors = matmax + 1
    if matmax-matmin < 10:
        return matrix_plot(
            mat,
            xrange=xrange,
            yrange=yrange,
            colorbar=True,
            colorbar_options={'ticks': range(ncolors)},
            **options)
    else:
        return matrix_plot(
            mat,
            xrange=xrange,
            yrange=yrange,
            colorbar=True,
            **options)
