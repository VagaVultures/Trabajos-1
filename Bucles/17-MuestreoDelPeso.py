#Joshua Ontiveros Cabrero - 250206
#Codigo que calcula el muestreo del peso basado en distinta edades.

# Variables para acumular pesos y contar personas en cada categoría
peso_niños = 0
count_niños = 0

peso_jovenes = 0
count_jovenes = 0

peso_adultos = 0
count_adultos = 0

peso_viejos = 0
count_viejos = 0

total_personas = 50

for i in range(1, total_personas + 1):
    print(f"\nPersona {i}:")
    edad = int(input("Edad: "))
    peso = float(input("Peso (kg): "))

    if 0 <= edad <= 12:
        peso_niños += peso
        count_niños += 1
    elif 13 <= edad <= 29:
        peso_jovenes += peso
        count_jovenes += 1
    elif 30 <= edad <= 59:
        peso_adultos += peso
        count_adultos += 1
    elif edad >= 60:
        peso_viejos += peso
        count_viejos += 1
    else:
        print("Edad inválida, no se contabilizará.")

# Calcular promedios (con control para evitar división entre cero)
print("\n--- Promedio de peso por categoría ---")

if count_niños > 0:
    print(f"Niños (0-12): {peso_niños / count_niños:.2f} kg")
else:
    print("Niños (0-12): No hay datos.")

if count_jovenes > 0:
    print(f"Jóvenes (13-29): {peso_jovenes / count_jovenes:.2f} kg")
else:
    print("Jóvenes (13-29): No hay datos.")

if count_adultos > 0:
    print(f"Adultos (30-59): {peso_adultos / count_adultos:.2f} kg")
else:
    print("Adultos (30-59): No hay datos.")

if count_viejos > 0:
    print(f"Viejos (60+): {peso_viejos / count_viejos:.2f} kg")
else:
    print("Viejos (60+): No hay datos.")