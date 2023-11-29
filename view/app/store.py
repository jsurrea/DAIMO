from dash import dcc

def create_app_storage():
    """
    Create storage component
    """
    return dcc.Store(id = 'app-storage', storage_type = 'local')
    