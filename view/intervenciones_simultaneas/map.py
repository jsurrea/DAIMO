import locale
from dash import dcc
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from logic import get_intervenciones_simultaneas_map_data
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def render_map():
    """
    Render the map of the simulation
    """
    # TODO
    
    # Get the data from the model
    data = get_intervenciones_simultaneas_map_data()

    # Create a figure with scattermapbox trace for points
    fig = go.Figure()

    for (
        latitudes, 
        longitudes, 
        flujo
    ) in data:

        # Add scattermapbox trace for the bridge start and end coordinates
        fig.add_trace(
            go.Scattermapbox(
                mode = "lines",
                lat = latitudes,
                lon = longitudes,
                #marker = dict(color = color), TODO
                line = dict(color = "blue", width = flujo / 100), #TODO
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
