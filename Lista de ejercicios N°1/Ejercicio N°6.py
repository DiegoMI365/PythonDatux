#Realice un programa que calcule la suma de los números hasta el valor ingresado.
#Ejemplo : si se ingresa 5 se tendrá que calcular 1+2+3+4+5.

número=int(input("Ingrese un valor numérico entero positivo"))

p1=número+1
suma=p1*número/2

print(f"La sumatoria de los números desde el 0 hasta el {número} es igual a {suma}")