risa = "Ja"

carcajada = risa * 5

print("\n")
print(carcajada)
print("\n")

nombre = input("Ingrese su nombre: ")
saludo = 'Hola, un "saludo" ' + nombre # No usar "" ni '' en la misma entrada
saludo2 = f'Hola, un "saludo" {nombre} ' 

print(saludo)

var1 = 3 + 5 # 8 (entero)
var2 = "3" + "5" # 25 (cadena)
var3 = 3 + "5" # TypeError
var4 = str(3) + "5" # 35 (cadena)
var5 = 3 + int("5") # 8 (entero)