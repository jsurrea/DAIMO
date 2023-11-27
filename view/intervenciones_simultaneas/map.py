import locale
from dash import dcc
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from logic import get_puentes_criticos_content_data #TODO
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def render_map():
    """
    Render the map of the simulation
    """
    # TODO
    
    # Get the data from the model
    data = get_puentes_criticos_content_data()

    # Create a figure with scattermapbox trace for points
    fig = go.Figure()

    for (
        puente, 
        costo_excedente, 
        porcentaje_excedente, 
        latitudes, 
        longitudes,
    ) in data:

        # Add scattermapbox trace for the bridge start and end coordinates
        fig.add_trace(
            go.Scattermapbox(
                mode = "lines+markers",
                lat = latitudes,
                lon = longitudes,
                name = f"Puente {puente}",
                hovertext = "<br>".join([
                    f"Costo excedente por intervención: {locale.currency(costo_excedente, grouping = True)}",
                    f"Porcentaje excedente por intervención: {porcentaje_excedente*100:.5f}%",
                ]),
                #marker = dict(color = color), TODO
                #line = dict(color = color, width = 2), TODO
                showlegend = False,
            )
        )
    
    # Set the layout properties
    fig.update_layout(
        mapbox_style = "carto-positron",
        mapbox_center = {"lat": 4, "lon": -72},
        mapbox_zoom = 5,
        margin = {"r": 0, "t": 0, "l": 0, "b": 0},
    )
    
    return dcc.Graph(figure = fig)
