from dash import html
import dash_bootstrap_components as dbc

def create_intervenciones_simultaneas_content_layout():
    """
    Create layout of the intervenciones_simultaneas content component
    """

    intervenciones_simultaneas = dbc.Row([
        dbc.Col(
            id = "intervenciones-simultaneas-map",
        ),
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
                                    className = "lead",
                                    style = {"margin": 0, "text-align": "center"},
                                    id = "intervenciones-simultaneas-result-text",
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
                            children = "Visualice a su izquierda los flujos de vehículos afectados en la red vial de Colombia. Los puentes intervenidos son:",
                            className = "lead",
                            style = {"margin-bottom": 5}
                        ),
                        html.Ul(
                            style = {
                                "max-height": "220px", 
                                "overflowY": "auto",
                            },
                            id = "intervenciones-simultaneas-result-list",
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
                            children = "En el mapa podrá observar los puentes seleccionados hasta el momento.",
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
