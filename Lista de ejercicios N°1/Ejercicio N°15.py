#Iterar una lista de elementos que contengan nombre y edad e imprimir solo los mayores de
#edad.

Personas=[["Marcos",14],["Julia",22],["Diego",17],["Maria",25]]

for object in Personas:
    if object[1]>=18:
        print (f"{object[0]} es mayor de edad, por que tiene {object[1]} años")
