import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px

def create_navbar_layout(app):
    """
    Create layout of the navbar component
    """

    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                dbc.NavLink(
                    children = "Puentes Críticos",
                    active = "exact",
                    href = "/puentes-criticos",
                ),
            ),
            dbc.NavItem(
                dbc.NavLink(
                    children = "Intervenciones Simultáneas",
                    active = "exact",
                    href = "/intervenciones-simultaneas",
                ),
            ),
            dbc.Button(
                children = "Configuración", 
                outline = True, 
                color = "secondary", 
                class_name = "mr-1", 
                id = "btn_sidebar"
            ),
        ],
        brand = dbc.NavItem(
            dbc.NavLink(
                children = "DAIMO",
                active = "exact",
                href = "/",
            ),
        ),
        color = "dark",
        dark = True,
        fluid = True,
        pills = True,
        fill = True,
    )
    
    return navbar
