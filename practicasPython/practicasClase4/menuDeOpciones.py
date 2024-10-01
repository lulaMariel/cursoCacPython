# Menú de opciones

print()
print("Menú de Gestión para tus Productos", sep="")
print()
print("1. Alta de productos nuevos", sep="")
print("2. Consulta de datos de productos", sep="")
print("3. Modificar la cantidad en stock de un producto", sep="")
print("4. Dar de baja prodcutos", sep="")
print("5. Listado completo de los productos", sep="")
print("6. Lista de prodcutos con cantidad bajo mínimo", sep="")
print("7. Salir", sep="")
print()

# Solicitar al usuario que seleccione una opción
opcion = int(input("Por favor, seleccione una opción (1-7): "))
print()

# Mostramos el númeor de la opción seleccionada
print("Has seleccionado: ", opcion, sep="")