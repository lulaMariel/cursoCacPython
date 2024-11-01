# Lista de listas

# matiz = [
#     [0, 1, 2] # Subíndice 0
#     [3, 4, 5] # Subíndice 1
#     [6, 7, 8] # Subíndice 2
# ]

listaCompras = [
    ["Manzana", 4, 10], # Poner "," SI O SI, sino no los toma como índices
    ["Peras", 2, 5],
    ["Kiwi", 4, 15],
]

# Acceder a elementos de la lista

print(listaCompras [0][0]) # = "Manzana" El primer subíndice indica la lista dentro de "listaCompras" y el segundo subíndice indica el elemento dentro de la lista que indicamos
print(listaCompras [0][2]) # = "10"
print(listaCompras [2][1]) # = "4"
print(listaCompras [2][0]) # = "Kiwi"