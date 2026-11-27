"""ALEJANDRO_MATA_proyectoM3.py - Simulación de Máquina de Galton y graficación."""

import random
import matplotlib.pyplot as plt


def simular_canica(niveles=12):
    """Simula el recorrido de una canica a través de niveles de obstáculos.

    En cada nivel elige aleatoriamente entre izquierda y derecha. Cada paso a
    la derecha incrementa en 1 el índice del contenedor final.

    Args:
        niveles (int, optional): Número de niveles de obstáculos. Por defecto 12.

    Returns:
        int: Contenedor final alcanzado por la canica.
    """
    # Acumula los pasos hacia la derecha para determinar el contenedor final
    contenedor = 0

    # Evalúa un rebote aleatorio en cada nivel del tablero
    for _ in range(niveles):
        if random.choice(["Izquierda", "Derecha"]) == "Derecha":
            contenedor += 1

    return contenedor


def ejecutar_simulacion_masiva(total_canicas=3000, niveles=12):
    """Ejecuta la simulación de múltiples canicas y guarda sus contenedores finales.

    Args:
        total_canicas (int, optional): Cantidad de canicas a simular. Por defecto 3000.
        niveles (int, optional): Niveles por simulación. Por defecto 12.

    Returns:
        list[int]: Lista con el contenedor final de cada canica.
    """
    resultados = []

    # Simula cada canica de forma independiente y almacena su resultado
    for _ in range(total_canicas):
        resultados.append(simular_canica(niveles=niveles))

    return resultados


def graficar_resultados(resultados, niveles=12):
    """Genera y muestra el histograma a partir de los resultados de simulación.

    Args:
        resultados (list[int]): Contenedores finales obtenidos en la simulación.
        niveles (int, optional): Cantidad de niveles del tablero. Por defecto 12.
    """
    # Define los límites de las barras para centrar cada contenedor entero
    bins = range(0, niveles + 2)
    plt.hist(resultados, bins=bins, align="left", rwidth=0.85, edgecolor="black")

    # Configura título, etiquetas solicitadas y formato visual del gráfico
    plt.title("Simulación de Máquina de Galton (3,000 canicas)")
    plt.xlabel("Distribución de canicas")
    plt.ylabel("Cantidad de canicas")
    plt.xticks(range(0, niveles + 1))
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


def main():
    """Coordina la ejecución de la simulación masiva y la generación del gráfico."""
    niveles = 12
    resultados = ejecutar_simulacion_masiva(total_canicas=3000, niveles=niveles)
    print(f"Simulación completada: {len(resultados)} canicas procesadas.")
    graficar_resultados(resultados, niveles=niveles)


if __name__ == "__main__":
    main()
    