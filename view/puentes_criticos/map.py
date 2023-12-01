import locale
from dash import dcc
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from matplotlib.colors import Normalize
from plotly.graph_objects import Layout
from plotly.validator_cache import ValidatorCache
from plotly.validators import DataValidator
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def render_map(map_data, edge_data, flow_by_node):
    """
    Render the map of the bridges and their costs
    """

    # Create a figure with scattermapbox trace for points
    fig = go.Figure()

    if len(map_data) > 0:

        # Unpack the data for better performance
        latitudes, longitudes, flujo = [], [], []
        for lat, lon in edge_data:
            latitudes.append(lat[0])
            latitudes.append(lat[1])
            latitudes.append(None)
            longitudes.append(lon[0])
            longitudes.append(lon[1])
            longitudes.append(None)
            flujo.append(f'Flujo de vehículos equivalente: {int(flow_by_node[lat[0] + "/" + lon[0]])}')
            flujo.append(f'Flujo de vehículos equivalente: {int(flow_by_node[lat[1] + "/" + lon[1]])}')
            flujo.append(None)

        # Paint the edges that are not bridges
        fig.add_trace(
            go.Scattermapbox(
                mode="lines+markers",
                lat=latitudes,
                lon=longitudes,
                hovertext = flujo,
                line=dict(color="hsla(240, 100%, 80%, 1)"),
                marker=dict(color="hsla(240, 100%, 80%, 1)", opacity=0.1, allowoverlap=False),
                showlegend=False,
            )
        )

        # Create a colormap between green, yellow, and red
        norm = Normalize(vmin = min(item.porcentaje_excedente for item in map_data), vmax = max(item.porcentaje_excedente for item in map_data))
        colormap = plt.cm.get_cmap("RdYlGn")

        for (
            puente, 
            costo_excedente, 
            porcentaje_excedente, 
            latitudes, 
            longitudes,
        ) in map_data:
            # Map cost to a color in the colormap
            color = f'rgba{tuple(int(255 * c) for c in colormap(1 - norm(porcentaje_excedente)))}' 

            # Add scattermapbox trace for the bridge start and end coordinates
            fig.add_trace(
                go.Scattermapbox(
                    mode = "lines+markers",
                    lat = latitudes,
                    lon = longitudes,
                    hovertext = "<br>".join([
                        f"Puente {puente}",
                        f"Costo excedente por intervención: {locale.currency(costo_excedente, grouping = True)}",
                        f"Porcentaje excedente por intervención: {porcentaje_excedente*100:.5f}%",
                        f"Flujo de vehículos equivalente: {int(flow_by_node[latitudes[0] + '/' + longitudes[0]])}",
                    ]),
                    marker = dict(color = color, size = 6),
                    line = dict(color = color, width = 4),
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
