from dash import dcc
from dash import html

def create_home_layout(app):
    """
    Create layout of the home component
    """

    home = html.Div(
        dbc.Container(
            [
                html.H1(
                    children = "DAIMO: Dashboard para el Análisis de Intervenciones en Movilidad", 
                    class_name = "display-3",
                ),
                html.P(
                    children = "Descubra las interacciones entre las intervenciones de movilidad y su impacto en la movilidad de Colombia.",
                    class_name = "lead",
                ),
                html.Hr(
                    class_name = "my-2",
                ),
                html.P(
                    children = "Identifique los puentes críticos de la red vial nacional",
                ),
                html.P(
                    dbc.Button("Learn more", color="primary"), 
                    class_name = "lead",
                ),
            ],
            fluid = True,
            class_name = "py-3",
        ),
        class_name = "p-3 bg-light rounded-3",
    )

    return home