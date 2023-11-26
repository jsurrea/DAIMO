from dash import html

def create_content_layout(app):
    """
    Create layout of the content component
    """
    
    # Create layout
    layout = html.Div([
        html.Div(id='page-content'),
    ])
    
    return layout
