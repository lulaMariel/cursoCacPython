# Inicio de la Tienda

# Salundando al usaurio

while True:
    nombre = str(input("\nIngrese su nombre: "))
    
    if nombre == "":
        print("¿Nombre vacío?")
    elif nombre.isdigit():
        print("¿Nombre con números?")
    elif not nombre.isalpha():
        print("¿Caracteres especiales?")
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
            print("\nSaliendo del sistema... ¡Vuelva pronto!")
            break
        
        elif opcion == 1:
            print("\nHa seleccionado 'Registro: Alta de productos nuevos'")
            
            while True:
                while True:
                    nombreProducto = str(input("\nIngrese el nombre del producto nuevo: "))
                
                    if nombreProducto == "":
                        print("¿Nombre vacío?")
                    elif nombreProducto.isdigit():
                        print("¿Nombre con números?")
                    elif not nombreProducto.isalpha():
                        print("¿Caracteres especiales?")
                    else:
                        break
                
                while True:
                    try:
                        precio = float(input(f"\nIngrese el precio de '{nombreProducto}': $"))
                        
                        if precio <= 0:
                            print("\n¿Sin precio?")
                        else:
                            break
                    except ValueError:
                        print("\n¿Sin precio x2?")
                        
                while True:
                    try:
                        stock = int(input(f"\nIngrese el stock de '{nombreProducto}': "))
                        
                        if stock <= 0:
                            print("\n¿Sin stock?")
                        else:
                            break
                    except ValueError:
                        print("¿Sin stock x2?")
                        
                productos.append((nombreProducto, precio, stock))
                print(f"El producto '{nombreProducto}' fue agergado con éxito")
                
                otroProducto = int(input("¿Desea agregar otro producto? (1 para sí o 2 para no): "))
                
                if otroProducto != 1:
                    break
        
        elif opcion == 2:
            print("\nHa seleccionado 'Visualización: Consulta de datos de productos'")
            print("\n\tListado de productos ingresados: ")
            
            for producto in productos:
                print(f"\nProducto: {producto[0]} \n\tPrecio: ${producto[1]} ; Stock: {producto[2]}")
        
        elif opcion == 3:
            print("\nHa seleccionado 'Actualización: Modificar la cantidad en stock del producto'")
        elif opcion == 4:
            print("\nHa seleccionado 'Eliminacióon: Dar de baja algún producto'")
        elif opcion == 5:
            print("\nHa seleccionado 'Listado: Listado completo de los productos'")
        elif opcion == 6:
            print("\nHa seleccionado 'Reporte: Lista de productos con stock mínimo'")
    except ValueError:
        print("Error: Por favor, ingrese una opción que se encuentre en el menú de opciones (1-7)")