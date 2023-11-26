from dash import dcc
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
                html.P(
                    children = "Descubra las interacciones entre las intervenciones de movilidad y su impacto en la movilidad de Colombia.",
                    className = "lead",
                ),
                html.Hr(
                    className = "my-2",
                ),
                html.P(
                    children = "Identifique los puentes críticos de la red vial nacional",
                ),
                html.P(
                    dbc.Button("Learn more", color="primary"), 
                    className = "lead",
                ),
            ],
            fluid = True,
            className = "py-3",
        ),
        className = "p-3 bg-light rounded-3",
    )

    return home