from .content import create_home_content
from .sidebar import create_home_sidebar

def create_home_layout(app):
    """
    Create layout of the home component
    """

    # Create layout
    content = create_home_content(app)
    sidebar = create_home_sidebar(app)

    return (content, sidebar)
