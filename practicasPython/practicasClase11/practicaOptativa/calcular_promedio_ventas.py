# Tarea: Desarrollar un programa que permita calcular el promedio de ventas de la tienda.
    # Indicaciones:
        # 1. Crear una función que reciba como parámetro una lista de ventas diarias y devuelva el promedio de esas ventas;
        # 2. Solicitá a la persona que ingrese las ventas de cada día durante una semana. Usá la función para calcular y mostrar el promedio de vetnas al finalizar.

print("")
ventas_diarias = []

def calcular_promedio(ventas):
    total_ventas = sum(ventas)
    promedio_ventas = total_ventas / len(ventas)
    
    return promedio_ventas

for dia in range (1, 8):
    venta = float(input("Ingrese la venta del día " + str(dia) + ": ")) # El "str(dia)" vuelve dinámico el "contador" de los días del rango, convirtiendolos en string para poder concatenarlo
    ventas_diarias.append(venta)

promedio_de_ventas = calcular_promedio(ventas_diarias)

print("")
print(f"El promedio de las ventas diarias durante 7 días es de: {promedio_de_ventas:.2f}")