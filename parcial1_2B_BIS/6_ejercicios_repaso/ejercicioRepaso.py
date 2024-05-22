'''
Crear un programa que calcule y obtenga el total a 
pagar por un producto determinado. Se deberá de 
solicitar nombre o descripción del producto, código, 
cantidad del producto, precio unitario del producto.

El total a pagar incluy el iva, y el descuento. Si
se compran de 1 a 5 producto se otorga el 10% de desc.
Si se compran de 6 a 10 el 15%, y si compran mas de 10 el 20%.

'''
nombre = input("Ingresa nombre del producto: ")
codigo = input("Ingresa el código: ")
cantidad = int(input("Ingresa la cantidad: "))
punit = float(input("Ingresa el precio unitario: "))

if cantidad <= 5:
    descuento = 0.10  # 10% de descuento
elif cantidad <= 10:
    descuento = 0.15  # 15% de descuento
else:
    descuento = 0.20  # 20% de descuento

total_bruto = cantidad * punit

total_descuento = total_bruto * (1 - descuento)

iva = 0.16
total_final = total_descuento * (1 + iva)

print("--------------------------")
print("Nombre del producto:", nombre)
print("Código del producto:", codigo)
print("Cantidad:", cantidad)
print("Precio unitario: ${:.2f}".format(punit))
print("Descuento aplicado: {:.0f}%".format(descuento * 100))
print("Total con descuento: ${:.2f}".format(total_descuento))
print("IVA aplicado: {:.0f}%".format(iva * 100))
print("Total a pagar (incluyendo IVA): ${:.2f}".format(total_final))
