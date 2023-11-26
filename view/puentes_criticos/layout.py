from .content import create_puentes_criticos_content
from .sidebar import create_puentes_criticos_sidebar

def create_puentes_criticos_layout(app):
    """
    Create layout of the puentes_criticos component
    """

    # Create layout
    content = create_puentes_criticos_content(app)
    sidebar = create_puentes_criticos_sidebar(app)

    return (content, sidebar)
