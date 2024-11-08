# Diccionario: Es como una lista, pero en lugar de usar índices (0, 1, 2, 3) para poder acceder, usamos claves y valores.
# El dicionario trabaja con métodos.


# Formato:
# diccionario = {
#     "Clave 1": "Valor 1",
#     "Clave 2": "Valor 2",
#     "Clave 3": "Valor 3"
# } 

edades = {
    "Ana": 25,
    "Agustina": 23,
    "Pablo": 35,
}

print("\n")
print("\tDiccionario: ")
print(edades)

# Acceder a diferenes elementos del diccionario

print("\n")
print("\tEdades iniciales: ")
print(f"Ana: {edades["Ana"]}")
print(f"Agustina: {edades["Agustina"]}")
print(f"Pablo: {edades["Pablo"]}")

# Agregar elemntos del diccionario:

print("\n")
print("Agregar un elemento: ")
print("\tDiccionario actualiado: ")
edades["Joaquín"] = 18
print(edades)

# Modificar elementos del diccionario:

edades["Ana"] = 30
edades["Agustina"] = 28
edades["Pablo"] = 40
edades["Joaquín"] = 23

print("\n")
print("Modificar elementos")
print("\tEdades actuales: ")
print(f"Ana: {edades["Ana"]}")
print(f"Agustina: {edades["Agustina"]}")
print(f"Pablo: {edades["Pablo"]}")
print(f"Joaquín: {edades["Joaquín"]}")

# Eliminar elementos del diccionario

print("\n")
print("Eliminar elementos: ")
print("\tDiccionario actualiado: ")
del edades["Joaquín"]
print(edades)
print("\n")

# Recorrer un diccionario

for nombre in edades:
    print(f"{nombre} tiene: {edades[nombre]}")
    
print("\n")
for nombre, edad in edades.items(): # items() método
    print(f"{nombre} tiene: {edad}")