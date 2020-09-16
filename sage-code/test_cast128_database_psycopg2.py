r"""
Check the cast128 database.
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

print "Checking the Cayley graph classifications of bent functions from the CAST-128 S-boxes."

with open("postgresql-auth.json") as auth_file:
    auth = json.load(auth_file)

conn = connect_to_database(
    "cast128",
    user=auth["user"],
    password=auth["password"],
    host=auth["host"])

curs = conn.cursor()
print datetime.datetime.now(), "before"
curs.execute("SELECT COUNT(*) FROM cayley_graph")
print datetime.datetime.now(), "after"
print "Number of Cayley graphs of bent functions:"
for row in curs:
    for x in row:
        print x

print datetime.datetime.now(), "before"
curs.execute("SELECT COUNT(*) FROM graph")
print datetime.datetime.now(), "after"
print "Number of non-isomorphic graphs:"
for row in curs:
    for x in row:
        print x

print "Checking cast128_8_31 by name in database:"
cgc1 = select_classification_where_name(
    conn,
    "cast128_8_31")
cgc1.report()

cgc2 = BentFunctionCayleyGraphClassification.load_mangled(
    "cast128_8_31",
    directory="/data/sobj")
bentf = BentFunction(cgc2.algebraic_normal_form)

print "Checking cast128_8_31 by bent function in database:"
cgc3 = select_classification_where_bent_function(
    conn,
    bentf)
cgc3.report()

print ""
print "Checking for graphs occuring as the Cayley graph of more than 1 bent function."
curs = conn.cursor()
print datetime.datetime.now(), "before"
curs.execute("""
select name, cayley_graph_index, graph_id, count(*)
from matrices, (
    select name, bent_function, cayley_graph_index, graph_id
    from (
        select graph_id
        from cayley_graph
        group by graph_id
        having count (graph_id) > 1 ) as repeats
    natural join cayley_graph
    natural join bent_function )
as repeats_with_counts
where matrices.bent_function = repeats_with_counts.bent_function
and matrices.bent_cayley_graph_index = repeats_with_counts.cayley_graph_index
group by name, cayley_graph_index, graph_id
order by graph_id
""")
print datetime.datetime.now(), "after"
print "Repeated graphs:"
for row in curs:
    for x in row:
        print x,
    print ""

conn.close()

