import dash
import dash_bootstrap_components as dbc
from view.base.layout import create_layout

def run_app(debug = False):
    """
    Create and run the app on port 8086
    debug: True if you want to run the app in debug mode
    """
    
    # Create app
    app = dash.Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])
    app.title = "DAIMO"
    app.layout = create_layout(app)
        
    # Run app
    app.run_server(debug=debug, port=8086)


if __name__ == "__main__":
    run_app(debug = True)
