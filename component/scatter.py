from dash import Dash,html,dcc
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from util import get_data
from ids import *


def render(app):
    df = get_data()
    @app.callback(
        Output(POINTS, 'children'),
        Input(DROPDOWN, "value")
    )
    def update_bar_chart(dropdown):
        filtered_data = df.query(" in @dropdown")
        if filtered_data.shape[0]==0:
            return html.Div("No data selected.", id=POINTS)
        fig = px.scatter(
                filtered_data, 
                x="", 
                y="",
                title="".format(dropdown))
        return html.Div(dcc.Graph(figure=fig), id=POINTS)
    return html.Div(id=POINTS)