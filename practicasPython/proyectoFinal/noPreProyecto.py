# MENU PRINCIPAL
#////////////////////////////////////////////////////////////////////////////////////
# ENTRADA: MENÚ DE OPCIONES.
productos = []  # Lista para almacenar los productos

while True:
    print("Menú para la Gestión de Productos:\n")
    print("1. Registro: Alta de productos nuevos.")
    print("2. Visualización: Consulta de datos de productos.")
    print("3. Actualización: Modificar la cantidad en stock de un producto.")
    print("4. Eliminación: Dar de baja productos.")
    print("5. Listado: Listado completo de los productos en la base de datos.")
    print("6. Reporte de Bajo Stock: Lista de productos con cantidad bajo mínimo.")
    print("7. Salir.")

    try:
        opcion = int(input("Por favor, seleccione una opción (1-7): "))

        if opcion == 7:
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        elif opcion == 1:
            print("Ha seleccionado 'Registro: Alta de productos nuevos.'")

            while True:  # Bucle para registrar múltiples productos si el usuario lo desea
                nombre = input("Nombre del producto: ")

                # Bucle para asegurarse de que el precio sea válido
                while True:
                    try:
                        precio = float(input("Precio del producto: "))
                        if precio <= 0:
                            print("El precio debe ser mayor a 0. Inténtelo de nuevo.")
                        else:
                            break  # Salir del bucle si el precio es válido
                    except ValueError:
                        print("Entrada no válida para el precio. Debe ser un número mayor a 0.")

                # Bucle para asegurarse de que el stock sea válido
                while True:
                    try:
                        stock = int(input("Stock del producto: "))
                        if stock <= 0:
                            print("El stock debe ser mayor a 0. Inténtelo de nuevo.")
                        else:
                            break  # Salir del bucle si el stock es válido
                    except ValueError:
                        print("Entrada no válida para el stock. Debe ser un número entero mayor a 0.")

                producto = [nombre, precio, stock]
                productos.append(producto)
                print("Producto registrado con éxito.")

                # Preguntar si el usuario desea agregar otro producto
                agregar_mas = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
                if agregar_mas != 's':
                    break  # Salir del bucle de registro y volver al menú principal

        elif opcion == 2:
            print("Ha seleccionado 'Visualización: Consulta de datos de productos.'")
            print("\nListado de Productos Registrados:")

            for producto in productos:
                print(f"Nombre: {producto[0]} - Precio: ${producto[1]}, Stock: {producto[2]}")
                print("-" * 60)
        elif opcion == 3:
            print("Ha seleccionado 'Actualización: Modificar la cantidad en stock de un producto.'")
        elif opcion == 4:
            print("Ha seleccionado 'Eliminación: Dar de baja productos.'")
        elif opcion == 5:
            print("Ha seleccionado 'Listado: Listado completo de los productos en la base de datos.'")
        elif opcion == 6:
            print("Ha seleccionado 'Reporte de Bajo Stock: Lista de productos con cantidad bajo mínimo.'")
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 7.")

    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número del 1 al 7.")

    print("\n")  # Salto de línea para mejor visualización






#SALIDA: NRO DE OPCIÓN SOLICITADA.
#////////////////////////////////////////////////////////////////////////////////////