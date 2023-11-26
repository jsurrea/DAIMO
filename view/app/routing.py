from dash import dcc
from dash.dependencies import Input, Output
from ..home.layout import create_home_layout
from ..intervenciones_simultaneas.layout import create_intervenciones_simultaneas_layout
from ..puentes_criticos.layout import create_puentes_criticos_layout

def create_app_routing(app):
    """
    Create location component 
    Add routing callbacks for the app
    """

    # Create location component
    location = dcc.Location(id='url', refresh=False),
    
    # Create routing layouts 
    home_layout = create_home_layout(app)
    puentes_criticos_layout = create_puentes_criticos_layout(app)
    intervenciones_simultaneas_layout = create_intervenciones_simultaneas_layout(app)

    @app.callback(
        Output('page-content', 'children'), 
        Input('url', 'pathname'),
    )
    def display_page(pathname):
        if pathname == '/':
            return home_layout
        elif pathname == '/puentes_criticos':
            return puentes_criticos_layout
        elif pathname == '/intervenciones-simultaneas':
            return intervenciones_simultaneas_layout
        else:
            return f"The pathname {pathname} was not recognised..."

    return location
