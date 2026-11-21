# reto_bifurcacion.py - Semana 7: Optimización con Colecciones

# Tupla con los nombres fijos de los cuadrantes cartesianos.
# Se usa una tupla (y no una lista) porque los nombres de los cuadrantes
# son un conjunto constante que no debe modificarse durante la ejecución.
# Acceso por índice:
#   índice 0 -> "Cuadrante I" (+X, +Y)
#   índice 1 -> "Cuadrante II" (-X, +Y)
#   índice 2 -> "Cuadrante III" (-X, -Y)
#   índice 3 -> "Cuadrante IV" (+X, -Y)
CUADRANTES = ("Cuadrante I", "Cuadrante II", "Cuadrante III", "Cuadrante IV")


def verificar_longitud_palabra():
    """
    Solicita una palabra hasta que su longitud esté entre 4 y 8 caracteres.
    Registra cada intento en una lista para conservar el historial de la sesión.
    """
    print("--- 1. VERIFICACIÓN DE LONGITUD DE PALABRA ---")

    # Colección tipo lista: almacena todas las palabras ingresadas en la sesión,
    # incluyendo las que fueron rechazadas antes de acertar.
    intentos_palabras = []

    while True:
        # Variable simple (str): guarda la palabra ingresada en este intento
        palabra_actual = input("Ingresa una palabra (entre 4 y 8 letras): ").strip()

        # Agregamos el intento a la lista historial antes de validar
        intentos_palabras.append(palabra_actual)

        # Variable simple (int): almacena la cantidad de caracteres de la palabra actual
        longitud = len(palabra_actual)

        if longitud < 4:
            print(f"Hacen falta letras ({longitud}). Intenta con una palabra nueva.\n")
        elif longitud > 8:
            print(f"Sobran letras ({longitud}). Intenta con una palabra nueva.\n")
        else:
            print(f"¡Palabra correcta! '{palabra_actual}' tiene {longitud} letras.\n")
            break

    # Resumen de la colección de intentos realizada en este bloque
    print(f"Total de intentos en esta sesión: {len(intentos_palabras)}")
    print(f"Historial de palabras ingresadas: {intentos_palabras}\n")
    return intentos_palabras


def determinar_cuadrante():
    """
    Solicita coordenadas X y Y distintas de cero mediante un ciclo while
    y selecciona el nombre correspondiente desde la tupla CUADRANTES usando índices.
    """
    print("--- 2. UBICACIÓN EN EL PLANO CARTESIANO ---")

    while True:
        try:
            # Variables simples (float): representan un único valor numérico por eje
            x = float(input("Ingresa la coordenada X (distinta de 0): "))
            if x == 0:
                print("Error: la coordenada X no puede ser 0. Inténtalo de nuevo.\n")
                continue

            y = float(input("Ingresa la coordenada Y (distinta de 0): "))
            if y == 0:
                print("Error: la coordenada Y no puede ser 0. Inténtalo de nuevo.\n")
                continue

            # Variable simple (int): determina qué índice de la tupla CUADRANTES corresponde
            if x > 0 and y > 0:
                indice_cuadrante = 0
            elif x < 0 and y > 0:
                indice_cuadrante = 1
            elif x < 0 and y < 0:
                indice_cuadrante = 2
            else:
                indice_cuadrante = 3

            # Se accede al elemento de la tupla mediante su índice numérico
            nombre_cuadrante = CUADRANTES[indice_cuadrante]
            print(f"El punto ({x}, {y}) está ubicado en {nombre_cuadrante}.\n")
            break

        except ValueError:
            print("Error: debes ingresar un número válido. Inténtalo de nuevo.\n")


if __name__ == "__main__":
    print("==========================================")
    print("   RETO SEMANAL: COLECCIONES EN PYTHON    ")
    print("==========================================\n")

    historial = verificar_longitud_palabra()
    determinar_cuadrante()

    print("==========================================")
    print(f"   Sesión finalizada ({len(historial)} palabra(s) probadas)   ")
    print("==========================================")