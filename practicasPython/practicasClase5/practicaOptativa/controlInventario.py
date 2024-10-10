# Saludando

print("\n")
nombre = str(input("Ingrese su nombre: "))
print("\n")
print("¡Hola ", nombre, "!", sep="")
print("\n")

# Pedir datos al usuario

videojuego = str(input("Ingrese el nombre del videojuego del que quiere actualizar inventario: "))
stockActual = int(input(f"Ingrese el stock actual de {videojuego}: "))

# Condicionales

if stockActual < 3:
    print(f"Hay poco stock de {videojuego}. Se necesita comprar más unidades.", sep="")
else:
    print(f"Hay stock suficiente de {videojuego}. No es necesario comprar más unidades.", sep="")