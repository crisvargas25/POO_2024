
# 1.- 
#  Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado

lista = [1, 4, 5, 6, 7, 3, 4, 4]

def recorrer_lista(lista):
    print("recorrer la lista y mostrarla:")
    for i in lista:
        print(i)

def recorrer_y_devolver_string(lista):
    print (', '.join(str(i) for i in lista))


def sort_lista():
    lista.sort()
    print("\nlista ordenada:")
    print(lista)

def longitud_lista(lista):
    longitud = len(lista)
    print("\nlongitud de la lista:")
    print(longitud)


def buscar(lista):
    numero = int(input("\nescribe un número para buscar en la lista: "))

    if numero in lista:
        index = lista.index(numero)
        print(f"el número {numero} se encuentra en la posición {index}.")
    else:
        print(f"el número {numero} no se encuentra en la lista.")


while True:
        print("\nMenú de opciones:")
        print("1. Recorrer la lista y mostrarla")
        print("2. Recorrer la lista y devolver un string")
        print("3. Ordenar la lista y mostrarla")
        print("4. Mostrar la longitud de la lista")
        print("5. Buscar un elemento en la lista")
        print("6. Salir")
        
        opcion = input("\nElige una opción (1-6): ")
        
        if opcion == '1':
            recorrer_lista(lista)
        elif opcion == '2':
            resultado = recorrer_y_devolver_string(lista)
            print("\nLista como string:")
            print(resultado)
        elif opcion == '3':
            sort_lista(lista)
        elif opcion == '4':
            longitud_lista(lista)
        elif opcion == '5':
            buscar(lista)
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")