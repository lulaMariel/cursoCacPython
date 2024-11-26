# Tarea: Escribir una función que permita registrar un nuevo producto en el inventario, pero con la condición de que el stock debe ser mayor a 0 y el precio debe ser un valor positivo.
# En caso de ingresar un stock o precio no válido, debe mostrar un mensaje de error y pedir los datos nuevamente hasta que sean correctos.

print("")

inventario = {}
id_producto = 0

def registrar_producto():
    global id_producto

    while True: # Para ingresar varios productos
    
        nombre = input("Por favor, ingrese el nombre del producto: ")
        descripcion = input("Por favor, ingrese una breve descripción del producto: ")

        print("")

        # Validar que stock > 0 

        stock = -1 # Declaro la variable negativa para que siempre se ejecute el programa

        while stock <= 0:
            stock = int(input("Por favor, ingrese el stock del producto: "))

            if stock <= 0:
                print("Error: La cantidad del producto debe ser mayor a 0.")
            else:
                print(f"El stock de {nombre} es de {stock}. Stock cargado correctamente.")

        print("")
        
        # Validar que precio > 0

        precio = -1

        while precio <= 0:
            precio = int(input("Por favor, ingrese el precio del producto: $"))

            if stock <= 0:
                print("Error: El precio debe ser mayor a 0.")
            else:
                print(f"El precio de {nombre} es ${precio}. Precio cargado correctamente.")
        
        print("")

        # Guardar producto en el inventario
        inventario[id_producto] = {
            "nombre": nombre,
            "descripción": descripcion,
            "stock": stock,
            "precio": precio,
        }

        # Mostrar el producto cargado
        print("El producto fue cargado correctamente.")
        print(f"Código del producto {nombre}: {id_producto}")
        id_producto += 1

        print("")
        
        # Preguntar si desea registrar otro producto
        otro_producto = int(input("\n¿Desea agregar otro producto al inventario? (1 para sí o 2 para no): "))
        if otro_producto != 1:
            print("¡Gracias por usar nuestro sistema! Hasta luego.")
            break

    # Mostrar inventario
    print("\nInventario actual: \n")
    for codigo, datos in inventario.items():
        print(f"Producto {codigo}: \n Nombre: {datos['nombre']}, \n Descripción: {datos['descripción']}, \n Stock: {datos['stock']}, \n Precio: ${datos['precio']}")

registrar_producto()