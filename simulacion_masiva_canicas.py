"""simulacion_masiva_canicas.py - Semana 10: Procesamiento de Datos Masivos."""

import random


def simular_canica(niveles=12, mostrar_ruta=False):
    """Simula el recorrido de una canica a través de niveles con pasos aleatorios.

    En cada nivel elige aleatoriamente entre izquierda y derecha. Cada paso a
    la derecha suma 1 al contenedor final, sin usar funciones de distribución normal.

    Args:
        niveles (int, optional): Cantidad de niveles de obstáculos. Por defecto 12.
        mostrar_ruta (bool, optional): Si es True, imprime el recorrido paso a paso.

    Returns:
        int: Contenedor final alcanzado por la canica.
    """
    contenedor = 0
    ruta = []

    for _ in range(niveles):
        paso = random.choice(["Izquierda", "Derecha"])
        if mostrar_ruta:
            ruta.append(paso)
        if paso == "Derecha":
            contenedor += 1

    if mostrar_ruta:
        print(f"Ruta seguida ({niveles} niveles): {' -> '.join(ruta)}")

    return contenedor


def ejecutar_simulacion_masiva(total_canicas=3000, niveles=12):
    """Ejecuta simular_canica repetidamente y guarda cada resultado en una lista.

    Args:
        total_canicas (int, optional): Número de canicas a simular. Por defecto 3000.
        niveles (int, optional): Niveles por simulación. Por defecto 12.

    Returns:
        list[int]: Lista con el contenedor final de cada canica simulada.
    """
    resultados_canicas = []

    for _ in range(total_canicas):
        contenedor_final = simular_canica(niveles=niveles, mostrar_ruta=False)
        resultados_canicas.append(contenedor_final)

    return resultados_canicas


if __name__ == "__main__":
    cantidad_simulaciones = 3000
    resultados = ejecutar_simulacion_masiva(total_canicas=cantidad_simulaciones, niveles=12)

    print(f"Total de canicas simuladas: {len(resultados)}")
    print(f"Primeros 15 contenedores obtenidos: {resultados[:15]}")
    print(f"Contenedor mínimo alcanzado: {min(resultados)} | Máximo: {max(resultados)}")
    