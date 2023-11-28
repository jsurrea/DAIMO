import pandas as pd
from os import path
from collections import Counter


def clean_dataframes(dfs):
    """
    Clean dataframes from the dictionary of dataframes
    """

    # Sheet 1: principal
    print("Cleaning sheet 'principal'...")
    df_principal = dfs["principal"]
    df_principal["CODIGOVIA"] = df_principal["CODIGOVIA"].astype(str)
    df_principal["CODIGOVIA"] = df_principal["CODIGOVIA"].apply(lambda x: x[1:] if x.startswith("0") else x)
    df_principal["nodo_inicial"] = df_principal["START_Y"].astype(str) + "/" + df_principal["START_X"].astype(str)
    df_principal["nodo_final"] = df_principal["END_Y"].astype(str) + "/" + df_principal["END_X"].astype(str)
    df_principal["arco"] = df_principal[["nodo_inicial","nodo_final"]].apply(lambda row: (min(row), max(row)), axis = 1)
    df_principal["source"] = df_principal["arco"].apply(lambda x: x[0])
    df_principal["target"] = df_principal["arco"].apply(lambda x: x[1])
    df_principal = df_principal.drop_duplicates("arco")
    df_principal = df_principal[~(df_principal.source == df_principal.target)]
    df_principal = df_principal.rename(columns={
        "COSTO_C2": "C-2",  
        "COSTO_C3__C4": "C-3-4",
        "COSTO_C5": "C-5",
        "COSTO_MAS_C5": ">C-5",
    })

    # Sheet 2: od
    print("Cleaning sheet 'od'...")
    def map_vehicle_code(x):
        if x == 9:
            return "C-2"
        elif 9 < x < 15:
            return "C-3-4"
        elif x == 15:
            return "C-5"
        elif x > 15:
            return ">C-5"
    
    df_od = dfs["od"]
    df_od = df_od.groupby(["DANE O", "DANE D", "TIPO_VEH"]).sum() / 365
    df_od = df_od.reset_index()
    df_od["DANE O"] = df_od["DANE O"].astype(str)
    df_od["DANE D"] = df_od["DANE D"].astype(str)
    df_od["vehiculo"] = df_od["TIPO_VEH"].apply(map_vehicle_code)
    df_od = df_od.rename(columns={
        "DANE O": "municipio_origen", 
        "DANE D": "municipio_destino",
        "VIAJES_AÑO": "demanda", 
    })

    # Sheet 3: puentes
    print("Cleaning sheet 'puentes'...")
    df_puentes = dfs["puentes"]
    df_puentes = df_puentes.drop_duplicates('PUENTE')
    df_puentes["nodo_inicial"] = df_puentes["START_Y"].str.replace(",", ".") + "/" + df_puentes["START_X"].str.replace(",", ".")
    df_puentes["nodo_final"] = df_puentes["END_Y"].str.replace(",", ".") + "/" + df_puentes["END_X"].str.replace(",", ".")
    df_puentes["arco"] = df_puentes[["nodo_inicial","nodo_final"]].apply(lambda row: (min(row), max(row)), axis = 1)
    df_puentes["source"] = df_puentes["arco"].apply(lambda x: x[0])
    df_puentes["target"] = df_puentes["arco"].apply(lambda x: x[1])
    df_puentes = df_puentes.rename(columns = {"PUENTE":"id_puente"})

    # Map municipalities to nodes
    print("Mapping municipalities to nodes...")
    municipalities = set(map(str, set(df_od["municipio_origen"]) | set(df_od["municipio_destino"])))
    nodes_by_municipality = {municipality: [] for municipality in municipalities}
    is_municipality = df_principal["CODIGOVIA"].isin(municipalities)
    is_municipality_road = df_principal["CLASE_DE_R"] == "Vía Municipal"
    for _, row in df_principal[is_municipality & is_municipality_road].iterrows():
        nodes_by_municipality[row["CODIGOVIA"]].append(row["nodo_inicial"])
        nodes_by_municipality[row["CODIGOVIA"]].append(row["nodo_final"])
    counts_by_municipality = {municipality: Counter(nodes_by_municipality[municipality]) for municipality in municipalities}
    most_common_node_by_municipality = {municipality: counts_by_municipality[municipality].most_common(1) for municipality in municipalities}
    most_common_node_by_municipality = {municipality: value[0][0] if len(value) > 0 else None for municipality, value in most_common_node_by_municipality.items()}

    # Replace municipalities with nodes
    df_od["nodo_origen"] = df_od["municipio_origen"].apply(most_common_node_by_municipality.get)
    df_od["nodo_destino"] = df_od["municipio_destino"].apply(most_common_node_by_municipality.get)
    df_od = df_od.dropna()

    # Keep only the relevant columns
    df_principal = df_principal[["source", "target", "C-2", "C-3-4", "C-5", ">C-5"]]
    df_od = df_od[["nodo_origen", "nodo_destino", "vehiculo", "demanda"]]
    df_puentes = df_puentes[["id_puente", "source", "target"]]
    
    return {
        "principal": df_principal,
        "od": df_od,
        "puentes": df_puentes,
    }
