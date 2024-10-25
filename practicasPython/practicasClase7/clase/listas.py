# Listas: 

lista = ["Leche", "Huevos", "Carne", "Queso", "Salchichas"]

print("\n")
print(lista) # Muestra la lista completa
print("\n")

# Subíndices de la lista, forma de acceder a él

print(lista[0]) # Muestra el primer elemento de la lista, es decir, "Leche"
print(lista[1]) # Muestra "Huevos"
print(lista[2]) # Muestra "Carne"
print(lista[3]) # Muestra "Queso"
print(lista[4]) # Muestra "Salchichas"
print("\n")

# Modificaciones

lista[0] = "Yogurt" # Cambia el primer elemento, es decir, "Leche" por "Yogurt"
print(lista[0]) # Muestra el nuevo elemento del índice
print("\n")

lista.append("Postre") # Agrega un elemento a la lista
print(lista) # Muestra la lista con el nuevo elemento
print("\n")

lista.insert(2, "Pollo") # Inserta / agrega en el subíndice indicado, un nuevo elemento
print(lista) # Muestra la lista con el nuevo elemento
print("\n")

lista.remove("Salchichas") # Borra el elemento específico, es decir, borra "Salchichas", no va por índices
print(lista) # Muestra la lista con el elemento borrado
print("\n")

lista.pop(1) # Borra el elemento que esté en el índice indicado, es decir, borra "Huevos"
print(lista) # Muestra la lista con el índice borrado
print("\n")

# Tuplas: 

tupla = (1, 2, 3, 4, 5) # Funciona igual a la lista, con la diferencia que se pone entre "()" y no permite modificaciones