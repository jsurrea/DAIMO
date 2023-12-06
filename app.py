from dash import Dash
from view import create_app_layout
import dash_bootstrap_components as dbc

def run_app(debug = False):
    """
    Create and run the app on port 8086
    debug: True if you want to run the app in debug mode
    """
    # Create app
    app = Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])
    app.title = "DAIMO"
    app.layout = create_app_layout()
        
    # Run app
    app.run_server(debug=debug, port=8080, host="0.0.0.0")


if __name__ == "__main__":
    run_app(debug = True)
