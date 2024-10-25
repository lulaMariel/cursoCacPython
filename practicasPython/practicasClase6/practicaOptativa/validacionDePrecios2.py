# Saludando

print("\n")
nombre = str(input("Ingrese su nombre: "))
print("\n")
print("¡Hola ", nombre, "!", sep="")
print("\n")

# Entrada: Variables

precio = float(input("Ingrese el precio del producto: $ "))

# Proceso: 

while precio <= 0:
    precio = float(input("Por favor, ingrese un valor válido (mayor a 0)."))
print("\n")
print(f"Precio cargado: $ {precio}")