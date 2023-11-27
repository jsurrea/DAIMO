from dash import html
from .map import render_map

def create_puentes_criticos_content_layout():
    """
    Create layout of the puentes_criticos content component
    """

    puentes_criticos = html.Div([
        html.Div(
            children = [
                html.Span(
                    children = ">", 
                    className = "h1",
                    style = {"margin": 0},
                ),
                html.P(
                    children = "El costo total de la red vial sin intervención es de $",
                    className = "lead",
                    style = {"margin": 0}
                ),
            ],
            style = {
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
                "gap": "10px",
                "margin-bottom": "10px",
            },
        ),
        render_map(),
    ])

    return puentes_criticos
