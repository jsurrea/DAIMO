from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

def create_puentes_criticos_sidebar_layout():
    """
    Create layout of the puentes_criticos sidebar component
    """

    puentes_criticos = html.Div(
        children = [
            html.H3(
                children = "Configuración", 
                className = "h3",
            ),
            html.Hr(),
            html.P(
                children = "Seleccione los puentes críticos a visualizar:",
                className = "lead",
            ),
            dcc.Checklist(
                id = "puentes-checklist",
                style = {
                    "max-height": "300px", 
                    "overflowY": "auto",
                },
                labelStyle = {
                    "padding-left": 10,
                },
                inputStyle = {
                    "margin-right": 5,
                },
            ),
        ],
        className = "px-2 py-4",
    )

    return puentes_criticos
