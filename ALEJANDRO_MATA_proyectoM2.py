"""ALEJANDRO_MATA_proyectoM2.py - Proyecto Módulo 2 (Fundamentos de Python).

Consolida la validación de longitud de palabras (con historial en lista) y la
ubicación en el plano cartesiano (con validación de ceros, casting numérico,
manejo de excepciones y tupla de cuadrantes).
"""

# Tupla inmutable con los nombres de los cuadrantes del plano cartesiano.
# Se accede mediante índice según el signo de las coordenadas X e Y:
#   0 -> Cuadrante I   (X > 0, Y > 0)
#   1 -> Cuadrante II  (X < 0, Y > 0)
#   2 -> Cuadrante III (X < 0, Y < 0)
#   3 -> Cuadrante IV  (X > 0, Y < 0)
CUADRANTES = (
    "Cuadrante I",
    "Cuadrante II",
    "Cuadrante III",
    "Cuadrante IV",
)


def validar_longitud_palabra():
    """Solicita una palabra hasta que tenga entre 4 y 8 caracteres."""
    print("\n--- SECCIÓN 1: VALIDACIÓN DE LONGITUD DE PALABRA ---")
    intentos = []

    while True:
        palabra = input("Ingresa una palabra (entre 4 y 8 letras): ").strip()
        intentos.append(palabra)
        longitud = len(palabra)

        if longitud < 4:
            print(f"Faltan letras ({longitud} caracteres). Intenta de nuevo.\n")
        elif longitud > 8:
            print(f"Sobran letras ({longitud} caracteres). Intenta de nuevo.\n")
        else:
            print(f"¡Palabra válida! '{palabra}' tiene {longitud} letras.\n")
            break

    print(f"Total de intentos: {len(intentos)}")
    print(f"Historial de palabras ingresadas: {intentos}\n")


def leer_coordenada(etiqueta):
    """Lee una coordenada numérica distinta de cero con casting a float."""
    while True:
        entrada = input(f"Ingresa la coordenada {etiqueta} (distinta de 0): ").strip()
        try:
            # Conversión explícita (casting) de texto (str) a número decimal (float)
            valor = float(entrada)
        except ValueError:
            print(f"Error: '{entrada}' no es un número válido. Intenta de nuevo.\n")
            continue

        if valor == 0.0:
            print(f"Error: la coordenada {etiqueta} no puede ser 0. Intenta de nuevo.\n")
            continue

        return valor


def calcular_cuadrante():
    """Solicita coordenadas X y Y distintas de cero y muestra su cuadrante."""
    print("\n--- SECCIÓN 2: CUADRANTES DEL PLANO CARTESIANO ---")
    coord_x = leer_coordenada("X")
    coord_y = leer_coordenada("Y")

    if coord_x > 0 and coord_y > 0:
        indice = 0
    elif coord_x < 0 and coord_y > 0:
        indice = 1
    elif coord_x < 0 and coord_y < 0:
        indice = 2
    else:
        indice = 3

    cuadrante_nombre = CUADRANTES[indice]
    print(f"El punto ({coord_x}, {coord_y}) se encuentra en {cuadrante_nombre}.\n")


def mostrar_menu():
    """Muestra el menú principal y ejecuta la opción seleccionada."""
    while True:
        print("==========================================")
        print("      PROYECTO MÓDULO 2 - PYTHON          ")
        print("==========================================")
        print("1. Validar longitud de palabra (4-8 letras)")
        print("2. Determinar cuadrante en plano cartesiano")
        print("3. Ejecutar ambos retos en secuencia")
        print("4. Salir")
        opcion = input("Elige una opción (1-4): ").strip()

        if opcion == "1":
            validar_longitud_palabra()
        elif opcion == "2":
            calcular_cuadrante()
        elif opcion == "3":
            validar_longitud_palabra()
            calcular_cuadrante()
        elif opcion == "4":
            print("Programa finalizado. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Selecciona un número del 1 al 4.\n")


if __name__ == "__main__":
    mostrar_menu()
    