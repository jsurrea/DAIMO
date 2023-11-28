import pandas as pd
import pdb, traceback, sys, base64, io, os
from .graph import create_graph
from .odv import calculate_odv_parameters
from .dataframes import clean_dataframes
from .costs import calculate_initial_costs

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
        G = create_graph(dfs["principal"])
        cost_by_odv, odv_by_bridge = calculate_odv_parameters(dfs["od"], dfs["puentes"], G)
        base_cost, intervention_costs = calculate_initial_costs(cost_by_odv, odv_by_bridge, dfs["puentes"], dfs["od"], G)
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

def save_new_data(data, base_dir):
    """
    Save data in the application
    """
    save_dir = os.path.join("data", base_dir)

def load_saved_data():
    """
    Load data previously saved in the application
    """
    ...
