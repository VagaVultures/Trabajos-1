max_area = 0
x_max = 0

print("Valor de X   Área")
print("-----------------")

for x in range(10, 15):
    area = x * (15 - x)
    print(f"{x:<11} {area}")

    if area > max_area:
        max_area = area
        x_max = x

print(f"\nEl área máxima es: {max_area} con X = {x_max}")