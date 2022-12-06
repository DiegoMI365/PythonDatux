nombre=input("Ingrese los nombres y apellidos del cliente")
Dni=input("Ingrese su DNI")
pais=input("Ingrese su pais de nacionalidad")
metododepago=input("Ingrese su metodo de pago")
NumProductos=input("Ingrese la cantidad de productos adquiridos")
Fecha=input("Ingrese la fecha en la que el cliente realizo la compra")

with open("Clientes.txt","w") as archivo:
    archivo.write(nombre)
    archivo.write(f"\n{Dni}")
    archivo.write(f"\n{pais}")
    archivo.write(f"\n{metododepago}")
    archivo.write(f"\n{NumProductos}")
    archivo.write(f"\n{Fecha}")





