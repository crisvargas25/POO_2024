from conexionBD import *


try:
    micursor=conexion.cursor()
    sql="CREATE TABLE clientes2(ID INT PRIMARY KEY AUTO_INCREMENT, nombre VARCHAR(60),direccion VARCHAR(120),telefono VARCHAR(10))"

    micursor.execute(sql)
        
except:
    print("Ocurrio un error con el sistema, por favor verifique")
else:
    print('se creo la tabla exitosamente')  