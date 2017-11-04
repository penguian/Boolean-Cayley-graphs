r"""
AUTHORS:

- Paul Leopardi (2017-10-28)

"""
#*****************************************************************************
#       Copyright (C) 2017 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

import sqlite3

from sage.arith.srange import xsrange
from sage.matrix.constructor import matrix

from boolean_cayley_graphs.bent_function import BentFunction
from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
from boolean_cayley_graphs.weight_class import weight_class

def create_classification_db(db_name):

    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()
    curs.execute('''CREATE TABLE bent_cayley_graph_index(
                    bent_function TEXT,
                    b INTEGER,
                    c INTEGER,
                    cayley_graph_index INTEGER,
                    PRIMARY KEY(bent_function, b, c))''')
    curs.execute('''CREATE INDEX idx_bent_cayley_graph_index
                    ON bent_cayley_graph_index(bent_function)''')

    curs.execute('''CREATE TABLE dual_cayley_graph_index(
                    bent_function TEXT,
                    b INTEGER,
                    c INTEGER,
                    cayley_graph_index INTEGER,
                    PRIMARY KEY(bent_function, b, c))''')
    curs.execute('''CREATE INDEX idx_dual_cayley_graph_index
                    ON dual_cayley_graph_index(bent_function)''')

    curs.execute('''CREATE TABLE cayley_graph_class(
                    bent_function TEXT,
                    cayley_graph_index INTEGER,
                    canonical_form TEXT,
                    PRIMARY KEY(bent_function, cayley_graph_index))''')
    curs.execute('''CREATE INDEX idx_cayley_graph_class_bent_function
                    ON cayley_graph_class(bent_function)''')
#   curs.execute('''CREATE INDEX idx_cayley_graph_class_canonical_form
#                   ON cayley_graph_class(canonical_form)''')

    curs.execute('''CREATE TABLE weight_class(
                    bent_function TEXT,
                    b INTEGER,
                    c INTEGER,
                    weight_class INTEGER,
                    PRIMARY KEY(bent_function, b, c))''')
    curs.execute('''CREATE INDEX idx_weight_class
                    ON weight_class(bent_function)''')
    conn.commit()
    return conn


def connect_to_classification_db(db_name):

    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    return conn


def insert_classification(curs, bfcgc):

    bentf = BentFunction(bfcgc.algebraic_normal_form)
    dim = bentf.nvariables()
    v = 2 ** dim
    bftt = bentf.truth_table(format='hex')
    bcim = bfcgc.bent_cayley_graph_index_matrix
    dcim = bfcgc.dual_cayley_graph_index_matrix
    cgcl = bfcgc.cayley_graph_class_list
    wcm  = bfcgc.weight_class_matrix

    for b in range(v):
        bcim_b_row = ((bftt, b, c, int(bcim[c,b])) for c in range(v))
        curs.executemany('''INSERT INTO bent_cayley_graph_index
                            VALUES (?,?,?,?)''', bcim_b_row)

        dcim_b_row = ((bftt, b, c, int(dcim[c,b])) for c in range(v))
        curs.executemany('''INSERT INTO dual_cayley_graph_index
                            VALUES (?,?,?,?)''', dcim_b_row)

        wcm_b_row  = ((bftt, b, c, int(wcm[c,b])) for c in range(v))
        curs.executemany('''INSERT INTO weight_class
                            VALUES (?,?,?,?)''', wcm_b_row)

    cgcl_row = ((bftt, n, cgcl[n]) for n in range(len(cgcl)))
    curs.executemany('''INSERT INTO cayley_graph_class
                        VALUES (?,?,?)''', cgcl_row)

    curs.connection.commit()


def select_classification(curs, bentf):

    dim = bentf.nvariables()
    v = 2 ** dim
    bftt = (bentf.truth_table(format='hex'),)

    bcim = matrix(v, v)
    curs.execute('''SELECT *
                    FROM bent_cayley_graph_index
                    WHERE bent_function == (?)''', bftt)
    for row in curs:
        b = row["b"]
        c = row["c"]
        index = row["cayley_graph_index"]
        bcim[c, b] = index

    dcim = matrix(v, v)
    curs.execute('''SELECT *
                    FROM dual_cayley_graph_index
                    WHERE bent_function == (?)''', bftt)
    for row in curs:
        b = row["b"]
        c = row["c"]
        index = row["cayley_graph_index"]
        dcim[c, b] = index

    wcm = matrix(v, v)
    curs.execute('''SELECT *
                    FROM weight_class
                    WHERE bent_function == (?)''', bftt)
    for row in curs:
        b = row["b"]
        c = row["c"]
        weight_class = row["weight_class"]
        wcm[c, b] = weight_class

    curs.execute('''SELECT COUNT(*)
                    FROM cayley_graph_class
                    WHERE bent_function == (?)''', bftt)
    cgcl_len = [count for count in curs][0][0]
    cgcl = [None] * cgcl_len

    curs.execute('''SELECT cayley_graph_index, canonical_form
                    FROM cayley_graph_class
                    WHERE bent_function == (?)''', bftt)
    for row in curs:
        index = row["cayley_graph_index"]
        canonical_form = row["canonical_form"]
        cgcl[index] = str(canonical_form)

    return BentFunctionCayleyGraphClassification(
        algebraic_normal_form=bentf.algebraic_normal_form(),
        bent_cayley_graph_index_matrix=bcim,
        dual_cayley_graph_index_matrix=dcim,
        cayley_graph_class_list=cgcl,
        weight_class_matrix=wcm)
