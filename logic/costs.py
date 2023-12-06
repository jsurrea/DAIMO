import networkx as nx
from tqdm import tqdm
from .odv import calculate_costs_flows_for_odvs 

def calculate_initial_costs(data_model):
    """
    Calculate initial costs of the road network.
    """

    base_cost, flow_by_edge = calculate_costs_flows_for_odvs(data_model)
    print("Base cost:", base_cost)
    id_puentes = data_model.puentes.id_puente.unique()
    intervention_costs = {}
    for bridge in tqdm(id_puentes, desc="Calculating intervention costs", total=len(id_puentes)):
        intervention_costs[bridge], _ = calculate_intervention_cost([bridge], data_model)
        print(bridge, ":", intervention_costs[bridge])
    return base_cost, flow_by_edge, intervention_costs


def calculate_intervention_cost(bridges, data_model):
    """
    Calculate difference of cost of the road network after an intervention.
    """

    # Remove edges
    edge_data = {}
    for bridge in set(bridges):
        source = data_model.puentes[data_model.puentes.id_puente == bridge].source.values[0]
        target = data_model.puentes[data_model.puentes.id_puente == bridge].target.values[0]
        edge_data[source, target] = data_model.G.get_edge_data(source, target)
        data_model.G.remove_edge(source, target)
    
    # Calculate new cost and flows
    try:
        new_cost, flow_by_edge = calculate_costs_flows_for_odvs(data_model)
    except Exception as e:
        # Add edges back
        for i,j in edge_data.keys():
            data_model.G.add_edge(i,j, **edge_data[i,j])
        raise e

    # Add edges back
    for i,j in edge_data.keys():
        data_model.G.add_edge(i,j, **edge_data[i,j])

    return new_cost - data_model.base_cost, flow_by_edge 
