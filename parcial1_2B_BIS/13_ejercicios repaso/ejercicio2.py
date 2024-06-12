# 2.- 
# Escribir un programa  que añada valores a una lista mientras que su longitud 
#  sea menor a 120, y luego mostrar la lista: Usar un while y for

lista=[]

# while len(lista)<120:
#     try:
#         numero=int(input("ingrese numero: "))
#         lista.append(numero)
#     except:
#         print("ingresa numero valido")

# print("gracias , tu lista es: ", lista)
    
for i in  range(1,121):
    try:
        numero=int(input("ingrese numero: "))
        lista.append(numero)
    except:
        print("ingresa numero valido")

print("gracias , tu lista es: ", lista)