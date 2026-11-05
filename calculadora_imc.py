# calculadora_imc.py

print("=== CALCULADORA DE IMC ROBUSTA ===")

# 1. Validación para que los nombres no estén vacíos
while True:
    nombre = input("Ingresa tu nombre: ").strip()
    if nombre:
        break
    print("El campo no puede estar vacío. Inténtalo de nuevo.")

while True:
    apellido_paterno = input("Ingresa tu apellido paterno: ").strip()
    if apellido_paterno:
        break
    print("El campo no puede estar vacío. Inténtalo de nuevo.")

while True:
    apellido_materno = input("Ingresa tu apellido materno: ").strip()
    if apellido_materno:
        break
    print("El campo no puede estar vacío. Inténtalo de nuevo.")

# Formato estético con .title()
nombre_f = nombre.title()
ap_paterno_f = apellido_paterno.title()
ap_materno_f = apellido_materno.title()

# 2. Validación de datos numéricos (Edad)
while True:
    try:
        edad = int(input("Ingresa tu edad (años): "))
        if edad > 0:
            break
        print("Por favor, ingresa una edad mayor a 0.")
    except ValueError:
        print("Error: Debes ingresar un número entero válido para la edad.")

# Validación de datos numéricos (Peso)
while True:
    try:
        peso = float(input("Ingresa tu peso en kg (ej. 75.5): "))
        if peso > 0:
            break
        print("Por favor, ingresa un peso mayor a 0.")
    except ValueError:
        print("Error: Debes ingresar un valor numérico válido para el peso.")

# Validación de datos numéricos (Estatura)
while True:
    try:
        estatura = float(input("Ingresa tu estatura en metros (ej. 1.75): "))
        if estatura > 0:
            break
        print("Por favor, ingresa una estatura mayor a 0.")
    except ValueError:
        print("Error: Debes ingresar un valor numérico válido para la estatura.")

# 3. Cálculo del IMC
imc = peso / (estatura ** 2)

# 4. Salida formateada con f-strings y redondeo a 2 decimales
print("\n" + "="*30)
print("     REPORTE DE SALUD (IMC)")
print("="*30)
print(f"Nombre completo: {nombre_f} {ap_paterno_f} {ap_materno_f}")
print(f"Edad:            {edad} años")
print(f"Peso:            {peso} kg")
print(f"Estatura:        {estatura} m")
print("-"*30)
print(f"Tu IMC es:       {imc:.2f}")
print("="*30)
