#supongamos que tenemos 17 grupos con N numeros, se necesita
# sumar e imprimir la suma por grupo hasta que el usuario ingrese X,
# con S cambiara de grupo#


num_grupos=17
grupos=[0]*num_grupos
grupoactual=0

print("Habran distintos grupos, cada grupo sumara entre si sus valores. \nUse X para finalizar el programa o S para cambiar de grupo")

while grupoactual<num_grupos:
    dato=input(f"Grupo {grupoactual+1}: ")

    if dato.upper()=='X':
        break
    elif dato.upper()=='S':
        print(f"Suma del grupo {grupoactual+1}: {grupos[grupoactual]}")
        grupoactual+=1
    else:
        try: 
            numero=float(dato)
            grupos[grupoactual]+=numero
        except ValueError:
            print("Entrada no valida")
        print

print ("--Resultados Finales--")
for i in range(grupoactual+1):
    print(f"Grupo {i+1}: {grupos[i]}")




    