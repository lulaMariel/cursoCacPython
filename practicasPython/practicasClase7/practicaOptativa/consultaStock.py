# Variables

productos = ["Leche", "Azúcar", "Chocolate", "Café", "Queso", "Atún", "Gaseosa"]
consulta = str(input("Ingrese el nombre del producto que querés consultar: "))
indice = 0
encontrado = False

# Proceso

while indice < len(productos):
    if productos[indice] == consulta:
        encontrado = True
        break
    
    indice += 1

if encontrado:
    print("\n")
    print(f"El producto '{consulta}' se encuentra en stock.")
else:
    print("\n")
    print(f"El producto '{consulta}' no está disponible.")