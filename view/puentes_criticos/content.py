from dash import html

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
                    children = "Seleccione un archivo de datos válido",
                    className = "lead",
                    style = {"margin": 0},
                    id = "puentes-criticos-text",
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
        html.Div(
            id = "puentes-criticos-map",
        ),
    ])

    return puentes_criticos
