#Joshua Ontiveros Cabrero - 250206
#Sumar todos los numeros enteros del 1 al 100

acumulador=0

input("Sumador de numeros pares (Del 1 al 100).")

for i in range(0,101,1):
    
    print(i)
    acumulador+=i

print(f"La suma de numeros enteros de 1 al 100 es de {acumulador}.")