from math import sqrt, ceil, floor  # Cada vez que tenga que usarlo no necesito llamar al módulo
import math # Cada vez que quiera usar una función de math, debo llamar al módulo

# Funciones comunes
print("")

# Raiz cuadrada

raiz_cuadrada = sqrt(25) # 5.
print(raiz_cuadrada)

# Redondeo
print("")

redondeo_arriba = ceil(8.3) # 9
print(redondeo_arriba)
print("")
redondeo_abajo = floor(3.8) # 3
print(redondeo_abajo)
print("")

# Valor absoluto
print("")

valor_absoluto = math.fabs(-10) # 10 (módulo)
print(valor_absoluto)

print("Bienvenidos a esta calculadora mágica")
print("\n1. Calcular la raíz cuadrada.")
print("2. Redondear un número hacia arriba.")
print("3. Redondear un número hacia abajo.")
print("4. Sacar un valor absoluto.")

opcion = int(input("\nPor favor, elija una de las opciones (1-4): "))

if opcion == 1:
    numero = float(input("Ingrese un valor para sacar la raíz cuadrada: "))
    resultado = sqrt(numero)
    print(f"La raíz cuadrada de {numero} es de: {resultado}")
elif opcion == 2:
    numero = float(input("Ingrese un número para redondear para arriba: "))
    resultado = ceil(numero)
    print(f"El redondeo hacia arriba de {numero} es de: {resultado}")
elif opcion == 3:
    numero = float(input("Ingrese un número para redondear hacia abajo: "))
    resultado = floor(numero)
    print(f"El redondeo hacia abajo de {numero} es de: {resultado}")
else:
    numero = float(input("Ingrese un número para sacar el valor absoluto: "))
    resultado = math.fabs(numero)
    print(f"El valor absoluto de {numero} es de: {resultado}")

# Módulo random
import random
print("")

# Elegir un número al azar
numero_aleatorio = random.randint(1, 10)
print(f"Número aleatorio: {numero_aleatorio}")
print("")

# Seleccionar un elemento al azar de una lista
colores = ["rojo", "verde", "azul", "naranja"]
color_aleatorio = random.choice(colores)
print(f"Color aleatorio: {color_aleatorio}")
print("")

# Generar número aleatorio
numero_flotante = random.random()
print(f"Numero flotante aleatorio: {numero_flotante}")
