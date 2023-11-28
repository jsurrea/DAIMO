import networkx as nx
from tqdm import tqdm

def calculate_odv_parameters(odv_df, bridges_df, G):
    """
    Calculate cost and bridges of the road network for each ODV.
    """
    
    cost_by_odv = {}
    odv_by_bridge = {bridge: set() for bridge in bridges_df.id_puente.unique()}

    for nodo_origen, nodo_destino, vehiculo, demanda in tqdm(odv_df.itertuples(index=False, name=None), desc="Calculating ODV parameters", total=len(odv_df)):

        distance, path = nx.single_source_dijkstra(G, source=nodo_origen, target=nodo_destino, weight=vehiculo)
        cost = distance * demanda
        cost_by_odv[(nodo_origen, nodo_destino, vehiculo)] = cost

        edges_path = set((min(i,j), max(i,j)) for i,j in zip(path, path[1:]))
        for bridge_affected in bridges_df.id_puente[bridges_df.apply(lambda row: (row["source"], row["target"]), axis = 1).isin(edges_path)]:
            odv_by_bridge[bridge_affected].add((nodo_origen, nodo_destino, vehiculo))

    return cost_by_odv, odv_by_bridge

