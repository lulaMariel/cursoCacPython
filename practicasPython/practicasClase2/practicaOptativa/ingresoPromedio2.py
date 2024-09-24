# Variables para los ingresos

ene = 1000
feb = 1500
mar = 1600
abr = 1400
may = 1700
jun = 2000

# Leyenda de ingresos

print()
print("Los ingresos obtenidos mes a mes: ")
print()
print("Enero:", ene, "\nFebrero:", feb, "\nMarzo:", mar, "\nAbril:", abr, "\nMarzo:", mar, "\nMayo:", may, "\nJunio:", jun)

# Suma semestre

sumaSemestre = (ene + feb + mar + abr + may + jun)

# Valor promediado

promedioSemestre = sumaSemestre / 6
# promedioSemestre = sumaSemestre // 6 Con 2 /, da el número entero y no flotante.

# Leyendas a mostrar

print()
print("Los ingresos obtenidos el primer semestre es de: ", sumaSemestre)
print()
print("El promedio de los ingresos obtenidos el primer semestre es de: ", int(promedioSemestre))