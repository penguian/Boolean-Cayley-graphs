# -*- coding: utf-8 -*-

r"""
Authorization interface to SQL database via Psycopg2.
For use with bent_function_cayley_graph_dashboard.py and similar.

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

import json
import psycopg2

import boolean_cayley_graphs.classification_database_psycopg2 as cdb


def authorized(db_function):
    def function_wrapper(function):
        def db_wrapper(dbname):
            with open("postgresql-auth.json") as auth_file:
                auth = json.load(auth_file)
            return db_function(
                dbname,
                user=auth["user"],
                password=auth["password"],
                host=auth["host"])
        return db_wrapper
    return function_wrapper


@authorized(cdb.create_database)
def create_database(dbname):
    pass


@authorized(cdb.connect_to_database)
def connect_to_database(dbname):
    pass


@authorized(cdb.drop_database)
def drop_database(dbname):
    pass


@authorized(cdb.create_classification_tables)
def create_classification_tables(dbname):
    pass


