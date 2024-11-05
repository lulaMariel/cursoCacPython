# En esta preentrega, quise hacer los prints que se refieren a los datos ingresados por el usuario un poco más cómicos, espero no ofender, solo fue para divertir un rato (para la entrega final, va a estar lo más formal posible😁)
# Recomiendo probar todas las variaciones posibles, fui creativa

# Inicio del proyecto final

# Saludando al usuario

while True: # Incio el bucle para evitar que, si el usuario ingresa un tipo inválido, el programa no se frene
    nombre = str(input("\nIngrese su nombre: ")) # Pide al usuario que ingrese su nombre

    if nombre == "": # Verifica que el nombre no quede vacío
        print("Hola usuario fantasma, sin nombre no hay programa que funcione. Escriba su nombre por favor.")

    elif nombre.isdigit(): # El parámetro isdigit() verifica que el nombre no contenga números (aprendido por chatgpt)
        print("¿Su nombre tiene números? No se haga el chistoso, póngalo bien.")

    elif not nombre.isalpha(): # El parámtro isalpha() verifica que el nombre no contenga caracteres especiales (aprendido por chatgpt)
        print("No sabía que se permitían caracteres especiales en los nombres, de ser así me hubiera gustado que mi nombre sea $ol€d@d. Por favor, escriba bien su nombre, gracias.")

    else:
        print(f"\n¡Hoy es mi día de suerte! ¡¡¡Pusiste bien tu nombre!!! ¡Hola {nombre}!") # Saluda al usuario
        break

# Iniciando proceso

productos = [] # Variable para almacenar los productos que ingrese el usuario

while True: # Iniciamos el bucle principal
    print("\n \tMenú de opciones: ")
    print("1. Registro: Alta de productos nuevos")
    print("2. Visualización: Consulta de datos de productos")
    print("3. Actualización: Modificar la cantidad en stock de un producto")
    print("4. Eliminación: Dar de baja algún producto")
    print("5. Listado: Listado completo de los productos")
    print("6. Reporte: Lista de productos con stock mínimo")
    print("7. Salir")
    
    try: # Inicio el try para evitar que un error frene el programa
        
        opcion = int(input((f"\n{nombre}, por favor, ingrese una opción del menú (1-7): "))) # Solicito al usuario que ingrese la opción que necesite usar

        if opcion == 7: # Me aseguro de que si elige el número 7, genere los print de despido y se rompa el bucle

            print("\nYa que nos abandonas, no tenemos más opción que decirte: Saliendo del sistema...") # Me despido del usuario
            print(f"A pesar de que te vayas... ¡Te agradezco por usar nuestro sistema provisorio, {nombre}, vuelva pronto!") # Me despido del usuario
            break

        elif opcion == 1: # Inicio de la opción 1
            print("\nHa seleccionado 'Registro: Alta de prodcutos nuevos'") # Indico al usuario cuál fue la opción elegida

# 1. Solicitarle al usuario nombre del producto
            while True: # Inicio un nuevo bucle dentro de la opción 1 para asegurarme de que se puedan cargar múltiples productos
                while True: # Segundo bucle dentro de la opción 1 para asegurarme de que el nombre sea válido

                    nombreProducto = str(input("\nIngrese el nombre del producto nuevo: ")) # Solicito al usuario el nombre del producto nuevo

                    if nombreProducto == "": # Verifica que el nombre del producto no quede vacío 
                        print("¿En algún lugar del mundo fabrican productos y no les ponen un nombre? Por favor, no sea payaso y dígame que producto desea inrgesar.") # Aviso de que el dato ingresado no es válido

                    elif nombreProducto.isdigit(): # El parámetro isdigit() verifica que el nombre del producto nuevo no contenga números (aprendido por chatgpt)
                        print("Está bien, existen productos que tienen números en su nombre pero, ¿sabe que son? MARCAS y yo pedí producto. Ingrese un producto correcto.") # Aviso de que el dato ingresado no es válido

                    elif not nombreProducto.isalpha(): # El parámtro isalpha() verifica que el nombre del producto nuevo no contenga caracteres especiales (aprendido por chatgpt)
                        print("Esta si no la vi nunca... ¿Caracteres especiales en los nombres de producto? ¿Quién permitió eso? Dígale que acepto la moción, pero mientras tanto... Escriba bien el nombre del producto, gracias.") # Aviso de que el dato ingresado no es válido

                    else:
                        break # Sale del bucle si el nombre del producto nuevo es válido

