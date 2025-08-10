#Joshua Ontiveros Cabrero - 250206
#imprimir numeros impares del 1 al 100


impar=0

input("Impresora de numeros impares, presiona enter para continuar.")

for i in range(0,101,1):
    
    if i%2==1:
        print(f"{i}.")    
    