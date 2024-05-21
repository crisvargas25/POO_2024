# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for

c=1
while c<=60:
    resultado=c*c
    print(f"{c} x {c} = {resultado}")
    c+=1

for i in range(1,61):
    resultado=i*i
    print(f"{i} x {i} = {resultado}")