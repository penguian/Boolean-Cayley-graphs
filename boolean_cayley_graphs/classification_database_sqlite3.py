r"""
The ``classification_databasepsqlite3`` module defines interfaces
to manipulate an SQLite3 database of Cayley graph classifications.

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
import os
import sqlite3

from exceptions import OSError
from sage.arith.srange import xsrange
from sage.matrix.constructor import matrix

from boolean_cayley_graphs.bent_function import BentFunction
from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification, default_algorithm
from boolean_cayley_graphs.weight_class import weight_class


def create_database(db_name):
    """
    Create a database.

    INPUT:

    - ``db_name`` -- string. The name of the database to be created.

    OUTPUT: a database connection object.

    EXAMPLE:

    Create a database using a temporary filename, then drop the database.

    ::

        sage: from sage.misc.temporary_file import tmp_filename
        sage: db_name = tmp_filename(ext='.db')
        sage: from boolean_cayley_graphs.classification_database_sqlite3 import *
        sage: conn = create_database(db_name)
        sage: type(conn)
        <type 'sqlite3.Connection'>
        sage: drop_database(db_name)
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

    EXAMPLE:

    Create a database using a temporary filename, connect to it,
    then drop the database.

    ::

        sage: from sage.misc.temporary_file import tmp_filename
        sage: db_name = tmp_filename(ext='.db')
        sage: from boolean_cayley_graphs.classification_database_sqlite3 import *
        sage: conn = create_database(db_name)
        sage: con2 = connect_to_database(db_name)
        sage: type(con2)
        <type 'sqlite3.Connection'>
        sage: drop_database(db_name)
    """
    if os.path.isfile(db_name):
        conn = sqlite3.connect(db_name)
        conn.row_factory = sqlite3.Row
        return conn
    else:
        raise IOError("File not found: {}".format(db_name))

def drop_database(db_name):
    """
    Drop a database, if it exists.

    INPUT:

    - ``db_name`` -- string. The name of the existing database.

    OUTPUT: None.

    EXAMPLE:

    Create a database using a temporary filename, then drop the database.

    ::

        sage: from boolean_cayley_graphs.classification_database_sqlite3 import *
        sage: import os
        sage: db_name = tmp_filename(ext='.db')
        sage: conn = create_database(db_name)
        sage: os.path.exists(db_name)
        True
        sage: drop_database(db_name)
        sage: os.path.exists(db_name)
        False
        sage: drop_database(db_name)
        sage: os.path.exists(db_name)
        False
    """
    if os.path.exists(db_name):
        try:
            os.remove(db_name)
        except OSError:
            pass


def create_classification_tables(db_name):
    """
    Create the tables used for a database of Cayley graph classifications.

    INPUT:

    - ``db_name`` -- string. The name of an existing database.

    OUTPUT: a database connection object.

    EXAMPLE:

    Create a database, with tables, using a temporary filename,
    list the table names, then drop the database.

    ::

        sage: from boolean_cayley_graphs.classification_database_sqlite3 import *
        sage: import os
        sage: db_name = tmp_filename(ext='.db')
        sage: conn = create_database(db_name)
        sage: conn.close()
        sage: conn = create_classification_tables(db_name)
        sage: os.path.exists(db_name)
        True
        sage: curs = conn.cursor()
        sage: result = curs.execute("SELECT name FROM sqlite_master WHERE type='table'")
        sage: for row in curs:
        ....:     for x in row:
        ....:         print(x)
        ....:
        bent_function
        graph
        cayley_graph
        matrices
        sage: conn.close()
        sage: drop_database(db_name)
    """
    conn = connect_to_database(db_name)
    curs = conn.cursor()

    curs.execute("""
        CREATE TABLE bent_function(
        nvariables INTEGER,
        bent_function BLOB,
        name TEXT UNIQUE,
        PRIMARY KEY(nvariables, bent_function))""")
    curs.execute("""
        CREATE TABLE graph(
        graph_id INTEGER,
        canonical_label_hash BLOB UNIQUE,
        canonical_label TEXT,
        PRIMARY KEY(graph_id))""")
    curs.execute("""
        CREATE TABLE cayley_graph(
        nvariables INTEGER,
        bent_function BLOB,
        cayley_graph_index INTEGER,
        graph_id INTEGER,
        FOREIGN KEY(nvariables, bent_function)
            REFERENCES bent_function(nvariables, bent_function),
        FOREIGN KEY(graph_id)
            REFERENCES graph(graph_id),
        PRIMARY KEY(bent_function, cayley_graph_index))""")
    curs.execute("""
        CREATE TABLE matrices(
        nvariables INTEGER,
        bent_function BLOB,
        b INTEGER,
        c INTEGER,
        bent_cayley_graph_index INTEGER,
        dual_cayley_graph_index INTEGER,
        weight_class INTEGER,
        FOREIGN KEY(nvariables, bent_function)
            REFERENCES bent_function(nvariables, bent_function),
        FOREIGN KEY(bent_function, bent_cayley_graph_index)
            REFERENCES cayley_graph(bent_function, cayley_graph_index),
        FOREIGN KEY(bent_function, dual_cayley_graph_index)
            REFERENCES cayley_graph(bent_function, cayley_graph_index),
        PRIMARY KEY(bent_function, b, c))""")
    conn.commit()
    return conn


canonical_label_hash = lambda g: buffer(hashlib.sha256(g).digest())


def insert_classification(
    conn,
    bfcgc,
    name=None):
    """
    Insert a Cayley graph classification into a database.

    INPUT:

    - ``conn`` -- a connection object for the database.
    - ``bfcgc`` -- a Cayley graph classification.
    - ``name`` -- string (default: `None`). The name of the bent function.

    OUTPUT: None.

    A cursor object corresponding to state of the database after the
    classification is inserted.

    EXAMPLE:

    Create a database, with tables, using a temporary filename, insert
    a classification, retrieve it by bent function, then drop the database.

    ::

        sage: from boolean_cayley_graphs.classification_database_sqlite3 import *
        sage: from boolean_cayley_graphs.bent_function import BentFunction
        sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
        sage: bentf = BentFunction([0,0,0,1])
        sage: bfcgc = BentFunctionCayleyGraphClassification.from_function(bentf)
        sage: bfcgc.algebraic_normal_form
        x0*x1
        sage: db_name = tmp_filename(ext='.db')
        sage: conn = create_classification_tables(db_name)
        sage: insert_classification(conn, bfcgc, 'bentf')
        sage: result = select_classification_where_bent_function(conn, bentf)
        sage: result.algebraic_normal_form
        x0*x1
        sage: drop_database(db_name)
    """
    bentf = BentFunction(bfcgc.algebraic_normal_form)
    dim = bentf.nvariables()
    nvar = int(dim)
    bftt = bentf.tt_buffer()
    cgcl = bfcgc.cayley_graph_class_list
    bcim = bfcgc.bent_cayley_graph_index_matrix
    dcim = bfcgc.dual_cayley_graph_index_matrix
    wcm  = bfcgc.weight_class_matrix

    curs = conn.cursor()
    curs.execute("""
        INSERT INTO bent_function
        VALUES (?,?,?)""",
        (nvar, bftt, name))
    for n in range(len(cgcl)):
        cgc = cgcl[n]
        cgc_hash = canonical_label_hash(cgc)
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
            VALUES (?,?,?,?)""",
            (nvar, bftt, n, graph_id))

    v = 2 ** dim
    for b in range(v):
        matrices_b_rows = (
            (
                nvar,
                bftt,
                b,
                c,
                int(bcim[c,b]),
                int(dcim[c,b]),
                int(wcm[c,b]))
            for c in range(v))
        curs.executemany("""
            INSERT INTO matrices
            VALUES (?,?,?,?,?,?,?)""",
            matrices_b_rows)
    conn.commit()


