# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 21:13:27 2022

@author: Sam
"""

#Application 
#Usefull for interactive management 

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, State
import pandas as pd


app = dash.Dash(external_stylesheets=[dbc.themes.MATERIA])
server = app.server


tab = html.Div(
    [
        html.H2("DisneyLand", style = {"font-size" : 50, "text-align": "center"}),
        html.Hr(),
        dbc.Tabs(
            [
                dbc.Tab(label = "Acceuil", tab_id="Acceuil"),
                dbc.Tab(label = "Base de données", tab_id="bdd"),
                dbc.Tab(label = "DashBoard", tab_id="DashBoard"),
            ],
            id = "onglet", active_tab="Acceuil"
        ),
    ], style = {"color": "black"}
)



content = dbc.Container( 

    [
        
        html.Div([
  
                        
    ],
        id= "active_accueil"
    ),
    html.Div([

       
    ],
    id="active_bdd"
    ),
    html.Div([
        

    ],
    id="active_dashboard"
    )
    ]
 )

app.layout = html.Div([tab, content])



@app.callback([Output("active_accueil", "style"),Output("active_bdd", "style"), Output("active_dashboard", "style")],
                                                                [Input("onglet","active_tab")])
def render_tab_content(active_tab):

    on = {"display":"block"}

    off = {"display":"none"}

    if active_tab is not None:

        if active_tab == "Acceuil":

            return on, off, off

        elif active_tab == "bdd":

            return off, on, off

        elif active_tab == "DashBoard":

            return off, off,on

    return "No tab selected"


if __name__ == "__main__":
    app.run_server(debug = True)