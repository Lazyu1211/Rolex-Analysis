from dash import Dash, html, dcc
from dash.dependencies import Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from util import get_model_byprice, get_bymovement, get_bymatrial, get_bydiameter, get_bycondition, get_countries

def render(app):
    df = get_countries()

    @app.callback(
        Output("bar_volume", component_property='children'),
        Input("countries_dropdown",component_property='value')
    )

    def update_bar_chart(dropdown):
        filtered_data = df.query("Country in @dropdown")
        fig = px.bar(
                filtered_data,
                x="Country",
                y="Total Price",
                title="Total Price by Country")
        return html.Div(dcc.Graph(figure=fig),id="bar_volume")
    return html.Div(id="bar_volume")

def render_store(app):
    df = get_countries()

    @app.callback(
        Output("bar_volume1", component_property='children'),
        Input("countries_dropdown",component_property='value')
    )

    def update_bar_chart(dropdown):
        filtered_data = df.query("Country in @dropdown")
        fig = px.bar(
                filtered_data,
                x="Country",
                y="Stores Amount",
                title="Total Stores Amount by Country")
        return html.Div(dcc.Graph(figure=fig),id="bar_volume1")
    return html.Div(id="bar_volume1")

def render1(app):
    df = get_bymovement()
    fig = px.bar(df, x='movement', y='price') 
    return html.Div(dcc.Graph(figure=fig),id="bar_chart")

def render2(app):
    df = get_bymatrial()
    fig = px.bar(df, x='case material', y='price') 
    return html.Div(dcc.Graph(figure=fig),id="bar_chart1")

def render3(app):
    df = get_bydiameter()
    fig = px.bar(df, x='price', y='case diameter') 
    return html.Div(dcc.Graph(figure=fig),id="bar_chart2")

def render4(app):
    df = get_bycondition()
    fig = px.bar(df, x='condition', y='price') 
    return html.Div(dcc.Graph(figure=fig),id="bar_chart3")