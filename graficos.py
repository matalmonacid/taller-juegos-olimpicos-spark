# Taller 1 - Grupo 4
# Matías Almonacid y Carolina Castro

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter


carpeta_resultados = Path(__file__).resolve().parent / "resultados"
carpeta_figuras = carpeta_resultados / "figuras"
carpeta_figuras.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titleweight": "bold",
    "axes.labelcolor": "#334155",
    "xtick.color": "#475569",
    "ytick.color": "#475569",
    "savefig.facecolor": "white",
})


def leer_csv(nombre):
    with (carpeta_resultados / nombre).open(encoding="utf-8-sig", newline="") as archivo:
        return list(csv.DictReader(archivo))


def guardar_figura(figura, nombre):
    figura.tight_layout()
    figura.savefig(carpeta_figuras / nombre, dpi=180, bbox_inches="tight")
    plt.close(figura)


# 1. Participaciones con medalla por equipo

medallas = leer_csv("medallas_por_equipo.csv")
for fila in medallas:
    fila["Gold"] = int(fila["Gold"])
    fila["Silver"] = int(fila["Silver"])
    fila["Bronze"] = int(fila["Bronze"])
    fila["total"] = fila["Gold"] + fila["Silver"] + fila["Bronze"]

# Elegimos los diez equipos con mayor total y dejamos el primero arriba.
principales = sorted(medallas, key=lambda fila: fila["total"], reverse=True)[:10]
principales.reverse()
equipos = [fila["equipo"] or "Unknown team" for fila in principales]
oro = [fila["Gold"] for fila in principales]
plata = [fila["Silver"] for fila in principales]
bronce = [fila["Bronze"] for fila in principales]

fig, ax = plt.subplots(figsize=(11, 6.5))
ax.barh(equipos, oro, color="#d7a62b", label="Gold", height=0.65)
ax.barh(equipos, plata, left=oro, color="#94a3b8", label="Silver", height=0.65)
acumulado = [o + p for o, p in zip(oro, plata)]
ax.barh(equipos, bronce, left=acumulado, color="#b77945", label="Bronze", height=0.65)

for posicion, fila in enumerate(principales):
    ax.text(fila["total"] + 55, posicion, f"{fila['total']:,}", va="center", fontsize=10)

ax.set_title("Medal-winning participations by team", loc="left", pad=20, fontsize=17)
ax.set_xlabel("Athlete participations with a medal")
ax.set_ylabel("Team")
ax.set_xlim(0, max(fila["total"] for fila in principales) * 1.16)
ax.xaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))
ax.grid(axis="x", alpha=0.18)
ax.set_axisbelow(True)
ax.legend(loc="lower right", frameon=False)
guardar_figura(fig, "medallas_por_equipo.png")


# 2. Edad promedio por medalla

tabla_edades = leer_csv("edad_por_medalla.csv")
promedios = {fila["medalla"]: float(fila["promedio_edad"]) for fila in tabla_edades}
tipos_medalla = ["Gold", "Silver", "Bronze"]
edades = [promedios[tipo] for tipo in tipos_medalla]

fig, ax = plt.subplots(figsize=(7, 5))
barras = ax.bar(tipos_medalla, edades, color=["#d7a62b", "#94a3b8", "#b77945"], width=0.58)
ax.bar_label(barras, labels=[f"{edad:.2f}" for edad in edades], padding=6, fontsize=12)
ax.set_title("Mean age by medal type", loc="left", pad=20, fontsize=16)
ax.set_ylabel("Mean age (years)")
ax.set_ylim(0, 30)
ax.grid(axis="y", alpha=0.18)
ax.set_axisbelow(True)
guardar_figura(fig, "edad_por_medalla.png")


# 3. Altura promedio por temporada

tabla_alturas = leer_csv("altura_por_temporada.csv")
promedios = {fila["temporada"]: float(fila["promedio_altura"]) for fila in tabla_alturas}
alturas = [promedios["Verano"], promedios["Invierno"]]

