# 7.- Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

n1=int(input("ingresa el numero inicial"))
n2=int(input("ingresa el numero final"))

for i in range(n1,n2):
    if not i % 2 == 0:
        print(i)