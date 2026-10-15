# calculadora_imc.py

# Captura de datos desde el teclado
nombre = input("Ingresa tu nombre: ")
apellido_paterno = input("Ingresa tu apellido paterno: ")
apellido_materno = input("Ingresa tu apellido materno: ")

# Realizamos el casting (conversión) de tipos
edad = int(input("Ingresa tu edad: "))             # int
peso = float(input("Ingresa tu peso en kg: "))     # float
estatura = float(input("Ingresa tu estatura en metros: ")) # float

# Cálculo del IMC: peso / estatura al cuadrado
imc = peso / (estatura ** 2)

# Mostrar resultados
print(f"\n--- Resultados para {nombre} {apellido_paterno} ---")
print(f"Edad: {edad}")
print(f"Tu IMC calculado es: {imc:.2f}")

