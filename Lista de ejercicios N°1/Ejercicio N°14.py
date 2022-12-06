print("Bienvenido")

while True:
    print("Elija una opción"
          "1)Saludar"
          "2)Multiplicar"
          "3)Salir")
    opcion=input()
    if opcion=="1":
        print("Hola mundo")
    elif opcion=="2":
        print("Ingrese dos numeros:")
        N1=int(input("Numero 1"))
        N2=int(input("Numero 2"))
        Producto=N1*N2
        print(f"El producto es {Producto}")
    elif opcion=="3":
        break;
    else:
        print("Ingrese una opcion valida")