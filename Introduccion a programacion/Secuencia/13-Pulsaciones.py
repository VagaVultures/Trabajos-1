#Joshua Ontiveros Cabrero - 250206
#Calcular el numero de pulsaciones de una persona.


#presentacion
print("Este programa determina tu numero de pulsaciones sanas durante 10 segundos")

#Capturamos datos
age=int(input("Ingresa tu edad: "))

#calculos
pulse= ((220-age/10))

#salida

print(f"Tu numero de pulsaciones en un promedio de 10 segundos deberia ser: {pulse}")
