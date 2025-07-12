#Joshua Ontiveros Cabrero - 250206
#Programa que invertira los digitos de un numero de 3 digitos

Num=int(input("Ingrese un numero de tres digitos: "))

if Num>=1000:
    print("El numero no debe superar los 3 digitos.")
    exit()
elif Num<100:
    print("El numero debe superar los 2 digitos.")
    exit()

else:
    Unidad= (Num//100)
    Centena= (Num%10)
    Decena= (Num-(Unidad*100+Centena))
    Reverse=((Centena*100)+Decena+Unidad)

#imprimimos el resultado

print(f"El numero {Num} invertido seria: {Reverse}")

