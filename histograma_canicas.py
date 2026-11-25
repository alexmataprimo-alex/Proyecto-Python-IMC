"""histograma_canicas.py - Modularidad y Graficación con random y matplotlib."""

import random
import matplotlib.pyplot as plt


def simular_canica(niveles=12):
    """Simula una canica con pasos aleatorios izquierda/derecha y retorna su contenedor."""
    contenedor = 0
    for _ in range(niveles):
        if random.choice(["Izquierda", "Derecha"]) == "Derecha":
            contenedor += 1
    return contenedor


def ejecutar_simulacion_masiva(total_canicas=3000, niveles=12):
    """Ejecuta simular_canica repetidamente y devuelve la lista de resultados."""
    resultados = []
    for _ in range(total_canicas):
        resultados.append(simular_canica(niveles=niveles))
    return resultados


def graficar_resultados(resultados, niveles=12):
    """Recibe una lista de contenedores finales y genera un histograma."""
    bins = range(0, niveles + 2)
    plt.hist(resultados, bins=bins, align="left", rwidth=0.85, edgecolor="black")
    plt.title(f"Distribución de {len(resultados)} canicas ({niveles} niveles)")
    plt.xlabel("Contenedor final")
    plt.ylabel("Cantidad de canicas")
    plt.xticks(range(0, niveles + 1))
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    total = 3000
    niveles_tablero = 12
    datos_canicas = ejecutar_simulacion_masiva(total_canicas=total, niveles=niveles_tablero)
    print(f"Simulación completada: {len(datos_canicas)} canicas registradas.")
    graficar_resultados(datos_canicas, niveles=niveles_tablero)

    