import os
from colorama import Fore, Style, Back


# Funciones del sistema de inventario

# Limpiar la terminal
def limpiar_terminal(): # Cada vez que el usuario termina de usar una función, "borra" la terminal para que quede un menú limpio
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar el menú
def mostrar_menu():
    print(Fore.RED, Style.BRIGHT, Back.WHITE, "\n\t••••• Gestión de Inventario •••••")
    print(Fore.CYAN +"\n• Menú de opciones: ")
    print("\t1. Registrar producto")
    print("\t2. Actualizar producto")
    print("\t3. Eliminar producto")
    print("\t4. Mostrar productos")
    print("\t5. Buscar producto")
    print("\t6. Generar reporte de stock")
    print("\t7. Salir")

# Función para registrar los productos
def registrar_producto(inventario):
    print(Fore.RED, Style.BRIGHT, Back.WHITE, "\n\t••••• Registrar Producto •••••\n")
    
    while True:
        print(Fore.CYAN, end='')
        codigo = input("Ingrese el código del producto: ")
        if not codigo:
            print("El código no puede estar vacío.\n")
        elif codigo in inventario:
            print("El producto ya existe. Intente con otro código.\n")
        else:
            break 
    
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        if not nombre:
            print("El nombre no puede estar vacío.\n")
        else:
            break 
        
    while True:
        try:
            precio = input("Ingrese el precio del producto: ")
            precio = float(precio)
            if precio <= 0:
                print("El precio debe ser mayor a 0.\n")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un valor numérico válido para el precio.\n")
            
    while True:
        try:
            cantidad = input("Ingrese la cantidad en stock: ")
            cantidad = int(cantidad)
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0.\n")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número entero válido para la cantidad.\n")
    
    inventario[codigo] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    print("\n✔ Producto registrado con éxito.")

# Función para actualizar los productos
def actualizar_producto(inventario):
    print(Fore.RED, Style.BRIGHT, Back.WHITE, "\n••••• Actualizar Producto •••••\n")
    
    while True:
        print(Fore.CYAN, end='')
        codigo = input("Ingrese el código del producto que desea actualizar: ")
        if not codigo:
            print("El código no puede estar vacío. Intente nuevamente.")
        elif codigo not in inventario:
            print("El producto no existe. Intente nuevamente.")
        else:
            break
    
    print(f"Producto actual: {inventario[codigo]}")
    
    nombre = input("Ingrese el nuevo nombre del producto (dejar vacío para mantener el actual): ")
    if not nombre: 
        nombre = inventario[codigo]["nombre"]
    
    while True:
        try:
            precio = input("Ingrese el nuevo precio del producto (dejar vacío para mantener el actual): ")
            if precio: 
                precio = float(precio)
                if precio <= 0:
                    print("El precio debe ser mayor a 0. Intente nuevamente.")
                    continue
            else:
                precio = inventario[codigo]["precio"]
            break
        except ValueError:
            print("Por favor, ingrese un valor numérico válido para el precio.")
    
    while True:
        try:
            cantidad = input("Ingrese la nueva cantidad en stock (dejar vacío para mantener el actual): ")
            if cantidad: 
                cantidad = int(cantidad)
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0. Intente nuevamente.")
                    continue
            else:
                cantidad = inventario[codigo]["cantidad"]
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido para la cantidad.")
    
    
    inventario[codigo] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    print("\n✔ Producto actualizado con éxito.")

# Función para eliminar los productos
def eliminar_producto(inventario):
    print(Fore.RED, Style.BRIGHT, Back.WHITE, "\n••••• Eliminar Producto •••••\n")
    print(Fore.CYAN, end='')
    codigo = input("Ingrese el código del producto que desea eliminar: ")
    if codigo in inventario:
        del inventario[codigo]
        print("\n✔ Producto eliminado con éxito.")
    else:
        print("\nEl producto no existe.")

# Función para mostrar los productos
def mostrar_productos(inventario):
    print(Fore.RED, Style.BRIGHT, Back.WHITE, "\n••••• Listado de Productos •••••\n")
    if inventario:
        for codigo, datos in inventario.items():
            print(Fore.CYAN, f"Código: {codigo}, Nombre: {datos['nombre']}, Precio: ${datos['precio']:.2f}, Stock: {datos['cantidad']}")
    else:
        print("El inventario está vacío.")

# Función para buscar los productos
def buscar_producto(inventario):
    print(Fore.RED, Style.BRIGHT, Back.WHITE, "\n••••• Buscar Producto •••••\n")
    print(Fore.CYAN, end='')
    producto_buscado = input("Ingrese el código o nombre del producto que desea buscar: ").lower()
    resultados = [
        (codigo, datos)
        for codigo, datos in inventario.items()
        if producto_buscado in codigo.lower() or producto_buscado in datos["nombre"].lower()
    ]
    if resultados:
        print("\nResultados de búsqueda:")
        for codigo, datos in resultados:
            print(f"Código: {codigo}, Nombre: {datos['nombre']}, Precio: ${datos['precio']:.2f}, Stock: {datos['cantidad']}")
    else:
        print("\nNo se encontraron productos.")

# Función para generar el reporte de bajo stock
def generar_reporte(inventario):
    print(Fore.RED, Style.BRIGHT, Back.WHITE, "\n••••• Reporte de Stock Bajo •••••\n")
    print(Fore.CYAN, end='')
    minimo = int(input("Ingrese la cantidad mínima de stock para el reporte: "))
    bajo_stock = {codigo: datos for codigo, datos in inventario.items() if datos["cantidad"] < minimo}
    if bajo_stock:
        print("\nProductos con stock bajo:")
        for codigo, datos in bajo_stock.items():
            print(f"Código: {codigo}, Nombre: {datos['nombre']}, Precio: ${datos['precio']:.2f}, Stock: {datos['cantidad']}")
    else:
        print("\nNo hay productos con stock bajo.")

# Programa principal

def main():
    inventario = {}
    while True:
        limpiar_terminal()
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            registrar_producto(inventario)
        elif opcion == "2":
            actualizar_producto(inventario)
        elif opcion == "3":
            eliminar_producto(inventario)
        elif opcion == "4":
            mostrar_productos(inventario)
        elif opcion == "5":
            buscar_producto(inventario)
        elif opcion == "6":
            generar_reporte(inventario)
        elif opcion == "7":
            print("Gracias por usar nuestro sistema de inventario. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()  