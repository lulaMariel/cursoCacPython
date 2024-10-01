# Saludando

print("\n")
nombre = str(input("Ingresá tu nombre: "))
print("\n")
print("¡Hola, ", nombre,"!", sep="")
print("\n")

# Solicitando el nombre, la cantidad y el valor unitario

nombreProducto1 = str(input("Introduzca el nombre del primer producto: "))
cantidadProducto1 = int(input("Introduzca la cantidad que va a llevar del primer producto: "))
valorProducto1 = float(input("Introduzca el valor unitario del primer producto: "))
print("\n")
nombreProducto2 = str(input("Introduzca el nombre del segundo producto: "))
cantidadProducto2 = int(input("Introduzca la cantidad que va a llevar del segundo producto: "))
valorProducto2 = float(input("Introduzca el valor unitario del segundo producto: "))
print("\n")
nombreProducto3 = str(input("Introduzca el nombre del tercer producto: "))
cantidadProducto3 = int(input("Introduzca la cantidad que va a llevar del tercer producto: "))
valorProducto3 = float(input("Introduzca el valor unitario del tercer producto: "))
print("\n")

# Haciendo los cálculos e IVA

iva = (21 / 100)

precioTotalProducto1 = cantidadProducto1 * valorProducto1
precioTotalProducto2 = cantidadProducto2 * valorProducto2
precioTotalProducto3 = cantidadProducto3 * valorProducto3

precioFinalProducto1 = (precioTotalProducto1 * iva) + precioTotalProducto1
precioFinalProducto2 = (precioTotalProducto2 * iva) + precioTotalProducto2
precioFinalProducto3 = (precioTotalProducto3 * iva) + precioTotalProducto3

totalFinal = precioFinalProducto1 + precioFinalProducto2 + precioFinalProducto3

# Mostrar en la terminal el ticket de compra con todos los datos

print("Ticket de Compra", sep="")
print("\n")
print("El Precio Final incluye el IVA del 21%", sep="")
print("\n")
print("Producto", "\t\t", "Cantidad", "\t\t", "Precio", "\t\t", "Precio total", "\t\t", "Precio final", sep="")
print(nombreProducto1, "\t\t", cantidadProducto1, "\t\t\t", "$ ", valorProducto1, "\t\t", "$ ", precioTotalProducto1, "\t\t\t", "$ ", precioFinalProducto1, sep="")
print(nombreProducto2, "\t\t\t", cantidadProducto2, "\t\t\t", "$ ", valorProducto2, "\t\t", "$ ", precioTotalProducto2, "\t\t\t", "$ ", precioFinalProducto2, sep="")
print(nombreProducto3, "\t\t\t", cantidadProducto3, "\t\t\t", "$ ", valorProducto3, "\t\t", "$ ", precioTotalProducto3, "\t\t\t", "$ ", precioFinalProducto3, sep="")
print("\n")
print("Total a abonar: ", "\t\t\t\t\t\t\t\t\t", "$ ", totalFinal, sep="")