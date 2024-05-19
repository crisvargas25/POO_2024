'''
existe una estructura de considción llamada if, 
la cual evalua una condición para encontrar el 
valor del verdadero o sr cumple la condición
se ejecuta el bloque de código.

3 variantes del if

1.if simple
2.if compuesto
3.if anidado 
4. if y elif

'''


#ejemplo if simple
color='rojo'

if color=='rojo':
    print('soy rojo')



#ejemplo if compuesto
color='rojo'

if color=='rojo':
    print('soy rojo')
else:
    print('no soy rojo')


#ejemplo if 
color='rojo'

if color=='rojo':
    print('soy rojo')
    if color=='rojo':
        print('soy rojo')
else:
    print('no soy rojo')


#ejemplo if compuesto
color='rojo'

if color=='rojo':
    print('soy rojo')
elif color=='negro':
    print('soy verde')
elif color=="negro":
    print('soy negro')
else:
    print('no soy ningun color')
