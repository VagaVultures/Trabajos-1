#Joshua Ontiveros Cabrero - 250206
#Leer 100 numeros, determinar la media positiva y negativa.

contadorPos=0
contadorNeg=0
acumuladorNeg=0
acumuladorPos=0

print("ingresar 100 numeros a el calculador de media (Pueden ser negativos o positivos).")

for i in range(1,101,1):
    
    numero=int(input("Ingresa un numero: "))

    if numero>=0:
        try:
            contadorPos+=1
            acumuladorPos+=numero

        except ValueError:
            print("Ingresa un caracter Valido.")
            
            break

    else:
        try:
            contadorNeg+=1
            acumuladorNeg+=numero

        except ValueError:
            print("Ingresa un caracter Valido.")

            break
    

MediaPos=acumuladorPos/contadorPos
MediaNeg=acumuladorNeg/contadorNeg

print(f"La media Positiva es de {MediaPos} y la Negativa es de {MediaNeg}")