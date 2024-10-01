# Saludando

print("\n")
nombre = input("Ingresá tu nombre: ")
print("\n")
print("¡Hola, ", nombre,"!", "¡Bienvenido a la calculadora de propinas!", sep="")

# Solitando monto total de la cuenta y porcentaje de propina que se desea dejar

print("\n")
montoTotal = float(input("Ingresá el monto total de la cuenta: "))
porcentajePropina = float(input("Ahora, ingresá el porcentaje de propia que desea dejar (sin el %): "))

# Haciendo los cálculos

valorPropina = montoTotal * (porcentajePropina / 100)
totalAPagar = montoTotal + valorPropina

print("\n")
print("Ticket")
print("\n")
print("Cuenta: $", montoTotal, sep="")
print("\n")
print("Propina: $", valorPropina, sep="")
print("\n")
print("Total a pagar: $", totalAPagar, sep="")
print("\n")
print("Si se desea dejar una propina del ", porcentajePropina, "%, de $", montoTotal, ", entonces, el total a pagar es de $", totalAPagar, sep="")