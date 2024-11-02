# Inicio del proyecto final

# Saludando al usuario

while True: # Incio el bucle para evitar que, si el usuario ingresa un tipo inválido, el programa no se frene
    nombre = str(input("\nIngrese su nombre: ")) # Pide al usuario que ingrese su nombre

    if nombre == "": # Verifica que el nombre no quede vacío
        print("Por favor, ingrese su nombre.")

    elif nombre.isdigit(): # El parámetro isdigit() verifica que el nombre no contenga números (aprendido por chatgpt)
        print("Por favor, ingrese únicamente letras.")

    elif not nombre.isalpha(): # El parámtro isalpha() verifica que el nombre no contenga caracteres especiales (aprendido por chatgpt)
        print("Por favor, ingrese únicamente letras.")

    else:
        print(f"\n¡Hola {nombre}!") # Saluda al usuario
        break

# Iniciando proceso

productos = [] # Variable para almacenar los productos que ingrese el usuario

while True: # Iniciamos el bucle principal
    print("\n \tMenú de opciones: ")
    print("\n1. Registro: Alta de productos nuevos")
    print("\n2. Visualización: Consulta de datos de productos")
    print("\n3. Actualización: Modicar la cantidad en stock de un producto")
    print("\n4. Eliminación: Dar de baja algún producto")
    print("\n5. Listado: Listado completo de los productos")
    print("\n6. Reporte: Lista de productos con stock mínimo")
    print("\n7. Salir")
    
    try: # Inicio el try para evitar que un error frene el programa
        
        opcion = int(input((f"{nombre}, por favor, ingrese una opción del menú (1-7): "))) # Solicito al usuario que ingrese la opción que necesite usar

        if opcion == 7: # Me aseguro de que si elige el número 7, genere los print de despido y se rompa el bucle

            print("\nSaliendo del sistema...")
            print(f"¡Gracias por usar nuestro sistema provisorio, {nombre}, vuelva pronto!")
            break

        elif opcion == 1: # Inicio de la opción 1
            print("\nHa seleccionado la opción para dar de alta un producto nuevo")

# 1. Solicitarle al usuario nombre del producto
            while True: # Inicio un nuevo bucle dentro de la opción 1 para asegurarme de que se puedan cargar múltiples productos

                nombreProducto = str(input("\nIngrese el nombre del producto nuevo: ")) # Solicito al usuario el nombre del producto nuevo

                if nombreProducto == "": # Verifica que el nombre del producto no quede vacío
                    print("Por favor, ingrese el nombre del producto nuevo.")

                elif nombreProducto.isdigit(): # El parámetro isdigit() verifica que el nombre del producto nuevo no contenga números (aprendido por chatgpt)
                    print("Por favor, ingrese únicamente letras.")

                elif not nombreProducto.isalpha(): # El parámtro isalpha() verifica que el nombre del producto nuevo no contenga caracteres especiales (aprendido por chatgpt)
                    print("Por favor, ingrese únicamente letras.")

                else:
                    break # Sale del bucle si el nombre del producto nuevo es válido

# 2. Solicitarle al usuario precio del producto 
            while True: # Segundo bucle dentro de la opción 1 para asegurarme de que el precio sea válido

                try: # Inicio el try para evitar que un error en la carga del precio del producto frene el programa

                    precio = float(input(f"\nIngrese el precio de '{nombreProducto}': $")) # Solicito al usuario el precio del producto nuevo

                    if precio <= 0: # Concicional para evitar que el precio cargado no sea inválido

                        print("\nEl precio debe ser mayor a 0, por favor, vuelva a intentarlo.") # Si el precio es 0 o menor a 0, devuelve este print para avisarle al usuario y vuelve a solicitar el precio

                    else:
                        break # Sale del bucle si el precio es válido

                except ValueError:
                    print("\nPor favor, ingrese un precio válido.")

# 3. Solicitarle al usuario stock del producto
            while True: # Tercer bucle dentro de la opción 1 para asegurarme de que el stock sea válido
                    
                try: # Incio el try para evitar que un error en la carga del stock del producto frene el prorgama

                    stock = int(input(f"\nIngrese el stock de '{nombreProducto}': ")) # Solicito al usuario el stock del producto nuevo

                    if stock <= 0:

                        print("\nEl stock debe ser mayor a 0, por favor, vuelva a intentarlo.") # Si el stock es 0 o menor a 0, devuelve este print para avisarle al usuario y vuelve a solicitar el stock
                        
                    else:
                        break # Sale del bucle si el stock es válido
                    
                except ValueError:
                    print("El stock debe ser cargado en números enteros, por unidades.")
        
            # Agregar el producto completo a la lista
            productos.append((nombreProducto, precio, stock)) # Agrego el nombre del producto, su precio y su stock
            print(f"\nProducto '{nombreProducto}' agregado correctamente.")
            
    except ValueError:
        print("Por favor, ingrese una opción que se encuentre en el menú de opciones (1-7)")
    

    
print("\n\t Listado de productos ingresados: ")

for producto in productos: # Bucle que recorre la lista para poder mostrarsela al usuario al finalizar el programa
    nombreProducto, precio, stock = producto
    print(f"Producto: {nombreProducto}, Precio: ${precio:.2f}, Stock: {stock} unidades")