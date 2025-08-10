#Joshua Ontiveros Cabrero 250206
#Velocidad de una pelota

V0 = 96  # velocidad inicial en m/s

print("t (s) | h(t) (m)")
print("-----------------")

for t in range(1, 9):
    h = V0 * t - 5 * (t**2)
    print(f"{t:5} | {h:8}")