codigos = []

for i in range(4): # Inicia en 0 y termina en 3, por ende son 4 códigos. Sino podría darle inicio 1 y fin 5, donde empezaría en 1 y termina en 4
    
    codigo = input("\nIngrese el código del producto: ") # Pide un código hasta llegar al rango 4
    codigos.append(codigo)
    
for i in range(4):
    print(f"Producto {i + 1}: {codigos[i]}")
    
# for i in range(0, 4): # Inicio 0 y fin 4 para que muestre los 4 productos
#     print(f"Producto {i + 1}: {codigos[i]}")