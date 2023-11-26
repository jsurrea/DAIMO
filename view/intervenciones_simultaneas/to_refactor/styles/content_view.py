import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px

from view.map_view import render_map

from styles.content_styles import CONTENT_STYLE

def create_content(app):

    content = html.Div(
        [
            html.H1("Criticidad de los puentes: Variación por intervenciones individuales"),
            render_map(),
        ],
        id="page-content",
        style=CONTENT_STYLE
    )
    
    return content
