from .content import create_home_content
from .sidebar import create_home_sidebar
from .callbacks import register_home_callbacks

def create_home_layout():
    """
    Create layout of the home component
    """

    # Create layout
    content = create_home_content()
    sidebar = create_home_sidebar()

    # Register callbacks
    register_home_callbacks()

    return (content, sidebar)
