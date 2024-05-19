'''
Nota: Cunado se imprime en pantalla una cadena de caracteres
se trabaja por default don cadenas es decir python no puede 
concatenar otra cosa que nio sea un string.
'''

texto="soy una cadena de caracteres"
numero=88
numero_str=str(numero)

#concatenar cadena con str

print(f'soy otra cadena y {texto}')

#string y un numero

print(f"el numero es {numero}")
print("el numero es " +  numero_str)

print("el numero es " + str(numero))

#int con str

n1="32"
n2=45

suma=int(n1)+n2
print(f"la suma es {suma}")

#concatenar float y entero con un str

n1=32
n2=344.33

suma=float(n1)+n2
print(f"la suma es {suma}")


n1=32.66
n2=344.33

suma=int(n1+n2)
print(f"la suma es {suma}")

print('suma', type(suma))