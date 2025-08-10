#Joshua Ontiveros Cabrero - 250206
#Programa que pide numeros y luego los suma #


#Pedimos un numero inicial y especificamos el uso del programa#
print("pedir numeros al usuario y sumarlos, hasta que el usuario ingrese 0")

#Definimos el valor inicial de las variables#
suma=0
contar=0

n=float(input(f"Ingrese un numero, 0 para terminar: "))

while n !=0:

    suma+=n
    contar+=1

    n=int(input(f"Ingrese numero, 0 para terminar: "))
    
print(f"la suma de los numero es: {suma} y la cantidad: {contar}")
