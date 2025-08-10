#Joshua Ontiveros Cabrero - 250206
#Estadisticas de alumnos


aprobados = 0
prom80omas = 0
contador = 1

while contador <= 10:
    print(f"\nAlumno {contador}")
    nombre = input("Nombre: ")

    c1 = float(input("Calificación 1: "))
    c2 = float(input("Calificación 2: "))
    c3 = float(input("Calificación 3: "))

    promedio = (c1 + c2 + c3) / 3

    if promedio >= 60:
        estado = "Aprobado"
        aprobados += 1
    else:
        estado = "Reprobado"

    if promedio >= 80:
        prom80omas += 1

    #Salida por alumno
    print(f"Nombre: {nombre}")
    print(f"Calificaciones: {c1}, {c2}, {c3}")
    print(f"Promedio: {promedio:.2f} → {estado}")

    contador += 1

#estadísticas
print("\n=== Estadísticas finales ===")
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos con promedio de 80 o más: {prom80omas}")