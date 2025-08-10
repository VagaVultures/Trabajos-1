#Joshua Ontiveros Cabrero - 250206
#Calcular los cuadrados del 20 hasta el 50

#Presentamos el programa.
input("Presiona enter para calcular los cuadrados de los numeros del 20 hasta el 50.")

#definimos variables.

Acumulador=0

#Comenzamos el ciclo

for i in range (20,51,1):

    Acumulador+=i*i

    print(f"{i}^2: {Acumulador}")
    