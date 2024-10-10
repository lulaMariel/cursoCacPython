# Ejemplo 1 IF

nota = float(input("Nota: "))

if nota >= 7:
    print("Aprobado.")

# Esa pequeña sangría al principio de la línea no es sólo por estilo; le dice a Python que esas líneas de código forman parte del bloque del if.

edad = 18

if edad >= 18:
  print("Sos mayor de edad.")

# Ejemplo 2 IF ... ELSE

# SE PUEDEN CREAR TANTOS ELIF COMO SE QUEIRA, PERO SIEMPRE Y CUANDO EL PRIMER IF CIERRE CON SU ELSE AL FINAL.

if edad >= 18:
  # Bloque de instrucciones que se ejecuta si la condición es verdadera
  print("Puedes pasar.")
else:
  # Bloque de instrucciones que se ejecuta si la condición es falsa
  print("No admitido.")

# Ejemplo 3 IF ... ELSE AND

edad = int(input("Ingresá tu edad: "))
tiene_licencia = input("¿Tenés licencia de conducir? (S/N): ")

# Verificamos si la persona puede conducir

if edad >= 18 and tiene_licencia == "S":
   print("Podés conducir.")
else:
   print("No podés conducir.")