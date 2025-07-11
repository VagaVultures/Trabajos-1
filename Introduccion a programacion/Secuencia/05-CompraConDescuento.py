#Joshua Ontiveros Cabrero - 250206
# Descuento de una compra.

#Definimos los valores y variables.

compra=int(input("Digite el costo del producto: "))

descuento=(compra*.08)

total=(compra-descuento)

#imprimimos resultados

print(f"Tu producto con valor de ${compra} obtuvo un 8% de descuento!!!")
print (f"El valor final de tu producto es de ${total}")