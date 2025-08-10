#Joshua Ontiveros Cabrero - 250206
#Calcular la media aritmética de n números ingresados por teclado

#definimos las variables
acumulador=0
media=0

#presentamos programa y capturamos el limite del programa
print("Calculadora de la media aritmetica.")
contador=int(input("Ingrese la cantidad de numeros a medir: "))

#comenzamos el bucle
for i in range(0,contador):
    numero=int(input("Ingrese un numero: "))
    acumulador+=numero
#hacemos la ecuacion de la media
media=acumulador/contador
#imprimimos resultados.
print(f"La media de los {(i+1)} numeros que introdujo es {media}.\n")
