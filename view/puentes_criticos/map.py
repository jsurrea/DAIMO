import locale
from dash import dcc
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from matplotlib.colors import Normalize
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def render_map(map_data):
    """
    Render the map of the bridges and their costs
    """

    # Create a figure with scattermapbox trace for points
    fig = go.Figure()

    if len(map_data) > 0:

        # Create a colormap between green, yellow, and red
        norm = Normalize(vmin = 0, vmax = max(item.porcentaje_excedente for item in map_data))
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
                    name = f"Puente {puente}",
                    hovertext = "<br>".join([
                        f"Costo excedente por intervención: {locale.currency(costo_excedente, grouping = True)}",
                        f"Porcentaje excedente por intervención: {porcentaje_excedente*100:.5f}%",
                    ]),
                    marker = dict(color = color),
                    line = dict(color = color, width = 2),
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
