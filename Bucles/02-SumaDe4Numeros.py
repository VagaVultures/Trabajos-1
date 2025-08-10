#Joshua Ontiveros Cabrero - 250206
#Calcular la suma de 4 numeros introducidos.

#definimos las variables
Intentos=0
Acumulador=0
Numero=0

#presentamos el programa a el publico
input("Programa que suma 4 numeros que introduzca, Presione enter para continuar.")

#usamos el ciclo while para que se repita hasta alcanzar un limite definido
while Intentos<4:

    Numero=int(input("Ingrese un numero: "))

    Intentos+=1
    Acumulador+=Numero

#imprimimos resultados.
print(f"La suma de los 4 numeros es: {Acumulador}.")
