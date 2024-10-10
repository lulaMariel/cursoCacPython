#Se trata de poner una condición dentro de otra. Esto te permite manejar situaciones donde la decisión que vas a tomar depende de una serie de condiciones que deben evaluarse en secuencia.

nota = print("Ingrese Nota (aprueba mayor o igual a 60):")

if nota >= 60:
   print("¡Aprobaste!")
   if nota >= 90:
       print("¡Excelente calificación!")
   else:
       if nota >= 75:
           print("Muy buen trabajo.")
       else:
           print("Buen esfuerzo, pero hay margen de mejora.")
else:
   print("No alcanzaste la calificación mínima para aprobar.")


#Condicionales | if…elif…else
#Este es un script que hace lo mismo que el anterior, pero usando elif.
#Ahora el código se ve mucho más ordenado y fácil de seguir. Pero ¿qué es exactamente lo que hace elif? 

#Básicamente, es una forma de agregar más condiciones en una estructura if, pero sin necesidad de anidar 
# los bloques de código uno dentro del otro.

nota = print("Ingrese Nota (aprueba mayor o igual a 60):")

if nota >= 60:
   print("¡Aprobaste!")
   if nota >= 90:
       print("¡Excelente calificación!")
   elif nota >= 75:
       print("Muy buen trabajo.")
   else:
       print("Buen esfuerzo, pero hay margen de mejora.")
else:
   print("No alcanzaste la calificación mínima para aprobar.")