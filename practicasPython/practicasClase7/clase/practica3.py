# Estudiantes

estudiantes = [
    ["Juan", 2],
    ["Giuliana", 5],
    ["Maximiliano", 4],
    ["Juana", 6],
    ["Melina", 10],
    ["Valeria", 7],
    ["Carla", 3],
    ["Tomás", 6],
    ["Valentino", 2],
    ["Samanta", 9]
]

print("\n")
print("\t Alumnos aprobados: ")

for estudiante in estudiantes:
    nombre = estudiante[0]
    nota = estudiante[1]
    
    if nota >= 4:
        print("\n")
        print(f"Nombre: {nombre} \nNota del parcial: {nota}")
    
print("\n")
print("\t Alumnos desaprobados: \t")
    
for calificacion in estudiantes:
    nombre = calificacion[0]
    nota = calificacion[1]
    
    if nota <= 3:
        print("\n")
        print(f"Nombre: {nombre} \nNota del parcial: {nota}")
        