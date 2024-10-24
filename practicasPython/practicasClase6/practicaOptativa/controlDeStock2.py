# Saludando

print("\n")
nombre = str(input("Ingrese su nombre: "))
print("\n")
print("¡Hola ", nombre, "!", sep="")

# Declarando variables

productos = "" # Es una variable que adentro va a almacenar un string, y se va a ir llenando con los productos que agregue el usuario
stockTotal = 0 # La inicio para contabilizar el stock total. Empieza en sin stocl (0), el cual va aumentando a medida que se cargan productos

# Proceso

while productos.lower() != "salir":
    print("\n")
    productos = str(input("Ingrese el nombre del producto que desea agregar (o 'salir' para terminar): "))
    if productos.lower() != "salir":
        cantidad = int(input(f"Ingrese la cantidad en stock de {productos.lower()}: "))
        stockTotal += cantidad # Acumulamos el total de productos ingresados, en vez de sumar de a 1 porque no es el stock real
else: # Qué hace el programa si se corta el ciclo. Para no usar "break". No es necesario escribir "else", podemos escribir los print respetando el indentado (del if o del while, es indistinto)
    print("\n")
    print(f"El total de productos es de {stockTotal}.")