from collections import namedtuple, defaultdict
from .model import DataModel
from .costs import calculate_intervention_cost

def has_data():
    """
    Check if the data has been loaded
    """
    data_model = DataModel()
    return data_model.principal is not None

def get_puentes():
    """
    Get the puentes
    """
    data_model = DataModel()
    if data_model.puentes is None:
        return []
    return data_model.puentes.id_puente.unique().tolist()

def get_base_cost():
    """
    Get the base cost
    """
    data_model = DataModel()
    return data_model.base_cost

def get_puentes_criticos_content_data(puentes_to_show):
    """
    Get the data for the puentes_criticos component
    """

    data_model = DataModel()
    
    PuenteCriticoData = namedtuple(
        "PuenteCriticoData", 
        [
            "puente", 
            "costo_excedente", 
            "porcentaje_excedente", 
            "latitudes", 
            "longitudes",
        ],
    )

    if any([
        data_model.intervention_costs is None,
        data_model.base_cost is None,
        data_model.puentes is None,
    ]):
        return []

    puentes_criticos_data = []
    for puente in puentes_to_show:
        costo_excedente = data_model.intervention_costs[puente]
        porcentaje_excedente = costo_excedente / data_model.base_cost
        source = data_model.puentes[data_model.puentes.id_puente == puente].source.values[0]
        target = data_model.puentes[data_model.puentes.id_puente == puente].target.values[0]
        latitudes = (source.split("/")[0], target.split("/")[0])
        longitudes = (source.split("/")[1], target.split("/")[1])
        puentes_criticos_data.append(
            PuenteCriticoData(
                puente = puente,
                costo_excedente = costo_excedente,
                porcentaje_excedente = porcentaje_excedente,
                latitudes = latitudes,
                longitudes = longitudes,
            ),
        )

    return puentes_criticos_data


def get_non_bridge_edges(puentes_to_show):
    """
    Get the non bridge edges
    """
    data_model = DataModel()
    if data_model.flow_by_edge is None:
        return []

    flow_by_node = defaultdict(int)

    non_bridge_edges_data = []
    for i,j in data_model.flow_by_edge:

        flow = data_model.flow_by_edge[i,j]

        flow_by_node[i] += flow
        flow_by_node[j] += flow

        i,j = min(i,j), max(i,j)
        if (i,j) in puentes_to_show:
            continue

        latitud = (i.split("/")[0], j.split("/")[0])
        longitud = (i.split("/")[1], j.split("/")[1])

        non_bridge_edges_data.append(
            (latitud, longitud),
        )

    return non_bridge_edges_data, flow_by_node


def get_intervenciones_simultaneas_data(puentes_to_show):
    """
    Get the data for the intervenciones_simultaneas component
    """

    data_model = DataModel() # TODO bridge_data, edge_data, additional_cost

    # Data hasn't been loaded yet
    if data_model.flow_by_edge is None:
        return [], [], 0

    if len(puentes_to_show) == 0:
        return [], [], 0
        
    additional_cost, flows = calculate_intervention_cost(puentes_to_show, data_model)
    
    edge_data = []
    for edge in flows:

        source = edge[0]
        target = edge[1]
        latitudes = (source.split("/")[0], target.split("/")[0])
        longitudes = (source.split("/")[1], target.split("/")[1])
        flow_before = data_model.flow_by_edge[edge]
        flow_after = flows[edge]
        flow_change = flow_after - flow_before

        edge_data.append(
            (latitudes, longitudes, flow_change, flow_before, flow_after)
        )

    bridge_data = []
    for puente in set(puentes_to_show):
        source = data_model.puentes[data_model.puentes.id_puente == puente].source.values[0]
        target = data_model.puentes[data_model.puentes.id_puente == puente].target.values[0]
        latitudes = (source.split("/")[0], target.split("/")[0])
        longitudes = (source.split("/")[1], target.split("/")[1])
        bridge_data.append(
            (puente, latitudes, longitudes)
        )

    return bridge_data, edge_data, additional_cost
