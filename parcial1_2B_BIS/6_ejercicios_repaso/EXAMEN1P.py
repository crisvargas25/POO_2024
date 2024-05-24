estudiantes=1
promedioTODOS=0

while True:
    nombre=input("ingresa nombre: ")
    carrera=input("ingrese carrera: ")
    c1=int(input("ingresa calificación parcial 1: "))
    c2=int(input("ingresa calificación parcial 2: "))
    c3=int(input("ingresa calificación parcial 3: "))
    proyecto=int(input("ingresa calificación de proyecto final: "))
    promedioP=(c1+c2+c3)/3
    final=(promedioP+proyecto)/2
    promedioTODOS+=final
    print(f"\n ..... OVERALL .....")
    print(f"Nombre del alumno: {nombre}")
    print(f"Carrera: {carrera}")
    print(f"Promedio parciales: {promedioP}")
    print(f"Promedio FINAL: {final}")
    if final<80 or proyecto<50:
        print("\n Presenta examen extraordinario")
        estudiantes+=1
    continuar=input("\n Deseas otra captura (SI/NO)?").upper()
    if continuar != "SI":
        break

promedioFINAL=promedioTODOS/estudiantes
print(f"PROMEDIO DE LA CALIFICACIÓN FINAL DE LOS {estudiantes} ALUMNOS: {promedioFINAL}")

