'''
Crear un programa que calcule y obtenga el total a 
pagar por un producto determinado. Se deberá de 
solicitar nombre o descripción del producto, código, 
cantidad del producto, precio unitario del producto.

El total a pagar incluy el iva, y el descuento. Si
se compran de 1 a 5 producto se otorga el 10% de desc.
Si se compran de 6 a 10 el 15%, y si compran mas de 10 el 20%.

'''

nombre=input("ingresa nombre del producto: ")
codigo=input("Ingresa el codigo: ")
cantidad=input("Ingresa la cantidad: ")
punit=input("ingresa el precio unitario: ")

if cantidad<=5:
    descuento=.9
elif cantidad<=10:
    descuento=.85