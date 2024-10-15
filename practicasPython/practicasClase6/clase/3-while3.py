# while para dar inicio a un rango inicial y a un rango final, mostrandonos qué cantidad de pares y cuáles son

import time

rangoInicial = int(input("Ingrese el rango inicial: "))
rangoFinal = int(input("Ingrese el rango final: "))
cantidad = 0
rango = rangoInicial

while rango < rangoFinal:
    rango += 1
    if rango % 2 == 0:
        print(rango)
        cantidad += 1
        time.sleep(1)

print(f"La cantidad de pares encontrados entre {rangoInicial} y {rangoFinal} fue de: {cantidad}")
