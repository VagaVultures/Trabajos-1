#Joshua Ontiveros Cabrero - 250206
#Calcular la suma de N numeros introducidos.

#definimos el valor de las variables y las variables mismas.
Acumulador=0
Suma=0

#Pedimos que digite una cantidad fija que seran los numeros sumados al final.
Contador=int(input("Ingrese la cantidad de numeros que desea sumar: "))

#comenzamos el ciclo For, definiendo el limite con el numero antes pedido.
for i in range(Contador):
    
    numero=int(input("Ingrese un numero: "))
    Suma+=numero

#imprimimos resultados.
print(f"La suma de tu(s) {i+1} numero(s) es de {Suma}")
