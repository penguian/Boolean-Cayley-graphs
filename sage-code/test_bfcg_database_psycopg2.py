r"""
Check the bent function Cayley graph databases.
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

def check_bfcg_database(auth, dbname, nbr_f):
    
    print(dbname, ":")
    conn = connect_to_database(
        dbname,
        user=auth["user"],
        password=auth["password"],
        host=auth["host"])

    for i in range(1, nbr_f + 1):
        stri = ("%01d" if nbr_f < 10 else "%02d") % i 
        name = dbname + "_" + stri
        print(datetime.datetime.now(), stri)
        cgc_check = select_classification_where_name(
            conn,
            name)
        cgc_check.report()

    conn.close()
    print(datetime.datetime.now())


with open("postgresql-auth.json") as auth_file:
    auth = json.load(auth_file)

check_bfcg_database(auth, "p2", 1)
check_bfcg_database(auth, "p4", 1)
check_bfcg_database(auth, "p6", 4)
check_bfcg_database(auth, "p8", 10)
check_bfcg_database(auth, "sigma", 4)
check_bfcg_database(auth, "tau", 4)