# 2. Solicitarle al usuario precio del producto 
                while True: # Tercer bucle dentro de la opción 1 para asegurarme de que el precio sea válido

                    try: # Inicio el try para evitar que un error en la carga del precio del producto frene el programa

                        precio = float(input(f"\nIngrese el precio de '{nombreProducto}': $")) # Solicito al usuario el precio del producto nuevo

                        if precio <= 0: # Concicional para evitar que el precio cargado no sea inválido

                            print("\n¿En qué lugar me dejan este producto gratis o me dan dinero a mi favor por llevarlo? ¡Pero paseme la dirección que voy corriendo! No sea ingenuo e ingrese bien el precio, gracias.") # Si el precio es 0 o menor a 0, devuelve este print para avisarle al usuario y vuelve a solicitar el precio

                        else:
                            break # Sale del bucle si el precio es válido

                    except ValueError:
                        print("\n¿Se olvidaron de ponerle el precio en la góndola? Ingrese el precio por favor.") # Aviso de que el dato ingresado no es válido

# 3. Solicitarle al usuario stock del producto
                while True: # Cuarto bucle dentro de la opción 1 para asegurarme de que el stock sea válido
                    
                    try: # Incio el try para evitar que un error en la carga del stock del producto frene el prorgama

                        stock = int(input(f"\nIngrese el stock de '{nombreProducto}': ")) # Solicito al usuario el stock del producto nuevo

                        if stock <= 0: # Concicional para evitar que el stock cargado no sea inválido

                            print("\nSi no tenes stock del producto, ¿Para qué lo cargas en sistema exactamente? ¡Ya dígame cuántas unidades tiene del producto!") # Si el stock es 0 o menor a 0, devuelve este print para avisarle al usuario y vuelve a solicitar el stock
                        
                        else:
                            break # Sale del bucle si el stock es válido
                    
                    except ValueError:
                        print("¿Acaso usted puede tener 11,5 manzanas? Debería denunciarlo, creo que le robaron...") # Aviso de que el dato ingresado no es válido
            
                # Agregar el producto completo a la lista
                productos.append((nombreProducto, precio, stock)) # Agrego el nombre del producto, su precio y su stock
                print(f"\n¡Gracias al cielo! El producto '{nombreProducto}' fue agregado correctamente.") # Aviso de que el producto fue agregado con éxito
                
                # Preguntar si desea agregar otro producto
                otroProducto = int(input("¿Desea agregar otro producto? (1 para sí o 2 para no): ")) # Le pido que indique 1 para agregar otro producto o 2 para cortar el ciclo
                if otroProducto != 1: # Condicional para verificar que el número ingresado sea distinto de 1
                    break # Sale del bucle si el usuario no quiere agreagar otro producto
            
        elif opcion == 2: # Inicio de la opción 2
            
            print("\nHa seleccionado 'Visualización: Consulta de datos de productos'") # Indico al usuario cuál fue la opción elegida
                
            print("\n\t Listado de productos ingresados: ") # Título del listado

            for producto in productos: # Bucle que recorre la lista para poder mostrarsela al usuario al finalizar el programa
                print(f"\nProducto: {producto[0]} \n\tPrecio: ${producto[1]} ; Stock: {producto[2]}") # Muestra los valores ingresados por producto en la opción 1, tomando los índices de cada solicitud (nombre del producto nuevo = índice 0, precio del producto = índice 1, stock de producto = índice 2)
        
        # elif opcion == 3: # Inicio de la opción 3
            
        #     print("\nHa seleccionado 'Actualización: Modicar la cantidad en stock de un producto'")
            
        # elif opcion == 4: # Inicio de la opción 4
            
        #     print("\nHa seleccionado 'Eliminación: Dar de baja algún producto'")
            
        # elif opcion == 5: # Inicio de la opción 5
            
        #     print("\nHa seleccionado 'Listado completo de los productos'")
            
        # elif opcion == 6: # Inicio de la opción 6
            
        #     print("\nHa seleccionado 'Reporte: Lista de productos con stock mínimo'")

    except ValueError:
        print("Error: Por favor, ingrese una opción que se encuentre en el menú de opciones (1-7)")