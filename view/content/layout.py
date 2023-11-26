from dash import html

def create_content_layout(app):
    """
    Create layout of the content component
    """
    
    # Create layout
    content = html.Div([
        html.Div(id='page-content'),
    ])
    
    return content
