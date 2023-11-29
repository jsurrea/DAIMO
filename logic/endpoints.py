from collections import namedtuple
from .model import DataModel

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

#TODO: Implementar endpoints para obtener los datos de los reportes
def get_intervenciones_simultaneas_map_data():
    """
    Get the data for the intervenciones_simultaneas map component
    """

    FlujoArcoData = namedtuple(
        "FlujoArcoData", 
        [
            "latitudes",
            "longitudes", 
            "flujo",
        ],
    )

    return [
        FlujoArcoData(
            latitudes = (5.318413, 5.347274),
            longitudes = (-73.807117, -73.793354),
            flujo = 100,
        ),
        FlujoArcoData(
            latitudes = (5.347274, 5.359037),
            longitudes = (-73.793354, -73.788623),
            flujo = 200,
        ),
        FlujoArcoData(
            latitudes = (5.359037, 5.373800),
            longitudes = (-73.788623, -73.781019),
            flujo = 300,
        ),
        FlujoArcoData(
            latitudes = (5.373800, 5.388563),
            longitudes = (-73.781019, -73.772415),
            flujo = 400,
        ),
        FlujoArcoData(
            latitudes = (5.388563, 5.403326),
            longitudes = (-73.772415, -73.765811),
            flujo = 500,
        ),
        FlujoArcoData(
            latitudes = (5.403326, 5.418089),
            longitudes = (-73.765811, -73.758207),
            flujo = 600,
        ),
        FlujoArcoData(
            latitudes = (5.418089, 5.432852),
            longitudes = (-73.758207, -73.750603),
            flujo = 700,
        ),
        FlujoArcoData(
            latitudes = (5.432852, 5.447615),
            longitudes = (-73.750603, -73.743999),
            flujo = 800,
        ),
        FlujoArcoData(
            latitudes = (5.447615, 5.462378),
            longitudes = (-73.743999, -73.736395),
            flujo = 900,
        ),
        FlujoArcoData(
            latitudes = (5.462378, 5.477141),
            longitudes = (-73.736395, -73.728791),
            flujo = 1000,
        ),
    ]
