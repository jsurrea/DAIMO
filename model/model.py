import networkx as nx
import pandas as pd
from datetime import datetime
from tqdm import tqdm
import pickle
from os import path


class Model:
    
    instance = None
    
    @staticmethod
    def get_model():
        if not Model.instance:
            Model.instance = Model()
        return Model.instance
    

    def load_parameters(self):
        
        if all([
            hasattr(self, "G"),
            hasattr(self, "bb"),
            hasattr(self, "axp"),
            hasattr(self, "puentes"),
            hasattr(self, "nodoMunicipio"),
        ]):
            return
        
        pkl_path = path.join("resources", "pickles")
        
        # Check pickle files for parameters if they do not exist
        if not all([
            path.exists(path.join(pkl_path, "G.pkl")),
            path.exists(path.join(pkl_path, "bb.pkl")),
            path.exists(path.join(pkl_path, "axp.pkl")),
            path.exists(path.join(pkl_path, "puentes.pkl")),
            path.exists(path.join(pkl_path, "nodoMunicipio.pkl")),
        ]):
            raise Exception("Should run save_parameters before")
            
        # Load parameters
        self.G = pickle.load(open(path.join(pkl_path, "G.pkl"), "rb"))
        self.bb = pickle.load(open(path.join(pkl_path, "bb.pkl"), "rb"))
        self.axp = pickle.load(open(path.join(pkl_path, "axp.pkl"), "rb"))
        self.puentes = pickle.load(open(path.join(pkl_path, "puentes.pkl"), "rb"))
        self.nodoMunicipio = pickle.load(open(path.join(pkl_path, "nodoMunicipio.pkl"), "rb"))
        
        
    def load_costs(self):
        
        if all([
            hasattr(self, "costos"),
            hasattr(self, "costoExcedente"),
            hasattr(self, "ODVxPuente"),
            hasattr(self, "arco2puente"),
        ]):
            return
        
        pkl_path = path.join("resources", "pickles")
        
        # Check pickle files for costs if they do not exist
        if not all([
            path.exists(path.join(pkl_path, "costos.pkl")),
            path.exists(path.join(pkl_path, "costoExcedente.pkl")),
            path.exists(path.join(pkl_path, "ODVxPuente.pkl")),
            path.exists(path.join(pkl_path, "arco2puente.pkl")),
        ]):
            raise Exception("Should run save_costs before")
            
        # Load parameters
        self.costos = pickle.load(open(path.join(pkl_path, "costos.pkl"), "rb"))
        self.costoExcedente = pickle.load(open(path.join(pkl_path, "costoExcedente.pkl"), "rb"))
        self.ODVxPuente = pickle.load(open(path.join(pkl_path, "ODVxPuente.pkl"), "rb"))
        self.arco2puente = pickle.load(open(path.join(pkl_path, "arco2puente.pkl"), "rb"))
        
        
    def load_coordinates(self):
        
        if hasattr(self, "coords"):
            return
        
        # Load parameters
        df_path = path.join("resources", "dataframes", "puentes.csv")
        df = pd.read_csv(df_path)

        # Drop duplicates based on the "PUENTE" column, keeping the first occurrence
        df = df.drop_duplicates(subset="PUENTE", keep="last")

        # Set the "PUENTE" column as the index
        df = df.set_index("PUENTE")

        self.coords = {puente : {
            "start_lon": df.loc[puente, "START_X"],
            "start_lat": df.loc[puente, "START_Y"],
            "end_lon": df.loc[puente, "END_X"],
            "end_lat": df.loc[puente, "END_Y"],
        } for puente in df.index}
        

    def calculate_cost(self, puentes):

        self.load_parameters()
        self.load_costs()

        puentes = set(puentes)

        costoAlternativa = self.costos["TOTAL"][0]
        ODVs = set()

        edge_data = {}
        for puente in puentes:

            arcos = self.axp[puente]

            for i,j in arcos:
                i,j = (min(i,j), max(i,j))
                if self.G.has_edge(i,j):
                    edge_data[i,j] = self.G.get_edge_data(i,j)
                    self.G.remove_edge(i,j)
                    costoAlternativa -= self.costoExcedente[(i,j)]

            ODVs |= set(self.ODVxPuente[puente])
            
        costoAlternativa += self.calculate_weighted_distances(ODVs)
        deltaCosto = costoAlternativa - self.costos["TOTAL"][0]

        for i,j in edge_data.keys():
            self.G.add_edge(i,j, **edge_data[i,j])

        return costoAlternativa, deltaCosto
    

    def calculate_weighted_distances(self, odv, total_cost_params = None):
        
        self.load_parameters()

        costo_calculado = 0

        for origen,destino,veh in odv:

            #Nodo inicio y fin
            s = self.nodoMunicipio[origen]
            t = self.nodoMunicipio[destino]

            distance, path = nx.single_source_dijkstra(self.G, source=s, target=t, weight=veh)
            distance *= self.bb[origen,destino,veh]
            costo_calculado += distance
            
            if total_cost_params:
                
                for i in range(1, len(path)):
                    arco = (min(path[i-1], path[i]), max(path[i-1], path[i]))
                    if arco in total_cost_params["arco2puente"]:
                        puente = total_cost_params["arco2puente"][arco]
                        total_cost_params["ODVxPuente"][puente].append((origen,destino,veh))
                        total_cost_params["costoExcedente"][arco] += distance
                        
        if total_cost_params:
            self.arco2puente = total_cost_params["arco2puente"]
            self.ODVxPuente = total_cost_params["ODVxPuente"]
            self.costoExcedente = total_cost_params["costoExcedente"]
            
        return costo_calculado
    
    
    def rutas_por_puente(self):
    
        self.load_parameters()

        arco2puente = {}
    
        for puente in self.puentes:
            arcos = self.axp[puente]
            for arco in arcos:
                arco2puente[arco] = puente
                arco2puente[arco[::-1]] = puente
                
        self.arco2puente = arco2puente
        return arco2puente
    
    
    def get_coords(self):
        self.load_coordinates()
        return self.coords

    def get_base_costs(self):
        self.load_costs()
        return self.costos

    def get_puentes(self):
        self.load_parameters()
        return self.puentes
    
    