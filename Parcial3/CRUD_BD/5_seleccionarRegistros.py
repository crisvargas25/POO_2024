from conexionBD import *

try:
    micursor=conexion.cursor()

    sql="SELECT * FROM clientes"

    micursor.execute(sql)


    #crear un objeto para mandar el resultado del codigo sql, para posteriormente buscar con un ciclo

    resultado=micursor.fetchall()
except:
    print("Ocurrio un error con el sistema, por favor verifique")
else:
    for x in resultado:
        print(x)
