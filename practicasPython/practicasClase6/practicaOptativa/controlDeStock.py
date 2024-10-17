# Saludando

print("\n")
nombre = str(input("Ingrese su nombre: "))
print("\n")
print("¡Hola ", nombre, "!", sep="")
print("\n")

# Inciando variables

contadorProductos = 0
nombreProducto = ""

# Solicitando datos al usuario y mostrando la cantidad de productos ingresados

while nombreProducto.lower() != "salir":
    nombreProducto = str(input("Ingrese el nombre del producto (o 'salir' para terminar): "))

    if nombreProducto.lower() == "salir":
        break
    
    cantidadStock = int(input(f"Ingrese la cantidad de stock para {nombreProducto}: "))
    contadorProductos += 1

print("\n")
print(f"La cantidad de productos ingresados fueron {contadorProductos} productos.")