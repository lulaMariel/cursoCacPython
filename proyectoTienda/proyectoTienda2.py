import os
import sqlite3
from colorama import Fore, Style

# Creación y conexión de la base de datos

def iniciar_bbdd():
    conexion = sqlite3.connect("inventario.db") # Nombre de la bbdd
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                        codigo TEXT PRIMARY KEY,
                        nombre TEXT NOT NULL,
                        precio REAL NOT NULL,
                        cantidad INTEGER NOT NULL,
                        categoria TEXT DEFAULT 'Sin categoría'
                    )''')
    conexion.commit() # Confirma los cambios realizados
    return conexion, cursor

# Funciones del sistema de inventario

# Función para limpiar la terminal
def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar el menú
def mostrar_menu():
    print(Fore.RED, Style.BRIGHT, "\n\t••••• Gestión de Inventario •••••")
    print(Fore.CYAN + "\n• Menú de opciones: ")
    print("\t1. Registrar producto")
    print("\t2. Actualizar producto")
    print("\t3. Eliminar producto")
    print("\t4. Mostrar productos")
    print("\t5. Buscar producto")
    print("\t6. Generar reporte de stock")
    print("\t7. Vaciar tabla de productos")
    print("\t8. Salir")

# Función para registrar productos
def registrar_producto(cursor, conexion):
    print(Fore.RED, Style.BRIGHT, "\n\t••••• Registrar Producto •••••\n")
    
    # Condicional para que el código no pueda quedar vacío ni se repita
    while True:
        codigo = input("Ingrese el código del producto: ")
        if not codigo:
            print("El código no puede estar vacío.\n")
        else:
            cursor.execute("SELECT * FROM productos WHERE codigo = ?", (codigo,))
            if cursor.fetchone():
                print("El producto ya existe. Intente con otro código.\n")
            else:
                break

    # Nombre junto a un condicional para que no pueda quedar vacío
    nombre = input("Ingrese el nombre del producto: ").strip()
    while not nombre:
        print("El nombre no puede estar vacío.\n")
        nombre = input("Ingrese el nombre del producto: ").strip()

    # Condicional para que el precio sea válido
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio <= 0:
                print("El precio debe ser mayor a 0.\n")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un valor numérico válido para el precio.\n")

    # Condicional para que la cantidad sea válida
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad en stock: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0.\n")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número entero válido para la cantidad.\n")

    # Categoría junto a un condicional para que no pueda quedar vacío
    categoria = input("Ingrese la categoría del producto: ").strip()
    while not nombre:
        print("La categoría no puede estar vacía.\n")
        categoria = input("Ingrese la categoría del producto: ").strip()

    # Consulta SQL para que inserte los datos en la bbdd
    cursor.execute("INSERT INTO productos VALUES (?, ?, ?, ?, ?)", (codigo, nombre, precio, cantidad, categoria))
    conexion.commit() # Confirma los cambios realizados
    print("\n✔ Producto registrado con éxito.")

# Función para actualizar productos
def actualizar_producto(cursor, conexion):
    print(Fore.RED, Style.BRIGHT, "\n\t••••• Actualizar Producto •••••\n")
    codigo = input("Ingrese el código del producto que desea actualizar: ")

    # Consulta SQL para que busque y traiga el producto con el código ingresado
    cursor.execute("SELECT * FROM productos WHERE codigo = ?", (codigo,))
    producto = cursor.fetchone()

    if not producto: # Si el código no existe
        print("El producto no existe.")
        return

    # Si el código existe, le muestro cuál es el producto
    print(f"\nProducto actual: Código: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Stock: {producto[3]}, Categoría: {producto[4]}\n")

    # Para actualizar el nombre del producto
    nombre = input("Ingrese el nuevo nombre del producto (dejar vacío para mantener el actual): ") or producto[1]

    # Condional para actualizar el precio del producto y que el mismo sea válido
    while True:
        try:
            precio = input("Ingrese el nuevo precio del producto (dejar vacío para mantener el actual): ")
            precio = float(precio) if precio else producto[2]
            if precio <= 0:
                print("El precio debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un valor numérico válido para el precio.")

    # Condicional para actualizar la cantidad del producto y que la misma sea válida
    while True:
        try:
            cantidad = input("Ingrese la nueva cantidad en stock (dejar vacío para mantener el actual): ")
            cantidad = int(cantidad) if cantidad else producto[3]
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido para la cantidad.")

    # Para actualizar la categoría del producto
    categoria = input("Ingrese la nueva categoría del producto (dejar vacío para mantener el actual): ") or producto[4]

    # Consulta SQL para que actualice los datos en la bbdd
    cursor.execute("UPDATE productos SET nombre = ?, precio = ?, cantidad = ?, categoria = ? WHERE codigo = ?", (nombre, precio, cantidad, categoria, codigo))
    conexion.commit() # Confirma los cambios realizados
    print("\n✔ Producto actualizado con éxito.")

# Función para eliminar productos
def eliminar_producto(cursor, conexion):
    print(Fore.RED, Style.BRIGHT, "\n\t••••• Eliminar Producto •••••\n")
    codigo = input("Ingrese el código del producto que desea eliminar: ")

    # Consulta SQL para que busque y elimine los datos del código ingresado
    cursor.execute("DELETE FROM productos WHERE codigo = ?", (codigo,))
    if cursor.rowcount > 0: # Verifica si al menos una fila fue afectada
        conexion.commit() # Confirma los cambios realizados
        print("\n✔ Producto eliminado con éxito.")
    else:
        print("\nEl producto no existe.")

# Función para mostrar productos
def mostrar_productos(cursor):
    print(Fore.RED, Style.BRIGHT, "\n\t••••• Listado de Productos •••••\n")

    # Consulta SQL para que busque y traiga todos los datos de la bbdd
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall() # Recupera todas las filas que cumplen con la consulta SQL y las guarda en la variable
    if productos:
        for codigo, nombre, precio, cantidad, categoria in productos:
            print(Fore.CYAN, f"Código: {codigo}, Nombre: {nombre}, Precio: ${precio:.2f}, Stock: {cantidad}, Cateogoría: {categoria}\n")
    else:
        print("El inventario está vacío.")

# Función para buscar productos
def buscar_producto(cursor):
    print(Fore.RED, Style.BRIGHT, "\n\t••••• Buscar Producto •••••\n")
    busqueda = input("Ingrese el código o nombre del producto: ").lower()

    # Consulta SQL para que busque y traiga los datos del código o nombre ingresado
    cursor.execute("SELECT * FROM productos WHERE LOWER(codigo) LIKE ? OR LOWER(nombre) LIKE ?", (f"%{busqueda}%", f"%{busqueda}%"))
    resultados = cursor.fetchall() # Recupera todas las filas que cumplen con la consulta SQL y las guarda en la variable
    if resultados:
        for codigo, nombre, precio, cantidad, categoria in resultados:
            print(Fore.CYAN, f"\nCódigo: {codigo}, Nombre: {nombre}, Precio: ${precio:.2f}, Stock: {cantidad}, Categoría: {categoria}")
    else:
        print("\nNo se encontraron productos.")

# Función para generar reporte de bajo stock
def generar_reporte(cursor):
    print(Fore.RED, Style.BRIGHT, "\n\t••••• Reporte de Stock Bajo •••••\n")

    # Try/except para controlar que el número ingresado sea válido
    try:
        minimo = int(input("Ingrese la cantidad mínima de stock: "))

        # Consulta SQL para que busque y traiga los productos cuya cantidad sean menores al número ingresado
        cursor.execute("SELECT * FROM productos WHERE cantidad < ?", (minimo,))
        productos = cursor.fetchall() # Recupera todas las filas que cumplen con la consulta SQL y las guarda en la variable
        if productos:
            for codigo, nombre, precio, cantidad, categoria in productos:
                print(Fore.CYAN, f"Código: {codigo}, Nombre: {nombre}, Precio: ${precio:.2f}, Stock: {cantidad}, Categoría: {categoria}\n")
        else:
            print("\nNo hay productos con stock bajo.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Función para vaciar el inventario completo
def vaciar_inventario(cursor, conexion):
    print(Fore.RED, Style.BRIGHT, "\n\t••••• Vaciar Inventario •••••\n")

    # Consulta SQL para que busque si hay elementos en la tabla
    cursor.execute("SELECT COUNT(*) FROM productos")
    inventario = cursor.fetchone()[0] # Recupera una fila que cumple con la consulta SQL y, si hay, las guarda en la variable, sino devuelve None

    # Condicional para chequear que el inventario no esté vacío
    if inventario == 0:
        print("No hay productos en el inventario.")
        return 

    # Si el inventario no está vacío, advertencia
    confirm_delete = input("CUIDADO: ¿Está seguro que desea vaciar el inventario COMPLETO? (S/N): ").strip().lower()

    # Si el usuario elige S
    if confirm_delete == "s":
        
        # Consulta SQL para borrar todos los datos de la base de datos
        cursor.execute("DELETE FROM productos")
        conexion.commit() # Confirma los cambios realizados
        print("\n✔ Todos los productos han sido eliminados del inventario.")
    else:
        print("\n❌ Operación cancelada. El inventario no ha sido modificado.")

# Función principal
def main():

    # Incio la base de datos
    conexion, cursor = iniciar_bbdd()

    # Condicional que comienza una vez iniciada la base de datos
    while True:
        limpiar_terminal()
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            registrar_producto(cursor, conexion)
        elif opcion == "2":
            actualizar_producto(cursor, conexion)
        elif opcion == "3":
            eliminar_producto(cursor, conexion)
        elif opcion == "4":
            mostrar_productos(cursor)
        elif opcion == "5":
            buscar_producto(cursor)
        elif opcion == "6":
            generar_reporte(cursor)
        elif opcion == "7":
            vaciar_inventario(cursor, conexion)
        elif opcion == "8":
            print("Gracias por usar nuestro sistema de inventario. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
        input("\nPresione Enter para continuar...")

# Ejecuta el código contenido en def main()
if __name__ == "__main__":
    main()