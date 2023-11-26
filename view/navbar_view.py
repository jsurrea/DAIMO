import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px

def create_navbar(app):

    navbar = dbc.NavbarSimple(
        children=[
            #dcc.Link("Puentes Críticos", href="/puentes-criticos", outline=True, color="secondary", className="mr-1", id="btn_sidebar"),
            #dcc.Link("Intervenciones Simultáneas", href="/intervenciones-simultaneas"),
            dbc.Button("Configuración", outline=True, color="secondary", className="mr-1", id="btn_sidebar"),
        ],
        brand="DAIMO: Dashboard para el Análisis de Intervenciones en Movilidad",
        color="dark",
        dark=True,
        fluid=True,
    )
    
    return navbar
