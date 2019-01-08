r"""
Populate the bent function Cayley graphs databases.
"""

#*****************************************************************************
#       Copyright (C) 2018 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

import datetime
import json
import psycopg2

from boolean_cayley_graphs.bent_function import BentFunction
from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
from boolean_cayley_graphs.classification_database_psycopg2 import *

def populate_bfcg_database(dbname, nbr_f):
    
    print dbname, ":"
    conn = create_classification_tables(
        dbname,
        user=auth["user"],
        password=auth["password"],
        host=auth["host"])

    for i in range(1, nbr_f + 1):
        stri = ("%01d" if nbr_f < 10 else "%02d") % i 
        sobj_name = dbname + "_" + str(i) + ".sobj"
        name = dbname + "_" + stri
        cgc = BentFunctionCayleyGraphClassification.load_mangled(
            sobj_name,
            directory="./sobj")
        print datetime.datetime.now(), stri
        insert_classification(
            conn, 
            cgc, 
            name)
        cgc_check = select_classification_where_name(
            conn,
            name)
        cgc_check.report()

    conn.close()
    print datetime.datetime.now()


with open("postgresql-auth.json") as auth_file:
    auth = json.load(auth_file)

populate_bfcg_database("p2", 1)
populate_bfcg_database("p4", 1)
populate_bfcg_database("p6", 4)
populate_bfcg_database("p8", 10)
populate_bfcg_database("sigma", 4)
populate_bfcg_database("tau", 4)

