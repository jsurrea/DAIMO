from .content import create_intervenciones_simultaneas_content
from .sidebar import create_intervenciones_simultaneas_sidebar

def create_intervenciones_simultaneas_layout():
    """
    Create layout of the intervenciones_simultaneas component
    """

    # Create layout
    content = create_intervenciones_simultaneas_content()
    sidebar = create_intervenciones_simultaneas_sidebar()

    return (content, sidebar)
