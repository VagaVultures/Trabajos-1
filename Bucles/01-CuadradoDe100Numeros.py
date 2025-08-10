#Joshua Ontiveros Cabrero - 250206
#Saca el cuadrado de los primeros 100 numeros y sumarlos.

input("Presione enter para mostrar la suma de los cuadrados de los 100 primeros numeros ")

Acumulador=0

for i in range(101):

    Exponente=i*i

    print(f"{i}^2= {Exponente }")

    Acumulador = Acumulador+Exponente

    if i>=101: 
        break

print(f"La suma total de todos los cuadrados de los numeros listados es:{Acumulador}")