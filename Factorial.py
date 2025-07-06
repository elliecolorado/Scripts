def factorial(numero):
    if(numero > 1): return numero * factorial(numero-1)
    else: return 1

numero = int(input("Introduce un número para calcular su factorial: "))
if(numero < 1): print("No se pueden introducir números menores a 1.")
else: print("El resultado es: " + str(factorial(numero)))