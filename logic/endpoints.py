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

#TODO: Implementar endpoints para obtener los datos de los reportes
def get_puentes_criticos_content_data():
    """
    Get the data for the puentes_criticos component
    """
    
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

    return [
        PuenteCriticoData(
            puente = "1",
            costo_excedente = 100000,
            porcentaje_excedente = 0.1,
            longitudes = (-73.807117, -73.793354),
            latitudes = (5.318413, 5.347274),
        ),
        PuenteCriticoData(
            puente = "2",
            costo_excedente = 200000,
            porcentaje_excedente = 0.2,
            longitudes = (-73.793354, -73.788623),
            latitudes = (5.347274, 5.359037),
        ),
        PuenteCriticoData(
            puente = "3",
            costo_excedente = 300000,
            porcentaje_excedente = 0.3,
            longitudes = (-73.788623, -73.781019),
            latitudes = (5.359037, 5.373800),
        ),
        PuenteCriticoData(
            puente = "4",
            costo_excedente = 400000,
            porcentaje_excedente = 0.4,
            longitudes = (-73.781019, -73.772415),
            latitudes = (5.373800, 5.388563),
        ),
        PuenteCriticoData(
            puente = "5",
            costo_excedente = 500000,
            porcentaje_excedente = 0.5,
            longitudes = (-73.772415, -73.765811),
            latitudes = (5.388563, 5.403326),
        ),
        PuenteCriticoData(
            puente = "6",
            costo_excedente = 600000,
            porcentaje_excedente = 0.6,
            longitudes = (-73.765811, -73.758207),
            latitudes = (5.403326, 5.418089),
        ),
        PuenteCriticoData(
            puente = "7",
            costo_excedente = 700000,
            porcentaje_excedente = 0.7,
            longitudes = (-73.758207, -73.750603),
            latitudes = (5.418089, 5.432852),
        ),
        PuenteCriticoData(
            puente = "8",
            costo_excedente = 800000,
            porcentaje_excedente = 0.8,
            longitudes = (-73.750603, -73.743999),
            latitudes = (5.432852, 5.447615),
        ),
        PuenteCriticoData(
            puente = "9",
            costo_excedente = 900000,
            porcentaje_excedente = 0.9,
            longitudes = (-73.743999, -73.736395),
            latitudes = (5.447615, 5.462378),
        ),
        PuenteCriticoData(
            puente = "10",
            costo_excedente = 1000000,
            porcentaje_excedente = 1.0,
            longitudes = (-73.736395, -73.728791),
            latitudes = (5.462378, 5.477141),
        ),
    ]

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
