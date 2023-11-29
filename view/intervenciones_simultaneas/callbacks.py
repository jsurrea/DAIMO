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

    # @callback(
    #     Output("puentes-criticos-text", "children"),
    #     Input("app-storage", "data"),
    # )
    # def update_text(data_name):
    #     """
    #     Update the text of the intervenciones_simultaneas component
    #     """
    #     base_cost = get_base_cost()
    #     return f"El costo total de la red vial sin intervención es de {locale.currency(base_cost, grouping = True)}"

    # @callback(
    #     Output("puentes-criticos-map", "children"),
    #     Input("puentes-checklist", "value"),
    # )
    # def update_map(puentes_to_show):
    #     """
    #     Update the map of the intervenciones_simultaneas component
    #     """
    #     ...
