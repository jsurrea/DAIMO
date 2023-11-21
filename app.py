import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px

from view.navbar_view import create_navbar
from view.sidebar_view import create_sidebar
from view.content_view import create_content
from view.modal_view import create_modal


def run_app(debug = False):    
    
    app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.title = "DAIMO"
    
    # Retrieve components
    
    content = create_content(app)
    sidebar = create_sidebar(app)
    navbar = create_navbar(app)
    modal = create_modal(app)
    
    app.layout = html.Div(
        [
            navbar,
            sidebar,
            modal,
            content,
        ],
    )
    
    app.run_server(debug=debug, port=8086)



if __name__ == "__main__":
    run_app(debug = True)
