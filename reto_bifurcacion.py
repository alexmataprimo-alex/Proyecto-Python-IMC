# reto_bifurcacion.py - Semana 6: Validación y Ciclos

def verificar_longitud_palabra():
    """Solicita una palabra hasta que tenga entre 4 y 8 letras."""
    print("--- 1. VERIFICACIÓN DE LONGITUD DE PALABRA ---")
    while True:
        palabra = input("Ingresa una palabra (entre 4 y 8 letras): ").strip()
        longitud = len(palabra)

        if longitud < 4:
            print(f"Hacen falta letras ({longitud}). Intenta con una palabra nueva.\n")
        elif longitud > 8:
            print(f"Sobran letras ({longitud}). Intenta con una palabra nueva.\n")
        else:
            print(f"¡Palabra correcta! Tiene {longitud} letras.\n")
            break


def determinar_cuadrante():
    """Solicita X y Y distintas de cero mediante ciclos while y ubica el cuadrante."""
    print("--- 2. UBICACIÓN EN EL PLANO CARTESIANO ---")
    while True:
        try:
            x = float(input("Ingresa la coordenada X (distinta de 0): "))
            if x == 0:
                print("Error: la coordenada X no puede ser 0. Inténtalo de nuevo.\n")
                continue

            y = float(input("Ingresa la coordenada Y (distinta de 0): "))
            if y == 0:
                print("Error: la coordenada Y no puede ser 0. Inténtalo de nuevo.\n")
                continue

            # Con X != 0 y Y != 0 garantizados, siempre cae en un cuadrante
            if x > 0 and y > 0:
                print(f"El punto ({x}, {y}) está en el Cuadrante I (+, +).\n")
            elif x < 0 and y > 0:
                print(f"El punto ({x}, {y}) está en el Cuadrante II (-, +).\n")
            elif x < 0 and y < 0:
                print(f"El punto ({x}, {y}) está en el Cuadrante III (-, -).\n")
            else:
                print(f"El punto ({x}, {y}) está en el Cuadrante IV (+, -).\n")

            break

        except ValueError:
            print("Error: debes ingresar un número válido. Inténtalo de nuevo.\n")


if __name__ == "__main__":
    print("==========================================")
    print("   RETO SEMANAL: VALIDACIÓN Y CICLOS      ")
    print("==========================================\n")

    verificar_longitud_palabra()
    determinar_cuadrante()

    print("==========================================")
    print("   ¡Reto de la semana completado!         ")
    print("==========================================")
    