# Saludando

print("\n")
nombre = str(input("Ingrese su nombre: "))
print("\n")
print("¡Hola ", nombre, "!", sep="")
print("\n")

# Entrada: Solicitando datos al usuario

montoTotal = float(input(f"{nombre}, ingrese el monto total de su compra: $"))
cantidadArticulos = int(input(f"Ahora, ingrese la cantidad de artículos que está comprando por ${montoTotal:.2f}: "))
print("\n")

# Proceso: Determinar los descuentos con condicionales

descuento = 0

if cantidadArticulos >= 5 and montoTotal > 10000:
    descuento = 0.15
elif cantidadArticulos >= 3 and cantidadArticulos < 5:
    descuento = 0.10
elif cantidadArticulos < 3:
    montoFinal = montoTotal
    print("No se aplican descuentos.")
    print(f"El monto final a abonar es ${montoFinal}.")
print("\n")

montoFinal = montoTotal * (1 - descuento)

# Salida: Imprimir montos

print(f"Monto original: {montoTotal}")
