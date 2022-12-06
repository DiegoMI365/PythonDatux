#Definir una función que multiplique 2 números mayores de cero.
N1=0.0
N2=0.0
def Producto():
    print("Ingrese dos numeros mayores que cero para multiplicarlos")
    V1=float(input("Primer numero:"))
    if V1>0:
        V1==V1
    else:
        while True:
            if V1<=0:
                V1=float(input("Ingrese un numero mayor que cero"))
            else:
                break;
    
    V2=float(input("Segundo numero:"))
    if V2>0:
        V2==V2
    else:
        while True:
            if V2<=0:
                V2=float(input("Ingrese un numero mayor que cero"))
            else:
                break;
    return (V1*V2)

print("El producto de los dos numeros es",Producto())
