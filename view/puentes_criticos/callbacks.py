from dash import Input, Output, State, callback, html
from logic import get_puentes

def register_puentes_criticos_callbacks():
    """
    Register callbacks of the puentes_criticos component
    """
    
    @callback(
        Output("puentes-checklist", "options"),
        Output("puentes-checklist", "value"),
        Input("app-storage", "data"),
    )
    def update_options(data_name):
        """
        Update the options of the sidebar
        """
        options = get_puentes()
        if options is not None:
            return options, options
        else:
            return [], []
