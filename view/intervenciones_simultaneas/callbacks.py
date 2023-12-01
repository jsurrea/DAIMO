import locale
from dash import Input, Output, State, callback, html, ctx
from logic import get_puentes, get_intervenciones_simultaneas_data, get_base_cost, has_data
from .map import render_map
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def register_intervenciones_simultaneas_callbacks():
    """
    Register callbacks of the intervenciones_simultaneas component
    """
    
    @callback(
        Output("intervenciones-checklist", "options"),
        Input("tmp-storage", "data"),
    )
    def update_options(data_name):
        """
        Update the options of the sidebar
        """
        options = get_puentes()
        if not has_data() or options is None:
            return []
        else:
            return options

    @callback(
        Output("intervenciones-simultaneas-text-finished", "className"),
        Output("intervenciones-simultaneas-text-unfinished", "className"),
        Output("intervenciones-simultaneas-result-list", "children"),
        Output("intervenciones-simultaneas-result-text", "children"),
        Output("intervenciones-simultaneas-map", "children"),
        Input("intervenciones-button", "n_clicks"),
        Input("tmp-storage", "data"),
        State("intervenciones-checklist", "value"),
    )
    def update_content(n_clicks, data_name, puentes_to_show):
        """
        Update the text of the intervenciones_simultaneas component
        """

        # Data is not loaded yet
        if not has_data():
            return "d-none", "d-block", [], "Por favor cargue los datos primero", html.P("Por favor cargue los datos primero", className = "lead text-center m-5 alert alert-warning")

        # No puentes selected
        if puentes_to_show is None:
            puentes_to_show = []

        display_finished = "d-none" if len(puentes_to_show) == 0 else "d-block"
        display_unfinished = "d-block" if len(puentes_to_show) == 0 else "d-none"

        bridge_data, edge_data, additional_cost = get_intervenciones_simultaneas_data(puentes_to_show)
        percentage = additional_cost / get_base_cost() * 100

        map_figure = render_map(bridge_data, edge_data)

        puentes_list = [html.Li(i, className = "lead") for i in puentes_to_show]
        total_cost_text = f"El costo total de la red vial es de {locale.currency(additional_cost, grouping = True)} ({percentage:.5f}% adicional)"

        return display_finished, display_unfinished, puentes_list, total_cost_text, map_figure

