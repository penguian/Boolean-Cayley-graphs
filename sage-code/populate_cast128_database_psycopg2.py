r"""
Populate the cast128 database.
"""

#*****************************************************************************
#       Copyright (C) 2017 Paul Leopardi paul.leopardi@gmail.com
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

with open("BCG-DB.json") as auth_file:
    auth = json.load(auth_file)

conn = create_classification_tables(
    "cast128",
    user=auth["user"],
    password=auth["passwd"],
    host=auth["host"])

for i in range(1,9):
    stri = "%01d" % i
    for j in range(32):
        strj = "%02d" % j
        sobj_name = "cast128_" + stri + "_" + str(j) + ".sobj"
        name = "cast128_" + stri + "_" + strj
        cgc = BentFunctionCayleyGraphClassification.load_mangled(
            sobj_name,
            directory="/data/sobj")
        print datetime.datetime.now(), stri, strj
        insert_classification(conn, cgc, name)
print datetime.datetime.now()

curs = conn.cursor()
print datetime.datetime.now(), "before"
curs.execute("SELECT COUNT(*) FROM cayley_graph")
print datetime.datetime.now(), "after"
for row in curs:
    for x in row:
        print x

print datetime.datetime.now(), "before"
curs.execute("SELECT COUNT(*) FROM graph")
print datetime.datetime.now(), "after"
for row in curs:
    for x in row:
        print x

cgc1 = select_classification_where_name(
    conn,
    "cast128_1_09")
cgc1.report()

cgc2 = BentFunctionCayleyGraphClassification.load_mangled(
    "cast128_1_9",
    directory="/data/sobj")
bentf = BentFunction(cgc.algebraic_normal_form)

cgc3 = select_classification_where_bent_function(
    conn,
    bentf)
cgc3.report()

conn.close()

