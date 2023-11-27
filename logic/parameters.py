import pandas as pd
import numpy as np
import networkx as nx
import math
import pickle
from os import path
from datetime import datetime

def create_parameters():
    """
    Creates the parameters for the model.
    """
    
    df_path = path.join("resources", "dataframes")

    # Initial time
    tinicio = datetime.now()

    ## Parameters
    arcos = list()
    nodos = list() 
    municipios = []
    pares_origen_destino = []
    vehiculos = ["Autos", "Buses", "C-2", "C-3-4", "C-5", ">C-5"]
    costo_transitar_arco = {} 
    capacidad_arco = {} 
    demanda_arco = {}
    nodos_por_municipio = {} 
    arcos_por_municipio = {} 
    fid = {} 

    # Leer Excel la hoja de los municipios
    df_municipios = pd.read_csv(path.join(df_path, "municipios.csv"))

    # Añadir los municipios que efectivamente estén
    for indice_fila, linea in df_municipios.iterrows():
        if linea[1] == "Sí":
            municipios.append(str(linea[0]))

    # inicializar los arcos para cada municipio en una lista
    for m in municipios:
        arcos_por_municipio[m] = list()

    #Leer excel la hoja principal
    df_principal = pd.read_excel(path.join(df_path, "principal.csv"))

    for indice_fila, linea in df_principal.iterrows():

        # Obtener los nodos
        inicio = str(linea[8]) + "/" + str(linea[9])   # START_X / START_Y
        final = str(linea[10]) + "/" + str(linea[11])  # END_X / END_Y

        # Identificar correctamente el municipio(quitarle el 0)
        if str(linea[0])[0] == "0":  # CODIGOVIA
            municipio = str(linea[0])[1:]
        else:
            municipio = str(linea[0])

        # Identificar los arcos y nodos en los municipios
        if linea[7] == "Vía Municipal" and municipio in municipios:  # CLASE_DE_R
            arcos_por_municipio[municipio].append((inicio, final))
            arcos_por_municipio[municipio].append((final, inicio))
            if not municipio in nodos_por_municipio:
                nodos_por_municipio[municipio] = inicio

        #Agregar nodos
        if not inicio in nodos:
            nodos.append(inicio)
        if not final in nodos:
            nodos.append(final)

        #Agregar arco (inicio,final)
        if(inicio != final) and (inicio, final) not in arcos:
            arco1 =  (inicio, final)
            fid[arco1]=(linea[19],linea[8],linea[9],linea[10],linea[11])
            arcos.append(arco1)
            # Asignar costos # COSTO
            costo_transitar_arco[inicio, final,vehiculos[0]] = float(linea[12])
            costo_transitar_arco[inicio, final,vehiculos[1]] = float(linea[13])
            costo_transitar_arco[inicio, final,vehiculos[2]] = float(linea[14])
            costo_transitar_arco[inicio, final,vehiculos[3]] = float(linea[15])
            costo_transitar_arco[inicio, final,vehiculos[4]] = float(linea[16])
            costo_transitar_arco[inicio, final,vehiculos[5]] = float(linea[17])
            # Asignar capacidad  # TPD / 2
            capacidad_arco[inicio, final,vehiculos[0]] = math.ceil(int(linea[1])/2)
            capacidad_arco[inicio, final,vehiculos[1]] = math.ceil(int(linea[2])/2)
            capacidad_arco[inicio, final,vehiculos[2]] = math.ceil(int(linea[3])/2)
            capacidad_arco[inicio, final,vehiculos[3]] = math.ceil(int(linea[4])/2)
            capacidad_arco[inicio, final,vehiculos[4]] = math.ceil(int(linea[5])/2)
            capacidad_arco[inicio, final,vehiculos[5]] = math.ceil(int(linea[6])/2)

        #Agregar arco (inicio,final)
        if(inicio != final) and (final, inicio) not in arcos:
            arco2 =  (final, inicio)
            fid[arco2]=(linea[19],linea[10],linea[11],linea[8],linea[9])
            arcos.append(arco2)     
            # Asignar costos
            costo_transitar_arco[final, inicio,vehiculos[0]] = float(linea[12])
            costo_transitar_arco[final, inicio,vehiculos[1]] = float(linea[13])
            costo_transitar_arco[final, inicio,vehiculos[2]] = float(linea[14])
            costo_transitar_arco[final, inicio,vehiculos[3]] = float(linea[15])
            costo_transitar_arco[final, inicio,vehiculos[4]] = float(linea[16])
            costo_transitar_arco[final, inicio,vehiculos[5]] = float(linea[17])
            # Asignar capacidad
            capacidad_arco[final, inicio,vehiculos[0]] = math.ceil(int(linea[1])/2)
            capacidad_arco[final, inicio,vehiculos[1]] = math.ceil(int(linea[2])/2)
            capacidad_arco[final, inicio,vehiculos[2]] = math.ceil(int(linea[3])/2)
            capacidad_arco[final, inicio,vehiculos[3]] = math.ceil(int(linea[4])/2)
            capacidad_arco[final, inicio,vehiculos[4]] = math.ceil(int(linea[5])/2)
            capacidad_arco[final, inicio,vehiculos[5]] = math.ceil(int(linea[6])/2)

    # Leer matriz od 
    df_od = pd.read_excel(path.join(df_path, "od.csv")) 

    for indice_fila, linea in df_od.iterrows(): 
        # obtener origen destino
        origen = str(int(linea[0]))
        destino = str(int(linea[1]))

        # Revisar que tanto el origen como el destino estén en los municipios
        if( origen in nodos_por_municipio and destino in nodos_por_municipio):
            # qué tipo de vehículo es? (para asignarlo al parametro)
            if linea[2] == 9:
                v = vehiculos[2]
            elif linea[2] > 9 and linea[2] < 15:
                v = vehiculos[3]
            elif linea[2] == 15:
                v = vehiculos[4]
            else:
                v = vehiculos[5]

            # Añadir los pares origen-destino sin repetir
            # Asignar la demanda

            if origen != destino:

                if not (origen,destino) in pares_origen_destino:
                    pares_origen_destino.append((origen,destino))

                try:
                    demanda_arco[origen,destino,v] += math.ceil(float(linea[3])/360)
                except:
                    demanda_arco[origen,destino,v] = math.ceil(float(linea[3])/360)


    #Asignar nodo interno del municipio si hay
    for m in municipios:
        nodos = []
        for i in arcos_por_municipio[m]:
            nodos.append(i[0])
        for i in nodos:
            if nodos.count(i)>1:
                nodos_por_municipio[m] = i

    ## pares_origen_destino para cada camión
    # Camiones
    camiones = ["C-2", "C-3-4", "C-5", ">C-5"]
    # Pares pares_origen_destino por camión
    ODC = {camion: [] for camion in camiones}
    for o,d in pares_origen_destino:
        for camion in camiones:
            if (o,d,camion) in demanda_arco:
                ODC[camion].append((o,d))

    #Gran M
    MM = 10*max(costo_transitar_arco.values())

    #Arcos por puente
    axp = {}
    puentes = []
    df_principal = pd.read_excel(path.join(df_path, "puentes.csv"))
    for indice_fila, linea in df_principal.iterrows():
        # Obtener los nodos
        inicio = (str(linea[1]) + "/" + str(linea[2])).replace(",",".")
        final = (str(linea[3]) + "/" + str(linea[4])).replace(",",".")

        #Agregar arco al diccionario
        if linea[0] not in axp:
            puentes.append(linea[0])
            axp[linea[0]] = [(inicio, final)]
        else:
            axp[linea[0]].append((inicio, final))

            
    arcosConPuentes = []
    for i in puentes:
        arcosConPuentes += axp[i]

    #Costos por tipo de vehículo
    w = {}
    for v in ["C-2", "C-3-4", "C-5", ">C-5"]:
        w[v] = {}
        for i in costo_transitar_arco:
            if i[2] == v:
                w[v][i[0],i[1]] = costo_transitar_arco[i]

    #Creación grafo
    G = nx.Graph()
    for i,j in arcos:
        G.add_edge(i, j, weightC2=w["C-2"][i,j], weightC34=w["C-3-4"][i,j], weightC5=w["C-5"][i,j], weightCmas5=w[">C-5"][i,j])

    #Runtime
    print("Tiempo de ejecución [Seg]:",round((datetime.now() - tinicio).total_seconds(),2))

    
    # Save as pickle files
    pkl_path = path.join("resources", "pickles")
    pickle.dump(G, open(path.join(pkl_path, "G.pkl"), 'wb'))
    pickle.dump(demanda_arco, open(path.join(pkl_path, "demanda_arco.pkl"), 'wb'))
    pickle.dump(axp, open(path.join(pkl_path, "axp.pkl"), 'wb'))
    pickle.dump(puentes, open(path.join(pkl_path, "puentes.pkl"), 'wb'))
    pickle.dump(nodos_por_municipio, open(path.join(pkl_path, "nodos_por_municipio.pkl"), 'wb'))
    

