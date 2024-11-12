# Inicio de la Tienda

# Salundando al usaurio

while True:
    nombre = str(input("\nIngrese su nombre: "))
    
    if nombre == "":
        print("Por favor, ingrese su nombre")
    elif nombre.isdigit():
        print("No se permiten números en el nombre. Por favor, ingrese su nombre correctamente")
    elif not nombre.isalpha():
        print("No se permiten caracteres especiales en el nombre. Por favor, ingrese su nombre correctamente")
    else:
        print(f"¡Hola {nombre}!")
        break
    
# Inciando proceso

productos = []

while True:
    print("\n\tMenú de opciones: ")
    print("1. Registro: Alta de producto nuevos")
    print("2. Visualización: Consulta de datos de productos")
    print("3. Actualiación: Modificar la cantidad en stock de un producto")
    print("4. Eliminación: Dar de baja algún producto")
    print("5. Listado: Listado completo de los productos")
    print("6. Reporte: Lista de productos con stock mínimo")
    print("7. Salir")
    
    try:
        opcion = int(input(f"\n{nombre}, por favor, ingrese una opción del menú (1-7): "))
        
        if opcion == 7:
            print("\nSaliendo del sistema... ¡Gracias por usar nuestro sistema! \n¡Vuelva pronto!")
            break
        
        elif opcion == 1:
            print("\nHa seleccionado 'Registro: Alta de productos nuevos'")
            
            while True:
                while True:
                    nombreProducto = str(input("\nIngrese el nombre del producto nuevo: "))
                
                    if nombreProducto == "":
                        print("Por favor, ingrese el nombre del producto")
                    elif nombreProducto.isdigit():
                        print("No se permiten números en el nombre del producto. Por favor, ingrese el nombre del producto correctamente")
                    elif not nombreProducto.isalpha():
                        print("No se permiten caracteres especiales en el nombre de producto. Por favor, ingrese el nombre del producto correctamente")
                    else:
                        break
                
                while True:
                    try:
                        precio = float(input(f"\nIngrese el precio de '{nombreProducto}': $"))
                        
                        if precio <= 0:
                            print("\nEl precio no puede ser menor o igual a 0. Por favor, ingese el precio del producto correctamente")
                        else:
                            break
                    except ValueError:
                        print("\nPor favor, ingrese el precio del producto")
                        
                while True:
                    try:
                        stock = int(input(f"\nIngrese el stock de '{nombreProducto}': "))
                        
                        if stock <= 0:
                            print("\nEl stock no puede ser menor o igual a 0. Por favor, ingrese el stock del producto correctamente")
                        else:
                            break
                    except ValueError:
                        print("Por favor, ingrese el stock del producto,")
                        
                productos.append({"nombre": nombreProducto, "precio": precio, "stock": stock}) # Agrego los productos a un DICCIONARIO en vez de a una TUPLA para que se puedan modificar en la opción 3.
                print(f"El producto '{nombreProducto}' fue agergado con éxito")
                
                otroProducto = int(input("¿Desea agregar otro producto? (1 para sí o 2 para no): "))
                
                if otroProducto != 1:
                    break
        
        elif opcion == 2:
            print("\nHa seleccionado 'Visualización: Consulta de datos de productos'")
            print("\n\tListado de productos ingresados: ")
            
            for producto in productos:
                print(f"\nProducto: {producto[0]} \n\tPrecio: ${producto[1]} ; Stock: {producto[2]}")
        
        # elif opcion == 3:
        #     print("\nHa seleccionado 'Actualización: Modificar la cantidad en stock del producto'")

        #     # Primero necesito saber sobre qué producto se va a hacer la actualización
        #     vendido = input("Ingrese el nombre del producto que desea actualizar: ")

        #     # Variable de control para indicar si el producto se encontró
        #     producto_encontrado = False

        #     for producto in productos:
        #         if producto["nombre"] == vendido:
        #             producto_encontrado = True
        #             # Solicitud de cantidad vendida y actualización de stock
        #             while True:
        #                 try:
        #                     cantidadVendida = int(input(f"Ingrese la cantidad vendida de {producto['nombre']}: "))
        #                     if cantidadVendida <= 0:
        #                         print("Por favor, ingrese un valor mayor a 0.")
        #                     elif cantidadVendida > producto["stock"]:
        #                         print("No hay stock suficiente para esta cantidad, intente con un valor menor.")
        #                     else:  # Actualización de stock
        #                         producto["stock"] -= cantidadVendida
        #                         print(f"Stock actualizado: Nueva cantidad de stock de {producto['nombre']}: {producto['stock']}")
        #                         print("Producto actualizado con éxito.")
        #                     eliminarMas = input("¿Desea actualizar más productos? (S para sí o N para no): ")
        #                     if eliminarMas.lower() != "s":
        #                         break
        #                 except ValueError:
        #                     print("Por favor, ingrese un número válido.")
        #             break  # Salir del bucle si se encontró el producto y se actualizó

        #     if not producto_encontrado:
        #         print("Producto no encontrado, vuelva a intentarlo.")

        elif opcion == 4:
            print("\nHa seleccionado 'Eliminacióon: Dar de baja algún producto'")
        elif opcion == 5:
            print("\nHa seleccionado 'Listado: Listado completo de los productos'")
        elif opcion == 6:
            print("\nHa seleccionado 'Reporte: Lista de productos con stock mínimo'")
    except ValueError:
        print("Error: Por favor, ingrese una opción que se encuentre en el menú de opciones (1-7)")