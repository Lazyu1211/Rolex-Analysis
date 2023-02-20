from dash import Dash, html, dcc
from dash.dependencies import Output,Input
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from util import get_countries_name
import matplotlib.pyplot as plt
import seaborn as sns

def render(app):
    list_countries = get_countries_name()
    all_countries = [{'label':i,'value':i} for i in list_countries]
    @app.callback(
    Output(component_id='countries_dropdown', component_property='value'),
    Input(component_id='select_all_button', component_property='n_clicks')
    )
    def update_all_countries(n):
        return list_countries



    return html.Div(
        children=[
            html.H6("Select country"),
            dcc.Dropdown(
                options=all_countries,
                multi=True,
                id = "countries_dropdown",
                value= "United States of America"
            ),
            dbc.Button(
                children=["Select all"],
                color="primary",
                className="me-1",
                id="select_all_button",
                n_clicks=0
            )
        ]
    )