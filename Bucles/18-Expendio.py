#Joshua Ontiveros Cabrero - 250206
#Codigo que hace descuento si se cruza cierta cantidad de compra.

precio_por_kilo = float(input("Precio por kilo de naranja: "))
total_recaudado = 0

for cliente in range(1, 16):
    print(f"\nCliente {cliente}")
    kilos = float(input("Kilos comprados: "))

    pago = kilos * precio_por_kilo

    if kilos > 10:
        descuento = pago * 0.15
        pago -= descuento
        print(f"Se aplica descuento del 15%: -${descuento:.2f}")

    print(f"Total a pagar: ${pago:.2f}")

    total_recaudado += pago

print(f"\nLa tienda recibirá un total de: ${total_recaudado:.2f}")