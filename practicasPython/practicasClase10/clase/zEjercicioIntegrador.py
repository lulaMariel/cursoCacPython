# Creamos un programa que:

# 1. Permita al usuario ingresar los nombres y edades de varias personas.
# 2. Muestre todas las edades ingresadas.
# 3. Permita actualizar la edad de una persona.
# 4. Permita eliminar a una persona.
# 5. Permita vaciar el diccionario al final.

# 1. Crear el diccionario

print("\n")
edades = {}

print("Ingrese los nombres y edades de las personas. \nEscribí 'fin' como nombre para finalizar.")
print("\n")

while True:
    nombre = str(input("Nombre: "))
    
    if nombre.lower() == "fin":
        break # Sale del bucle
    
    edad = int(input("Edad: "))
    
    edades[nombre] = edad

# 2. Mostrar todas personas ingresdas con sus edades

print("\n")
print("\t Lista de personas con sus edades: ")
print("\n")
for nombre, edad in edades.items():
    print(f"{nombre} tiene {edad} años.")
    
# 3. Actualizar la edad de una persona

print("\n")
nombreActualizar = str(input("Ingrese el nombre de la persona cuya edad quiera actualizar: "))
print("\n")

while nombreActualizar not in edades:
    print(f"{nombreActualizar} no se encuentra en el diccionario. Por favor, vuelva a intentarlo.")

    nombreActualizar = str(input("Ingrese el nombre de la persona cuya edad quiera actualizar: "))
    print("\n")
    
edadActualizada = int(input(f"Ingrese la edad actualizada de {nombreActualizar}: "))
print("\n")
edades[nombreActualizar] = edadActualizada

print(f"Edad actualizada: {nombreActualizar} actualmente tiene {edadActualizada} años.")

# 4. Eliminar a una persona

print("\n")
nombreEliminar = str(input("Ingrese el nombre de la persona que quiera borrar del diccionario: "))
print("\n")

while nombreEliminar not in edades:
    print(f"{nombreEliminar} no se encuentra en el diccionario. Por favor, vuelva a intentarlo.")
    
    nombreEliminar = str(input("Ingrese el nombre de la persona que quiera borrar del diccionario: "))
    
del edades[nombreEliminar]
print(f"{nombreEliminar} fue borrado del diccionario.")
print("\n")
for nombre, edad in edades.items():
    print(f"{nombre} tiene {edad} años.")
    
# 5. Vaciar el diccionario

print("\n")
vaciarDiccionario = int(input("¿Desea vaciar el diccionario completo? (1 para sí o 2 para no): "))

if vaciarDiccionario == 1:
    print("\n")
    edades.clear()
    print("\n")
    print("El diccionario fue vaciado correctamente.")
else:
    print("¡Gracias!")

print("Diccionario: ", edades)