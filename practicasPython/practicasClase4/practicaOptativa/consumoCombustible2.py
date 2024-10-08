# Entrada: Solicitud de datos al Usuario
litros_por_100_km= float(input("Ingresá el consumo del auto en litros por cada 100km:"))
precio_por_litro= float(input("Ingresá el costo por litro de Nafta Super:"))
distancia_viaje= float(input("Ingresá la distancia del viaje en KM:"))

# Proceso: Cálculo de litros consumidos y plata gastada
litros_consumidos = (litros_por_100_km / 100) * distancia_viaje
costo_de_viaje= litros_consumidos * precio_por_litro

# Calcular el consumo del auto por litro ()
consumo_por_litro_auto= distancia_viaje / (litros_consumidos + (litros_consumidos == 0))

# Salida: Muestra el detalle del viaje
print("\n --- DETALLES DEL VIAJE ---")
print(f"Litros consumidos: {litros_consumidos} litros")
print(f"Costo del viaje: ${costo_de_viaje}")
print(f"Consumo por litro de tu auto es de: {consumo_por_litro_auto} km/litro")