def select_classification_where_bent_function(
    conn,
    bentf):
    """
    Retrieve a Cayley graph classification for a given bent function from a database.

    INPUT:

    - ``conn`` -- a connection object for the database.
    - ``bentf`` -- class BentFunction. A bent function.

    OUTPUT:

    class BentFunctionCayleyGraphClassification.
    The corresponding Cayley graph classification.

    EXAMPLE:

    Create a database, with tables, using a temporary filename, insert
    a classification, retrieve it by bent function, then drop the database.

    ::

        sage: from boolean_cayley_graphs.classification_database_sqlite3 import *
        sage: from boolean_cayley_graphs.bent_function import BentFunction
        sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
        sage: bentf = BentFunction([0,0,0,1])
        sage: bfcgc = BentFunctionCayleyGraphClassification.from_function(bentf)
        sage: bfcgc.algebraic_normal_form
        x0*x1
        sage: db_name = tmp_filename(ext='.db')
        sage: conn = create_classification_tables(db_name)
        sage: insert_classification(conn, bfcgc, 'bentf')
        sage: result = select_classification_where_bent_function(conn, bentf)
        sage: result.algebraic_normal_form
        x0*x1
        sage: type(result)
        <class 'boolean_cayley_graphs.bent_function_cayley_graph_classification.BentFunctionCayleyGraphClassification'>
        sage: result.report(report_on_matrix_details=True)
        Algebraic normal form of Boolean function: x0*x1
        Function is bent.
        <BLANKLINE>
        Weight class matrix:
        [0 0 0 1]
        [0 1 0 0]
        [0 0 1 0]
        [1 0 0 0]
        <BLANKLINE>
        SDP design incidence structure t-design parameters: (True, (1, 4, 1, 1))
        <BLANKLINE>
        Classification of Cayley graphs and classification of Cayley graphs of duals are the same:
        <BLANKLINE>
        There are 2 extended Cayley classes in the extended translation class.
        <BLANKLINE>
        Matrix of indices of Cayley graphs:
        [0 0 0 1]
        [0 1 0 0]
        [0 0 1 0]
        [1 0 0 0]
        sage: drop_database(db_name)
    """
    dim = bentf.nvariables()
    nvar = int(dim)
    bftt = bentf.tt_buffer()
    curs = conn.cursor()
    curs.execute("""
        SELECT COUNT(*)
        FROM cayley_graph
        WHERE nvariables = (?)
        AND bent_function = (?)""",
        (nvar, bftt))
    row = curs.fetchone()
    if row == None:
        return None

    cgcl_len = row[0]
    cgcl = [None] * cgcl_len
    curs.execute("""
        SELECT cayley_graph_index, canonical_label
        FROM cayley_graph, graph
        WHERE nvariables = (?)
        AND bent_function = (?)
        AND cayley_graph.graph_id = graph.graph_id""",
        (nvar, bftt))
    for row in curs:
        cayley_graph_index = row["cayley_graph_index"]
        canonical_label = row["canonical_label"]
        cgcl[cayley_graph_index] = str(canonical_label)

    v = 2 ** dim
    bcim = matrix(v, v)
    dcim = matrix(v, v)
    wcm  = matrix(v, v)
    curs.execute("""
        SELECT *
        FROM matrices
        WHERE nvariables = (?)
        AND bent_function = (?)""",
        (nvar, bftt))
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


