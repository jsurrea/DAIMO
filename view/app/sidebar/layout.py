from dash import html

def create_sidebar_layout():
    """
    Create layout of the sidebar component
    """
    
    # Create layout
    sidebar = html.Div(
        children = [],
        id='page-sidebar',
    )
    
    return sidebar
