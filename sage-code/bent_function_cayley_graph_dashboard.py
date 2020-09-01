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
from __future__ import print_function

#*****************************************************************************
#       Copyright (C) 2018 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from future import standard_library
standard_library.install_aliases()
from builtins import range
import dash
import dash_core_components as dcc
import dash.dependencies as dd
import dash_html_components as html
import flask
import os
import pandas as pd
import plotly.graph_objs as go
import database_interface as db
import sys

from io import StringIO
from flask import Flask
from pandas import DataFrame

import sage.all

from boolean_cayley_graphs.bent_function import BentFunction
from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification

# From https://github.com/mbkupfer/dash-with-flask/blob/master/dash_app.py
server = Flask(__name__)
app = dash.Dash(__name__, server = server)

app.config.requests_pathname_prefix = ''

app.config['suppress_callback_exceptions'] = True

output_dir = 'downloads'
output_files = {
    '1_bent_function': {
        'filename': 'download_bent_function.csv',
        'label':    'Bent function'},
    '2_cg_class_list': {
        'filename': 'download_cg_class_list.csv',
        'label':    'Cayley graph class list'},
    '3_matrices': {
        'filename': 'download_matrices.csv',
        'label':    'Contents of matrices'}}

app.layout = html.Div([
    html.H2('Bent function--Cayley graph virtual laboratory (prototype)'),
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
    ),
    html.Div([
        html.H3(
            'Select a CSV file to Download.'),
        dcc.Dropdown(
            id='download-dropdown',
            value=output_files['1_bent_function']['filename'],
            options=[{
                    'label': output_files[key]['label'],
                    'value': output_files[key]['filename']}
                for key in sorted(output_files.keys())]),
        html.A(
            id='download-link',
            children='Download the CSV file from this link.',
            style={'padding-bottom': 200})])],
    style={'font-family': ["Open Sans", "Helvetica", "Arial"]})


# From https://github.com/mbkupfer/dash-with-flask/blob/master/dash_app.py
@server.route('/')
def bfcgd():
    return app


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
        conn = db.connect_to_database(
            selected_database)
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
        conn = db.connect_to_database(
            selected_database)
    except IOError:
        return ['Cannot connect to database {}.'.format(selected_database)]

    if bentf_name is None:
        return []
    bentf_c = db.cdb.select_classification_where_name(
        conn,
        bentf_name)
    bentf_path = os.path.join(output_dir, 'download')
    bentf_c.save_as_csv(bentf_path)
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


@app.callback(dd.Output('download-link', 'href'),
              [dd.Input('download-dropdown', 'value')])
def update_href(output_filename):
    relative_filename = os.path.join(
        output_dir,
        output_filename)
    return '/' + relative_filename


@app.server.route('/downloads/<path:path>')
def serve_static(path):
    root_dir = os.getcwd()
    return flask.send_from_directory(
        os.path.join(root_dir, output_dir),
        path,
        as_attachment=True)

if __name__ == '__main__':
    app.run_server(debug=False,host="0.0.0.0",port=8051)
