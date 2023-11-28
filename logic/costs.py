import networkx as nx


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
        intervention_costs[bridge] = calculate_intervention_costs([bridge], data_model)
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

    for nodo_origen, nodo_destino, vehiculo in changed_odvs:
        demanda = odv_df[(odv_df.nodo_origen == nodo_origen) & (odv_df.nodo_destino == nodo_destino) & (odv_df.vehiculo == vehiculo)].demanda.values[0]
        distance, path = nx.single_source_dijkstra(G, source=nodo_origen, target=nodo_destino, weight=vehiculo)
        cost = distance * demanda
        new_cost += cost

    for i,j in edge_data.keys():
        G.add_edge(i,j, **edge_data[i,j])

    return new_cost - old_cost
