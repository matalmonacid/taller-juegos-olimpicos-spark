# Ejecución del Taller 1

## 1. Abrir el proyecto

En la carpeta taller-1 están Taller1.ipynb y los seis archivos de datos. El notebook contiene el desarrollo, las explicaciones y las figuras.

## 2. Ejecutar las celdas

### 2.1. Librerías

Se usan PySpark y Matplotlib. Desde una terminal dentro de la carpeta del proyecto:

~~~bash
python -m pip install -r requirements.txt
python -m notebook
~~~

Abre Taller1.ipynb y ejecuta las celdas en orden. Las primeras celdas configuran Java y crean la sesión de Spark. Las salidas guardadas en el notebook corresponden al desarrollo de las secciones y permiten revisar las tablas.

### 2.2. Datos

Los archivos deportista.csv, deportista2.csv, resultados.csv, evento.csv, equipo.csv y juegos.json deben quedar junto al notebook porque las celdas los leen por su nombre.

### 2.3. Google Colab

Carga el notebook y los seis archivos de datos. Para repetir los gráficos también debes cargar los CSV de la carpeta resultados y conservar ese nombre de carpeta.

## 3. Generar los gráficos

### 3.1. Desde el notebook

Ejecuta las celdas de la sección 9, comenzando en 9.1. No necesitan que se vuelva a ejecutar Spark: leen las tablas que ya están guardadas en resultados.

Cada figura aparece debajo de su código y se guarda en resultados/figuras. Al terminar se muestra el mensaje:

~~~text
Resultados guardados en la carpeta resultados/figuras.
~~~

### 3.2. Desde el archivo Python

Como alternativa, graficos.py contiene las mismas seis figuras:

~~~bash
python graficos.py
~~~

## 4. Consultar los resultados

Las tablas están en resultados y las imágenes en resultados/figuras. El archivo participaciones.csv.gz contiene el detalle completo comprimido. En [resultados/README.md](../resultados/README.md) se describe cada archivo.
