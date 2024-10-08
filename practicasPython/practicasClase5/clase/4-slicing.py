frase = "Aprendamos sobre Python"
subcadena = frase[0:10] # El máximo no incluye al número que expresamos, es decir, la "s" es "9", pero ponemos "10" porque si ponemos "9", la "s" no se va a mostrar

print("\n")
print(subcadena)
print("\n")

subcadena = frase[:10] # Por defecto, el primer subíndice es 0
print(subcadena)

subcadena = frase[0:] # Por defecto, si no ponemos el segundo subíndice, coloca toda la cadena
print(subcadena)

subcadena = frase[::2] # Muestra todo el texto pero con saltos entre caracteres de 2 en 2
print(subcadena)