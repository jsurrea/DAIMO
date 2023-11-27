from dash import html
from ...home import create_home_content_layout
from ...puentes_criticos import create_puentes_criticos_content_layout
from ...intervenciones_simultaneas import create_intervenciones_simultaneas_content_layout

def create_content_layout():
    """
    Create layout of the content component
    """
    
    # Create routing layouts
    home_content_layout = create_home_content_layout()
    puentes_criticos_content_layout = create_puentes_criticos_content_layout()
    intervenciones_simultaneas_content_layout = create_intervenciones_simultaneas_content_layout()
    
    # Create layout
    content = html.Div([
        html.Div(
            children = [
                html.Div(
                    children = home_content_layout,
                    className = 'd-none',
                    id = 'home-content',
                ),
                html.Div(
                    children = puentes_criticos_content_layout,
                    className = 'd-none',
                    id = 'puentes-criticos-content',
                ),
                html.Div(
                    children = intervenciones_simultaneas_content_layout,
                    className = 'd-none',
                    id = 'intervenciones-simultaneas-content',
                ),
            ],
            id = 'page-content',
        ),
    ])
    
    return content
