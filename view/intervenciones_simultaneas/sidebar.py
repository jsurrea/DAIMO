from dash import html, dcc

def create_intervenciones_simultaneas_sidebar():
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
            # TODO
            dcc.Checklist(
                options = [
                    "Puente 1", #TODO
                    "Puente 2", #TODO
                    "Puente 3", #TODO
                    "Puente 4", #TODO
                    "Puente 5", #TODO
                    "Puente 6", #TODO
                    "Puente 7", #TODO
                    "Puente 8", #TODO
                    "Puente 9", #TODO
                    "Puente 10", #TODO
                ], 
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
