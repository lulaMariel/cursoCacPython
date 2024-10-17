# Saludando

print("\n")
nombre = str(input("Ingrese su nombre: "))
print("\n")
print("¡Hola ", nombre, "!", sep="")
print("\n")

# Inciando variables. En este caso, no son necesarios contadores o acumuladores

precio = 0.0

# Solicitando datos al usuario y mostrando el precio aceptado

while precio <= 0:
    precio = float(input("Ingrese el precio del producto: $ "))

    if precio > 0:
        print(f"Precio del producto: $ {precio}")
    else:
        print("Error: El precio debe ser mayor a 0. Intente nuevamente.")