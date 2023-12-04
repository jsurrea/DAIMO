# DAIMO: Dashboard para el Análisis de Intervenciones en Movilidad

## Introducción

DAIMO es un Dashboard interactivo que permite estudiar los costos indirectos asociados al cierre de un puente en la red vial de Colombia 🇨🇴. Por un lado, permite identificar los puentes críticos, es decir, aquellos cuyo cierre o intervención ocasiona el mayor costo sobre la red. Por otro lado, permite simular el cierre o intervención de un conjunto de puentes para examinar el cambio en el flujo de vehículos de todos los arcos de la red.

DAIMO se encuentra implementado en *Python* por medio de la librería *Plotly-Dash* y se ejecuta como una aplicación web a través del framework *Flask*. Permite procesar cualquier conjunto de datos válido por medio de las librerías *pandas*, *numpy* y *networkx*. Su arquitectura permite extender con facilidad nuevas páginas de funcionalidades, incluyendo modelos de Machine Learning. Además, se puede desplegar rápidamente en servicios Cloud para mejorar su rendimiento y disponibilidad.

A continuación, se presenta una demostración de su funcionamiento:

https://github.com/jsurrea/DAIMO/assets/68788933/a29172fb-1f94-4e03-b6a2-5d3d386bbbf6

## Instalación

DAIMO utiliza `Python3.8` para ejecutar la aplicación web. Para instalar todas las librerías necesarias, ejecute el siguiente comando la primera vez:

```shell
$ pip install -r requirements.txt
```

Para utilizar DAIMO, ejecute el siguiente comando desde el directorio del proyecto:

```shell
$ python app.py
```

DAIMO le informará si la aplicación se ejecutó correctamente:

```shell
Dash is running on http://127.0.0.1:8086/

 * Serving Flask app 'app'
 * Debug mode: on
```

Deberá abrir su navegador y dirigirse a la dirección web `http://127.0.0.1:8086/` para visualizar el dashboard.

## Manual de uso

### Carga de datos

Empiece haciendo click en el botón de configuración para abrir la barra lateral. Seguidamente, seleccione un archivo entre aquellos configurados previamente o arrastre un nuevo archivo a la sección delimitada. Podrá monitorear el progreso de la carga de datos en la consola de ejecución de DAIMO.

![Captura de Pantalla 2023-12-02 a la(s) 1 31 10 a m](https://github.com/jsurrea/DAIMO/assets/68788933/2d329814-c1ba-44fa-a64d-a92227f34f8a)

### Identificar puentes críticos de la red vial

En el contenido principal encontrará el costo total de la red vial de Colombia calculado a partir de los datos seleccionados. Además, podrá visualizar todos los arcos presentes en el grafo y los puentes de interés. Al ubicar su cursor sobre un arco (*hover*), podrá visualizar cuál es el flujo de vehículos diario a través de dicha ubicación. De forma similar, al ubicar su cursor sobre un puente, podrá obtener información relevante como el costo indirecto asociado a su intervención, el incremento de dicho costo con respecto al costo original y el flujo diario de vehículos sobre dicho puente. Además, es posible filtrar los puentes a través de la barra lateral de configuración y clasificarlos fácilmente según su costo de intervención a través del mapa de color.

> **Convención de color:** El color de los puentes se determina en una escala de color Verde-Amarillo-Rojo de forma lineal entre aquellos con menor y mayor valor del cambio porcentual de sus costos indirectos. Los demás arcos se representan con una tonalidad azul pálida.

![Captura de Pantalla 2023-12-02 a la(s) 2 03 20 a m](https://github.com/jsurrea/DAIMO/assets/68788933/3e78b47a-e6cd-4484-bfa0-dd053ec093e7)

### Simular una intervención simultánea de múltiples puentes

Inicialmente, se encontrará con un mapa vacío. Para añadir los puentes que desea incluir en la simulación, deberá abrir el menú lateral de configuración y seleccionarlos. A medida que los selecciona, podrá ir visualizándolos en el mapa del contenido principal. Una vez haya seleccionado todos los puentes de interés, deberá hacer click sobre el botón *Simular* para empezar a evaluar su política de intervención. Debido al volumen de datos, su consulta puede tardarse hasta 5 minutos; sin embargo, en este tiempo podrá consultar otras páginas del dashboard o explorar la información disponible en los mapas.

![Captura de Pantalla 2023-12-02 a la(s) 2 31 46 a m](https://github.com/jsurrea/DAIMO/assets/68788933/657df112-b0bd-40a9-b225-0f52175b0b1d)

Una vez se complete la simulación, podrá encontrar el costo excedente de la red vial con respecto a su estado original, los puentes bajo intervención y el cambio en los flujos de vehículos a través de cada arco de la red. Al ubicar su cursor sobre un arco (*hover*), podrá visualizar su flujo de vehículos antes y después de la intervención, así como la diferencia porcentual de estos flujos.

> **Convención de color:** El color de los puentes bajo intervención es negro. Por su parte, se asigna un color a los arcos según la diferencia porcentual de sus flujos de vehículos diarios. El color azul intenso se asigna a aquellos arcos con la mayor disminución porcentual, el color rojo intenso se asigna a aquellos con mayor aumento porcentual, y el color blanco se asigna a cambios cercanos al 0%.

![Captura de Pantalla 2023-12-02 a la(s) 2 40 59 a m](https://github.com/jsurrea/DAIMO/assets/68788933/5c35ab11-df2b-49fd-8cbe-6068ec9a2973)

### Interactuar con los mapas

*Plotly* permite interactuar de forma muy amigable con mapas. Dentro de su conjunto de herramientas, es posible moverse a través del mapa, cambiar el nivel de zoom y tomar capturas de pantalla. Encontrará dichas opciones en el menú superior derecho de toda gráfica al ubicar el cursor sobre esta. A continuación, se describen visualmente las principales funcionalidades ofrecidas:

![Captura de Pantalla 2023-12-02 a la(s) 1 38 23 a m](https://github.com/jsurrea/DAIMO/assets/68788933/a01103c3-7a38-443a-930b-d35be0881f67)

### Verificar que la aplicación se esté ejecutando correctamente

*Dash* ofrece un menú en la esquina inferior derecha de la aplicación que permite monitorear que esta se encuentre ejecutando correctamente. Al hacer click sobre el símbolo `<>` se mostrarán 3 nuevos íconos: 

- **Mapa de *callbacks* de la aplicación:** Permite entender cómo está estructurada la interacción de la aplicación web.
- **Historial de errores:** Permite obtener información precisa de cualquier error que ocurra durante la ejecución de la aplicación web.
- **Servidor disponible:** Permite verificar que la aplicación se encuentre en ejecución en un momento dado.

![Captura de Pantalla 2023-12-02 a la(s) 2 19 16 a m](https://github.com/jsurrea/DAIMO/assets/68788933/465d75ce-1e08-4ff5-9405-4a6ccaf30c5c)

### Solución de errores

#### El tamaño de los mapas no se visualiza correctamente

En ocasiones, los mapas solo mostrarán una parte de su contenido después de cargar los datos. Para visualizarlos correctamente, puede recargar la página o hacer click sobre el botón de *Regresar a la vista original* dentro de las opciones de interacción de cada gráfica.

![287426920-be6a2d64-bd14-4e46-9bcd-604fa8d390a4](https://github.com/jsurrea/DAIMO/assets/68788933/3b13141c-26c3-4ed2-9244-bd476e6006a9)
