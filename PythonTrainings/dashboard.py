# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div(children = [html.H1(children="Sample Dash WebApp Dashboard"), html.Div(children= '''Dash: A web based app to show the Bar Graph''' ),
                                  dcc.Graph(id='dash_graph_1',
                                            figure = {'data': [
                                                                {'x': [1,2,3,4,5], 'y': [4,6,3,8,1], 'type': 'bar', 'name': 'Bread'},
                                                                {'x': [1,2,3,4,5], 'y': [9,3,2,3,4], 'type': 'bar', 'name': 'Milk'},
                                                                {'x': [1,2,3,4,5], 'y': [4,6,3,8,1], 'type': 'line', 'name': 'Sugar'},],

                                                      'layout' : {'title': 'Dash Example App1'}
                                                        }),

                                  dcc.Graph(id='dash_graph_2',
                                            figure = {'data': [
                                                                {'x': [1,2,3,4,5], 'y': [4,6,3,8,1], 'type': 'bar', 'name': 'Aeroplane'},
                                                                {'x': [1,2,3,4,5], 'y': [9,3,2,3,4], 'type': 'bar', 'name': 'Car'},
                                                                {'x': [1,2,3,4,5], 'y': [4,6,3,8,1], 'type': 'line','name': 'Train'},],

                                                      'layout' : {'title': 'Dash Example App2'}
                                                        })

                                    ])


if __name__ == '__main__':
    app.run_server(debug=True)