import locale
from .map import render_map
from dash import Input, Output, State, callback, html
from logic import get_puentes, get_base_cost, get_puentes_criticos_content_data, has_data
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def register_puentes_criticos_callbacks():
    """
    Register callbacks of the puentes_criticos component
    """
    
    @callback(
        Output("puentes-checklist", "options"),
        Output("puentes-checklist", "value"),
        Input("app-storage", "modified_timestamp"),
        State("app-storage", "data"),
        prevent_initial_call = True,
    )
    def update_options(timestamp, data_name):
        """
        Update the options of the sidebar
        """
        options = get_puentes()
        if not has_data() or options is None:
            return [], []
        else:
            return options, options

    @callback(
        Output("puentes-criticos-text", "children"),
        Input("app-storage", "modified_timestamp"),
        State("app-storage", "data"),
        prevent_initial_call = True,
    )
    def update_text(timestamp, data_name):
        """
        Update the text of the puentes_criticos component
        """
        if not has_data():
            return "Por favor cargue los datos primero"
        base_cost = get_base_cost()
        return f"El costo total de la red vial sin intervención es de {locale.currency(base_cost, grouping = True)}"

    @callback(
        Output("puentes-criticos-map", "children"),
        Input("puentes-checklist", "value"),
        prevent_initial_call = True,
    )
    def update_map(puentes_to_show):
        """
        Update the map of the puentes_criticos component
        """
        if not has_data():
            return html.P("Por favor cargue los datos primero", className = "lead text-center m-5 alert alert-warning")
        map_data = get_puentes_criticos_content_data(puentes_to_show)
        return render_map(map_data)
