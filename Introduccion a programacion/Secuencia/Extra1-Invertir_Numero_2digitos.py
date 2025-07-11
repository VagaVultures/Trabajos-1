#Joshua Ontiveros Cabrero - 250206
#Invierte un numero de 2 digitos.

num=int(input("Ingrese un numero de dos digitos: "))

#matematicas

unidad=(num//10)
decena=(num%10)
reverse=((decena*10)+unidad)

#resultados

print(f"Tu numero que previamente era {num}, ahora es {reverse}.")