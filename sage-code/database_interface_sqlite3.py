# -*- coding: utf-8 -*-

r"""
Interface to SQL database via SQLite3, for use with
bent_function_cayley_graph_dashboard.py and similar.

AUTHORS:

- Paul Leopardi (2018-10-18): initial version

"""

#*****************************************************************************
#       Copyright (C) 2018 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

import sqlite3

import boolean_cayley_graphs.classification_database_sqlite3 as cdb


auth = None


def connect_to_database(
    selected_database,
    auth):
    conn = cdb.connect_to_database(
        selected_database + '.db')
    return conn



