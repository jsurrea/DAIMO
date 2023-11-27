import dash_bootstrap_components as dbc

def create_navbar_layout():
    """
    Create layout of the navbar component
    """

    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                dbc.NavLink(
                    children = "Puentes Críticos",
                    active = "exact",
                    href = "/puentes-criticos",
                ),
            ),
            dbc.NavItem(
                dbc.NavLink(
                    children = "Intervenciones Simultáneas",
                    active = "exact",
                    href = "/intervenciones-simultaneas",
                ),
            ),
            dbc.Button(
                children = "Configuración", 
                outline = True, 
                color = "secondary", 
                className = "mr-1", 
                id = "btn-sidebar"
            ),
        ],
        brand = dbc.NavItem(
            dbc.NavLink(
                children = "DAIMO",
                active = "exact",
                href = "/",
            ),
        ),
        color = "dark",
        dark = True,
        fluid = True,
    )
    
    return navbar
