from conexionBD import *

try:
    micursor=conexion.cursor()
    nombre=input("Ingresa nombre: ")
    direccion=input("Ingresa direccion: ")
    telefono=input("Ingresa telefono; ")


    sql="INSERT INTO clientes (id,nombre,direccion,telefono)VALUES(NULL, '%s','%s','%s')"
    valores=(nombre, direccion, telefono)

    micursor.execute(sql,valores)

    #sirve para finalizar de manera exitosa la ejecucion del sql
    micursor=conexion.commit()
except:
    print("Ocurrio un error con el sistema, por favor verifique")
else:
    print('se registro correctly')



