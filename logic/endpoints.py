from collections import namedtuple
from .model import DataModel
from .costs import calculate_intervention_cost

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


def get_intervenciones_simultaneas_data(puentes_to_show):
    """
    Get the data for the intervenciones_simultaneas component
    """

    data_model = DataModel()

    FlowEdgeData = namedtuple(
        "FlowEdgeData", 
        [
            "latitudes",
            "longitudes", 
            "flujo",
        ],
    )

    # Data hasn't been loaded yet
    if data_model.flow_by_edge is None:
        return [], 0

    if len(puentes_to_show) == 0:
        additional_cost, flows = 0, data_model.flow_by_edge
    else:
        additional_cost, flows = calculate_intervention_cost(puentes_to_show, data_model)
    
    flow_data = []
    print("hola", data_model.flow_by_edge)
    for edge in flows:
        source = edge[0]
        target = edge[1]
        latitudes = (source.split("/")[0], target.split("/")[0])
        longitudes = (source.split("/")[1], target.split("/")[1])
        flujo = flows[edge]
        flow_data.append(
            FlowEdgeData(
                latitudes = latitudes,
                longitudes = longitudes,
                flujo = flujo,
            ),
        )

    return flow_data, additional_cost
