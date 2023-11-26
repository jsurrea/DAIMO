from dash.dependencies import Input, Output
from .styles import get_visible_styles, get_hidden_styles

def register_callbacks(app):
    """
    Register callbacks of the app
    """

    hidden_styles = get_hidden_styles()
    visible_styles = get_visible_styles()

    @app.callback(
        Output("page-sidebar", "style"),
        Output("page-content", "style"),
        Input("btn-sidebar", "n_clicks"),
    )
    def toggle_sidebar(n):
        """
        Toggle sidebar visibility
        """
        
        return hidden_styles if n is None or n % 2 == 0 else visible_styles
