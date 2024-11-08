# Para poder recorrer los diccionarios podemos usar los bucles o ciclos, entre ellos: 3.

edades = {
    "Ana": 25,
    "Juan": 30,
    "Luis": 25
}

print("\n")
print(edades) # No se muestra de una forma bonita
print("\n")

# .items() devuelve clave-valor como tuplas.

for nombre, edad in edades.items():
    print(f"{nombre} tiene {edad} años.")
print("\n")

# .keys() devuelve solamente las claves.

for nombre in edades.keys():
    print(f"Su nombre es {nombre}.")
print("\n")

# .values() devuelve solamente los valores.

for edad in edades.values():
    print(f"Tiene {edad} años.")