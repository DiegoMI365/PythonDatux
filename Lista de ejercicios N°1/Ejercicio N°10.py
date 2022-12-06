#Realizar un programa que calcule la penalidad por la mora de una deuda,sabiendo que si se
#demora de 1 día a 10 se le agrega el 5% , si se demora hasta 30 días se le agrega 8% y pasando
#el rango máximo se le agrega un 10%

Ndias=int(input("Ingrese el número de días de retraso"))

if Ndias ==0:
    print("No se ha generado un interés por que el pago se ha realizado de manera puntual")
elif Ndias ==1:
    print(f"Se ha generado un interés del 5% por {Ndias} día de retraso en el pago")
elif Ndias >1 and Ndias<=10:
    print(f"Se ha generado un interés del 5% por {Ndias} días de retraso en el pago")
elif Ndias<=30:
    print(f"Se ha generado un interés del 8% por {Ndias} días de retraso en el pago")
else:
    print(f"Se ha generado un interés del 10% por {Ndias} días de retraso en el pago")