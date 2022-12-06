#Realiza un programa que lea 2 números por teclado y determine: 
#Si son iguales o diferentes o
#Si el primero es mayor que el segundo o viceversa

N1=int(input("Ingrese el valor del primer número"))
N2=int(input("Ingrese el valor del segundo número"))

if N1==N2:
    print("Los números son iguales")

else:
    if N1>N2:
        print(f"{N1} es mayor que {N2}, por lo tanto, son diferentes.")
    else:
        print(f"{N2} es mayor que {N1}, por lo tanto, son diferentes.")