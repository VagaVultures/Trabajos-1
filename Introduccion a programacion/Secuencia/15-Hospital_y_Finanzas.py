#Joshua Ontiveros Cabrero - 250206
#un hospital divide sus gastos en 3 areas
# Ginecologia       40%
# Pediatria         30%
# Traumatologia     30%
#obten la cantidad que recibira cada area por cada monto presupuestal #

#informacion
print("Bienvenido al hospital Mercy futuro inversor.")
monto=float(input("Cuanto desea invertir?: "))

#operaciones

gine=monto*.40
ped=monto*.30
trau=monto*.30

#resultados

print(f"{gine:.2f}mxn Fue para Ginecologia, {ped:.2f}mxn Fue para Pediatria y {trau:.2f}mxn fue para Traumatologia.")
print("Muchas gracias por su donativo")