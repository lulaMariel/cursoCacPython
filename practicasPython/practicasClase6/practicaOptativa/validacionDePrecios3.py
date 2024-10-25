# En esta solución, aprendemos a usar try except.
# try: Acaba puede haber un posible error. De haberlo, pasa directo al except. Primero verifica si hay erorres y después sigue con el bucle dependiendo de si lo hay o no

# Saludando

print("\n")
nombre = str(input("Ingrese su nombre: "))
print("\n")
print("¡Hola ", nombre, "!", sep="")
print("\n")

# Entrada: Variables

precio = -1 # Al ser un número inválido para nuestro bucle, este comienza a correr desde que lo iniciamos, no se lo pedimos al usuario

# Proceso: 

while precio <= 0:
    try:
        precio = float(input("Ingrese el precio del producto: $"))

        if precio <= 0:
            print("Por favor, ingrese un valor válido (mayor a 0).")

    except ValueError: 
        print("Error: Por favor, ingrese un valor numérico.")

else:
    print("\n")
    print(f"Precio cargado: ${precio}")
