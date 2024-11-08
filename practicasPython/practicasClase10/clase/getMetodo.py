# .get() nos permite acceder a los valores sin riesgo de errores si la clave no existe o está vacía.

edades = {
    "Ana": 25,
    "Juan": 30, # Teóricamente lo dejamos vacío
    "Luis": 22
}

print(edades.get("Ana", 0)) # Me muestra 25 porque no está vacío el valor
print(edades.get("Juan", 0)) # Me muestra 0 porque está vacío el valor