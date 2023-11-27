from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

def create_puentes_criticos_sidebar():
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
            # TODO
            dcc.Checklist(
                options = [
                    "Puente 1", #TODO
                    "Puente 2", #TODO
                    "Puente 3", #TODO
                    "Puente 4", #TODO
                    "Puente 5", #TODO
                    "Puente 6", #TODO
                    "Puente 7", #TODO
                    "Puente 8", #TODO
                    "Puente 9", #TODO
                    "Puente 10", #TODO
                ], 
                #value = "all", #TODO
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
