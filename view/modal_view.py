import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import no_update
from dash.exceptions import PreventUpdate
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Example for US dollars


from model.model import Model

def create_modal(app):

    # Load model
    model = Model.get_model()

    modal = dbc.Modal(
        [
            dbc.ModalHeader("Costo de intervención"),
            dbc.ModalBody(
                [
                    html.H6("Resultados:"),
                    html.Div(id="modal-body"),
                ]
            ),
            dbc.ModalFooter(
                dbc.Button("Cerrar", id="close-modal", className="ml-auto")
            ),
        ],
        id="cost-modal",
    )

    # Callbacks

    @app.callback(
        [
            Output("cost-modal", "is_open"),
            Output("modal-body", "children"),
        ],
        [
            Input("btn_calcular", "n_clicks"),
            Input("close-modal", "n_clicks"),
        ],
        [
            State("checklist", "value"),
        ],
    )
    def toggle_modal(btn_calcular, close_modal, selected_puentes):

        ctx = dash.callback_context

        if not ctx.triggered_id:
            raise PreventUpdate

        if "btn_calcular" in ctx.triggered_id:
            costo_alternativa, delta_costo = model.calculate_cost(selected_puentes)
            costo_alternativa = locale.currency(costo_alternativa, grouping=True)
            costo_original = model.get_base_costs()["TOTAL"][0]
            result_list = [
                html.P(f"El costo total de la intervención es: {costo_alternativa}"),
                html.P(f"La diferencia respecto al costo original es: {delta_costo/costo_original*100:.5f}%"),
                html.Hr(),
                html.P(f"Los puentes seleccionados fueron:"),
                html.Ul([html.Li(p) for p in selected_puentes]),
            ]
            return True, result_list

        return False, no_update

    return modal
