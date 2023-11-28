import networkx as nx

def create_graph(data_model):
    """
    Create a graph from the dataframes
    """

    print("Creating graph")
    edges_df = data_model.principal
    G = nx.from_pandas_edgelist(
        df = edges_df,
        source = "source",
        target = "target",
        edge_attr = ["C-2", "C-3-4", "C-5", ">C-5"],
    )
    return G
    