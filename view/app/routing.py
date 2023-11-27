from dash import dcc, Input, Output, callback

def create_app_routing():
    """
    Create location component 
    Add routing callbacks for the app
    """

    # Create location component
    location = dcc.Location(id = 'url', refresh = False)

    @callback(
        Output('home-content', 'className'), 
        Output('home-sidebar', 'className'), 
        Output('puentes-criticos-content', 'className'), 
        Output('puentes-criticos-sidebar', 'className'), 
        Output('intervenciones-simultaneas-content', 'className'), 
        Output('intervenciones-simultaneas-sidebar', 'className'), 
        Input('url', 'pathname'),
    )
    def display_page(pathname):
        if pathname == '/':
            return ['d-block'] * 2 + ['d-none'] * 4
        elif pathname == '/puentes-criticos':
            return ['d-none'] * 2 + ['d-block'] * 2 + ['d-none'] * 2
        elif pathname == '/intervenciones-simultaneas':
            return ['d-none'] * 4 + ['d-block'] * 2
        else:
            return ['d-none'] * 6

    return location
