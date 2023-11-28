import pickle
import pandas as pd
import pdb, traceback, sys, base64, io, os
from .graph import create_graph
from .odv import calculate_odv_parameters
from .dataframes import clean_dataframes
from .costs import calculate_initial_costs
from .model import DataModel

def load_new_data(contents, filename):
    """
    Load a new data file
    """
    if not filename.endswith(".xlsx"):
        raise ValueError("El archivo debe ser de tipo Excel (.xlsx)")
    
    # Try to load the file
    try:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        dfs = pd.read_excel(
            io.BytesIO(decoded), 
            sheet_name = ["principal", "od", "puentes"],
        )

        dfs = clean_dataframes(dfs)
        DataModel.principal = dfs["principal"]
        DataModel.od = dfs["od"]
        DataModel.puentes = dfs["puentes"]

        G = create_graph(DataModel)
        DataModel.G = G

        cost_by_odv, odv_by_bridge, flow_by_edge, affected_flows_by_odv = calculate_odv_parameters(DataModel)
        DataModel.cost_by_odv = cost_by_odv
        DataModel.odv_by_bridge = odv_by_bridge
        DataModel.flow_by_edge = flow_by_edge
        DataModel.affected_flows_by_odv = affected_flows_by_odv

        base_cost, intervention_costs = calculate_initial_costs(DataModel)
        DataModel.base_cost = base_cost
        DataModel.intervention_costs = intervention_costs

        save_new_data(DataModel, filename.replace(".xlsx", ".pkl"))
        print("Data loaded successfully")

    # Handle exceptions with debbuger
    except:
        exception_type, exception_object, traceback_object = sys.exc_info()
        print(f"Exception Type: {exception_type}")
        print(f"Exception Object: {exception_object}")
        print(f"Traceback Object: {traceback_object}")
        traceback.print_exc()
        pdb.post_mortem(traceback_object)
        raise exception_object


def save_new_data(data, filename):
    """
    Save data in the application
    """
    os.makedirs("data", exist_ok=True)
    filepath = os.path.join("data", filename)
    with open(filepath, "wb") as f:
        pickle.dump(data, f)


def load_saved_data():
    """
    Load data previously saved in the application
    """
    ...
