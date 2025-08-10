#Joshua Ontiveros Cabrero - 250206
#Programa que pide el genero y edad de una persona, da promedios y edades mas altas.

#definimos las variables antes de poder usarlas.
Hombres=0
Mujeres=0
usuarios_validos=0
errores=0
edadH=0
edadHmax=0
edadMmax=0
edadM=0
promedioH=0
promedioM=0
PromGeneral=0
acumuladorH=0
acumuladorM=0
cH=0
cM=0

#especificamos el uso del programa
print("ingrese el genero de 5 usuarios(H para hombre y M para mujer: )")

while usuarios_validos<5:
    genero=input(f"Ingrese el genero del usuario {usuarios_validos+1}: ").upper()#convertir a Mayus.
    

    if genero=='H':

        try:

            
            edadH=int(input("Ingrese la edad de la persona: "))
            acumuladorH+=edadH
            if edadH>cH:
                cH=edadH
                Hombres+=1
                usuarios_validos+=1 
  
            else:    
                cH=cH
                Hombres+=1
                usuarios_validos+=1 

        except ValueError:
                    print("Ingrese un numero porfavor.")
                    errores+=1


    elif genero=='M':

        try:
            edadM=int(input("Ingrese la edad de la persona: "))
 
            acumuladorM+=edadM
            if edadM>cM:
                cM=edadM
                Mujeres+=1
                usuarios_validos+=1
            else:
                cM=cM
                Mujeres+=1
                usuarios_validos+=1
        except ValueError:
                    print("Ingrese un numero porfavor.")
                    errores+=1


    else:
        errores+=1
        print("Entrada invalida, por favor, Ingrese H de hombre o M de mujer.")


PromGeneral=(acumuladorH+acumuladorM)/5

if Hombres>0:
    promedioH=acumuladorH/(5-Mujeres)
    print(f"\nLa cantidad de hombres es {Hombres}")
    print(f"El promedio masculino es de {promedioH}")
    print(f"La edad mas alta masculina fue: {cH}")
else:
    print("\nNo hubo hombres.")


if Mujeres>0:
    promedioM=acumuladorM/(5-Hombres)
    print(f"\nLa cantidad de mujeres es {Mujeres}")
    print(f"El promedio Femenino es {promedioM}.")
    print(f"La edad mas alta femenina fue: {cM}")
else:
    print("\nNo hubo mujeres")


print(f"\nLos usuarios totales es de {usuarios_validos}.")
print(f"La cantidad de errores es: {errores}.")
print(f"el promedio general es de: {PromGeneral}.")