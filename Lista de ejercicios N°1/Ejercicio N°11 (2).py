#Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es
#vocal”. Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle
#que no se puede procesar el dato

L=input("Ingrese una letra")
Letras={} 
Letras={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}
if L in Letras:
    print("Es vocal")
elif len(L)>=2:
    print("No se puede procesar el dato")
else:
    print("Es consonante")