fig, ax = plt.subplots(figsize=(7, 5))
barras = ax.bar(["Summer", "Winter"], alturas, color=["#246a92", "#69a9bc"], width=0.58)
ax.bar_label(barras, labels=[f"{altura:.2f}" for altura in alturas], padding=6, fontsize=12)
ax.set_title("Mean height by season", loc="left", pad=20, fontsize=16)
ax.set_ylabel("Mean height (cm)")
ax.set_ylim(0, 200)
ax.grid(axis="y", alpha=0.18)
ax.set_axisbelow(True)
guardar_figura(fig, "altura_por_temporada.png")


# 4. Edad promedio por sexo

tabla_sexos = leer_csv("edad_por_sexo.csv")
promedios = {fila["Descripción_sexo"]: float(fila["promedio_edad"]) for fila in tabla_sexos}
edades = [promedios["Hombre"], promedios["Mujer"]]

fig, ax = plt.subplots(figsize=(7, 5))
barras = ax.bar(["Male", "Female"], edades, color=["#246a92", "#7892be"], width=0.58)
ax.bar_label(barras, labels=[f"{edad:.2f}" for edad in edades], padding=6, fontsize=12)
ax.set_title("Mean age by sex", loc="left", pad=20, fontsize=16)
ax.set_ylabel("Mean age (years)")
ax.set_ylim(0, 30)
ax.grid(axis="y", alpha=0.18)
ax.set_axisbelow(True)
guardar_figura(fig, "edad_por_sexo.png")


# 5. Medidas sin información y referencias sin correspondencia

tabla_calidad = leer_csv("calidad_datos.csv")
conteos = {fila["observacion"]: int(fila["participaciones"]) for fila in tabla_calidad}
resumen = leer_csv("resumen_general.csv")
totales = {fila["indicador"]: int(fila["cantidad"]) for fila in resumen}
total_participaciones = totales["participaciones"]

# Una fila puede tener más de un campo sin información.
claves = ["edad_cero", "altura_cero", "peso_cero", "equipo_sin_nombre", "evento_sin_nombre"]
etiquetas = ['Age unavailable', 'Height unavailable', 'Weight unavailable', 'Team unmatched', 'Event unmatched']
porcentajes = [conteos[clave] / total_participaciones * 100 for clave in claves]

fig, ax = plt.subplots(figsize=(11, 5))
ax.barh(etiquetas, porcentajes, color="#246a92", height=0.62)
espacio = max(porcentajes) * 0.025
for posicion, clave in enumerate(claves):
    porcentaje = porcentajes[posicion]
    texto = "<0.01%" if 0 < porcentaje < 0.01 else f"{porcentaje:.2f}%"
    ax.text(porcentaje + espacio, posicion, f"{texto}  ({conteos[clave]:,})", va="center", fontsize=10)

ax.invert_yaxis()
ax.set_title("Data availability in athlete participations", loc="left", pad=20, fontsize=16)
ax.set_xlabel("Share of all participations (%)")
ax.set_xlim(0, max(porcentajes) * 1.55)
ax.grid(axis="x", alpha=0.18)
ax.set_axisbelow(True)
guardar_figura(fig, "calidad_datos.png")


# 6. Participaciones por edición

tabla_ediciones = leer_csv("participaciones_por_edicion.csv")
temporadas = ["Verano", "Invierno"]
titulos = ["Summer Games", "Winter Games"]
colores = ["#246a92", "#69a9bc"]

fig, ejes = plt.subplots(2, 1, figsize=(11, 7.5), sharex=True)
for i, temporada in enumerate(temporadas):
    filas = [fila for fila in tabla_ediciones if fila["temporada"] == temporada]
    filas = sorted(filas, key=lambda fila: int(fila["año"]))
    años = [int(fila["año"]) for fila in filas]
    participaciones = [int(fila["participaciones"]) for fila in filas]

    ax = ejes[i]
    ax.plot(años, participaciones, color=colores[i], linewidth=2.2, marker="o", markersize=4.5)
    ax.set_title(titulos[i], loc="left", fontsize=14, pad=10)
    ax.set_ylabel("Athlete participations")
    ax.set_ylim(bottom=0)
    ax.yaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))
    ax.grid(alpha=0.18)
    ax.set_axisbelow(True)

ejes[-1].set_xlabel("Year")
guardar_figura(fig, "participaciones_por_edicion.png")

print("Resultados guardados en la carpeta resultados/figuras.")
