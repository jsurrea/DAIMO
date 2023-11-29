import os
from dash import html, dcc


def create_home_sidebar_layout():
    """
    Create layout of the home sidebar component
    """

    # Get options for the radioitems
    options = [i.replace(".pkl", "") for i in os.listdir("data")]

    home = html.Div(
        children = [
            html.H3(
                children = "Configuración", 
                className = "h3",
            ),
            html.Hr(),
            html.P(
                children = "Seleccione un archivo de datos:",
                className = "lead",
            ),
            dcc.RadioItems(
                options = options, 
                value = options[0] if len(options) > 0 else None,
                id = "home-radioitems",
                style = {
                    "max-height": "250px", 
                    "overflowY": "auto",
                },
                labelStyle = {
                    "padding-left": 10,
                },
                inputStyle = {
                    "margin-right": 5,
                },
            ),
            dcc.Upload(
                id = 'upload-data',
                children = html.Div([
                    html.A('Añadir un archivo'),
                ]),
                style = {
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin-top': '10px',
                    'margin-bottom': '10px',
                    'cursor': 'pointer',
                },
                # Allow multiple files to be uploaded
                multiple = False,
            ),
            html.Div(id = 'output-data-upload'),
            html.P(
                children = "Tenga en cuenta que la carga de un nuevo conjunto de datos puede tardar varias horas.",
                className = "fst-italic",
            ),
        ],
        className = "px-2 py-4",
    )

    return home
