class DataModel:
    """
    Static shared class for all the application models.
    """
    
    def __init__(self):
        raise Exception("This class is static and should not be instantiated")

    # Dataframes  
    principal = None
    od = None
    puentes = None

    # Graph
    G = None

    # ODV
    cost_by_odv = None
    odv_by_bridge = None

    # Costs
    base_cost = None
    intervention_costs = None
    