def select_classification_where_bent_function_cayley_graph(
    conn,
    bentf,
    algorithm=default_algorithm):    
    """
    Given a bent function ``bentf``, retrieve all classifications that
    contain a Cayley graph isomorphic to the Cayley graph of ``bentf``.

    INPUT:

    - ``conn`` -- a connection object for the database.
    - ``bentf`` -- class BentFunction. A bent function.
    - ``algorithm`` -- string (default: BentFunctionCayleyGraphClassification.default_algorithm). 
      Algorithm used for canonical labelling.

    OUTPUT:

    A list where each entry has class BentFunctionCayleyGraphClassification.
    The corresponding list of Cayley graph classifications.

    NOTE:

    ::

        The list is not sorted in any way.

    EXAMPLE:

    Create a database, with tables, using a temporary filename, insert
    a classification, retrieve it by bent function Cayley graph, then drop the database.

    ::

        sage: from boolean_cayley_graphs.classification_database_sqlite3 import *
        sage: from boolean_cayley_graphs.bent_function import BentFunction
        sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
        sage: db_name = 'doctest_select_classification_where_bent_function_db_name'
        sage: drop_database(db_name)
        sage: conn = create_database(db_name)
        sage: conn.close()
        sage: conn = create_classification_tables(db_name)
        sage: bentf0 = BentFunction([0,0,0,1])
        sage: bfcgc0 = BentFunctionCayleyGraphClassification.from_function(bentf0)
        sage: bfcgc0.algebraic_normal_form
        x0*x1
        sage: insert_classification(conn, bfcgc0, 'bentf0')
        sage: bentf1 = BentFunction([1,0,0,0])
        sage: bfcgc1 = BentFunctionCayleyGraphClassification.from_function(bentf1)
        sage: bfcgc1.algebraic_normal_form
        x0*x1 + x0 + x1 + 1
        sage: insert_classification(conn, bfcgc1, 'bentf1')
        sage: result = select_classification_where_bent_function_cayley_graph(conn, bentf1)
        sage: type(result)
        <type 'list'>
        sage: len(result)
        2
        sage: sorted_result = sorted(result, key=lambda c: str(c.algebraic_normal_form))
        sage: for c in sorted_result:
        ....:     type(c)
        ....:     c.algebraic_normal_form
        ....:     c.report()
        <class 'boolean_cayley_graphs.bent_function_cayley_graph_classification.BentFunctionCayleyGraphClassification'>
        x0*x1
        Algebraic normal form of Boolean function: x0*x1
        Function is bent.
        <BLANKLINE>
        <BLANKLINE>
        SDP design incidence structure t-design parameters: (True, (1, 4, 1, 1))
        <BLANKLINE>
        Classification of Cayley graphs and classification of Cayley graphs of duals are the same:
        <BLANKLINE>
        There are 2 extended Cayley classes in the extended translation class.
        <class 'boolean_cayley_graphs.bent_function_cayley_graph_classification.BentFunctionCayleyGraphClassification'>
        x0*x1 + x0 + x1 + 1
        Algebraic normal form of Boolean function: x0*x1 + x0 + x1 + 1
        Function is bent.
        <BLANKLINE>
        <BLANKLINE>
        SDP design incidence structure t-design parameters: (True, (1, 4, 1, 1))
        <BLANKLINE>
        Classification of Cayley graphs and classification of Cayley graphs of duals are the same:
        <BLANKLINE>
        There are 2 extended Cayley classes in the extended translation class.
        sage: conn.close()
        sage: drop_database(db_name)
    """
    cayley_graph = bentf.extended_cayley_graph()
    cgcl = cayley_graph.canonical_label(algorithm=algorithm).graph6_string()
    cgcl_hash = canonical_label_hash(cgcl)

    curs = conn.cursor()
    curs.execute("""
        SELECT graph_id, canonical_label
        FROM graph
        WHERE canonical_label_hash = (?)""",
        (cgcl_hash,))

    row = curs.fetchone()
    graph_id = row["graph_id"]
    canonical_label = row["canonical_label"]

    # The result is a list of classifications.
    result = []
    # Check for a hash collision -- very unlikely.
    if canonical_label != cgcl:
        return result

    curs.execute("""
        SELECT DISTINCT nvariables, bent_function
        FROM cayley_graph
        WHERE graph_id = (?)""",
        (graph_id,))

    for row in curs:
        nvar = row["nvariables"]
        bftt = row["bent_function"]
        row_bentf = BentFunction.from_tt_buffer(nvar, bftt)
        result.append(
            select_classification_where_bent_function(
                conn,
                row_bentf))
    return result


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

    EXAMPLE:

    Create a database, with tables, using a temporary filename, insert
    a classification, retrieve it by name, then drop the database.

    ::

        sage: from boolean_cayley_graphs.classification_database_sqlite3 import *
        sage: from boolean_cayley_graphs.bent_function import BentFunction
        sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
        sage: db_name = tmp_filename(ext='.db')
        sage: conn = create_classification_tables(db_name)
        sage: bentf = BentFunction([0,0,0,1])
        sage: bfcgc = BentFunctionCayleyGraphClassification.from_function(bentf)
        sage: bfcgc.algebraic_normal_form
        x0*x1
        sage: insert_classification(conn, bfcgc,'bentf')
        sage: result = select_classification_where_name(conn, 'bentf')
        sage: result.algebraic_normal_form
        x0*x1
        sage: type(result)
        <class 'boolean_cayley_graphs.bent_function_cayley_graph_classification.BentFunctionCayleyGraphClassification'>
        sage: result.report(report_on_matrix_details=True)
        Algebraic normal form of Boolean function: x0*x1
        Function is bent.
        <BLANKLINE>
        Weight class matrix:
        [0 0 0 1]
        [0 1 0 0]
        [0 0 1 0]
        [1 0 0 0]
        <BLANKLINE>
        SDP design incidence structure t-design parameters: (True, (1, 4, 1, 1))
        <BLANKLINE>
        Classification of Cayley graphs and classification of Cayley graphs of duals are the same:
        <BLANKLINE>
        There are 2 extended Cayley classes in the extended translation class.
        <BLANKLINE>
        Matrix of indices of Cayley graphs:
        [0 0 0 1]
        [0 1 0 0]
        [0 0 1 0]
        [1 0 0 0]
        sage: drop_database(db_name)
    """
    curs = conn.cursor()
    curs.execute("""
        SELECT nvariables, bent_function
        FROM bent_function
        WHERE name = (?)""",
        (name,))
    row = curs.fetchone()
    if row == None:
        return None

    nvar = row["nvariables"]
    bftt = row["bent_function"]
    bentf = BentFunction.from_tt_buffer(nvar, bftt)

    return select_classification_where_bent_function(
        conn,
        bentf)
