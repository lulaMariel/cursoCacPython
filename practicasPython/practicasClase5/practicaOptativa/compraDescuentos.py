# Saludando

print("\n")
nombre = str(input("Ingrese su nombre: "))
print("\n")
print("¡Hola ", nombre, "!", sep="")
print("\n")

# Solicitando datos al usuario

montoTotal = float(input(f"{nombre}, ingrese el monto total de su compra: $"))
cantidadArticulos = int(input(f"Ahora, ingrese la cantidad de artículos que está comprando por ${montoTotal:.2f}: "))
print("\n")

descuento = 0

# Determinar los descuentos con condicionales e imprimo montos finales

if cantidadArticulos >= 5 and montoTotal > 10000:
    descuento = (montoTotal * 15) / 100
    print(f"Descuento aplicado 15%, descontamos: $ {descuento}.")
    print(f"El monto final a abonar es de $ {montoTotal - descuento}.")
elif cantidadArticulos >= 3 and cantidadArticulos < 5:
    descuento = (montoTotal * 10) / 100
    print(f"Descuento aplicado 10%, descontamos: $ {descuento}.")
    print(f"El monto final a abonar es de $ {montoTotal - descuento}.")
else: 
    print("No se aplican descuentos.")
    print(f"El monto final a abonar es de $ {montoTotal}.")