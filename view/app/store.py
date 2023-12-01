from dash import dcc, html

def create_app_storage():
    """
    Create storage component
    """
    return html.Div([
        dcc.Store(id = 'app-storage', storage_type = 'local'),
        dcc.Store(id = 'tmp-storage', storage_type = 'memory'),
    ])
    