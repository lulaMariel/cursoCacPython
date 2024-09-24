# Saludando

print()
nombre = input("Ingresá tu nombre: ")
print()
print("¡Hola, ", nombre,"!", sep="")

# Explicando conceptos y solicitando números

print()
print("Para este ejercicio, los números que ingreses deben ser exclusivamente enteros.")
print()
num1 = int(input("Ingresá el primer número: "))
num2 = int(input("Ingresá el segundo número: "))

# Hacemos los cálculos

suma = num1 + num2

resta = num1 - num2

multiplo = num1 * num2

modulo = num1 % num2

# Leyendas de resultados

print()
print("Ahora, con los números ingresados, procederemos a realizar los cálculos correspondientes a: Suma, resta, multiplicación y módulo.")
print()

print("Operador \t\tResultado")
print()
print("Suma: \t\t\t", suma, sep="")
print()
print("Resta: \t\t\t", resta, sep="")
print()
print("Multiplicación: \t", multiplo, sep="")
print()
print("Módulo: \t\t", modulo, sep="")