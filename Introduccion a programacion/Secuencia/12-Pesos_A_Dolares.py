#Joshua Ontiveros Cabrero - 250206
# Conversor de pesos a dolares.

#capturamos datos
input("Conversor de Pesosa dolares, (Tipo de cambio: 18.75MXN)")
Pesos=float(input("Ingrese la cantidad de Pesos a cambiar: "))

#matematicas

Dollar=(Pesos/18.75)

#Resultados

print(f"Tus {Pesos}MXN a dolares son ${Dollar:.2f}Dlls.")