import locale
import numpy as np
from dash import dcc
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from matplotlib.colors import Normalize
from logic import get_intervenciones_simultaneas_data
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def render_map(bridge_data, edge_data):
    """
    Render the map of the simulation
    edge_data only contains the edges whose flow changed
    """

    # Create a figure with scattermapbox trace for points
    fig = go.Figure()

    if  len(edge_data) > 0:

        print(f"Found {len(edge_data)} affected edges")

        # Paint the edges that were affected by the intervention
        # Create a divergent colormap to map the flow change to a color
        # coolwarm: 0 is blue, 0.5 is white, 1 is red
        # Alternative: vabs = max(-min(item[2] for item in edge_data), max(item[2] for item in edge_data))
        vmax = max(item[2] for item in edge_data)
        vmin = min(item[2] for item in edge_data)
        norm_positive = Normalize(vmin = 0, vmax = vmax)
        norm_negative = Normalize(vmin = vmin, vmax = 0)
        norm = lambda x: (1 + norm_positive(x))/2 if x >= 0 else norm_negative(x)/2
        colormap = plt.colormaps.get_cmap("coolwarm") 

        # For performance, classify the data by a range of its colormap value
        # This way, we can create a single trace for each range
        # and avoid creating a trace for each edge
        color_ranges = {}
        bins = np.linspace(0, 1, 15)
        bins[-1] += 1e-9
        range_by_edge = np.digitize([norm(item[2]) for item in edge_data], bins)

        for edge_info, range_index in zip(edge_data, range_by_edge):
            color_ranges.setdefault(range_index, []).append(edge_info)

        for edge_data_list in color_ranges.values():

            mean_flow_change = np.mean([item[2] for item in edge_data_list])
            mean_color = colormap(norm(mean_flow_change))
            color = f'rgba{tuple(int(255 * c) for c in mean_color)}'
        
            # Unpack the data for better performance
            latitudes, longitudes, hovertexts = [], [], []
            for lat, lon, flow_change, flow_before, flow_after in edge_data_list:

                latitudes.append(lat[0])
                latitudes.append(lat[1])
                latitudes.append(None)

                longitudes.append(lon[0])
                longitudes.append(lon[1])
                longitudes.append(None)

                text = "<br>".join([
                    f"Cambio del Flujo de vehículos equivalentes: {flow_change/100:.3f}%",
                    f"Flujo de vehículos antes: {flow_before}",
                    f"Flujo de vehículos después: {flow_after}",
                ])
                hovertexts.append(text)
                hovertexts.append(text)
                hovertexts.append(None)

            # Add scattermapbox trace for the edge start and end coordinates
            fig.add_trace(
                go.Scattermapbox(
                    mode = "lines+markers",
                    lat = latitudes,
                    lon = longitudes,
                    hovertext = hovertexts,
                    marker = dict(color = color),
                    line = dict(color = color),
                    showlegend = False,
                )
            )
    if len(bridge_data) > 0:

        # Paint the bridges
        # Unpack the data for better performance
        latitudes, longitudes, bridges = [], [], []
        for bridge, lat, lon in bridge_data:

            latitudes.append(lat[0])
            latitudes.append(lat[1])
            latitudes.append(None)

            longitudes.append(lon[0])
            longitudes.append(lon[1])
            longitudes.append(None)

            bridges.append(bridge)
            bridges.append(bridge)
            bridges.append(None)

        # Paint the bridges
        fig.add_trace(
            go.Scattermapbox(
                mode = "lines+markers",
                lat = latitudes,
                lon = longitudes,
                hovertext = bridges,
                line = dict(color = "black", width = 4),
                marker = dict(color = "black", size = 8),
                showlegend = False,
            )
        )

    # Default map
    else:
        fig.add_trace(go.Scattermapbox(showlegend = False))

    # Set the layout properties
    fig.update_layout(
        mapbox_style = "carto-positron",
        mapbox_center = {"lat": 6, "lon": -73},
        mapbox_zoom = 7,
        margin = {"r": 0, "t": 0, "l": 0, "b": 0},
    )
    
    return dcc.Graph(figure = fig)
