# DAIMO: Dashboard para el Análisis de Intervenciones en Movilidad

## Instalación

DAIMO utiliza `Python3.8` para ejecutar la aplicación web. Para instalar todas las librerías necesarias, ejecute el siguiente comando:

```shell
$ pip install -r requirements.txt
```

# Uso

Para utilizar DAIMO, ejecute el siguiente comando:

```shell
$ python main.py
```

DAIMO le mostrará el siguiente menú de opciones válidas:

```shell
DAIMO: Dashboard para el Análisis de Intervenciones en Movilidad
1. Construir el grafo
2. Calcular los costos
3. Ejecutar la aplicación
```

### Construir el grafo 

Deberá ejecutar esta opción si ha cambiado el conjunto de datos. DAIMO lee los archivos csv que se encuentran en la carpeta `resources/dataframes`.

### Calcular los costos

Deberá ejecutar esta opción si ha cambiado el conjunto de datos. DAIMO lee los archivos csv que se encuentran en la carpeta `resources/dataframes`.

### Ejecutar la aplicación 

DAIMO le informará si la aplicación se ejecutó correctamente:

```shell
Dash is running on http://127.0.0.1:8086/

 * Serving Flask app 'app'
 * Debug mode: on
```

Usted deberá abrir su navegador y dirigirse a la dirección web `http://127.0.0.1:8086/` para visualizar el dashboard.
