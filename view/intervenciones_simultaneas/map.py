import locale
from dash import dcc
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from logic import get_intervenciones_simultaneas_data
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def render_map(map_data):
    """
    Render the map of the simulation
    """
    
    # Create a figure with scattermapbox trace for points
    fig = go.Figure()

    # Unpack the data for better performance
    latitudes, longitudes, flujo = [], [], []
    for lat, lon, flow in map_data:
        latitudes.append(lat[0])
        latitudes.append(lat[1])
        latitudes.append(None)
        longitudes.append(lon[0])
        longitudes.append(lon[1])
        longitudes.append(None)
        flujo.append(flow)
        flujo.append(flow)

    # Add a single scattermapbox trace for all edges
    fig.add_trace(
        go.Scattermapbox(
            mode="lines",
            lat=latitudes,
            lon=longitudes,
            line=dict(color="blue"),#, width=[f / 100 for f in flujo]),
            showlegend=False,
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
