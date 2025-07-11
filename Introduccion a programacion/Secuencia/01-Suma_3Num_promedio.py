#Siempre hay que poner nombre completo y matricula a la hora de hacer un programa, tambien
#un titulo en el programa.

#Joshua Ontiveros Cabrero - 250206
#Programa para sumar 3 numeros y sacar su promedio (Diagrama-01)

#solicitar al usuario que digite 3 numeros

x= float(input("Ingresa el Primer numero: "))
y= float(input("Ingresa el Segundo numero: "))
z= float(input("Ingresa el Tercer numero: "))

#calcular la suma y promediar la suma

suma= x+y+z
promedio=suma/3

# La f azul es para darle un formato, permite poner el valor de una variable dentro de un texto 
# se mete entre llaves la variable para poder mostrar el valor en forma de texto. la funcion
# :.2f sirve para limitar la cantidad de decimales que muestra la consola #

print(f"La suma de los tres numeros es {suma}")
print(f"El promedio de los 3 numeros es {promedio:.2f}")

