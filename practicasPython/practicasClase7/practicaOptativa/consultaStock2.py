# Variables

print("\n")
productos = ["Leche", "Azúcar", "Chocolate", "Café", "Queso", "Atún", "Gaseosa"]
consulta = str(input("Ingrese el nombre del producto que querés consultar: "))
# encontrado = False --> Ponerlo por fuera del ciclo while hace que, una vez que se establezca True en una consulta, seguirá siendo True porque no se reincia dentro del ciclo.
# indice = 0 --> Pasa lo mismo que con el "encontrado".

# Proceso

while True:
    
    encontrado = False
    indice = 0
    
    while indice < len(productos):
        if productos[indice] == consulta:
            encontrado = True
    
        indice += 1
        
    if encontrado:
        print("\n")
        print(f"El producto '{consulta}' se encuentra en stock.")
        print("\n")
    
        nuevaConsulta = int(input("¿Deseas consultar otro producto? (1 para 'si' o 2 para 'no'): "))
    
        if nuevaConsulta == 1:
            print("\n")
            consulta = str(input("Ingrese el nombre del producto que querés consultar: "))
        else:
            print("\n")
            print("¡Gracias por utilizar nuestro sistema de consulta de stock!")
            break
        
    else:
        print("\n")
        print(f"El producto '{consulta}' no se encuentra disponible.")
        
        agregarProducto = int(input("¿Desea añadir el producto al inventario? (1 para 'si' o 2 para 'no'): "))
        
        if agregarProducto == 1:
            productos.append(consulta)
            print("\n")
            print(f"{consulta} ha sido añadido al inventario.")
            
        else:
            print("\n")            
            print("¡Gracias por utilizar nuestro sistema de consulta de stock!")
            break

print("\n")
print("\t Listado del nuevo inventario: ")
print("\n")

for producto in productos:
    print(f"{producto}")