from conexionBD import *


try:
    micursor=conexion.cursor()

    sql="UPDATE clientes SET direccion='Col.Viscaya' where id=1"

    micursor.execute(sql)


    conexion.commit()
except:
    print("Ocurrio un error con el sistema, por favor verifique")
else:
    print("bien hecho lo actualizaste")


