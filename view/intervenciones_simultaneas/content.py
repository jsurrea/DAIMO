from dash import html
from .map import render_map 
import dash_bootstrap_components as dbc

def create_intervenciones_simultaneas_content_layout():
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
                    id = "intervenciones-simultaneas-text-finished",
                    className = "d-none",
                ),
                html.Div(
                    children = [
                        html.P(
                            children = "Abra el menú de configuración para iniciar la simulación. Allí podrá seleccionar todos los puentes que desee intervenir. Tenga en cuenta que intervenir demasiados puentes puede desconectar el grafo.",
                            className = "lead",
                        ),
                        html.P(
                            children = "Por el momento, puede visualizar los flujos de la red sin intervención en el menú de la izquierda.",
                            className = "lead",
                        ),
                    ],
                    id = "intervenciones-simultaneas-text-unfinished",
                    className = "d-block",
                ),
            ],
            style = {"padding-top": "16px"},
        ),
    ])

    return intervenciones_simultaneas
