from dash import Dash,html
import dash_bootstrap_components as dbc
from component import pie_charts, bar_charts, dropdown

image_path = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTJL8ec1dVKVHbCuAQjS2Qmi0Am8DQZq1X4w&usqp=CAU" 

def create_layout(app):
    return dbc.Container(children=[
        dbc.Row([
        html.P(children="⌚⌚⌚⌚⌚✨✨✨✨✨", className="header-emoji"),
        html.H1(
                "Rolex Analysis", className="header-title"
              ),
        html.P(
                "Base on the dataset we can anlysis which watchs are the best!",
                className="header-description",
                ),
        dropdown.render(app)
        
,       
    ],className="mt-4"),
        dbc.Row([
            dbc.Col(bar_charts.render_store(app),lg=6),
            dbc.Col(bar_charts.render(app),lg=6),
            dbc.Col(pie_charts.render(app),lg=6),
            dbc.Col(pie_charts.render1(app),lg=6),
            dbc.Col(bar_charts.render1(app),lg=6),
            dbc.Col(bar_charts.render2(app),lg=6),
            dbc.Col(bar_charts.render3(app),lg=6),
            dbc.Col(bar_charts.render4(app),lg=6)
        ],className="mt-4")
    ])