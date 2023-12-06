import networkx as nx
from tqdm import tqdm
from collections import defaultdict

def calculate_costs_flows_for_odvs(data_model):
    """
    Calculate cost and flows of the road network.
    """

    bridges_df = data_model.puentes
    odv_df = data_model.od
    principal = data_model.principal
    G = data_model.G

    bridge_edges = bridges_df.apply(lambda row: (row["source"], row["target"]), axis = 1)
    
    already_checked = set()
    flow_by_edge = {(s,t): 0 for s,t in zip(principal.source, principal.target)}

    total_cost = 0

    for nodo_origen, nodo_destino, vehiculo, demanda in tqdm(odv_df.itertuples(index=False, name=None), desc="Calculating ODV parameters", total=len(odv_df)):

        if (nodo_origen, nodo_destino, vehiculo) in already_checked:
            continue

        multi_target = odv_df.nodo_destino[(odv_df.nodo_origen == nodo_origen) & (odv_df.vehiculo == vehiculo)].tolist()
        distance_all, path_all = nx.single_source_dijkstra(G, source=nodo_origen, weight=vehiculo)

        for nodo_destino in multi_target:

            if nodo_destino not in distance_all:
                raise Exception(f"El nodo {nodo_destino} no es alcanzable desde el nodo {nodo_origen} con el vehículo {vehiculo}") 

            distance = distance_all[nodo_destino]
            path = path_all[nodo_destino]

            cost = distance * demanda
            total_cost += cost

            already_checked.add((nodo_origen, nodo_destino, vehiculo))

            edges_path = set((min(i,j), max(i,j)) for i,j in zip(path, path[1:]))

            multiplier = 3 if vehiculo == "C-2" else 4 if vehiculo == "C-3-4" else 5
            demanda_equivalente = demanda * multiplier

            for i,j in edges_path:
                flow_by_edge[i,j] += demanda_equivalente

    return total_cost, flow_by_edge
