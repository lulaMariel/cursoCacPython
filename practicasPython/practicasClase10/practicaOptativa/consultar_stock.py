# Crear diccionario con un inventario ficticio.

inventario = {
    "Azúcar": 5,
    "Yerba": 2,
    "Harina": 8,
    "Sal": 10,
    "Huevo": 5,
    "Leche": 3,
}

print("")

producto = input("Ingrese el nombre del producto del que desea consultar el stock: ")

print("")
stock = inventario.get(producto, "Producto no encontrado")

# print(f"El stock de {producto} es: {stock}")