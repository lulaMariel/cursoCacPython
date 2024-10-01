# Saludando

print("\n")
nombre = str(input("Introduzca su nombre: "))
print("\n")
print("¡Hola ", nombre, "!", sep="")
print("\n")

# Solicitando litros, precio y distancia recorrida

litrosConsumidos100km = float(input("Introduzca la cantidad de litros consumidos por su vehículo por cada 100km de recorrido: "))
precioComustible = float(input("Introduzca el precio del combustible: "))
distanciaViaje = float(input("Introduzca la distancia (en km) del recorrido: "))
print("\n")

# Cálculos

litrosGastados = (litrosConsumidos100km * distanciaViaje) / 100
dineroGastado = (litrosGastados * precioComustible)

# Mostrar los detalles de los litros consumidos y el dinero gastado

print(nombre, ", los litros que consumió su vehículo en los ", distanciaViaje, "km recorridos fue de ", litrosGastados, "lt. \n"
    "El dinero gastado en combustible fue de $ ", dineroGastado, sep="")