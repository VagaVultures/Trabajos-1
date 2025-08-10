#Joshua Ontiveros Cabrero - 250206
#Codigo que calcula el factorial de el numero que sea introducido.

# Pedir número al usuario
n = int(input("Introduce un número para calcular su factorial: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Factorial {n} es {factorial}")