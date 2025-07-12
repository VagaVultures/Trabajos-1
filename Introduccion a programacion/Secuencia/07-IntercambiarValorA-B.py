#Joshua Ontiveros Cabrero - 250206
# Intercambiar los valores de A y B sin una variable extra.

a=int(input("Digite el valor de A: "))
b=int(input("Digite el valor de B: "))

#matematicas hijo!

b=a*b
a= b//a
b= b//a

print(f"el valor de A ahora es : {a}, y el valor de B ahora es: {b}!!!!")
