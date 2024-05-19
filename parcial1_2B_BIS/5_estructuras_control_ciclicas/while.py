'''
el ciclo while es una estructura de control que itera o repite
la ejecución de una serie de instrucciones tantas veces como 
la condición se cumpla (true)

sitnaxis:
while condicion:
    bloque de codigo


'''

#1er ejemplo
c=1

while c<=5:
    print("@")
    c+=1


#2do ejemplo

c=1
suma=0
while c<=5:
    print(c)
    suma+=c
    c+=1
print(f"La suma es {suma}")


numero=int(input("ingresa el numero entero"))
c=1
while c<=10:
    resultado=c*numero
    print(f" {c} x {numero} = {resultado}")
    c+=1

