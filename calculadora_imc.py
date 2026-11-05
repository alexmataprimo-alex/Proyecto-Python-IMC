# calculadora_imc.py

# 1. Captura de datos
nombre = input("Ingresa tu nombre: ")
apellido_paterno = input("Ingresa tu apellido paterno: ")
apellido_materno = input("Ingresa tu apellido materno: ")

# 2. Convertir a formato Title (primera letra mayúscula)
# El método .title() pone la primera letra de cada palabra en mayúscula
nombre_f = nombre.title()
ap_paterno_f = apellido_paterno.title()
ap_materno_f = apellido_materno.title()

edad = int(input("Ingresa tu edad: "))
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))

# 3. Cálculo del IMC
imc = peso / (estatura ** 2)

# 4. Salida formateada con f-strings y redondeo a 2 decimales
print("\n" + "="*30)
print("   REPORTE DE SALUD (IMC)")
print("="*30)
print(f"Nombre completo: {nombre_f} {ap_paterno_f} {ap_materno_f}")
print(f"Edad:            {edad} años")
print(f"Peso:            {peso} kg")
print(f"Estatura:        {estatura} m")
print("-"*30)
print(f"Tu IMC es:       {imc:.2f}")
print("="*30)

