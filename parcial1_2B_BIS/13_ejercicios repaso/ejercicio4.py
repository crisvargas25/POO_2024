#  Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#   y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

lista=[]
cadena="hola mundo"
entero=3
logico=False

def tipo_de_Dato(dato):
    if type(dato)==bool:
        print(f"El dato '{dato}' es booleano.")
    elif type(dato)==int:
        print(f"El dato '{dato}' es entero.")
    elif type(dato)==list:
        print(f"El dato '{dato}' es una lista.")
    elif type(dato)==str:
        print(f"El dato '{dato}' es una cadena.")
    else:
        print("No es ninguna")



tipo_de_Dato(lista)
tipo_de_Dato(cadena)
tipo_de_Dato(entero)
tipo_de_Dato(logico)