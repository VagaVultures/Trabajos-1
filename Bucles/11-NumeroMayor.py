#Joshua Ontiveros Cabrero - 250206
#Programa que toma 50 numeros y muestra cual fue el mayor de todos.

Mayor=0
acumulador=0

input("Este programa te pedira 50 numeros, ingrese enter para comenzar: ")

for i in range (1,51,1):
    num=int(input("Ingrese un numero: "))
    
    if num>acumulador:
        acumulador=num
    else:
        acumulador=acumulador
        break

print(f"El numero mas grande fue {acumulador}.")
    