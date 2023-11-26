from dash import html
import dash_bootstrap_components as dbc

def create_home_layout(app):
    """
    Create layout of the home component
    """

    home = html.Div(
        dbc.Container(
            [
                html.H1(
                    children = "DAIMO: Dashboard para el Análisis de Intervenciones en Movilidad", 
                    className = "display-3",
                ),
                html.Hr(className="my-4"),
                dbc.Row(
                    children = [
                        dbc.Col(
                            children = [
                                html.Div(
                                    children = [
                                        html.H2(
                                            "Puentes Críticos", 
                                            className = "h2",
                                        ),
                                        html.P(
                                            "Identifique los puentes más críticos de la red vial de Colombia según los costos de su intervención", 
                                            className = "lead",
                                        ),
                                        dbc.Button(
                                            children = "Utilizar ahora", 
                                            color = "secondary", 
                                            outline = True,
                                            href="/puentes-criticos",
                                        ),
                                    ],
                                    className = "h-100 p-5 text-white bg-dark rounded-3",
                                )
                            ],
                            md=6,
                        ),
                        dbc.Col(
                            children = [
                                html.Div(
                                    children = [
                                        html.H2(
                                            "Intervenciones Simultáneas", 
                                            className = "h2",
                                        ),
                                        html.P(
                                            "Simule los costos sobre la red vial de Colombia de intervenir múltiples puentes al mismo tiempo", 
                                            className = "lead",
                                        ),
                                        dbc.Button(
                                            children = "Utilizar ahora", 
                                            color = "secondary", 
                                            outline = True,
                                            href="/intervenciones-simultaneas",
                                        ),
                                    ],
                                    className = "h-100 p-5 text-white bg-dark rounded-3",
                                )
                            ],
                            md=6,
                        ),
                    ],
                    className = "align-items-md-stretch",
                ),
            ],
            fluid = True,
            className = "py-3",
        ),
        className = "p-3 bg-light rounded-3",
    )

    return home