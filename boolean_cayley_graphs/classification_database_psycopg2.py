r"""
Interface to a classification database using psycopg2
=====================================================

The ``classification_database_psycopg2`` module defines interfaces
to manipulate a PostgreSQL database of Cayley graph classifications.

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

import binascii
import hashlib
import psycopg2
import psycopg2.extras

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT, quote_ident

from sage.arith.srange import xsrange
from sage.matrix.constructor import matrix

from boolean_cayley_graphs.bent_function import BentFunction
from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification, default_algorithm
from boolean_cayley_graphs.weight_class import weight_class


class Psycopg2Default(object):
    """
    A default psycopg2 value.

    NOTE:

    ::

        From: Daniele Varrazzo
        Date: `24 August 2014, 15:50:38`
        Source: `https://postgrespro.com/list/thread-id/1544890`
        See: `http://initd.org/psycopg/docs/advanced.html#adapting-new-python-types-to-sql-syntax`

    TESTS:

    ::

        sage: from boolean_cayley_graphs.classification_database_psycopg2 import *
        sage: PSYCOPG2_DEFAULT = Psycopg2Default()
    """
    def __conform__(self, proto):
        """
        See: http://initd.org/psycopg/docs/advanced.html

        TESTS:

        ::

            sage: from boolean_cayley_graphs.classification_database_psycopg2 import *
            sage: PSYCOPG2_DEFAULT = Psycopg2Default()
            sage: type(PSYCOPG2_DEFAULT.__conform__(psycopg2.extensions.ISQLQuote))
            <class 'boolean_cayley_graphs.classification_database_psycopg2.Psycopg2Default'>
        """
        if proto is psycopg2.extensions.ISQLQuote:
            return self


    def getquoted(self):
        """
        See: http://initd.org/psycopg/docs/advanced.html

        TESTS:

        ::

            sage: from boolean_cayley_graphs.classification_database_psycopg2 import *
            sage: PSYCOPG2_DEFAULT = Psycopg2Default()
            sage: PSYCOPG2_DEFAULT.getquoted()
            'DEFAULT'
        """
        return 'DEFAULT'


PSYCOPG2_DEFAULT = Psycopg2Default()


def create_database(
    dbname,
    user=None,
    password=None,
    host=None):
    """
    Create a database.

    INPUT:

    - ``dbname`` -- string. The name of the database to be created.
    - ``user`` -- string, optional. A Postgres user with appropriate
      permissions on the host.
    - ``password`` -- string, optional. The Postgres password of ``user``.
    - ``host`` -- string, optional. The machine running the Postgres database
      management system that hosts the database.

    OUTPUT: a database connection object.

    EXAMPLE:

    Create a database using a standardized name, then drop the database.

    ::

        sage: from boolean_cayley_graphs.classification_database_psycopg2 import *
        sage: from psycopg2 import ProgrammingError
        sage: dbname = 'doctest_create_database_dbname'
        sage: drop_database(dbname)
        sage: conn = create_database(dbname)
        sage: type(conn)
        <type 'psycopg2.extensions.connection'>
        sage: conn.close()
        sage: drop_database(dbname)
    """
    conn = psycopg2.connect(
        dbname="postgres",
        user=user,
        password=password,
        host=host)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    curs = conn.cursor()
    curs.execute(
        "CREATE DATABASE %s" %
        quote_ident(dbname, curs))
    conn.commit()
    return conn


def connect_to_database(
    dbname,
    user=None,
    password=None,
    host=None):
    """
    Connect to an existing database.

    INPUT:

    - ``dbname`` -- string. The name of the existing database.
    - ``user`` -- string, optional. A Postgres user with appropriate
      permissions on the host.
    - ``password`` -- string, optional. The Postgres password of ``user``.
    - ``host`` -- string, optional. The machine running the Postgres database
      management system that hosts the database.

    OUTPUT: a database connection object.

    EXAMPLE:

    Create a database using a standardized name, connect to it,
    then drop the database.

    ::

        sage: from boolean_cayley_graphs.classification_database_psycopg2 import *
        sage: from psycopg2 import ProgrammingError
        sage: dbname = 'doctest_connect_to_database_dbname'
        sage: drop_database(dbname)
        sage: conn = create_database(dbname)
        sage: conn.close()
        sage: con2 = connect_to_database(dbname)
        sage: type(con2)
        <type 'psycopg2.extensions.connection'>
        sage: con2.close()
        sage: drop_database(dbname)
    """
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host)
    return conn


def drop_database(
    dbname,
    user=None,
    password=None,
    host=None):
    """
    Drop a database, if it exists.

    INPUT:

    - ``dbname`` -- string. The name of the existing database.
    - ``user`` -- string, optional. A Postgres user with appropriate
      permissions on the host.
    - ``password`` -- string, optional. The Postgres password of ``user``.
    - ``host`` -- string, optional. The machine running the Postgres database
      management system that hosts the database.

    OUTPUT: None.

    EXAMPLE:

    Create a database using a standardized name, then drop the database.

    ::

        sage: from boolean_cayley_graphs.classification_database_psycopg2 import *
        sage: dbname = 'doctest_drop_database_dbname'
        sage: drop_database(dbname)
        sage: conn = create_database(dbname)
        sage: type(conn)
        <type 'psycopg2.extensions.connection'>
        sage: conn.close()
        sage: drop_database(dbname)
        sage: drop_database(dbname)
    """
    conn = psycopg2.connect(
        dbname="postgres",
        user=user,
        password=password,
        host=host)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    with conn.cursor() as curs:
        try:
            curs.execute(
                "DROP DATABASE %s" %
                quote_ident(dbname, curs))
        except psycopg2.ProgrammingError:
            pass
    conn.close()


def create_classification_tables(
    dbname,
    user=None,
    password=None,
    host=None):
    """
    Create the tables used for a database of Cayley graph classifications.

    INPUT:

    - ``dbname`` -- string. The name of an existing database.
    - ``user`` -- string, optional. A Postgres user with appropriate
      permissions on the host.
    - ``password`` -- string, optional. The Postgres password of ``user``.
    - ``host`` -- string, optional. The machine running the Postgres database
      management system that hosts the database.

    OUTPUT: a database connection object.

    EXAMPLE:

    Create a database, with tables, using a standardized name,
    list the table names, then drop the database.

    ::

        sage: from boolean_cayley_graphs.classification_database_psycopg2 import *
        sage: dbname = 'doctest_create_classification_tables_dbname'
        sage: drop_database(dbname)
        sage: conn = create_database(dbname)
        sage: conn.close()
        sage: conn = create_classification_tables(dbname)
        sage: curs = conn.cursor()
        sage: curs.execute(
        ....:     "SELECT table_name " +
        ....:     "FROM information_schema.tables " +
        ....:     "WHERE table_schema='public' AND table_type='BASE TABLE'")
        sage: for row in curs:
        ....:     for x in row:
        ....:         print(x)
        ....:
        bent_function
        cayley_graph
        graph
        matrices
        sage: conn.close()
        sage: drop_database(dbname)
    """
    conn = connect_to_database(
        dbname,
        user=user,
        password=password,
        host=host)
    curs = conn.cursor()

    curs.execute("""
        CREATE TABLE bent_function(
        nvariables INTEGER,
        bent_function BYTEA,
        name TEXT UNIQUE,
        PRIMARY KEY(nvariables, bent_function))""")
    curs.execute("""
        CREATE TABLE graph(
        graph_id SERIAL PRIMARY KEY,
        canonical_label_hash BYTEA UNIQUE,
        canonical_label TEXT)""")
    curs.execute("""
        CREATE TABLE cayley_graph(
        nvariables INTEGER,
        bent_function BYTEA,
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
        bent_function BYTEA,
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


def canonical_label_hash(canonical_label):
    r"""
    Hash function for Graph canonical labels.

    INPUT:

    - ``canonical_label`` -- string. A graph6_string encoding a Graph canonical label.

    OUTPUT: The sha256 hash of ``canonical_label`` as a ``psycopg2.Binary`` buffer.

    TESTS:

    ::

        sage: from boolean_cayley_graphs.classification_database_psycopg2 import *
        sage: clh = canonical_label_hash("Arbitrary string")
        sage: type(clh)
        <type 'psycopg2.extensions.Binary'>
    """
    return psycopg2.Binary(buffer(hashlib.sha256(canonical_label).digest()))


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

    Create a database, with tables, using a standardized name, insert
    a classification, retrieve it by bent function, then drop the database.

    ::

        sage: from boolean_cayley_graphs.classification_database_psycopg2 import *
        sage: from boolean_cayley_graphs.bent_function import BentFunction
        sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
        sage: bentf = BentFunction([0,0,0,1])
        sage: bfcgc = BentFunctionCayleyGraphClassification.from_function(bentf)
        sage: bfcgc.algebraic_normal_form
        x0*x1
        sage: dbname = 'doctest_insert_classification_dbname'
        sage: drop_database(dbname)
        sage: conn = create_database(dbname)
        sage: conn.close()
        sage: conn = create_classification_tables(dbname)
        sage: insert_classification(conn, bfcgc, 'bentf')
        sage: result = select_classification_where_bent_function(conn, bentf)
        sage: result.algebraic_normal_form
        x0*x1
        sage: conn.close()
        sage: drop_database(dbname)
    """
    bentf = BentFunction(bfcgc.algebraic_normal_form)
    dim = bentf.nvariables()
    nvar = int(dim)
    bftt = psycopg2.Binary(bentf.tt_buffer())
    cgcl = bfcgc.cayley_graph_class_list
    bcim = bfcgc.bent_cayley_graph_index_matrix
    dcim = bfcgc.dual_cayley_graph_index_matrix
    wcm  = bfcgc.weight_class_matrix

    curs = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    curs.execute("""
        INSERT INTO bent_function
        VALUES (%s,%s,%s)""",
        (nvar, bftt, name))
    for n in range(len(cgcl)):
        cgc = cgcl[n]
        cgc_hash = canonical_label_hash(cgc)
        curs.execute("""
            INSERT INTO graph
            VALUES (%s,%s,%s)
            ON CONFLICT DO NOTHING""",
            (PSYCOPG2_DEFAULT, cgc_hash, cgc))

        curs.execute("""
            SELECT graph_id
            FROM graph
            WHERE canonical_label_hash = (%s)""",
            (cgc_hash,))

        row = curs.fetchone()
        graph_id = row["graph_id"]

        curs.execute("""
            INSERT INTO cayley_graph
            VALUES (%s,%s,%s,%s)""",
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
            VALUES (%s,%s,%s,%s,%s,%s,%s)""",
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
    The corresponding a Cayley graph classification.

    EXAMPLE:

    Create a database, with tables, using a standardized name, insert
    a classification, retrieve it by bent function, then drop the database.

    ::

        sage: from boolean_cayley_graphs.classification_database_psycopg2 import *
        sage: from boolean_cayley_graphs.bent_function import BentFunction
        sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
        sage: bentf = BentFunction([0,0,0,1])
        sage: bfcgc = BentFunctionCayleyGraphClassification.from_function(bentf)
        sage: bfcgc.algebraic_normal_form
        x0*x1
        sage: dbname = 'doctest_select_classification_where_bent_function_dbname'
        sage: drop_database(dbname)
        sage: conn = create_database(dbname)
        sage: conn.close()
        sage: conn = create_classification_tables(dbname)
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
        sage: conn.close()
        sage: drop_database(dbname)
    """
    dim = bentf.nvariables()
    nvar = int(dim)
    bftt = psycopg2.Binary(bentf.tt_buffer())

    curs = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    curs.execute("""
        SELECT COUNT(*)
        FROM cayley_graph
        WHERE nvariables = (%s)
        AND bent_function = (%s)""",
        (nvar, bftt))
    row = curs.fetchone()
    if row == None:
        return None

    cgcl_len = row[0]
    cgcl = [None] * cgcl_len
    curs.execute("""
        SELECT cayley_graph_index, canonical_label
        FROM cayley_graph, graph
        WHERE nvariables = (%s)
        AND bent_function = (%s)
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
        WHERE nvariables = (%s)
        AND bent_function = (%s)""",
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

    Create a database, with tables, using a standardized name,
    insert a classification, retrieve all related classifications
    by bent function Cayley graph, then drop the database.

    ::

        sage: from boolean_cayley_graphs.classification_database_psycopg2 import *
        sage: from boolean_cayley_graphs.bent_function import BentFunction
        sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
        sage: dbname = 'doctest_select_classification_where_bent_function_dbname'
        sage: drop_database(dbname)
        sage: conn = create_database(dbname)
        sage: conn.close()
        sage: conn = create_classification_tables(dbname)
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
        sage: drop_database(dbname)
    """
    cayley_graph = bentf.extended_cayley_graph()
    cgcl = cayley_graph.canonical_label(algorithm=algorithm).graph6_string()
    cgcl_hash = canonical_label_hash(cgcl)

    curs = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    curs.execute("""
        SELECT graph_id, canonical_label
        FROM graph
        WHERE canonical_label_hash = (%s)""",
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
        WHERE graph_id = (%s)""",
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

    Create a database, with tables, using a standardized name, insert
    a classification, retrieve it by bent function, then drop the database.

    ::

        sage: from boolean_cayley_graphs.classification_database_psycopg2 import *
        sage: from boolean_cayley_graphs.bent_function import BentFunction
        sage: from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
        sage: bentf = BentFunction([0,0,0,1])
        sage: bfcgc = BentFunctionCayleyGraphClassification.from_function(bentf)
        sage: bfcgc.algebraic_normal_form
        x0*x1
        sage: dbname = 'doctest_select_classification_where_bent_function_dbname'
        sage: drop_database(dbname)
        sage: conn = create_database(dbname)
        sage: conn.close()
        sage: conn = create_classification_tables(dbname)
        sage: insert_classification(conn, bfcgc, 'bentf')
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
        sage: conn.close()
        sage: drop_database(dbname)
    """
    curs = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    curs.execute("""
        SELECT nvariables, bent_function
        FROM bent_function
        WHERE name = (%s)""",
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
