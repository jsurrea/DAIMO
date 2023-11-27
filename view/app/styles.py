def get_visible_styles():
    """
    Get styles for the application when the sidebar is visible
    """

    sidebar_style = {
        "position": "absolute",
        "top": 62.5,
        "left": 0,
        "bottom": 0,
        "width": "16rem",
        "height": "100%",
        "z-index": 1,
        "overflow-x": "hidden",
        "transition": "all 0.5s",
        "padding": "0.5rem 1rem",
        "background-color": "#f8f9fa",
    }

    content_style = {
        "transition": "margin-left .5s",
        "margin-left": "18rem",
        "margin-right": "2rem",
        "padding": "1rem 1rem",
        "background-color": "#f8f9fa",
    }

    return sidebar_style, content_style

def get_hidden_styles():
    """
    Get styles for the application when the sidebar is hidden
    """

    sidebar_style = {
        "position": "fixed",
        "top": 62.5,
        "left": "-16rem",
        "bottom": 0,
        "width": "16rem",
        "height": "100%",
        "z-index": 1,
        "overflow-x": "hidden",
        "transition": "all 0.5s",
        "padding": "0rem 0rem",
        "background-color": "#f8f9fa",
    }

    content_style = {
        "transition": "margin-left .5s",
        "margin-left": "2rem",
        "margin-right": "2rem",
        "padding": "1rem 1rem",
        "background-color": "#f8f9fa",
    }

    return sidebar_style, content_style
