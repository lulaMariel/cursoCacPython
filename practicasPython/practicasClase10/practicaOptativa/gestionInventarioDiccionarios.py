# Tarea: En un comercio se necesita gestionar los productos y sus precios. Desarrollar un programa.
    # Indicaciones: 
        # 1. Ingresar el nombre de tres productos y su precio correspondiente, guardándolos en un diccionario donde la clave es el nombre del producto y el valor es su precio;
        # 2. Una vez ingresados, mostrará todos los productos y sus precios en pantalla.

inventario = {
    "Manzana": "Precio: $100",
    "Naranja": "Precio: $110",
    "Uvas": "Precio: $132",
}

for producto, precio in inventario.items():
    print(f"Producto: {producto}, {precio}")