r"""
Utilities to manipulate an sqlite3 database of Cayley graph classifications.

AUTHORS:

- Paul Leopardi (2017-10-28)

"""
#*****************************************************************************
#       Copyright (C) 2017-2018 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************


import hashlib
import sqlite3

from sage.arith.srange import xsrange
from sage.matrix.constructor import matrix

from boolean_cayley_graphs.bent_function import BentFunction
from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
from boolean_cayley_graphs.weight_class import weight_class


def create_database(db_name):
    """
    Create a database.

    INPUT:

    - ``db_name`` -- string. The name of the database to be created.

    OUTPUT: a database connection object.
    """
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    return conn


def connect_to_database(db_name):
    """
    Connect to an existing database.

    INPUT:

    - ``db_name`` -- string. The name of the existing database.

    OUTPUT: a database connection object.
    """
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    return conn


def create_classification_tables(db_name):
    """
    Create the tables used for a database of Cayley graph classifications.

    INPUT:

    - ``db_name`` -- string. The name of an existing database.

    OUTPUT: a database connection object.
    """
    conn = connect_to_database(db_name)
    curs = conn.cursor()

    curs.execute("""
        CREATE TABLE bent_function(
        bent_function BLOB,
        name TEXT UNIQUE,
        PRIMARY KEY(bent_function))""")
    curs.execute("""
        CREATE TABLE graph(
        graph_id INTEGER,
        canonical_label_hash BLOB UNIQUE,
        canonical_label TEXT,
        PRIMARY KEY(graph_id))""")
    curs.execute("""
        CREATE TABLE cayley_graph(
        bent_function BLOB,
        cayley_graph_index INTEGER,
        graph_id INTEGER,
        FOREIGN KEY(bent_function)
            REFERENCES bent_function(bent_function),
        FOREIGN KEY(graph_id)
            REFERENCES graph(graph_id),
        PRIMARY KEY(bent_function, cayley_graph_index))""")
    curs.execute("""
        CREATE TABLE matrices(
        bent_function BLOB,
        b INTEGER,
        c INTEGER,
        bent_cayley_graph_index INTEGER,
        dual_cayley_graph_index INTEGER,
        weight_class INTEGER,
        FOREIGN KEY(bent_function)
            REFERENCES bent_function(bent_function),
        FOREIGN KEY(bent_function, bent_cayley_graph_index)
            REFERENCES cayley_graph(bent_function, cayley_graph_index),
        FOREIGN KEY(bent_function, dual_cayley_graph_index)
            REFERENCES cayley_graph(bent_function, cayley_graph_index),
        PRIMARY KEY(bent_function, b, c))""")
    conn.commit()
    return conn


def insert_classification(
    conn,
    bfcgc,
    name=None):
    """
    Insert a Cayley graph classification into a database.

    INPUT:

    - ``conn`` -- a connection object for the database.

    - ``bfcgc`` -- class BentFunctionCayleyGraphClassification. A Cayley graph classification.

    - ``name`` -- string (default: `None`). The name of the bent function.

    OUTPUT: a cursor object corresponding to the inserted classification.
    """
    bentf = BentFunction(bfcgc.algebraic_normal_form)
    dim = bentf.nvariables()
    v = 2 ** dim
    bftt = bentf.tt_buffer()
    cgcl = bfcgc.cayley_graph_class_list
    bcim = bfcgc.bent_cayley_graph_index_matrix
    dcim = bfcgc.dual_cayley_graph_index_matrix
    wcm  = bfcgc.weight_class_matrix

    curs = conn.cursor()
    curs.execute("""
        INSERT INTO bent_function
        VALUES (?,?)""",
        (bftt, name))
    for n in range(len(cgcl)):
        cgc = cgcl[n]
        cgc_hash = buffer(hashlib.sha256(cgc).digest())
        curs.execute("""
            INSERT OR IGNORE INTO graph
            VALUES (?,?,?)""",
            (None, cgc_hash, cgc))

        curs.execute("""
            SELECT graph_id
            FROM graph
            WHERE canonical_label_hash = (?)""",
            (cgc_hash,))

        row = curs.fetchone()
        graph_id = row["graph_id"]

        curs.execute("""
            INSERT INTO cayley_graph
            VALUES (?,?,?)""",
            (bftt, n, graph_id))

    for b in range(v):
        matrices_b_rows = (
            (bftt, b, c, int(bcim[c,b]), int(dcim[c,b]), int(wcm[c,b]))
            for c in range(v))
        curs.executemany("""
            INSERT INTO matrices
            VALUES (?,?,?,?,?,?)""",
            matrices_b_rows)

    conn.commit()
    return curs


def select_classification_where_bent_function(
    conn,
    bentf):
    """
    Retrieve a Cayley graph classification for a given bent function from a database.

    INPUT:

    - ``conn`` -- a connection object for the database.

    - ``bentf`` -- class BentFunction. A bent function.

    OUTPUT: class BentFunctionCayleyGraphClassification.
    The corresponding a Cayley graph classification.
    """
    dim = bentf.nvariables()
    v = 2 ** dim
    bftt = (bentf.tt_buffer(),)

    curs = conn.cursor()
    curs.execute("""
        SELECT COUNT(*)
        FROM cayley_graph
        WHERE bent_function = (?)""",
        bftt)
    row = curs.fetchone()
    if row == None:
        return None

    cgcl_len = row[0]
    cgcl = [None] * cgcl_len
    curs.execute("""
        SELECT cayley_graph_index, canonical_label
        FROM cayley_graph, graph
        WHERE bent_function = (?)
        AND cayley_graph.graph_id = graph.graph_id""",
        bftt)
    for row in curs:
        cayley_graph_index = row["cayley_graph_index"]
        canonical_label = row["canonical_label"]
        cgcl[cayley_graph_index] = str(canonical_label)

    bcim = matrix(v, v)
    dcim = matrix(v, v)
    wcm  = matrix(v, v)
    curs.execute("""
        SELECT *
        FROM matrices
        WHERE bent_function = (?)""",
        bftt)
    for row in curs:
        b = row["b"]
        c = row["c"]

        bent_cayley_graph_index = row["bent_cayley_graph_index"]
        bcim[c, b] = bent_cayley_graph_index

        dual_cayley_graph_index = row["dual_cayley_graph_index"]
        dcim[c, b] = dual_cayley_graph_index

        weight_class = row["weight_class"]
        wcm[c, b] = weight_class

    return BentFunctionCayleyGraphClassification(
        algebraic_normal_form=bentf.algebraic_normal_form(),
        cayley_graph_class_list=cgcl,
        bent_cayley_graph_index_matrix=bcim,
        dual_cayley_graph_index_matrix=dcim,
        weight_class_matrix=wcm)


def select_classification_where_name(
    conn,
    name):
    """
    Retrieve a Cayley graph classification for a bent function with a given name from a database.

    INPUT:

    - ``conn`` -- a connection object for the database.

    - ``name`` -- string. The name of the bent function.

    OUTPUT: class BentFunctionCayleyGraphClassification.
    The corresponding a Cayley graph classification.
    """
    curs = conn.cursor()
    curs.execute("""
        SELECT bent_function
        FROM bent_function
        WHERE name = (?)""",
        (name,))
    row = curs.fetchone()
    if row == None:
        return None

    bftt = row["bent_function"]
    bentf = BentFunction.from_tt_buffer(bftt)

    return select_classification_where_bent_function(
        conn,
        bentf)
