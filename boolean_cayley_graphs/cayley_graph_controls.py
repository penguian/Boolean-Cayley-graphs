r"""
The ``cayley_graph_controls`` module defines controls for checking, timing and tracing
that can be set and used anywhere they are imported.

AUTHORS:

- Paul Leopardi (2016-08-21): initial version

"""
#*****************************************************************************
#       Copyright (C) 2016-2017 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************


checking = False
r"""
Enable built-in diagnostic tests that may be time consuming.

EXAMPLE:

::

    sage: import boolean_cayley_graphs.cayley_graph_controls as controls
    sage: controls.checking = True
    sage: if controls.checking:
    ....:     print("Checking!")
    ....:
    Checking!
"""


timing   = False
r"""
Enable timers.

EXAMPLE:

::

    sage: import boolean_cayley_graphs.cayley_graph_controls as controls
    sage: controls.timing = True
    sage: if controls.timing:
    ....:     print("Timing!")
    ....:
    Timing!
"""


verbose  = False
r"""
Increase verbosity: print extra details.

EXAMPLE:

::

    sage: import boolean_cayley_graphs.cayley_graph_controls as controls
    sage: controls.verbose = True
    sage: if controls.verbose:
    ....:     print("This message is verbose.")
    ....:
    This message is verbose.
"""
