#Realizar una función que tenga por parámetro un lista de numerosy aumente cada
#elemento en +1

lista=[1,2,3,4] 

def Sumar(lista):
    print(lista)
    for i in lista:
        lista[i-1]+=1

Sumar(lista)
print(lista)





