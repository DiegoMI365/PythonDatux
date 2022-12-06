#Escribir un programa que le pida al usuario un número entero 
# y muestre por pantalla si es par o impar

número=int(input("Ingrese un número entero"))

residuo=número%2

if residuo == 0:
    print("El número es par")
else:
    print("El número es impar")