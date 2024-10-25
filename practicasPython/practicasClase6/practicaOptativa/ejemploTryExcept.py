# Dividir por 0 debería dar error

while True:
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        resultado = num1 / num2
        
        print(f"La división entre {num1} y {num2} es de: {resultado}")
        
        break # Detiene el programa si la división se realizó correctamente
    except ZeroDivisionError:
        print("Error: No se puede dividir por 0. Vuelva a intentarlo.")
    except ValueError:
        print("Error: Por favor, ingrese solamente valores numéricos.")