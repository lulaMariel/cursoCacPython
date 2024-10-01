# Saludando

print("\n")
nombre = input("Ingresá el nombre completo del Consumidor Final: ")
print("\n")
print("¡Hola, ", nombre,"!", "¡Bienvenido a la calculadora de propinas!", sep="")
print("\n")

# Armado de Factura

numFactura = int(input("Ingresá el número de tu factura: "))
numMesa = int(input("Ingresá el número de tu mesa: "))
print("\n")

# Cálculo del Servicio

porcentajePropina = int(input("Ingrese el porcentaje de propina que desea dejar (sin el %): "))
montoTotal = float(input("Ingrese el monto total de la factura: "))
propina = (porcentajePropina / 100) * montoTotal
print("\n")

# Impresión de la Factura

print("Restaurante Lulita", sep="")
print("\n")
print("Facuta N°:", numFactura, sep="")
print("Mesa N°: ", numMesa, sep="")
print("Consumidor final: ", nombre, sep="")
print("\n")

# Lista de Consumos

print("Unidades \t Descripción", sep="")
print("   2 \t\t Gaseosa", sep="")
print("   1 \t\t Mila. napolitana", sep="")
print("   1 \t\t Puré de papas", sep="")
print("   1 \t\t Papas fritas", sep="")
print("   2 \t\t Hamburguesas con queso", sep="")
print("\n")

# Total a pagar con propina incluída

print("El monto total a pagar es de: $ ", montoTotal, "\n",
    "La propina del ", porcentajePropina, "%", " quedaría en $ ", propina, "\n",
    "Total a Pagar: $ ", propina + montoTotal, sep="")