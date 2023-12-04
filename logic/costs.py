import networkx as nx
from tqdm import tqdm

def calculate_initial_costs(data_model):
    """
    Calculate initial costs of the road network.
    """

    cost_by_odv = data_model.cost_by_odv
    odv_by_bridge = data_model.odv_by_bridge
    bridges_df = data_model.puentes
    odv_df = data_model.od
    G = data_model.G

    base_cost = sum(cost_by_odv.values())
    intervention_costs = {}
    for bridge in tqdm(bridges_df.id_puente.unique(), desc="Calculating intervention costs", total=len(bridges_df.id_puente.unique())):
        intervention_costs[bridge], _ = calculate_intervention_cost([bridge], data_model)
    return base_cost, intervention_costs


def calculate_intervention_cost(bridges, data_model):
    """
    Calculate difference of cost of the road network after an intervention.
    """

    cost_by_odv = data_model.cost_by_odv
    odv_by_bridge = data_model.odv_by_bridge
    bridges_df = data_model.puentes
    odv_df = data_model.od
    G = data_model.G
    flow_by_edge = data_model.flow_by_edge.copy()
    affected_flows_by_odv = data_model.affected_flows_by_odv

    edge_data = {}
    changed_odvs = set()
    for bridge in set(bridges):
        changed_odvs |= odv_by_bridge[bridge]
        source = bridges_df[bridges_df.id_puente == bridge].source.values[0]
        target = bridges_df[bridges_df.id_puente == bridge].target.values[0]
        edge_data[source, target] = G.get_edge_data(source, target)
        G.remove_edge(source, target)

    old_cost = sum(cost_by_odv[odv] for odv in changed_odvs)
    new_cost = 0

    calculated_odvs = set()

    for nodo_origen, nodo_destino, vehiculo in changed_odvs:

        if (nodo_origen, nodo_destino, vehiculo) in calculated_odvs:
            continue

        multi_target = odv_df.nodo_destino[(odv_df.nodo_origen == nodo_origen) & (odv_df.vehiculo == vehiculo)].tolist()
        distance_all, path_all = nx.single_source_dijkstra(G, source=nodo_origen, weight=vehiculo)

        for nodo_destino in multi_target:

            if nodo_destino not in distance_all:
                print(f"Warning: {nodo_origen} -> {nodo_destino} not connected")
                continue

            for i,j,flow_to_remove in affected_flows_by_odv[nodo_origen, nodo_destino, vehiculo]:
                if flow_by_edge[i,j] - flow_to_remove < 0:
                    print(f"Warning: {i} -> {j} flow is negative by {flow_by_edge[i,j] - flow_to_remove}")
                    flow_by_edge[i,j] = 0
                else:
                    flow_by_edge[i,j] -= flow_to_remove

            distance = distance_all[nodo_destino]
            path = path_all[nodo_destino]
            demanda = odv_df[(odv_df.nodo_origen == nodo_origen) & (odv_df.nodo_destino == nodo_destino) & (odv_df.vehiculo == vehiculo)].demanda.values[0]
            
            cost = distance * demanda
            new_cost += cost

            multiplier = 3 if vehiculo == "C-2" else 4 if vehiculo == "C-3-4" else 5
            demanda_equivalente = demanda * multiplier
            edges_path = set((min(i,j), max(i,j)) for i,j in zip(path, path[1:]))
            for i,j in edges_path:
                flow_by_edge[i,j] += demanda_equivalente

            calculated_odvs.add((nodo_origen, nodo_destino, vehiculo))

    for i,j in edge_data.keys():
        G.add_edge(i,j, **edge_data[i,j])

    return new_cost - old_cost, flow_by_edge 
