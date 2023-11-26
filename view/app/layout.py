from dash import html
from .routing import create_app_routing
from ..navbar.layout import create_navbar_layout
from ..content.layout import create_content_layout

def create_app_layout(app):
    """
    Create layout component of the app
    """
    
    # Retrieve components
    location = create_app_routing(app)
    navbar = create_navbar_layout(app)
    content = create_content_layout(app)
    
    # Create layout
    app = html.Div([
        location,
        navbar,
        content,
    ])
    
    return app
