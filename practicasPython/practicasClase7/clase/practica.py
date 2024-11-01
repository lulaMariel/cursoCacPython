# Lista de compras

listaCompras = [
    ["Manzana", 25, 5],
    ["Pera", 30, 2],
    ["Kiwi", 40, 6],
    ["Limón", 50, 8]
]

# for ... in ... = Secuencia/bucle en cuanto al recorrido de una lista. Primero indica el nombre de la variable temporal/volátil, la cual va a almacenar los índices que tenga internamente la otra variable. En el siguiente caso, "producto" es la variable temporal que almacena los datos que están dentro de la variable "listaCompras". Una vez que termina con el primer subíndice de la lista, pasa al siguiente.

for producto in listaCompras:
    nombre = producto[0]
    precio = producto[1]
    cantidad = producto[2]
    
    print("\n")
    print(f"Producto: {nombre}, Precio: ${precio}, Cantidad: {cantidad}")