# reto_bifurcacion.py

def verificar_longitud_palabra():
    """Función 1: Compara la longitud de una palabra usando if-elif-else"""
    print("--- 1. VERIFICACIÓN DE LONGITUD DE PALABRA ---")
    palabra = input("Ingresa una palabra: ").strip()
    longitud = len(palabra)
    
    if longitud < 4:
        print(f"Hacen falta letras. La palabra tiene {longitud} caracteres (mínimo requerido: 4).\n")
    elif 4 <= longitud <= 8:
        print(f"¡Palabra correcta! Tiene {longitud} letras (está en el rango de 4 a 8).\n")
    else:
        print(f"Tiene demasiadas letras. La palabra tiene {longitud} caracteres (máximo permitido: 8).\n")

def determinar_cuadrante():
    """Función 2: Evalúa si X y Y son positivos o negativos para ubicar el cuadrante"""
    print("--- 2. UBICACIÓN EN EL PLANO CARTESIANO ---")
    try:
        x = float(input("Ingresa el valor de X: "))
        y = float(input("Ingresa el valor de Y: "))
        
        # Lógica de bifurcación basada en los signos de X y Y
        if x > 0 and y > 0:
            print(f"El punto ({x}, {y}) se encuentra en el Cuadrante I (+, +).\n")
        elif x < 0 and y > 0:
            print(f"El punto ({x}, {y}) se encuentra en el Cuadrante II (-, +).\n")
        elif x < 0 and y < 0:
            print(f"El punto ({x}, {y}) se encuentra en el Cuadrante III (-, -).\n")
        elif x > 0 and y < 0:
            print(f"El punto ({x}, {y}) se encuentra en el Cuadrante IV (+, -).\n")
        else:
            print(f"El punto ({x}, {y}) se encuentra sobre uno de los ejes cartesianos o en el origen (0,0).\n")
            
    except ValueError:
        print("Error: Debes ingresar valores numéricos válidos para las coordenadas.\n")

# Bloque principal para ejecutar ambas funciones
if __name__ == "__main__":
    print("==========================================")
    print("   RETO SEMANAL: LÓGICA DE BIFURCACIÓN    ")
    print("==========================================\n")
    
    verificar_longitud_palabra()
    determinar_cuadrante()
    
    print("==========================================")
    print("   ¡Prueba del reto finalizada con éxito! ")
    print("==========================================")