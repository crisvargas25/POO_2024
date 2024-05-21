 # 10.- Crear un programa que solicite la calificacion de 15 alumnos e 
# imprimir en pantalla cuantos aproboron y cuantos no aprobaron
aprobados=0
reprobados=0

for i in range(1,16):
    cali=float(input(f"Ingrese calificacion del alumno {i}: "))
    if cali>=80:
        aprobados+=1
    elif cali<80:
        reprobados+=1
    elif cali>100:
        print("respuesta no válida ")

print(f"cantidad de alumnos aprobados: {aprobados}")
print(f"cantidad de alumnos reprobados: {reprobados}")
