# Datos del Taller 1

## 1. Archivos de entrada

Los seis archivos vienen con el material del taller. Los conservamos en la raíz del proyecto y aplicamos las correcciones durante su lectura.

| Archivo | Formato | Encabezado |
| --- | --- | --- |
| deportista.csv | CSV separado por comas | Sin encabezado |
| deportista2.csv | CSV separado por comas | Sin encabezado |
| resultados.csv | CSV separado por punto y coma | Con encabezado |
| evento.csv | CSV separado por comas | Con encabezado; algunas filas necesitan una segunda lectura |
| equipo.csv | CSV separado por comas | Con encabezado |
| juegos.json | Lista de objetos JSON | Nombres ajustados durante el análisis |

## 2. Campos y relaciones

### 2.1. Deportistas

Los dos archivos usan siete campos en el mismo orden.

| Campo | Contenido |
| --- | --- |
| deportista_id | Identificador del deportista. |
| nombre | Nombre registrado en el catálogo. |
| genero | Código del taller: 1 para Hombre y 2 para Mujer. |
| edad | Edad registrada, en años. |
| altura | Altura en centímetros. |
| peso | Peso en kilogramos. |
| equipo_id | Clave para relacionar al deportista con un equipo. |

La unión reúne 135.571 registros. Durante la lectura se elimina un campo final vacío de una fila que contiene ocho valores.

### 2.2. Resultados

Cada registro identifica una participación.

| Campo | Contenido |
| --- | --- |
| resultado_id | Identificador de la participación. |
| medalla | Gold, Silver, Bronze o NA. |
| deportista_id | Clave del deportista. |
| juego_id | Clave de la edición. |
| evento_id | Clave del evento; los códigos no disponibles quedan nulos. |

NA indica una participación sin medalla. El archivo contiene 271.116 registros.

### 2.3. Equipos y eventos

En equipo.csv, id se relaciona con equipo_id. equipo guarda el nombre y sigla la abreviación.

En evento.csv, cod_evento se relaciona con evento_id. evento guarda el nombre de la prueba y deporte_id su código de deporte. Las filas guardadas como una cadena CSV entre comillas se separan con una segunda lectura.

El catálogo contiene 1.184 equipos y 765 eventos. En el detalle integrado quedan 200 participaciones sin nombre de equipo y 9 sin nombre de evento.

### 2.4. Ediciones

El archivo juegos.json tiene 51 ediciones. Ajustamos los nombres al contenido para obtener estos campos:

| Campo final | Contenido |
| --- | --- |
| juego_id | Identificador de la edición. |
| edicion | Texto que combina año y temporada. |
| año | Año numérico. |
| temporada | Verano o Invierno. |

El archivo entregado no incluye la ciudad sede. Las tablas resultantes usan año de forma consistente.

## 3. Tabla integrada

La base es Resultado. La primera unión relaciona resultados y deportistas mediante deportista_id. Después unimos equipos, eventos y juegos con uniones izquierdas.

Las 20 columnas finales son:

| Grupo | Columnas |
| --- | --- |
| Participación | resultado_id, medalla |
| Deportista | deportista_id, nombre, genero, edad, altura, peso |
| Equipo | equipo_id, equipo, sigla |
| Evento | cod_evento, evento, deporte_id |
| Edición | juego_id, edicion, temporada, año |
| Calculadas | IMC, Descripción_sexo |

La tabla se reparte en cinco particiones. Una misma persona puede aparecer varias veces si tiene más de una participación.

## 4. Medidas y valores no disponibles

Convertimos la altura de centímetros a metros para calcular el IMC: peso dividido por el cuadrado de la altura en metros. El resultado se redondea a dos decimales y queda nulo si la altura o el peso no son positivos.

Las edades y alturas cero se excluyen de sus estadísticas. En el archivo integrado se conservan para poder revisar los registros originales.

Descripción_sexo convierte 1 en Hombre, 2 en Mujer y cualquier otro código en Desconocido. Las agregaciones usan las categorías disponibles en el archivo.
