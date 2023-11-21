import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px

from styles.sidebar_styles import SIDEBAR_HIDEN, SIDEBAR_STYLE
from styles.content_styles import CONTENT_STYLE, CONTENT_STYLE1

from model.model import Model

def create_sidebar(app):

    # Load model
    model = Model.get_model()
    
    # Definition
    sidebar = html.Div(
        [
            html.H5("Config", className="display-4"),
            html.Hr(),
            html.P("Seleccione los puentes que desea evaluar:", className="lead"),
            dcc.Checklist(
                model.get_puentes(), 
                id="checklist",
                style={"height": "300px", "overflowY": "auto"},  # Set a fixed height and enable vertical scrolling if needed
            ),
            html.Div(
                dbc.Button("Calcular", outline=True, color="primary", className="mb-1", id="btn_calcular"),
                style={"margin-top": "20px", "display":"grid", "align-items": "center"}
            ),  # Add margin to separate the checklist and the button
        ],
        id="sidebar",
        style=SIDEBAR_STYLE,
    )

    # Callbacks
    
    @app.callback(
        [
            Output("sidebar", "style"),
            Output("page-content", "style"),
        ],
        [
            Input("btn_sidebar", "n_clicks")
        ],
    )
    def toggle_sidebar(n):
        if n is None or n % 2 == 0:
            sidebar_style = SIDEBAR_HIDEN
            content_style = CONTENT_STYLE1
        else:
            sidebar_style = SIDEBAR_STYLE
            content_style = CONTENT_STYLE

        return sidebar_style, content_style
    
    
    return sidebar

