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

print("1. La suma entre los números ingresados dá como resultado: ", suma, sep="")
print()
print("2. La resta entre los números ingresados dá como resultado: ", resta, sep="")
print()
print("3. La multiplicación entre los números ingresados dá como resultado: ", multiplo, sep="")
print()
print("4. El módulo entre los números ingresados dá como resultado: ", modulo, sep="")