from dash import html
from .map import render_map 
import dash_bootstrap_components as dbc

def create_intervenciones_simultaneas_content():
    """
    Create layout of the intervenciones_simultaneas content component
    """

    intervenciones_simultaneas = dbc.Row([
        dbc.Col([
            render_map(),
        ]),
        dbc.Col(
            children = [
                html.H2(
                    children = "Resultados de la simulación",
                    className = "h2",
                    style = {"text-align": "center"},
                ),
                html.Hr(),
                html.Div(
                    children = [
                        html.Span(
                            children = ">", 
                            className = "h1",
                            style = {"margin": 0},
                        ),
                        html.P(
                            children = "El costo total de la red vial es de 100.000.000.000$",  #TODO
                            className = "lead",
                            style = {"margin": 0, "text-align": "center"}
                        ),
                    ],
                    style = {
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "center",
                        "gap": "10px",
                        "margin-bottom": "20px",
                    },
                ),
                html.P(
                    children = "Visualice a su izquierda los flujos de vehículos en la red vial de Colombia. Los puentes intervenidos son:",
                    className = "lead",
                    style = {"margin-bottom": 5}
                ),
                html.Ul(
                    children = [
                        html.Li("Puente 1", className = "lead"), #TODO
                        html.Li("Puente 2", className = "lead"),
                        html.Li("Puente 3", className = "lead"),
                        html.Li("Puente 3", className = "lead"),
                        html.Li("Puente 3", className = "lead"),
                        html.Li("Puente 3", className = "lead"),
                        html.Li("Puente 3", className = "lead"),
                        html.Li("Puente 3", className = "lead"),
                        html.Li("Puente 3", className = "lead"),
                        html.Li("Puente 3", className = "lead"),
                        html.Li("Puente 3", className = "lead"),
                        html.Li("Puente 3", className = "lead"),
                    ],
                    style = {
                        "max-height": "220px", 
                        "overflowY": "auto",
                    },
                ),
            ],
            style = {"padding-top": "16px"},
        ),
    ])

    return intervenciones_simultaneas
