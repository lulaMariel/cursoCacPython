# Saludando

print("\n")
nombre = str(input("Ingrese su nombre: "))
print("\n")
print("¡Hola ", nombre, "!", sep="")
print("\n")

# Entrada: 
# 1. Solicitar al usuario el nombre del juego

juego = str(input("Ingrese el nombre del juego del que quiere verificar stock: "))

# 2. Solicitar al usuario la cantidad actual de stock

cantidadStockActual = int(input(f"Ingrese la cantidad actual de stock de {juego}: "))

# Proceso:

if cantidadStockActual <= 1:
    print(f"Tenes en stock {cantidadStockActual} unidad de {juego}, REPONER URGENTE.")
elif cantidadStockActual <= 5:
    print(f"Tenes en stock {cantidadStockActual} unidades de {juego}, recomendable reponer.")
else:
    print(f"Tenes en stock {cantidadStockActual} unidades de {juego}, no es necesario reponer.")