#Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un
#menú:
# ● Mostrar una suma de los dos números
# ● Mostrar una resta de los dos números (el primero menos el segundo)
# ● Mostrar una multiplicación de los dos números
# ● En caso de introducir una opción inválida, el programa informará de que no es correcta

N1=int(input("Ingrese el primer número:"))
N2=int(input("Ingrese el segundo número:"))
acción=float(input("Escriba 0 para mostrar la suma de los números, 1 para mostrar su diferencia o 2 para mostrar la multiplicación de los números"))

if acción==0:
    Suma=int(N1+N2)
    print ("La suma de los números es",Suma)

elif acción==1:
    Resta=int(N1-N2)
    print ("La diferencia de los números es",Resta)

elif acción==2:
    Producto=int(N1*N2)
    print ("El producto de los números es",Producto)

else:
    print("Ha introducido una opción inválida")