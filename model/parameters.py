import pandas as pd
import numpy as np
import networkx as nx
import math
import pickle
from os import path
from datetime import datetime

def save_parameters():
    
    df_path = path.join("resources", "dataframes")

    # Initial time
    tinicio = datetime.now()

    ## Parameters
    A = list() # Arcos
    N = list() # Nodos
    M = [] # Municipios
    OD = [] # Pares Origen Destino
    V = ["Autos", "Buses", "C-2", "C-3-4", "C-5", ">C-5"] # Vehiculos
    c = {} # Costo de transitar por el arco
    u = {} # Capacidad del arco
    bb = {} # Demanda de los arcos que son mayor a 0
    nodoMunicipio = {} # Nodos que se encuentran en un municipio
    arcosMunicipio = {} # Arcos que se encuentran en un municipio 
    fid = {} # FID y coordenadas

    # Leer Excel la hoja de los municipios
    df1 = pd.read_csv(path.join(df_path, "municipios.csv"))

    # Añadir los municipios que efectivamente estén
    for indice_fila, linea in df1.iterrows():
        if linea[1] == "Sí":
            M.append(str(linea[0]))

    # inicializar los arcos para cada municipio en una lista
    for m in M:
        arcosMunicipio[m] = list()

    #Leer excel la hoja principal
    df = pd.read_excel(path.join(df_path, "principal.csv"))

    for indice_fila, linea in df.iterrows():

        # Obtener los nodos
        inicio = str(linea[8]) + "/" + str(linea[9])   # START_X / START_Y
        final = str(linea[10]) + "/" + str(linea[11])  # END_X / END_Y

        # Identificar correctamente el municipio(quitarle el 0)
        if str(linea[0])[0] == "0":  # CODIGOVIA
            municipio = str(linea[0])[1:]
        else:
            municipio = str(linea[0])

        # Identificar los arcos y nodos en los municipios
        if linea[7] == "Vía Municipal" and municipio in M:  # CLASE_DE_R
            arcosMunicipio[municipio].append((inicio, final))
            arcosMunicipio[municipio].append((final, inicio))
            if not municipio in nodoMunicipio:
                nodoMunicipio[municipio] = inicio

        #Agregar nodos
        if not inicio in N:
            N.append(inicio)
        if not final in N:
            N.append(final)

        #Agregar arco (inicio,final)
        if(inicio != final) and (inicio, final) not in A:
            arco1 =  (inicio, final)
            fid[arco1]=(linea[19],linea[8],linea[9],linea[10],linea[11])
            A.append(arco1)
            # Asignar costos # COSTO
            c[inicio, final,V[0]] = float(linea[12])
            c[inicio, final,V[1]] = float(linea[13])
            c[inicio, final,V[2]] = float(linea[14])
            c[inicio, final,V[3]] = float(linea[15])
            c[inicio, final,V[4]] = float(linea[16])
            c[inicio, final,V[5]] = float(linea[17])
            # Asignar capacidad  # TPD / 2
            u[inicio, final,V[0]] = math.ceil(int(linea[1])/2)
            u[inicio, final,V[1]] = math.ceil(int(linea[2])/2)
            u[inicio, final,V[2]] = math.ceil(int(linea[3])/2)
            u[inicio, final,V[3]] = math.ceil(int(linea[4])/2)
            u[inicio, final,V[4]] = math.ceil(int(linea[5])/2)
            u[inicio, final,V[5]] = math.ceil(int(linea[6])/2)

        #Agregar arco (inicio,final)
        if(inicio != final) and (final, inicio) not in A:
            arco2 =  (final, inicio)
            fid[arco2]=(linea[19],linea[10],linea[11],linea[8],linea[9])
            A.append(arco2)     
            # Asignar costos
            c[final, inicio,V[0]] = float(linea[12])
            c[final, inicio,V[1]] = float(linea[13])
            c[final, inicio,V[2]] = float(linea[14])
            c[final, inicio,V[3]] = float(linea[15])
            c[final, inicio,V[4]] = float(linea[16])
            c[final, inicio,V[5]] = float(linea[17])
            # Asignar capacidad
            u[final, inicio,V[0]] = math.ceil(int(linea[1])/2)
            u[final, inicio,V[1]] = math.ceil(int(linea[2])/2)
            u[final, inicio,V[2]] = math.ceil(int(linea[3])/2)
            u[final, inicio,V[3]] = math.ceil(int(linea[4])/2)
            u[final, inicio,V[4]] = math.ceil(int(linea[5])/2)
            u[final, inicio,V[5]] = math.ceil(int(linea[6])/2)

    # Leer matriz od 
    df2 = pd.read_excel(path.join(df_path, "od.csv")) 

    for indice_fila, linea in df2.iterrows(): 
        # obtener origen destino
        origen = str(int(linea[0]))
        destino = str(int(linea[1]))

        # Revisar que tanto el origen como el destino estén en los municipios
        if( origen in nodoMunicipio and destino in nodoMunicipio):
            # qué tipo de vehículo es? (para asignarlo al parametro)
            if linea[2] == 9:
                v = V[2]
            elif linea[2] > 9 and linea[2] < 15:
                v = V[3]
            elif linea[2] == 15:
                v = V[4]
            else:
                v = V[5]

            # Añadir los pares origen-destino sin repetir
            # Asignar la demanda

            if origen != destino:

                if not (origen,destino) in OD:
                    OD.append((origen,destino))

                try:
                    bb[origen,destino,v] += math.ceil(float(linea[3])/360)
                except:
                    bb[origen,destino,v] = math.ceil(float(linea[3])/360)


    #Asignar nodo interno del municipio si hay
    for m in M:
        nodos = []
        for i in arcosMunicipio[m]:
            nodos.append(i[0])
        for i in nodos:
            if nodos.count(i)>1:
                nodoMunicipio[m] = i

    ## OD para cada camión
    # Camiones
    camiones = ["C-2", "C-3-4", "C-5", ">C-5"]
    # Pares OD por camión
    ODC = {camion: [] for camion in camiones}
    for o,d in OD:
        for camion in camiones:
            if (o,d,camion) in bb:
                ODC[camion].append((o,d))

    #Gran M
    MM = 10*max(c.values())

    #Arcos por puente
    axp = {}
    puentes = []
    df = pd.read_excel(path.join(df_path, "puentes.csv"))
    for indice_fila, linea in df.iterrows():
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
        for i in c:
            if i[2] == v:
                w[v][i[0],i[1]] = c[i]

    #Creación grafo
    G = nx.Graph()
    for i,j in A:
        G.add_edge(i, j, weightC2=w["C-2"][i,j], weightC34=w["C-3-4"][i,j], weightC5=w["C-5"][i,j], weightCmas5=w[">C-5"][i,j])

    #Runtime
    print("Tiempo de ejecución [Seg]:",round((datetime.now() - tinicio).total_seconds(),2))

    
    # Save as pickle files
    pkl_path = path.join("resources", "pickles")
    pickle.dump(G, open(path.join(pkl_path, "G.pkl"), 'wb'))
    pickle.dump(bb, open(path.join(pkl_path, "bb.pkl"), 'wb'))
    pickle.dump(axp, open(path.join(pkl_path, "axp.pkl"), 'wb'))
    pickle.dump(puentes, open(path.join(pkl_path, "puentes.pkl"), 'wb'))
    pickle.dump(nodoMunicipio, open(path.join(pkl_path, "nodoMunicipio.pkl"), 'wb'))
    

