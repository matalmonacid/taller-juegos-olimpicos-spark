# Resultados del Taller 1

## 1. Tablas principales

medallas_por_equipo.csv contiene el conteo de oro, plata y bronce por equipo.

edad_por_medalla.csv, altura_por_temporada.csv y edad_por_sexo.csv contienen suma, promedio, máximo y mínimo. Las estadísticas de edad y altura usan medidas positivas.

participaciones_por_edicion.csv reúne el año, la temporada, las participaciones, los deportistas distintos y las participaciones con medalla de cada edición.

## 2. Revisión y detalle

resumen_general.csv guarda los conteos generales. calidad_datos.csv guarda las medidas no disponibles y las referencias sin correspondencia.

muestra_participaciones.csv incluye los primeros 100 registros ordenados por resultado_id. esquema_integrado.json describe los nombres y tipos de las 20 columnas.

participaciones.csv.gz contiene el detalle completo de las 271.116 participaciones. Es un CSV comprimido con el mismo encabezado de la muestra. La columna del año se llama año.

## 3. Figuras

La carpeta figuras contiene las seis imágenes del README. Se generan con los bloques finales del notebook o con graficos.py.

## 4. Abrir el detalle comprimido

Se puede revisar con las herramientas de Python:

~~~python
import csv
import gzip

with gzip.open("resultados/participaciones.csv.gz", "rt", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo, escapechar="\\")
    for i, fila in enumerate(lector):
        if i == 5:
            break
        print(fila)
~~~

El notebook vuelve a generar estos archivos al ejecutar las celdas de guardado.
