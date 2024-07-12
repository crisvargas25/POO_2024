from conexionBD import *


try:
    micursor=conexion.cursor()

    sql="DELETE FROM clientes WHERE ID=4"

    micursor.execute(sql)


    conexion.commit()
except:
    print("Ocurrio un error con el sistema, por favor verifique")
else:
    print("bien hecho lo eliminaste")


