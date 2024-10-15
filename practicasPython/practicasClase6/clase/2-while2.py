# Tabla de multiplicar

import time

tabla = int(input("Ingrese la tabla que desea multiplicar: "))
multiplo = 1

while multiplo <= 10:
    resultado = tabla * multiplo
    print(f" {multiplo} * {tabla} = {resultado}")
    multiplo += 1
    time.sleep(1)