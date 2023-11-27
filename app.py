from view import create_app_layout

def run_app(debug = False):
    """
    Create and run the app on port 8086
    debug: True if you want to run the app in debug mode
    """
    # Create app
    app = create_app_layout()
        
    # Run app
    app.run_server(debug=debug, port=8086)


if __name__ == "__main__":
    run_app(debug = True)
