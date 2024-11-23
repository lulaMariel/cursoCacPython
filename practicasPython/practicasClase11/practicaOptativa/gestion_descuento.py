# Tarea: Implementar un sistema de descuentos automáticos. Desarrollar un programa que permita calcular el precio final de un producto después del aplicar un descuento.
    # Indicaciones:
        # 1. Crear una función que reciba como parámetros el precio original del producto y el procentaje de descuento y que retorne el precio final con el descuento aplicado;
        # 2. Pedir que se ingrese el precio y el porcentaje de descuento;
        # 3. Mostrar el precio final.

print("")
precio_producto = float(input("Ingrese el precio del producto: $"))

porcentaje_descuento = int(input("Ingrese el descuento a aplicar (sin %): "))

def calcular_precio_final(precio, descuento):
    precio_descuento = precio - ((precio * descuento) / 100)
    return precio_descuento

precio_producto_final = calcular_precio_final(precio_producto, porcentaje_descuento)

print(f"El precio final del producto es de: ${precio_producto_final}")