class DataModel:
    """
    Singleton class to store data
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Create a new instance of the class if it doesn't exist
        """
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """
        Initialize the class
        """
        if not hasattr(self, 'initialized'):
            self.initialized = True

            # Dataframes  
            self.principal = None
            self.od = None
            self.puentes = None

            # Graph
            self.G = None

            # ODV
            self.cost_by_odv = None
            self.odv_by_bridge = None
            self.flow_by_edge = None
            self.affected_flows_by_odv = None

            # Costs
            self.base_cost = None
            self.intervention_costs = None


    @staticmethod
    def update(new_data_model):
        """
        Update the data model with new data
        """
        if not DataModel._instance:
            old_data_model = DataModel()
        else:
            old_data_model = DataModel._instance

        old_data_model.initialized = new_data_model.initialized

        old_data_model.principal = new_data_model.principal
        old_data_model.od = new_data_model.od
        old_data_model.puentes = new_data_model.puentes

        old_data_model.G = new_data_model.G
        
        old_data_model.cost_by_odv = new_data_model.cost_by_odv
        old_data_model.odv_by_bridge = new_data_model.odv_by_bridge
        old_data_model.flow_by_edge = new_data_model.odv_by_bridge
        old_data_model.affected_flows_by_odv = new_data_model.odv_by_bridge

        old_data_model.base_cost = new_data_model.base_cost
        old_data_model.intervention_costs = new_data_model.intervention_costs
    
    