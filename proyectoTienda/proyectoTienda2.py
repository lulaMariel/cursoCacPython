import os
import sqlite3
from colorama import Fore, Style

# Funciones del sistema de inventario

# Limpiar la terminal
def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Conexión y creación de la base de datos
def inicializar_base_datos():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                        codigo TEXT PRIMARY KEY,
                        nombre TEXT NOT NULL,
                        precio REAL NOT NULL,
                        cantidad INTEGER NOT NULL,
                        categoria TEXT DEFAULT 'Sin categoría'
                    )''')
    conexion.commit()
    return conexion, cursor

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

    nombre = input("Ingrese el nombre del producto: ").strip()
    while not nombre:
        print("El nombre no puede estar vacío.\n")
        nombre = input("Ingrese el nombre del producto: ").strip()

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio <= 0:
                print("El precio debe ser mayor a 0.\n")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un valor numérico válido para el precio.\n")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad en stock: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0.\n")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número entero válido para la cantidad.\n")

    categoria = input("Ingrese la categoría del producto: ").strip()
    while not nombre:
        print("La categoría no puede estar vacía.\n")
        categoria = input("Ingrese la categoría del producto: ").strip()

    cursor.execute("INSERT INTO productos VALUES (?, ?, ?, ?, ?)", (codigo, nombre, precio, cantidad, categoria))
    conexion.commit()
    print("\n✔ Producto registrado con éxito.")

# Función para actualizar productos
def actualizar_producto(cursor, conexion):
    print(Fore.RED, Style.BRIGHT, "\n\t••••• Actualizar Producto •••••\n")
    codigo = input("Ingrese el código del producto que desea actualizar: ")

    cursor.execute("SELECT * FROM productos WHERE codigo = ?", (codigo,))
    producto = cursor.fetchone()

    if not producto:
        print("El producto no existe.")
        return

    print(f"Producto actual: Código: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Stock: {producto[3]}, Categoría: {producto[4]}")

    nombre = input("Ingrese el nuevo nombre del producto (dejar vacío para mantener el actual): ") or producto[1]
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

    categoria = input("Ingrese la nueva categoría del producto (dejar vacío para mantener el actual): ") or producto[4]

    cursor.execute("UPDATE productos SET nombre = ?, precio = ?, cantidad = ?, categoria = ? WHERE codigo = ?", 
                (nombre, precio, cantidad, categoria, codigo))
    conexion.commit()
    print("\n✔ Producto actualizado con éxito.")

# Función para eliminar productos
def eliminar_producto(cursor, conexion):
    print(Fore.RED, Style.BRIGHT, "\n\t••••• Eliminar Producto •••••\n")
    codigo = input("Ingrese el código del producto que desea eliminar: ")

    cursor.execute("DELETE FROM productos WHERE codigo = ?", (codigo,))
    if cursor.rowcount > 0:
        conexion.commit()
        print("\n✔ Producto eliminado con éxito.")
    else:
        print("\nEl producto no existe.")

# Función para mostrar productos
def mostrar_productos(cursor):
    print(Fore.RED, Style.BRIGHT, "\n\t••••• Listado de Productos •••••\n")
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    if productos:
        for codigo, nombre, precio, cantidad, categoria in productos:
            print(Fore.CYAN, f"Código: {codigo}, Nombre: {nombre}, Precio: ${precio:.2f}, Stock: {cantidad}, Cateogoría: {categoria}")
    else:
        print("El inventario está vacío.")

# Función para buscar productos
def buscar_producto(cursor):
    print(Fore.RED, Style.BRIGHT, "\n\t••••• Buscar Producto •••••\n")
    busqueda = input("Ingrese el código o nombre del producto: ").lower()
    cursor.execute("SELECT * FROM productos WHERE LOWER(codigo) LIKE ? OR LOWER(nombre) LIKE ?", 
                (f"%{busqueda}%", f"%{busqueda}%"))
    resultados = cursor.fetchall()
    if resultados:
        for codigo, nombre, precio, cantidad, categoria in resultados:
            print(Fore.CYAN, f"Código: {codigo}, Nombre: {nombre}, Precio: ${precio:.2f}, Stock: {cantidad}, Categoría: {categoria}")
    else:
        print("\nNo se encontraron productos.")

# Función para generar reporte de bajo stock
def generar_reporte(cursor):
    print(Fore.RED, Style.BRIGHT, "\n\t••••• Reporte de Stock Bajo •••••\n")
    try:
        minimo = int(input("Ingrese la cantidad mínima de stock: "))
        cursor.execute("SELECT * FROM productos WHERE cantidad < ?", (minimo,))
        productos = cursor.fetchall()
        if productos:
            for codigo, nombre, precio, cantidad, categoria in productos:
                print(Fore.CYAN, f"Código: {codigo}, Nombre: {nombre}, Precio: ${precio:.2f}, Stock: {cantidad}, Categoría: {categoria}")
        else:
            print("\nNo hay productos con stock bajo.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

def vaciar_inventario(cursor, conexion):
    print(Fore.RED, Style.BRIGHT, "\n\t••••• Vaciar Inventario •••••\n")
    
    cursor.execute("SELECT COUNT(*) FROM productos")
    inventario = cursor.fetchone()[0]
    
    if inventario == 0:
        print("No hay productos en el inventario.")
        return 
    confirm_delete = input("CUIDADO: ¿Está seguro que desea vaciar el inventario COMPLETO? (S/N): ").strip().lower()
    
    if confirm_delete == "s":
        cursor.execute("DELETE FROM productos")
        conexion.commit()
        print("\n✔ Todos los productos han sido eliminados del inventario.")
    else:
        print("\n❌ Operación cancelada. El inventario no ha sido modificado.")

# Función principal
def main():
    conexion, cursor = inicializar_base_datos()
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

if __name__ == "__main__":
    main()