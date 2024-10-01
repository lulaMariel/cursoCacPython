# Precio total con IVA:

# Entrada: Solicitar el precio del prodcuto y el procentaje de IVA
print()
precio = float(input("Precio del producto: "))
iva = float(input("Porcentaje de IVA (sin el %): "))
print()

# Proceso: Calcular el monto del IVA y el precio total
montoIva = (precio * iva) / 100
precioTotal = precio + montoIva

# Salida: Mostrar el precio total incluyendo IVA
print("El precio total con IVA es: ", precioTotal, sep="")



# Calculo del descuento: 

# Entrada: Solicitar el precio del producto y el porcentaje de descuento
print()
precio = float(input("Precio del producto: "))
descuento = float(input("Porcentaje de descuento (sin el %): "))
print()

# Proceso: Calcular el monto del descuento y el precio final
montoDescuento = (precio * descuento) / 100
precioFinal = precio - montoDescuento

# Salida: Mostrar el precio final después del descuento
print("El precio final después del descuento es: ", precioFinal, sep="")



# Compra con varios artículos

# Entrada: Solicitar el precio unitario y la cantidad de artículos
print()
precioUnitario = float(input("Ingresá el precio unitario del artículo: "))
cantidad = int(input("Ingresá la cantidad de artículos comprados: "))
print()

# Proceso: Calcular el costo total
costoTotal = precioUnitario * cantidad

# Salida: Mostrar el costo total de la compra
print("El costo total de la compra es: ", costoTotal, sep="")