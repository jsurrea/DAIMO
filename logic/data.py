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
        data_model = DataModel()
        data_model.principal = dfs["principal"]
        data_model.od = dfs["od"]
        data_model.puentes = dfs["puentes"]

        G = create_graph(data_model)
        data_model.G = G

        cost_by_odv, odv_by_bridge, flow_by_edge, affected_flows_by_odv = calculate_odv_parameters(data_model)
        data_model.cost_by_odv = cost_by_odv
        data_model.odv_by_bridge = odv_by_bridge
        data_model.flow_by_edge = flow_by_edge
        data_model.affected_flows_by_odv = affected_flows_by_odv

        base_cost, intervention_costs = calculate_initial_costs(data_model)
        data_model.base_cost = base_cost
        data_model.intervention_costs = intervention_costs

        save_new_data(data_model, filename.replace(".xlsx", ".pkl"))
        print(f"Data loaded successfully into {filename.replace('.xlsx', '')}")

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


def load_saved_data(filename):
    """
    Load data previously saved in the application
    """
    filepath = os.path.join("data", f"{filename}.pkl")
    with open(filepath, "rb") as f:
        data_model = pickle.load(f)
    print(f"Data loaded successfully from {filename}")
    DataModel.update(data_model)
