# Función para calificaciones y promedios

print("")

def calificaciones_alumnos():

    calificaciones = []
    print("\tRegistro de Calificaciones")
    print("Ingrese las calificaciones de los estudiantes. Escribe 'salir' para detener el programa.")

    while True:
        entrada = input("Ingrese una calificación o 'salir' para detener el programa: ")

        if entrada.lower() == 'salir':
            break
        
        try:
            calificacion = float(entrada)

            if 0 <= calificacion <= 10:
                calificaciones.append(calificacion)
            else:
                print("Error: Por favor, ingrese una calificación entre 0 y 10.")
        except ValueError:
            print("Por favor, ingrese un valor numérico.")
    return calificaciones

def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones) if calificaciones else 0

def main():

    calificaciones = calificaciones_alumnos()

    if calificaciones:
        print(f"Calificaciones cargadas: {calificaciones}")
        print(f"El promedio es de: {calcular_promedio(calificaciones)}")

    else:
        print("Error: No se encontaron calificaciones cargadas. Por favor, vuelva a intetnarlo.")

main()