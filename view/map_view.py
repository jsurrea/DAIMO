import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Example for US dollars

from model.model import Model



def render_map():
    
    # Load model
    model = Model.get_model()
    coords = model.get_coords()
    costs = model.get_base_costs()
    
    # Create a figure with scattermapbox trace for points
    fig = go.Figure()

    # Create a colormap between green, yellow, and red
    costo_excedente_values = [cost[1]/cost[0] for p, cost in costs.items() if p != "TOTAL"]
    norm = Normalize(vmin=0, vmax=max(costo_excedente_values))
    colormap = plt.cm.get_cmap("RdYlGn")

    for puente in model.get_puentes():

        if not puente in coords:
            continue
        coord_dict = coords.get(puente)
        costs_tuple = costs.get(puente)
        costoTotal = locale.currency(costs_tuple[0], grouping=True)
        costoExced = costs_tuple[1]/costs_tuple[0]
        hover_text = f"Puente {puente}<br>Costo Total: {costoTotal}<br>Costo Excedente: {costoExced*100:.5f}%"

        # Map costoExcedente to a color in the colormap
        color = f'rgba{tuple(int(255 * c) for c in colormap(1 - norm(costs_tuple[1]/costs_tuple[0])))}' 

        # Add scattermapbox trace for the bridge start and end coordinates
        fig.add_trace(
            go.Scattermapbox(
                mode="lines+markers",
                lat=(coord_dict["start_lat"], coord_dict["end_lat"]),
                lon=(coord_dict["start_lon"], coord_dict["end_lon"]),
                name="",
                hovertext=hover_text,
                marker=dict(color=color),
                line=dict(color=color, width=2),
                showlegend=False,  # Hide the legend for this trace
            )
        )
    
    # Set the layout properties
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_center={"lat": 4, "lon": -72},
        mapbox_zoom=5,
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
    )
    
    return dcc.Graph(figure=fig)
