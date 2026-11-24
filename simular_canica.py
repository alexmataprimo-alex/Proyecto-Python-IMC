

import random


def simular_canica(niveles=12):
    """Simula el recorrido de una sola canica a través de niveles de obstáculos.

    En cada nivel, la canica elige aleatoriamente ir hacia la izquierda o
    hacia la derecha. Avanzar a la derecha incrementa en 1 el índice del
    contenedor final.

    Args:
        niveles (int, optional): Cantidad de niveles de obstáculos a atravesar.
            Por defecto es 12.

    Returns:
        int: Número entero que representa el contenedor final alcanzado.
    """
    contenedor = 0
    ruta = []

    for _ in range(niveles):
        direccion = random.choice(["Izquierda", "Derecha"])
        ruta.append(direccion)

        if direccion == "Derecha":
            contenedor += 1

    print(f"Ruta seguida ({niveles} niveles): {' -> '.join(ruta)}")
    return contenedor


if __name__ == "__main__":
    contenedor_final = simular_canica()
    print(f"Contenedor final de la canica: {contenedor_final}")