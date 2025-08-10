#Joshua Ontiveros Cabrero - 250206
#Codigo que escribe el abecedario invertido.

#mostramos lo que hara el programa
print("Letras del abecedario de Z a A:")

#parametrizamos nuestro bucle
for codigo in range(90, 64, -1):  # de 90 ('Z') a 65 ('A')

    #traducimos los numeros a letras, y las imprimimos.

    print(chr(codigo), end=" ")


print()  # salto de línea al final