
from dash import Dash, html, dcc
import plotly.express as px
from util import get_model_count, get_model_byprice

def render(app):
    df = get_model_count()
    fig = px.pie(df, values = 'model', names = "index", title = 'Model Porpotion')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart")

def render1(app):
    df = get_model_byprice()
    fig = px.pie(df, values = 'price', names = "model", title = 'Model Total Price Porpotion')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart1")