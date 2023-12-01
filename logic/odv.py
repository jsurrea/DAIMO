import networkx as nx
from tqdm import tqdm
from collections import defaultdict

def calculate_odv_parameters(data_model):
    """
    Calculate cost and bridges of the road network for each ODV.
    """

    odv_df = data_model.od
    bridges_df = data_model.puentes
    G = data_model.G

    bridge_edges = bridges_df.apply(lambda row: (row["source"], row["target"]), axis = 1)
    
    cost_by_odv = {}
    odv_by_bridge = {bridge: set() for bridge in bridges_df.id_puente.unique()}
    flow_by_edge = defaultdict(int)
    affected_flows_by_odv = defaultdict(list)

    for nodo_origen, nodo_destino, vehiculo, demanda in tqdm(odv_df.itertuples(index=False, name=None), desc="Calculating ODV parameters", total=len(odv_df)):

        if (nodo_origen, nodo_destino, vehiculo) in cost_by_odv:
            continue

        multi_target = odv_df.nodo_destino[(odv_df.nodo_origen == nodo_origen) & (odv_df.vehiculo == vehiculo)].tolist()
        distance_all, path_all = nx.single_source_dijkstra(G, source=nodo_origen, weight=vehiculo)

        for nodo_destino in multi_target:

            distance = distance_all[nodo_destino]
            path = path_all[nodo_destino]

            cost = distance * demanda
            cost_by_odv[(nodo_origen, nodo_destino, vehiculo)] = cost

            edges_path = set((min(i,j), max(i,j)) for i,j in zip(path, path[1:]))
            for bridge_affected in bridges_df.id_puente[bridge_edges.isin(edges_path)]:
                odv_by_bridge[bridge_affected].add((nodo_origen, nodo_destino, vehiculo))

            multiplier = 3 if vehiculo == "C-2" else 4 if vehiculo == "C-3-4" else 5
            demanda_equivalente = demanda * multiplier

            for i,j in edges_path:
                flow_by_edge[i,j] += demanda_equivalente
                affected_flows_by_odv[nodo_origen, nodo_destino, vehiculo].append((i,j,demanda_equivalente))

    print("Total cost:", base_cost)
    return cost_by_odv, odv_by_bridge, flow_by_edge, affected_flows_by_odv
