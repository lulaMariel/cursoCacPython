num = 11
suma = 0

for i in range(1, num + 1): # num + 1 es para que incluya el valor de la variable, sino el rango cortaría en 10 porque el índice de fin no incluye al valor
    suma +=  i
    
    print(f"Número: {i}")
    

print(f"\nLa suma de los números naturales hasta el {num}: {suma}")