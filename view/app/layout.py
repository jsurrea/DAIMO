from dash import Dash, html
import dash_bootstrap_components as dbc
from .routing import create_app_routing
from .navbar import create_navbar_layout
from .sidebar import create_sidebar_layout
from .content import create_content_layout
from .callbacks import register_callbacks

def create_app_layout():
    """
    Create layout component of the app
    """

    # Create app
    app = Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])
    app.title = "DAIMO"
    
    # Retrieve components
    location = create_app_routing()
    navbar = create_navbar_layout()
    sidebar = create_sidebar_layout()
    content = create_content_layout()
    
    # Create layout
    app.layout = html.Div([
        location,
        navbar,
        sidebar,
        content,
    ])

    # Register callbacks
    register_callbacks()
    
    return app
