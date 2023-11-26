from dash import html

def create_sidebar_layout(app):
    """
    Create layout of the sidebar component
    """
    
    # Create layout
    sidebar = html.Div([
        html.Div(id='page-sidebar'),
    ])
    
    return sidebar
