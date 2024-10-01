# Menú de opciones

print("\n")
print("Menú de Gestión de Inventario:", sep="")
print("\n")
print("1. Alta de productos nuevos", sep="")
print("2. Consulta de datos de productos", sep="")
print("3. Modificar la cantidad en stock de un producto", sep="")
print("4. Dar de baja prodcutos", sep="")
print("5. Listado completo de los productos", sep="")
print("6. Lista de prodcutos con cantidad bajo mínimo", sep="")
print("7. Salir", sep="")
print("\n")

# Solicitar al usuario que seleccione una opción
opcion = int(input("Por favor, seleccione una opción (1-7): "))
print("\n")

# Mostramos el númeor de la opción seleccionada
print("Usted ha seleccionado la opción: ", opcion, sep="")