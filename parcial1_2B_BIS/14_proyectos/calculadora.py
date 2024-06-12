import os
from funciones import *

opcion = True
while opcion:
    os.system("clear")
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicación \n 4.- División \n 5.- Raíz \n 6.- Potencia \n 7.- SALIR ")
    opcion = input("\t Elige una opción: ").upper()

    if opcion != "7":
        n1, n2 = solicitarDatos() if opcion not in ["5", "RAIZ"] else (solicitarDato(), None)
        print(getCalculadora(n1, n2, opcion))
        esperaTecla()
    else:
        opcion = False
        print("Gracias por utilizar el sistema ...")
