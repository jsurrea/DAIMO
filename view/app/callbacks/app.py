from ..styles import get_visible_styles, get_hidden_styles

hidden_styles = get_hidden_styles()
visible_styles = get_visible_styles()
    
def toggle_sidebar(n):
    """
    Toggle sidebar visibility
    """
    return hidden_styles if n is None or n % 2 == 0 else visible_styles
