# -*- coding: utf-8 -*-

r"""
Bent function Cayley graph dashboard

A simple web interface to the databases of bent function Cayley graph
classifications. This version uses Plotly Dash and SQLite3.

Run with:
sage -python bent_function_cayley_graph_dashboard.py

AUTHORS:

- Paul Leopardi (2018-06-17): initial version

"""

#*****************************************************************************
#       Copyright (C) 2018 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

import dash
import dash_core_components as dcc
import dash.dependencies as dd
import dash_html_components as html
import json
import pandas as pd
import plotly.graph_objs as go
import psycopg2
import sys

from cStringIO import StringIO
from flask import Flask
from pandas import DataFrame

import sage.all
import boolean_cayley_graphs.classification_database_psycopg2 as cdb

from boolean_cayley_graphs.bent_function import BentFunction
from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification

with open("BCG-DB.json") as auth_file:
    auth = json.load(auth_file)

# From https://github.com/mbkupfer/dash-with-flask/blob/master/dash_app.py
server = Flask(__name__)
app = dash.Dash(__name__, server = server)

app.config.requests_pathname_prefix = ''

conn = None

app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([
    html.H2('Bent function Cayley graph dashboard'),
    html.Div([
        html.H3('Choose a database'),
        dcc.RadioItems(
            options=[
                {
                    'label': '2 dimensions',
                    'value': 'p2'
                },
                {
                    'label': '4 dimensions',
                    'value': 'p4'
                },
                {
                    'label': '6 dimensions',
                    'value': 'p6'
                },
                {
                    'label': '8 dimensions to degree 3',
                    'value': 'p8'
                },
                {
                    'label': 'sigma functions to 8 dimensions',
                    'value': 'sigma'
                },
                {
                    'label': 'tau functions to 8 dimensions',
                    'value': 'tau'
                },
                {
                    'label': 'CAST-128 S-box functions',
                    'value': 'cast128'
                },
            ],
            value='p2',
            id='database-filter'
        )
    ]),
    html.Div([],
        id='bent-function-filter-div'
    ),
    html.Div([],
        id='report-output-div'
    )
])


# From https://github.com/mbkupfer/dash-with-flask/blob/master/dash_app.py
@server.route('/')
def bfcgd():
    return app



def connect_to_database(
    selected_database,
    auth):
    conn = cdb.connect_to_database(
        selected_database,
        user=auth["user"],
        password=auth["password"],
        host=auth["host"])
    return conn
    

def bent_function_filter(options):
    return [
        html.H3('Choose a bent function'),
        dcc.Dropdown(
            options=options,
            value=None,
            id='bent-function-filter'
        )
    ]


@app.callback(
    dd.Output('bent-function-filter-div', 'children'),
    [dd.Input('database-filter', 'value')])
def set_bent_function_options(selected_database):

    try:
        conn = connect_to_database(
            selected_database,
            auth)
    except IOError:
        print('Cannot connect to database {}.'.format(selected_database))
        return

    bent_function_names = pd.read_sql('''
        SELECT name
        FROM bent_function
        ''',
        conn)
    conn.close()
    options=[
        {
            'label': opt[0],
            'value': opt[0]
        }
        for opt in bent_function_names.values
    ]
    return bent_function_filter(options)


class Capturing(list):
    '''
    From kindall:
    https://stackoverflow.com/questions/16571150/how-to-capture-stdout-output-from-a-python-function-call
    '''
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


def matrix_figure(matrix, colorscale='Earth'):
    n = matrix.nrows()
    return {
        'data': [
            go.Heatmap(
                z=[
                    [
                        matrix[i,j]
                        for j in range(n)
                    ]
                    for i in range(n)
                ],
                colorscale=colorscale
            )
        ],
        'layout': {
            'width':  '512',
            'height': '512',
            'yaxis': {
                'autorange': 'reversed'
            }
        }
    }


@app.callback(
    dd.Output('report-output-div', 'children'),
    [dd.Input('bent-function-filter', 'value')],
    [dd.State('database-filter', 'value')])
def select_bent_function(bentf_name, selected_database):
    try:
        conn = connect_to_database(
            selected_database,
            auth)
    except IOError:
        return ['Cannot connect to database {}.'.format(selected_database)]

    if bentf_name is None:
        return []
    bentf_c = cdb.select_classification_where_name(
        conn,
        bentf_name)
    with Capturing() as report:
        bentf_c.report()
    wc_matrix = bentf_c.weight_class_matrix
    wc_graph = dcc.Graph(
        figure=matrix_figure(wc_matrix),
        id='wc-graph')
    ci_matrix = bentf_c.bent_cayley_graph_index_matrix
    ci_graph = dcc.Graph(
        figure=matrix_figure(ci_matrix),
        id='ci-graph')
    di_matrix = bentf_c.dual_cayley_graph_index_matrix
    di_graph = dcc.Graph(
        figure=matrix_figure(di_matrix),
        id='di-graph')
    return [
        html.P(bentf_name + ':')] + [
        html.P(line)
        for line in report] + [
        html.Table(
        # Header
        [
            html.Tr([
                html.Div([
                    html.Div([
                        html.B('Weight class matrix')],
                        style={
                            'textAlign': 'center',
                            'width': '33%',
                            'display': 'inline-block'}),
                    html.Div([
                        html.B('Cayley graph index matrix')],
                        style={
                            'textAlign': 'center',
                            'width': '33%',
                            'display': 'inline-block'}),
                    html.Div([
                        html.B('Dual Cayley graph index matrix')],
                        style={
                            'textAlign': 'center',
                            'width': '33%',
                            'display': 'inline-block'})],
                    style={
                        'width': '100%',
                        'display': 'inline-block'})])] +
        # Body
        [
            html.Tr([
                html.Div([
                    html.Div(
                        wc_graph,
                        style={
                            'width': '33%',
                            'display': 'inline-block'}),
                    html.Div(
                        ci_graph,
                        style={
                            'width': '33%',
                            'display': 'inline-block'}),
                    html.Div(
                        di_graph,
                        style={
                            'width': '33%',
                            'display': 'inline-block'})],
                style={
                    'width': '100%',
                    'display': 'inline-block'})])])]


if __name__ == '__main__':
    app.run_server(debug=False,host="0.0.0.0",port=8051)
