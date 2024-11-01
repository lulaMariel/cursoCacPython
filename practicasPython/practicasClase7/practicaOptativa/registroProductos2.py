# Variables

productos = [] # Va almacenando los productos que se van cargando
cargar = 1
indice = 0

# Proceso

while cargar == 1:
    print("\n")
    producto = str(input("Ingrese el nombre del producto: ")) # Creo la variable para pedirle al usuario
    productos.append(producto) # Agrega el "producto" que ingrese el usuario a la lista "productos"
    
    cargar = int(input("¿Desea agregar más productos? (1 para 'si' o 2 para 'no'): "))
    
print("\n")
print("Productos en inventario: ")
print("\n")

while indice < len(productos): # Muestra todos los índices (la longitud de la lista) que estén almacenados en la variable "productos"
    print(f"{productos[indice]}")
    indice += 1