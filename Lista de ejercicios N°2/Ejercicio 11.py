#Definir los atributos y métodos de una de las siguientes clases.
#- Persona
#- Gato
#- Producto

class Animal:
    pass
gato = Animal()

gato.familia="Felidae"
gato.numerodepatas="4"
gato.partes="cola"
gato.colorpelaje="blanco"

print(f"Los gatos pertenecen a la familia {gato.familia}")
print(f"Los gatos poseen {gato.numerodepatas} patas")
print(f"Los gatos poseen {gato.partes}")
print(f"El color del pelaje de los gatos puede ser {gato.colorpelaje}")