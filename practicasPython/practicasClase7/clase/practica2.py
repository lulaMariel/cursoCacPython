# Búsqueda de artículos

listaCompras = [
    ["Manzana", 25, 5],
    ["Pera", 30, 2],
    ["Kiwi", 40, 6],
    ["Limón", 50, 8]
]

productoBuscado = "Kiwi"
encontrado = False # Para que el programa pueda determinar de que, si su valor cambia a "True", entonces signifca que el "producto buscado" fue encontrado. En cambio, si continúa en "False", significa que no lo encontró.

for producto in listaCompras:
    nombre = producto[0]
    precio = producto[1]
    cantidad = producto[2]
    
    if nombre == productoBuscado:
        print("\n")
        print(f"El producto '{productoBuscado}' está disponible. Su cantidad en stock es de {cantidad} unidades y su precio es de ${precio} pesos.")
        
        encontrado = True
        break
        
if not encontrado:
    print("Producto no disponible. Cargarlo manualmente.")