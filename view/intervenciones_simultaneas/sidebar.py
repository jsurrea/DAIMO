from dash import html, dcc

def create_intervenciones_simultaneas_sidebar_layout():
    """
    Create layout of the intervenciones_simultaneas sidebar component
    """

    intervenciones_simultaneas = html.Div(
        children = [
            html.H3(
                children = "Configuración", 
                className = "h3",
            ),
            html.Hr(),
            html.P(
                children = "Seleccione los puentes a intervenir:",
                className = "lead",
            ),
            dcc.Checklist(
                id = "intervenciones-checklist",
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
            html.Button(
                children = 'Simular', 
                id = 'intervenciones-button',
                className = "btn btn-dark btn-lg btn-block mt-4", 
            ),
        ],
        className = "px-2 py-4",
    )

    return intervenciones_simultaneas
