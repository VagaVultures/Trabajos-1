#Joshua Ontiveros Cabrero - 250206
#Codigo que calcula los puntos contaminantes de 25 carros.

total_puntos = 0
min_puntos = None
max_puntos = None

for i in range(1, 26):
    puntos = float(input(f"Puntos contaminantes del auto {i}: "))
    
    total_puntos += puntos
    
    if min_puntos is None or puntos < min_puntos:
        min_puntos = puntos
    if max_puntos is None or puntos > max_puntos:
        max_puntos = puntos

promedio = total_puntos / 25

print("\nResultados:")
print(f"Promedio de puntos contaminantes: {promedio:.2f}")
print(f"Menor contaminación registrada: {min_puntos}")
print(f"Mayor contaminación registrada: {max_puntos}")