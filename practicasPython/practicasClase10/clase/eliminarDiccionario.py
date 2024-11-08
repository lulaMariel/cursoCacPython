# Existen 3 métodos para eliminar un diccionario.

edades = {
    "Ana": 25,
    "Juan": 30,
    "Luis": 22
}
print("\n")

# .pop(clave) elimina un elemento específico y nos devuelve su valor. Se puede proporcionar un valor predeterminado si la clave no existe.

edadJuan = edades.pop("Juan") # Busca en el diccionario a "Juan" y elimina su edad, guardandolo en la variable edadJuan

print(f"La edad de Juan fue eliminada ({edadJuan}).")
print("\n")
print(f"Diccionario actualizado: {edades}")
print("\n")

# .del clave elimina un elemento específico y no devuelve ningún valor.

print("Eliminar definitivamente a Luis")
del edades ["Luis"]
print("\n")
print(f"Diccionario actualiazdo: {edades}")

# .clear() vacía el diccionario, dejandolo sin elementos.

print("\n")
print("Eliminar diccionario completo")
print("\n")
edades.clear()
print(f"Diccioanrio actualizado: {edades}")
print("\n")