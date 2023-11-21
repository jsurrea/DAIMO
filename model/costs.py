import networkx as nx
import pandas as pd
from datetime import datetime
from tqdm import tqdm
import pickle
from os import path

from model.model import Model

def save_costs():

    # Init time
    inicio = datetime.now()
    
    model = Model.get_model()
    model.load_parameters()
    puentes = model.puentes
    bb = model.bb
    nodoMunicipio = model.nodoMunicipio
    
    costoExcedente = {puente: 0 for puente in puentes}
    ODVxPuente = {puente: [] for puente in puentes}
    arco2puente = model.rutas_por_puente()
    costos = {puente: 0 for puente in puentes}
    
    total_cost_params = {
        "arco2puente": arco2puente,
        "ODVxPuente": ODVxPuente,
        "costoExcedente": costoExcedente,
        "costos": costos,
    }

    # Costo original
    costoTotal = model.calculate_weighted_distances(bb, total_cost_params)

    # Alternativa con el puente
    costos = {puente : model.calculate_cost([puente]) for puente in puentes}
    costos["TOTAL"] = (costoTotal,0)
    model.costos = costos

    # Runtime
    print("Tiempo de ejecución [Seg]:", round((datetime.now() - inicio).total_seconds(),2))
    
    # Save pickles
    pkl_path = path.join("resources", "pickles")
    pickle.dump(arco2puente, open(path.join(pkl_path, "arco2puente.pkl"), 'wb'))
    pickle.dump(ODVxPuente, open(path.join(pkl_path, "ODVxPuente.pkl"), 'wb'))
    pickle.dump(costoExcedente, open(path.join(pkl_path, "costoExcedente.pkl"), 'wb'))
    pickle.dump(costos, open(path.join(pkl_path, "costos.pkl"), 'wb'))
    