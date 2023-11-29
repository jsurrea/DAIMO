import locale
from dash import Input, Output, State, callback, html
from logic import get_puentes
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def register_intervenciones_simultaneas_callbacks():
    """
    Register callbacks of the intervenciones_simultaneas component
    """
    
    @callback(
        Output("intervenciones-checklist", "options"),
        Input("app-storage", "data"),
    )
    def update_options(data_name):
        """
        Update the options of the sidebar
        """
        options = get_puentes()
        if options is not None:
            return options
        else:
            return []

    @callback(
        Output("intervenciones-simultaneas-text-finished", "className"),
        Output("intervenciones-simultaneas-text-unfinished", "className"),
        Input("app-storage", "data"),  # TODO cambiar
    )
    def update_text(data_name):
        """
        Update the text of the intervenciones_simultaneas component
        """
        return "d-block", "d-none" #TODO

    # @callback(
    #     Output("puentes-criticos-map", "children"),
    #     Input("puentes-checklist", "value"),
    # )
    # def update_map(puentes_to_show):
    #     """
    #     Update the map of the intervenciones_simultaneas component
    #     """
    #     ...
