#Definir una función que retorne el mayor valor al ingresar 2 números.

def Comparación():
    print("Ingrese dos numeros para determinar el mayor de ellos")
    N1=float(input("Primer numero:"))
    N2=float(input("Segundo numero:"))

    if N1<N2:
        return N2
        R=Comparación()
        print(R)
    elif N1>N2:
        return N1
        R=Comparación()
        print(R)
    else:
        print("Los números son iguales")
   
