# Iniciar una función

print("")
def nombre_funcion(parametros_opcionales):
    # Líneas de código
    resultado_opcional = print(f"¡Bienvenido {parametros_opcionales}!")
    return resultado_opcional
    
# Ejemplo 1:
print("")
def saludo():
    print("¡Bienvenido!")

saludo() # Llamo a la función para ejecutarla

# Ejemplo 2:
print("")
def saludar_persona(nombre):
    print(f"¡Bienvenido {nombre}!")

nombre = input("¿Cuál es tu nombre?: ")
saludar_persona(nombre)

# Ejemplo 3:
print("")
def division(numero):
    return numero / 2

resultado = division(10)
print(f"La división es = {resultado}")

# Ejemplo 4:
print("")

def suma(numero, numero2, numero3):
    return numero + numero2 + numero3

print(suma(2,4,3))

# Ejemplo 5:
print("")

def saludar_persona2(nombre = "Luciana"):
    print(f"¡Bienvenido {nombre.lower()}!")

saludar_persona2("Melina")
saludar_persona2()

# Ejemplo 6:
print("")

def calcular_promedio(lista):
    suma = sum(lista)
    cantidad = len(lista)
    return suma / cantidad

notas = [8,5,3,10]
promedio = calcular_promedio(notas)
print(f"El promedio de las notas es: {promedio: .2f}")