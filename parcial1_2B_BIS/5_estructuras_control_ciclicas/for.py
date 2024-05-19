'''
For en un ciclo iterativo que se ejecuta x veces 
dependiendo de los valores númericos enteros establecidos

Sintaxis:

for variable in elemento_iterable(lista,rango,etc):
    bloque de instrucciones

'''

#ejemplo 1 crear 8un programa que imprima 5 veces el caracter @


for d in range(0,5):
    print("@")

#crear un programa que imprima los numeros del 1 al 5, los sume y al final imprima la suma
suma=0

for c in range(1,6):
    print(c)
    suma+=c
print(f"la suma es {suma}")

#ejemplo 3. crerar un programa que solicite un numero entero
#y despues imprima la tabla de multiplicar corrrespomdiente


numero=int(input("ingresa el numero entero"))

for i in  range(1,11):
    resultado=i*numero
    print(f" {i} x {numero} = {resultado}")



