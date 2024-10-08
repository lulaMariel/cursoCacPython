print("\n")
nota = float(input("Ingrese la nota (entre 1 y 10): "))

# if nota >= 4: 
#     print("¡Aprobaste!")
#     if nota >= 7:
#         print("¡Excelente nota!")
#     else:
#         print("Buen esfuerzo, pero hay que meterle un poco más")
# else: 
#     print("Desaprobaste, suerte la próxima")

if nota >=4:
    print("¡Aprobado!")
    if nota == 7:
        print("¡Excelente nota!")
    elif nota > 7 and nota <= 10:
        print("Sobresaliente")
    elif nota >= 4 and nota < 7:
        print("Buen esfuerzo, pero hay que esforzarse un poco más.")
elif nota >= 1 and nota < 4:
    print("Desaprobado")
else:
    print("Error")