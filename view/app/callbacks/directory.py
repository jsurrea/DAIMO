from .app import toggle_sidebar
from .home import update_data_output
from dash import Input, Output, callback

def register_callbacks():
    """
    Register callbacks of the app
    """

    callback(
        Output("page-sidebar", "style"),
        Output("page-content", "style"),
        Input("btn-sidebar", "n_clicks"),
    )(toggle_sidebar)

    callback(
        Output('output-data-upload', 'children'),
        Input('upload-data', 'filename'),
    )(update_data_output)
