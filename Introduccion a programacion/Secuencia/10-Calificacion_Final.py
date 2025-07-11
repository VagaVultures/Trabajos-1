#Joshua Ontiveros Cabrero - 250206
# Un alumno desea saber su calificacion final en la materia de algoritmos.

#presentacion
print("Bienvenido a la calculadora de calificaciones.(Presione enter para continuar)")

#captura de  informacion
calif1=int(input("Ingrese su la calificacion del primer parcial: "))
calif2=int(input("Ingrese su la calificacion del segundo parcial: "))
calif3=int(input("Ingrese su la calificacion del tercer parcial: "))
examf=int(input("Ingrese la calificacion de su exmen final: "))
trabajof=int(input("Ingrese el valor de su trabajo final: "))

#Mr white, we need to do math!

prom=((calif1+calif2+calif3)/3)
promparcial=(prom*.55)
promexamen=(examf*.30)
promtrabajof=(trabajof*.15)

calF=promparcial+promexamen+promtrabajof

#Imprimimos el valor de su calificacion

print(f"Su calificacion final es de {calF:.1f}.")

#Puuura coqueteria!#

if calF==10:
    print("No eres humano!!!!")
elif calF>=7:
    print("Muy bien hecho! ")
else:
    print("Suerte a la proxima.")