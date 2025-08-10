#Joshua Ontiveros Cabrero - 250206
#Codigo que calcula los tiempos de un atleta para ver si es apto.

dia = 1
suma_tiempos = 0
ningun_mayor_16 = True
al_menos_un_mayor_16 = False

while dia <= 10:
    tiempo = float(input(f"Tiempo del día {dia} (minutos): "))
    suma_tiempos += tiempo

    if tiempo > 16:
        ningun_mayor_16 = False
        al_menos_un_mayor_16 = True

    dia += 1

promedio = suma_tiempos / 10

if ningun_mayor_16:
    apto = True
elif al_menos_un_mayor_16:
    apto = True
elif promedio <= 15:
    apto = True
else:
    apto = False

print("\nResultado:")
if apto:
    print("El atleta es apto para la prueba.")
else:
    print("El atleta no es apto para la prueba.")