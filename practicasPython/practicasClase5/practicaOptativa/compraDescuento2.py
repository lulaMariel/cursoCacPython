# Saludando

print("\n")
nombre = str(input("Ingrese su nombre: "))
print("\n")
print("¡Hola ", nombre, "!", sep="")
print("\n")

# Entrada: Solicitar datos al usuario

montoTotal = float(input("Ingrese el monto total de la compra: $ "))
cantidadArticulos = int(input("Ingrese la cantidad de artículos que está llevando: "))
descuento = 0

# Proceso: 

if cantidadArticulos >= 5 and montoTotal > 10000:
    descuento = (montoTotal * 15) / 100
    print(f"Tenes un 15% de descuento en tu compra. Te descontamos, del monto total, $ {descuento}.")
elif cantidadArticulos >= 3 and cantidadArticulos < 5:
    descuento = (montoTotal * 10) / 100
    print(f"Tenes un 10% de descuento en tu compra. Te descontamos, del monto total, $ {descuento}.")
else:
    print("\n")
    print("No aplica descuento / promoción.")
    print("\n")

# Salida: Imprimir valores
print("\t---Ticket de compra---\n")
print(f"Total: $ {montoTotal - descuento}")