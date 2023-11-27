from dash import html
from ...home import create_home_sidebar_layout
from ...puentes_criticos import create_puentes_criticos_sidebar_layout
from ...intervenciones_simultaneas import create_intervenciones_simultaneas_sidebar_layout

def create_sidebar_layout():
    """
    Create layout of the sidebar component
    """

    # Create routing layouts
    home_sidebar_layout = create_home_sidebar_layout()
    puentes_criticos_sidebar_layout = create_puentes_criticos_sidebar_layout()
    intervenciones_simultaneas_sidebar_layout = create_intervenciones_simultaneas_sidebar_layout()
    
    # Create layout
    sidebar = html.Div(
        children = [
            html.Div(
                children = home_sidebar_layout,
                className = 'd-none',
                id = 'home-sidebar',
            ),
            html.Div(
                children = puentes_criticos_sidebar_layout,
                className = 'd-none',
                id = 'puentes-criticos-sidebar',
            ),
            html.Div(
                children = intervenciones_simultaneas_sidebar_layout,
                className = 'd-none',
                id = 'intervenciones-simultaneas-sidebar',
            ),
        ],
        id = 'page-sidebar',
    )
    
    return sidebar
