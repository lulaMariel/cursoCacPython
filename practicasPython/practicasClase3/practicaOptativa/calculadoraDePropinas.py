# Saludando

print()
nombre = input("Ingresá tu nombre: ")
print()
print("¡Hola, ", nombre,"!", "¡Bienvenido a la calculadora de propinas!", sep="")

# Solitando monto total de la cuenta y porcentaje de propina que se desea dejar

print()
montoTotal = float(input("Ingresá el monto total de la cuenta: "))
porcentajePropina = float(input("Ahora, ingresá el porcentaje de propia que desea dejar (sin el %): "))

# Haciendo los cálculos

valorPropina = montoTotal * (porcentajePropina / 100)

totalAPagar = montoTotal + valorPropina

print()
print("Ticket")
print()
print("Cuenta: $", montoTotal, sep="")
print()
print("Propina: $", valorPropina, sep="")
print()
print("Total a pagar: $", totalAPagar, sep="")
print()
print("Si se desea dejar una propina del ", porcentajePropina, "%, de $", montoTotal, ", entonces, el total a pagar es de $", totalAPagar, sep="")