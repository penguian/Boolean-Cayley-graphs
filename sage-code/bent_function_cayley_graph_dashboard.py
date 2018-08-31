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
import pandas as pd
import plotly.graph_objs as go
import sqlite3
import sys

from cStringIO import StringIO
from pandas import DataFrame

import sage.all
import boolean_cayley_graphs.classification_database_sqlite3 as cdb

from boolean_cayley_graphs.bent_function import BentFunction
from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification

app = dash.Dash()
conn = None

app.config['suppress_callback_exceptions']=True

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
                    'label': 'CAST-128',
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


@app.callback(
    dd.Output('bent-function-filter-div', 'children'),
    [dd.Input('database-filter', 'value')])
def set_bent_function_options(selected_database):
    print(selected_database)
    global conn

    try:
        conn = cdb.connect_to_database(selected_database + '.db')
    except IOError:
        print('Cannot connect to database {}.'.format(selected_database))
        return

    bent_function_names = pd.read_sql('''
        SELECT name
        FROM bent_function
        ''',
        conn)
    return [
        html.H3('Choose a bent function'),
        dcc.Dropdown(
            options=[
                {
                    'label': opt[0],
                    'value': opt[0]
                }
                for opt in bent_function_names.values
            ],
            value=None,
            id='bent-function-filter'
        )
    ]


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
    [dd.Input('bent-function-filter', 'value')])
def select_bent_function(bentf_name):
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
    app.run_server(debug=False,port=8051)
