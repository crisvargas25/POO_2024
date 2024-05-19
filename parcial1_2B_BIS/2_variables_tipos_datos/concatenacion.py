#formas de concatenación en python 

nombre='cristian vargas'
especialidad='estudiante'
carrera='ingenieria gestión y desarrollo de software'

#1ra forma de cncatenar

print('mi nombre es ' + nombre + " soy " +  especialidad + ' y mi carrera es ' + carrera)
print("\n")

#2da forma de cncatenar

print('mi nombre es ', nombre , " soy ",  especialidad, ' y mi carrera es ', carrera)
print("\n")

#3ra forma de cncatenar

print(f'mi nombre es  {nombre} soy   {especialidad}  y mi carrera es  {carrera}')
print("\n")

#4ta forma de cncatenar

print('mi nombre es   {}  soy   {}  y mi carrera es  {}'.format(nombre,especialidad,carrera))
print("\n")

#5ta forma de cncatenar

print("mi nombre es " + nombre + " soy " +  especialidad + " y mi carrera es " + carrera)
print("\n")

