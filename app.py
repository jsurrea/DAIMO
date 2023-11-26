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
    #home = create_home(app)
    
    app.layout = html.Div(
        [
            dcc.Location(id='url', refresh=False),
            navbar,
            html.Div(id='page-content'),
            #sidebar,
            #modal,
            #content,
        ],
    )

    # Routing
    @app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/page-1':
            return html.P("This is Page 1")
        elif pathname == '/page-2':
            return html.P("This is Page 2")
        else:
            return html.P("This is the default page")
        
    app.run_server(debug=debug, port=8086)



if __name__ == "__main__":
    run_app(debug = True)
